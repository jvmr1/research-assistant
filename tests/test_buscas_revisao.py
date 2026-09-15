import unittest
from unittest.mock import patch, Mock
import requests
import test_motor


class BuscasTest(unittest.TestCase):
    setUp = test_motor.PesquisaTest.setUp

    def test_doi_equivalente(self):
        self.assertEqual(self.p._chave_artigo({'doi':'https://doi.org/10.123/ABC'}),
                         self.p._chave_artigo({'doi':'10.123/abc'}))

    def test_semantic_scholar_e_fonte_principal_por_padrao(self):
        sem = Mock()
        sem.json.return_value = {'data':[{'paperId':'1','title':'IoT revocation','year':2025,'abstract':'A useful abstract.'}]}
        self.p.cfg.update(ano_minimo=2025, resultados_por_consulta=10, fonte_academica_principal='semantic_scholar', fontes_academicas_auxiliares=[])
        with patch('motor.requests.get', return_value=sem) as get:
            resultados, fontes = self.p.buscar_fontes_academicas('IoT revocation',1)
        self.assertEqual(get.call_count, 1)
        self.assertEqual(resultados[0]['abstract'], 'A useful abstract.')
        self.assertIn('Semantic Scholar',fontes)
        self.assertEqual(fontes, ['Semantic Scholar'])
