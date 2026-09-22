import unittest
from unittest.mock import patch, Mock
import requests
import test_motor


class BuscasTest(unittest.TestCase):
    setUp = test_motor.PesquisaTest.setUp

    def test_doi_equivalente(self):
        self.assertEqual(self.p._chave_artigo({'doi':'https://doi.org/10.123/ABC'}),
                         self.p._chave_artigo({'doi':'10.123/abc'}))


    def test_fallback_openalex_quando_semantic_scholar_da_limite(self):
        sem = Mock()
        sem.raise_for_status.side_effect = requests.HTTPError('429 Too Many Requests')
        oa = Mock()
        oa.json.return_value = {'results': [{
            'id': 'https://openalex.org/W1',
            'title': 'Open smart city identity',
            'publication_year': 2025,
            'abstract_inverted_index': {'Smart': [0], 'city': [1], 'identity': [2]},
            'authorships': [],
            'best_oa_location': {'pdf_url': 'https://example.org/a.pdf', 'landing_page_url': 'https://example.org/a'},
            'open_access': {'is_oa': True},
        }]}
        self.p.cfg.update(ano_minimo=2025, resultados_por_consulta=10,
                          fonte_academica_principal='semantic_scholar',
                          fontes_academicas_auxiliares=['openalex'])
        with patch('src.motor.requests.get', side_effect=[sem, oa]) as get:
            resultados, fontes = self.p.buscar_fontes_academicas('smart city identity', 1)
        self.assertEqual(get.call_count, 2)
        self.assertEqual(fontes, ['OpenAlex'])
        self.assertEqual(resultados[0]['title'], 'Open smart city identity')
        self.assertEqual(resultados[0]['best_oa_location']['pdf_url'], 'https://example.org/a.pdf')

    def test_semantic_scholar_pode_ser_fonte_principal_configurada(self):
        sem = Mock()
        sem.json.return_value = {'data':[{'paperId':'1','title':'IoT revocation','year':2025,'abstract':'A useful abstract.'}]}
        self.p.cfg.update(ano_minimo=2025, resultados_por_consulta=10, fonte_academica_principal='semantic_scholar', fontes_academicas_auxiliares=[])
        with patch('src.motor.requests.get', return_value=sem) as get:
            resultados, fontes = self.p.buscar_fontes_academicas('IoT revocation',1)
        self.assertEqual(get.call_count, 1)
        self.assertEqual(resultados[0]['abstract'], 'A useful abstract.')
        self.assertIn('Semantic Scholar',fontes)
        self.assertEqual(fontes, ['Semantic Scholar'])
