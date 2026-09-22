import unittest
from unittest.mock import patch
import test_motor
from src import motor
from src import revisao


class RevisaoTest(unittest.TestCase):
    setUp = test_motor.PesquisaTest.setUp
    artigo = test_motor.PesquisaTest.artigo

    def test_citacao_incorreta_nao_descarta_ideias_nem_vira_evidencia(self):
        r = revisao.ficha_segura({'resumo': 'Resumo provisório.', 'evidencias': [
            {'afirmacao': 'x', 'citacao': 'não existe'}, {'afirmacao': 'y', 'citacao': 'texto real'}]}, 'texto real')
        self.assertEqual(len(r['evidencias']), 1)
        self.assertTrue(r['avisos'])
        self.assertEqual(r['resumo'], 'Resumo provisório.')

    def test_fichas_legadas_reaproveitadas_sem_reler_texto(self):
        a = self.artigo('A')
        a['triagem_agente'] = {'revisao': self.p.revisao, 'classificacao': 'priorizar'}
        a['pre_leitura_agente'] = {'revisao': self.p.revisao, 'decisao': 'ler_integralmente', 'justificativa': 'teste'}
        trechos = self.p.trechos(a)
        assinatura = motor.chave(['orientacao-antiga', a['id_openalex'], trechos])
        a['leitura_agente'] = {'assinatura': assinatura, 'revisao': 'orientacao-antiga'}
        motor.json_gravar(self.root / 'dados/leituras' / assinatura / '0.json',
                         {'id': 'ficha-antiga', 'resumo': 'Resumo já produzido.', 'evidencias': [], 'pagina': None, 'tipo': 'resumo'})
        with patch('src.revisao.chamar', return_value={'problema': 'Resumo já produzido.'}) as chamar:
            self.p.ler()
        self.assertEqual(chamar.call_count, 2)
        self.assertEqual(chamar.call_args_list[0].args[1], 'reaproveitar-leituras')
        self.assertTrue(a['leitura_agente']['concluida'])
        self.assertEqual(a['perfil_revisao']['problema'], 'Resumo já produzido.')

    def test_perfil_nao_transforma_inferencia_em_limite_observado(self):
        r = revisao.perfil_seguro({'solução':'Integra IoT.', 'limites':'Não integra IoT.',
                                  'possibilidades':'Testar revogação.'}, 'Integra IoT.')
        self.assertEqual(r['solucao'], 'Integra IoT.')
        self.assertTrue(r['limites'].startswith('Não identificado'))
        self.assertEqual(r['possibilidades'], 'Testar revogação.')

    def test_trecho_em_erro_nao_bloqueia_pagina_seguinte(self):
        a = self.artigo('A')
        a['triagem_agente'] = {'revisao': self.p.revisao, 'classificacao': 'priorizar'}
        a['pre_leitura_agente'] = {'revisao': self.p.revisao, 'decisao': 'ler_integralmente', 'justificativa': 'teste'}
        ts = [{'pagina': 1, 'texto': 'primeiro', 'tipo': 'pdf'}, {'pagina': 2, 'texto': 'segundo', 'tipo': 'pdf'}]
        assinatura = motor.chave(['revisao-exploratoria-v1', self.p.revisao, a['id_openalex'], ts])
        ident = motor.chave(['ler', assinatura, 0])
        self.p.estado['tarefas'][ident] = {'erro': 'temporário', 'tentar_em': 9999999999}
        with patch.object(self.p, 'trechos', return_value=ts), patch('src.revisao.chamar', return_value={'resumo': 'Segundo.', 'evidencias': []}) as chamar:
            self.p.ler()
        self.assertEqual(chamar.call_args.args[3]['pagina'], 2)
        self.assertEqual(a['leitura_agente']['feitos'], 1)
        self.assertFalse(a['leitura_agente']['concluida'])

    def test_brainstorm_parcial_nao_exige_experimento_para_publicar(self):
        for nome in ['A','B','C']:
            a = self.artigo(nome)
            a['perfil_revisao'] = dict(revisao=self.p.revisao, problema='P', solucao='S', limites='L')
            a['leitura_agente'] = {'revisao': self.p.revisao, 'assinatura': nome, 'feitos': 1, 'total': 20, 'tipo': 'pdf', 'concluida': False}
        resposta = {'panorama': 'Há três abordagens.', 'ideias': [{'titulo':'Experimento comparativo', 'contribuicao':'Comparar A e C.', 'oportunidade':'Avaliação distinta.', 'fontes':['A','C']}]}
        with patch('src.revisao.chamar', return_value=resposta) as chamar:
            self.p.propor()
        self.assertEqual(len(chamar.call_args.args[3]['trabalhos']), 3)
        self.assertEqual(len(self.p.estado['propostas']), 1)
        self.p.painel()
        rel = (self.root / 'dados/anotacoes-ia.md').read_text(encoding='utf-8')
        self.assertIn('Comparar A e C.', rel)
        self.assertIn('Caminho experimental ainda em desenvolvimento', rel)

    def test_falha_no_detalhamento_nao_remove_sugestao(self):
        self.p.estado['propostas'] = [{'id':'ideia', 'revisao':self.p.revisao, 'titulo':'Ideia'}]
        path = self.root / 'dados/propostas/ideia.json'
        motor.json_gravar(path, {'modo':'brainstorm', 'titulo':'Ideia', 'meu_trabalho':'Comparar soluções'})
        with patch('src.revisao.chamar', side_effect=ValueError('Falha')):
            revisao.detalhar(self.p)
        self.assertEqual(motor.ler_json(path, {})['meu_trabalho'], 'Comparar soluções')
        self.assertEqual(len(self.p.estado['propostas']), 1)

    def test_redacao_focada_publica_introducao_e_filtra_fontes(self):
        self.p.cfg['modo_pesquisa'] = 'focada'
        with patch('src.revisao.matriz', return_value=[{
            'id': 'A', 'titulo': 'SSI em cidades inteligentes',
            'escopo': {'tipo': 'pdf', 'feitos': 2, 'total': 2, 'concluida': True},
            'fichas_amostradas': [{'id': 'ficha-A', 'pagina': 1, 'resumo': 'SSI.',
                                   'evidencias': [{'afirmacao': 'Credencial verificável', 'citacao': 'verifiable credential'}]}],
        }]), patch('src.revisao.chamar', return_value={
            'introducao': ['Introdução [A].', 'Problema [A].', 'Objetivo [A].'],
            'fundamentacao_teorica': [
                {'titulo': 'SSI', 'texto': 'Fundamentação [A].', 'fontes': ['A']},
                {'titulo': 'Segurança', 'texto': 'Segurança [A].', 'fontes': ['A']},
                {'titulo': 'Governança', 'texto': 'Governança [A].', 'fontes': ['A']},
                {'titulo': 'Revogação', 'texto': 'Revogação [A].', 'fontes': ['A']},
            ],
            'mapa_fases': [{'fase': 'Revogação', 'acoes_cidadao': 'Solicita.', 'acoes_entidades': 'Publicam estado.',
                            'riscos': 'Perda de acesso.', 'estado_da_arte': 'Descrito em [A].',
                            'lacunas': 'Recuperação.', 'fontes': ['A', 'inventada']}],
            'fontes_usadas': ['A', 'inventada'],
        }):
            self.assertTrue(revisao.redigir_pesquisa_focada(self.p))
        self.assertEqual(self.p.estado['redacao_focada']['fontes_usadas'], ['A'])
        self.assertEqual(self.p.estado['redacao_focada']['mapa_fases'][0]['fontes'], ['A'])
        self.p.painel()
        redacao = (self.root / 'obsidian/TRABALHO.md').read_text(encoding='utf-8')
        self.assertIn('## Introdução', redacao)
        self.assertIn('Introdução [A].', redacao)
        self.assertNotIn('[inventada]', redacao)

    def test_dialogo_focado_le_anotacoes_trabalho_memoria_e_registra_consultas(self):
        self.p.cfg['modo_pesquisa'] = 'focada'
        self.base.ANOTACOES_PESQUISADOR.write_text('Decisão do pesquisador: priorizar recuperação.', encoding='utf-8')
        self.base.TRABALHO.write_text('# Trabalho atual\nTexto já consolidado.', encoding='utf-8')
        self.base.ANOTACOES_IA.write_text('# Memória\nJá verifiquei revogação.', encoding='utf-8')
        with patch('src.revisao.matriz', return_value=[{
            'id': 'A', 'titulo': 'Fonte SSI',
            'escopo': {'tipo': 'pdf', 'feitos': 1, 'total': 1, 'concluida': True},
            'fichas_amostradas': [{'id': 'ficha-A', 'pagina': 1, 'resumo': 'Resumo.', 'evidencias': []}],
        }]), patch('src.revisao.chamar', return_value={
            'introducao': ['Contexto [A].', 'Problema [A].', 'Objetivo [A].'],
            'fundamentacao_teorica': [
                {'titulo': 'SSI', 'texto': 'Fundamentação [A].', 'fontes': ['A']},
                {'titulo': 'Segurança', 'texto': 'Segurança [A].', 'fontes': ['A']},
                {'titulo': 'Governança', 'texto': 'Governança [A].', 'fontes': ['A']},
                {'titulo': 'Recuperação', 'texto': 'Recuperação [A].', 'fontes': ['A']},
            ],
            'mapa_fases': [], 'fontes_usadas': ['A'],
            'consultas_novas': ['SSI recuperação social smart cities'],
        }) as chamar:
            self.assertTrue(revisao.redigir_pesquisa_focada(self.p))
        dados = chamar.call_args.args[3]
        self.assertIn('Decisão do pesquisador', dados['anotacoes_do_pesquisador'])
        self.assertIn('Texto já consolidado', dados['trabalho_atual'])
        self.assertIn('Já verifiquei revogação', dados['memoria_operacional_da_ia'])
        self.assertTrue(any(
            item.get('consulta') == 'SSI recuperação social smart cities'
            for item in self.p.estado['consultas'].values()
        ))
    def test_extrai_decisoes_humanas_do_dialogo(self):
        texto = """# Anotações

<!-- agente:dialogo:inicio -->
#### 1. Recuperação social
resposta_pesquisador: aprovar se comparar com guardians.
#### 2. Identidade biométrica
resposta_pesquisador: rejeitar, não quero ir nessa direção.
#### 3. Revogação
resposta_pesquisador: revisar com mais fontes.
<!-- agente:dialogo:fim -->
"""
        decisoes = revisao.extrair_decisoes_pesquisador(texto)
        self.assertEqual(decisoes['aprovadas'][0]['titulo'], 'Recuperação social')
        self.assertEqual(decisoes['rejeitadas'][0]['titulo'], 'Identidade biométrica')
        self.assertEqual(decisoes['revisar'][0]['titulo'], 'Revogação')

