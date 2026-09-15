import unittest
from unittest.mock import patch, Mock
import requests
import test_motor


class BuscasTest(unittest.TestCase):
    setUp = test_motor.PesquisaTest.setUp

    def test_doi_equivalente(self):
        self.assertEqual(self.p._chave_artigo({'doi':'https://doi.org/10.123/ABC'}),
                         self.p._chave_artigo({'doi':'10.123/abc'}))

    def test_outras_fontes_funcionam_com_openalex_indisponivel(self):
        sem = Mock()
        sem.json.return_value = {'data':[{'paperId':'1','title':'IoT revocation','year':2025,'abstract':'A useful abstract.'}]}
        cross = Mock()
        cross.json.return_value = {'message':{'items':[]}}
        self.p.cfg.update(ano_minimo=2025, resultados_por_consulta=10)
        with patch('motor.requests.get', side_effect=[requests.ConnectionError('offline'),sem,cross]):
            resultados, fontes = self.p.buscar_fontes_academicas('IoT revocation',1)
        self.assertEqual(resultados[0]['abstract'], 'A useful abstract.')
        self.assertIn('Semantic Scholar',fontes)
        self.assertNotIn('OpenAlex',fontes)
