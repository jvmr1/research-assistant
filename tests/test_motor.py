import json
from pathlib import Path
import tempfile
import types
import unittest
from unittest.mock import patch

import agente
import motor


class PesquisaTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.base = types.SimpleNamespace(**{k: getattr(agente, k) for k in dir(agente) if not k.startswith('__')})
        self.base.ROOT = self.root
        self.base.ARTIGOS = self.root / 'vault/trabalhos'
        self.base.INSTRUCOES = self.root / 'vault/INSTRUCOES.md'
        self.base.INSTRUCOES.parent.mkdir(parents=True)
        self.texto = '# Decisões\nInvestigar revogação, sem exigir blockchain.\n## Consultas iniciais\n- IoT revocation\n- ano mínimo: 2025\n'
        self.base.INSTRUCOES.write_text(self.texto, encoding='utf-8')
        self.base.carregar_instrucoes = lambda: {'consultas': ['IoT revocation'], 'ano_minimo': 2025,
                                                'modelo_ollama': 'modelo-teste', 'artigos_por_ciclo_ia': 10,
                                                'resultados_por_consulta': 10}
        self.p = motor.Pesquisa(self.base)
        self.p.configurar()

    def artigo(self, nome, resumo=True):
        a = {'id_openalex': 'https://openalex.org/' + nome, 'nome_local': nome, 'titulo': nome,
             'resumo': {'A': [0], 'system': [1]} if resumo else None, 'url': 'https://example.org/' + nome,
             'status': 'triagem_pendente', 'pdf_local': ''}
        self.p.artigos.append(a)
        return a

    def test_instrucoes_preservadas_e_transmitidas(self):
        self.artigo('A')
        with patch('motor.gerar', return_value={'classificacao': 'priorizar', 'justificativa': 'Revogação'}) as gerar:
            self.p.triagem()
        self.assertEqual(gerar.call_args.args[1], self.texto)
        self.p.painel()
        self.assertEqual(self.base.INSTRUCOES.read_text(encoding='utf-8'), self.texto)
        self.assertTrue((self.root / 'vault/RELATORIO.md').exists())

    def test_variaveis_de_busca_geram_consultas(self):
        self.base.INSTRUCOES.write_text(
            '# Decisões\n## Variáveis de busca\n- domínio: smart cities, IoT\n- tecnologia: blockchain, self sovereign identity\n- problema: access control\n## Consultas iniciais\n- busca manual\n',
            encoding='utf-8')
        cfg = agente.carregar_instrucoes(self.base.INSTRUCOES)
        self.assertIn('busca manual', cfg['consultas'])
        self.assertTrue(any('blockchain' in q and 'access control' in q for q in cfg['consultas']))
        self.assertIn('tecnologia', cfg['variaveis_busca'])

    def test_preleitura_aprova_antes_da_leitura_integral(self):
        a = self.artigo('A')
        a['pdf_local'] = 'pdfs/A.pdf'
        a['triagem_agente'] = {'revisao': self.p.revisao, 'classificacao': 'priorizar'}
        with patch.object(self.p, 'trechos', return_value=[{'pagina': 1, 'texto': 'Introduction smart city access control. Conclusion aligned contribution.', 'tipo': 'pdf'}]), \
             patch('motor.gerar', return_value={'decisao': 'ler_integralmente', 'justificativa': 'alinhado', 'evidencias': ['access control']}):
            self.p.pre_leitura()
        self.assertEqual(a['pre_leitura_agente']['decisao'], 'ler_integralmente')
        self.assertTrue(self.p.aprovado_preleitura(a))


    def test_resolve_texto_aberto_via_unpaywall(self):
        a = self.artigo('A')
        a['doi'] = '10.1234/teste'
        a['triagem_agente'] = {'revisao': self.p.revisao, 'classificacao': 'priorizar'}
        resposta = types.SimpleNamespace(
            status_code=200,
            raise_for_status=lambda: None,
            json=lambda: {'best_oa_location': {'url_for_pdf': 'https://repo.example/a.pdf', 'url_for_landing_page': 'https://repo.example/a'}}
        )
        with patch('motor.requests.get', return_value=resposta):
            self.assertTrue(self.p.resolver_texto_aberto(a))
        self.assertEqual(a['url_pdf'], 'https://repo.example/a.pdf')
        self.assertTrue(a['acesso_aberto'])
        self.assertIn('Unpaywall', a['fontes_texto_completo'])

    def test_resolve_texto_aberto_via_semantic_scholar_quando_unpaywall_nao_tem(self):
        a = self.artigo('A')
        a['doi'] = '10.1234/teste'
        a['triagem_agente'] = {'revisao': self.p.revisao, 'classificacao': 'priorizar'}
        respostas = [
            types.SimpleNamespace(status_code=404, raise_for_status=lambda: None, json=lambda: {}),
            types.SimpleNamespace(status_code=200, raise_for_status=lambda: None,
                                  json=lambda: {'externalIds': {'DOI': '10.1234/teste'}, 'url': 'https://semanticscholar.org/paper/x',
                                                'openAccessPdf': {'url': 'https://pdf.example/a.pdf'}}),
        ]
        with patch('motor.requests.get', side_effect=respostas):
            self.assertTrue(self.p.resolver_texto_aberto(a))
        self.assertEqual(a['url_pdf'], 'https://pdf.example/a.pdf')
        self.assertIn('Semantic Scholar', a['fontes_texto_completo'])

    def test_preleitura_descarta_sem_texto_integral(self):
        a = self.artigo('A')
        a['triagem_agente'] = {'revisao': self.p.revisao, 'classificacao': 'priorizar'}
        with patch.object(self.p, 'trechos', return_value=[{'pagina': None, 'texto': 'Resumo apenas.', 'tipo': 'resumo'}]), \
             patch('motor.gerar') as gerar:
            self.p.pre_leitura()
        self.assertEqual(a['pre_leitura_agente']['decisao'], 'descartar_sem_texto_integral')
        self.assertFalse(self.p.aprovado_preleitura(a))
        gerar.assert_not_called()

    def test_preleitura_com_texto_nao_registra_falsa_falta_de_texto(self):
        a = self.artigo('A')
        a['triagem_agente'] = {'revisao': self.p.revisao, 'classificacao': 'priorizar'}
        a['pdf_local'] = 'pdfs/A.pdf'
        with patch.object(self.p, 'trechos', return_value=[{'pagina': 1, 'texto': 'Introdução e conclusão alinhadas.', 'tipo': 'pdf'}]), \
             patch('motor.gerar', return_value={'decisao': 'descartar_sem_texto_integral', 'justificativa': 'modelo confundiu a decisão'}):
            self.p.pre_leitura()
        self.assertEqual(a['pre_leitura_agente']['decisao'], 'precisa_texto_melhor')
        self.assertIn('texto integral local', a['pre_leitura_agente']['justificativa'])

    def test_sem_resumo_nao_bloqueia_os_seguintes(self):
        a = self.artigo('SemResumo', False)
        b = self.artigo('ComResumo')
        with patch('motor.gerar', return_value={'classificacao': 'priorizar', 'justificativa': 'Relevante'}) as gerar:
            self.p.triagem()
            self.p.triagem()
        self.assertEqual(gerar.call_count, 1)
        self.assertEqual(a['triagem_agente']['classificacao'], 'sem_resumo')
        self.assertEqual(b['triagem_agente']['classificacao'], 'priorizar')

    def test_falha_e_retomada_sem_repetir_concluida(self):
        self.assertEqual(self.p.tarefa('ok', lambda: 'feito'), 'feito')
        def falhar():
            raise ValueError('modelo indisponível')
        self.p.tarefa('erro', falhar)
        nova = motor.Pesquisa(self.base)
        self.assertIsNone(nova.tarefa('ok', lambda: self.fail('Reexecutou tarefa concluída')))
        self.assertIsNone(nova.tarefa('erro', lambda: self.fail('Ignorou o intervalo')))
        self.assertTrue(nova.estado['tarefas']['ok']['feito'])

    def test_citacao_inventada_rejeitada(self):
        with self.assertRaises(ValueError):
            motor.validar_ficha({'resumo': 'Teste', 'evidencias': [{'afirmacao': 'x', 'citacao': 'inventado'}]}, 'A system')
        motor.validar_ficha({'resumo': 'Teste', 'evidencias': [{'afirmacao': 'x', 'citacao': 'A system'}]}, 'A\n system')

    def test_leitura_evidencia_pagina_e_retomada(self):
        a = self.artigo('A')
        a['triagem_agente'] = {'revisao': self.p.revisao, 'classificacao': 'priorizar'}
        a['pre_leitura_agente'] = {'revisao': self.p.revisao, 'decisao': 'ler_integralmente', 'justificativa': 'teste'}
        ficha = {'resumo': 'O texto descreve um sistema.', 'evidencias': [{'afirmacao': 'Sistema', 'citacao': 'A system'}]}
        def responder(modelo, orientacao, tarefa, dados, **kwargs):
            if tarefa.startswith('Consolide'):
                return {'resumo': 'Resumo consolidado.', 'lacunas_possiveis': [], 'propostas_possiveis': []}
            return ficha.copy()
        with patch('motor.gerar', side_effect=responder) as gerar:
            self.p.ler()
            self.p.ler()
        self.assertEqual(gerar.call_count, 2)
        self.assertTrue(a['leitura_agente']['concluida'])
        self.assertEqual(a['sintese_artigo']['resumo'], 'Resumo consolidado.')
        self.assertEqual(a['leitura_agente']['tipo'], 'resumo')
        self.p.painel()
        nota = self.root / 'vault/trabalhos/A.md'
        self.assertIn('Página resumo', nota.read_text(encoding='utf-8'))

    def test_trabalho_ja_sintetizado_nao_e_relido(self):
        a = self.artigo('A')
        b = self.artigo('B')
        for artigo in (a, b):
            artigo['triagem_agente'] = {'revisao': self.p.revisao, 'classificacao': 'priorizar'}
            artigo['pre_leitura_agente'] = {'revisao': self.p.revisao, 'decisao': 'ler_integralmente', 'justificativa': 'teste'}
        a['leitura_agente'] = {'revisao': self.p.revisao, 'assinatura': 'a', 'feitos': 1, 'total': 1, 'concluida': True, 'tipo': 'resumo', 'paginas_sem_texto': []}
        a['sintese_artigo'] = {'revisao': self.p.revisao, 'assinatura': 'a', 'resumo': 'já analisado'}
        with patch.object(self.p, 'trechos', return_value=[{'pagina': None, 'texto': 'B system', 'tipo': 'resumo'}]) as trechos, \
                patch('motor.gerar', side_effect=lambda *args, **kwargs: {'resumo': 'B.', 'evidencias': [{'afirmacao': 'B', 'citacao': 'B system'}]}):
            self.p.ler()
        self.assertEqual(trechos.call_args.args[0]['nome_local'], 'B')
        self.assertEqual(a['sintese_artigo']['resumo'], 'já analisado')
        self.assertEqual(b['leitura_agente']['revisao'], self.p.revisao)
    def test_processa_um_trabalho_por_vez_reaproveitando_acervo_sem_teto(self):
        for i in range(12):
            self.artigo(f'A{i}')
        with patch.object(self.p, 'buscar') as buscar:
            lote1 = self.p.preparar_lote()
            self.assertEqual(lote1['ids'], ['A0'])
            self.assertEqual(lote1.get('modo'), 'um_trabalho_por_vez')
            self.p.concluir_lote()
            lote2 = self.p.preparar_lote()
        buscar.assert_not_called()
        self.assertEqual(lote2['ids'], ['A1'])
        self.assertNotIn('max_artigos_acervo', self.p.cfg)

    def test_le_um_artigo_inteiro_antes_do_seguinte(self):
        a = self.artigo('A')
        b = self.artigo('B')
        for artigo in (a, b):
            artigo['triagem_agente'] = {'revisao': self.p.revisao, 'classificacao': 'priorizar'}
            artigo['pre_leitura_agente'] = {'revisao': self.p.revisao, 'decisao': 'ler_integralmente', 'justificativa': 'teste'}
        trechos_a = [{'pagina': 1, 'texto': 'um', 'tipo': 'pdf'},
                     {'pagina': 2, 'texto': 'dois', 'tipo': 'pdf'}]
        def trechos(artigo):
            return trechos_a if artigo is a else [{'pagina': 1, 'texto': 'tres', 'tipo': 'pdf'}]
        def resposta(p, etapa, tarefa, dados, esquema=None):
            if etapa == 'sintese-artigo':
                return {'resumo': 'A completo.', 'lacunas_possiveis': [], 'propostas_possiveis': []}
            return {'resumo': dados['texto'], 'evidencias': []}
        with patch.object(self.p, 'trechos', side_effect=trechos), \
                patch('revisao.chamar', side_effect=resposta):
            self.p.ler()
        self.assertEqual(a['leitura_agente']['feitos'], 2)
        self.assertTrue(a['leitura_agente']['concluida'])
        self.assertNotIn('leitura_agente', b)

    def test_orientacao_nova_preserva_acervo_e_propostas(self):
        self.artigo('A')
        antiga = self.p.revisao
        self.p.estado['propostas'].append({'id': 'antiga', 'titulo': 'Antiga', 'revisao': antiga})
        self.base.INSTRUCOES.write_text(self.texto + '\nNova decisão: medir latência.', encoding='utf-8')
        self.p.configurar()
        self.p.painel()
        self.assertNotEqual(antiga, self.p.revisao)
        self.assertEqual(len(self.p.artigos), 1)
        self.assertEqual(len(self.p.estado['propostas']), 1)
        self.assertIn('orientações anteriores', (self.root / 'vault/RELATORIO.md').read_text(encoding='utf-8'))

    def test_proposta_usa_fontes_reais_e_registra_buscas(self):
        for nome in ['A', 'B']:
            a = self.artigo(nome)
            a['triagem_agente'] = {'revisao': self.p.revisao, 'classificacao': 'priorizar'}
            a['pre_leitura_agente'] = {'revisao': self.p.revisao, 'decisao': 'ler_integralmente', 'justificativa': 'teste'}
        with patch('motor.gerar', side_effect=lambda *args, **kwargs: {'resumo': 'Sistema.', 'evidencias': [{'afirmacao': 'Sistema', 'citacao': 'A system'}]}):
            self.p.ler()
            self.p.ler()
        def propor(modelo, orientacao, tarefa, dados, **kwargs):
            fontes = dados['trabalhos']
            self.assertEqual({f['id'] for f in fontes}, {'A', 'B'})
            return {'panorama': 'Panorama acumulado do modelo.', 'ideias': [{'titulo': 'Ideia', 'oportunidade': 'Investigar revogação',
                'contribuicao': 'Conteúdo do modelo meu_trabalho', 'fontes': ['A', 'B']}], 'buscas': ['IoT revocation experiment']}
        with patch('motor.gerar', side_effect=propor):
            self.p.propor()
            self.p.propor()
        self.assertEqual(len(self.p.estado['propostas']), 1)
        self.p.painel()
        path = self.root / 'vault/RELATORIO.md'
        texto = path.read_text(encoding='utf-8')
        self.assertIn('O que seria o meu trabalho', texto)
        self.assertIn('Conteúdo do modelo meu_trabalho', texto)
        self.assertEqual(len(self.p.estado['consultas']), 1)

    def test_feedback_humano_cria_consultas_direcionadas(self):
        a = self.artigo('A')
        a['titulo'] = 'Blockchain access control for smart cities'
        a['consulta'] = 'blockchain smart cities access control'
        self.p.estado['propostas'] = [{'id': 'p1', 'titulo': 'Controle de acesso adaptativo', 'revisao': self.p.revisao, 'fontes': ['A']}]
        motor.json_gravar(self.root / 'dados/propostas/p1.json', {
            'id': 'p1', 'titulo': 'Controle de acesso adaptativo', 'fontes': ['A'],
            'meu_trabalho': 'Avaliar controle de acesso com identidade descentralizada em cidades inteligentes.',
            'hipotese_lacuna': 'Falta avaliação integrada entre identidade e controle de acesso.'
        })
        (self.root / 'vault/AVALIAR-PROPOSTAS.md').write_text(
            '# Avaliar propostas\n\n## Controle de acesso adaptativo\nid: p1\navaliacao: gostei\ncomentario: direção promissora\n',
            encoding='utf-8')
        self.p.aplicar_feedback_propostas()
        consultas = list(self.p.estado['consultas'].values())
        self.assertTrue(any('feedback humano' in c['origem'] for c in consultas))
        self.assertTrue(any('access control' in c['consulta'] or 'identity' in c['consulta'] for c in consultas))

    def test_resposta_truncada_nao_aceita(self):
        class Response:
            def __enter__(self): return self
            def __exit__(self, *a): pass
            def raise_for_status(self): pass
            def iter_lines(self):
                yield json.dumps({'response': '{}', 'done': True, 'done_reason': 'length'}).encode()
        with patch('motor.requests.post', return_value=Response()), self.assertRaisesRegex(ValueError, 'cortada'):
            motor.gerar('teste', '', '', {})

    def test_openrouter_retorna_json_usando_chave_do_ambiente(self):
        resposta = types.SimpleNamespace()
        resposta.raise_for_status = lambda: None
        resposta.json = lambda: {'choices': [{'message': {'content': '{"ok": true}'}}]}
        with patch.dict('os.environ', {'OPENROUTER_API_KEY': 'chave-de-teste'}), \
             patch('motor.requests.post', return_value=resposta) as post:
            resultado = motor.gerar('openrouter/free', 'orientação', 'tarefa', {'x': 1})
        self.assertEqual(resultado, {'ok': True})
        self.assertEqual(post.call_args.kwargs['headers']['Authorization'], 'Bearer chave-de-teste')

    def test_ctrl_c_nao_marca_tarefa_concluida(self):
        def interromper():
            raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):
            self.p.tarefa('interrompida', interromper)
        self.assertNotIn('interrompida', self.p.estado['tarefas'])

    def test_pdf_real_extrai_paginas_e_detecta_pagina_sem_texto(self):
        from pypdf import PdfWriter
        from pypdf.generic import DecodedStreamObject, NameObject, DictionaryObject
        path = self.root / 'pdfs/teste.pdf'
        path.parent.mkdir()
        writer = PdfWriter()
        page = writer.add_blank_page(width=600, height=800)
        fonte = DictionaryObject({NameObject('/Type'): NameObject('/Font'), NameObject('/Subtype'): NameObject('/Type1'), NameObject('/BaseFont'): NameObject('/Helvetica')})
        page[NameObject('/Resources')] = DictionaryObject({NameObject('/Font'): DictionaryObject({NameObject('/F1'): fonte})})
        stream = DecodedStreamObject()
        stream.set_data(b'BT /F1 12 Tf 50 700 Td (A system) Tj ET')
        page[NameObject('/Contents')] = writer._add_object(stream)
        writer.add_blank_page(width=600, height=800)
        writer.write(path)
        a = self.artigo('PDF', False)
        a['pdf_local'] = 'pdfs/teste.pdf'
        trechos = self.p.trechos(a)
        self.assertEqual(trechos[0]['pagina'], 1)
        self.assertIn('A system', trechos[0]['texto'])
        self.assertEqual(trechos[1]['tipo'], 'pdf_sem_texto')
        self.assertEqual(trechos[1]['pagina'], 2)

    def test_html_local_extrai_texto_como_fonte_de_leitura(self):
        path = self.root / 'pdfs/teste.html'
        path.parent.mkdir()
        path.write_text('<html><script>ignorar()</script><h1>Título</h1><p>Texto aberto.</p></html>', encoding='utf-8')
        a = self.artigo('HTML', False)
        a['texto_local'] = 'pdfs/teste.html'
        trechos = self.p.trechos(a)
        self.assertEqual(trechos[0]['tipo'], 'html')
        self.assertIn('Título Texto aberto.', trechos[0]['texto'])

    def test_decisao_humana_irrelevante_respeitada(self):
        a = self.artigo('A')
        self.base.ARTIGOS.mkdir(parents=True)
        nota = self.base.ARTIGOS / 'A.md'
        original = '---\nstatus: irrelevante\n---\nDecisão do orientador: fora de escopo.'
        nota.write_text(original, encoding='utf-8')
        with patch('motor.gerar') as gerar:
            self.p.triagem()
        gerar.assert_not_called()
        self.assertEqual(nota.read_text(encoding='utf-8'), original)

    def test_tags_sao_tematicas_e_nao_genericas(self):
        tags = agente.criar_tags(
            'smart city interoperability blockchain',
            {'titulo': 'Privacy preserving data sharing', 'resumo': 'IoT access control'},
        )
        self.assertIn('cidades-inteligentes', tags)
        self.assertIn('interoperabilidade', tags)
        self.assertIn('blockchain', tags)
        self.assertIn('privacidade', tags)
        self.assertIn('iot', tags)
        self.assertNotIn('artigo', tags)
        self.assertNotIn('status/novo', tags)

    def test_modelos_ia_nao_usa_reserva_ollama_sem_modelo_instalado(self):
        self.p.cfg['modelo_ia'] = 'openrouter'
        self.p.cfg['modelo_openrouter'] = 'openai/gpt-oss-120b'
        self.p.cfg['modelo_ollama'] = 'qwen2.5:7b-instruct-q4_K_M'
        with patch.dict('motor.os.environ', {'OPENROUTER_API_KEY': 'x'}, clear=False), \
             patch('motor.garantir_ollama_rodando') as tags:
            tags.return_value.json.return_value = {'models': [{'name': 'outro-modelo'}]}
            modelos = self.p.modelos_ia()
        self.assertEqual(modelos, ['openai/gpt-oss-120b'])

    def test_modelo_ausente_nao_inicia_inferencia(self):
        from unittest.mock import Mock
        resposta = Mock()
        resposta.json.return_value = {'models': [{'name': 'outro-modelo'}]}
        with patch('motor.requests.get', return_value=resposta), patch('motor.gerar') as gerar:
            self.assertFalse(self.p.modelo_disponivel())
        gerar.assert_not_called()
        self.assertIn('ainda não instalado', self.p.mensagem)


if __name__ == '__main__':
    unittest.main()


