import unittest
from unittest.mock import patch
import test_motor
import motor
import revisao


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
        with patch('revisao.chamar', return_value={'problema': 'Resumo já produzido.'}) as chamar:
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
        with patch.object(self.p, 'trechos', return_value=ts), patch('revisao.chamar', return_value={'resumo': 'Segundo.', 'evidencias': []}) as chamar:
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
        with patch('revisao.chamar', return_value=resposta) as chamar:
            self.p.propor()
        self.assertEqual(len(chamar.call_args.args[3]['trabalhos']), 3)
        self.assertEqual(len(self.p.estado['propostas']), 1)
        self.p.painel()
        rel = (self.root / 'vault/RELATORIO.md').read_text(encoding='utf-8')
        self.assertIn('Comparar A e C.', rel)
        self.assertIn('Caminho experimental ainda em desenvolvimento', rel)

    def test_falha_no_detalhamento_nao_remove_sugestao(self):
        self.p.estado['propostas'] = [{'id':'ideia', 'revisao':self.p.revisao, 'titulo':'Ideia'}]
        path = self.root / 'dados/propostas/ideia.json'
        motor.json_gravar(path, {'modo':'brainstorm', 'titulo':'Ideia', 'meu_trabalho':'Comparar soluções'})
        with patch('revisao.chamar', side_effect=ValueError('Falha')):
            revisao.detalhar(self.p)
        self.assertEqual(motor.ler_json(path, {})['meu_trabalho'], 'Comparar soluções')
        self.assertEqual(len(self.p.estado['propostas']), 1)
