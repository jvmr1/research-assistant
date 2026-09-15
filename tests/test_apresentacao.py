import test_motor
import unittest
from pathlib import Path
import motor


class ApresentacaoTest(unittest.TestCase):
    setUp = test_motor.PesquisaTest.setUp
    artigo = test_motor.PesquisaTest.artigo
    def test_area_de_leitura_so_tres_entradas(self):
        a = self.artigo('A')
        a['pdf_local'] = 'pdfs/A.pdf'
        self.p.painel()
        self.assertEqual({p.name for p in (self.root / 'vault').iterdir()}, {
            'INSTRUCOES.md', 'RELATORIO.md', 'METODOLOGIA-REVISAO.md',
            'TRABALHOS-SEM-PROPOSTA.md', 'AVALIAR-PROPOSTAS.md', 'trabalhos',
        })

    def test_artigo_sem_texto_nao_cria_nota_no_grafo(self):
        self.artigo('A')
        self.p.painel()
        self.assertFalse((self.root / 'vault/trabalhos/A.md').exists())
        sem_proposta = (self.root / 'vault/TRABALHOS-SEM-PROPOSTA.md').read_text(encoding='utf-8')
        self.assertIn('`A`', sem_proposta)

    def test_relatorio_principal_nao_lista_acervo(self):
        self.artigo('A')
        self.p.painel()
        rel = (self.root / 'vault/RELATORIO.md').read_text(encoding='utf-8')
        self.assertNotIn('## Trabalhos do acervo', rel)
        self.assertNotIn('TRABALHOS-SEM-PROPOSTA.md', rel)
        self.assertNotIn('METODOLOGIA-REVISAO.md', rel)
        self.assertNotIn('INSTRUCOES.md', rel)

    def test_tags_do_trabalho_usam_frontmatter_inline(self):
        a = self.artigo('A')
        a['pdf_local'] = 'pdfs/A.pdf'
        self.base.ARTIGOS.mkdir(parents=True, exist_ok=True)
        (self.base.ARTIGOS / 'A.md').write_text(
            '---\ntags:\n  - artigo\n  - status/novo\n---\n# A\n\n## Tags\n\n#artigo #status/novo\n',
            encoding='utf-8',
        )
        self.p.painel()
        nota = (self.root / 'vault/trabalhos/A.md').read_text(encoding='utf-8')
        self.assertRegex(nota, r'(?m)^tags: \[[^\n]*\]$')
        self.assertNotRegex(nota, r'(?m)^  - (artigo|status/novo)$')

    def test_nota_exibe_entendimento_consolidado_do_trabalho(self):
        artigo = self.artigo('A')
        artigo['perfil_revisao'] = {
            'revisao': self.p.revisao,
            'problema': 'Problema sustentado por ficha.',
            'solucao': 'Abordagem descrita.',
            'limites': 'Limite observado.',
            'possibilidades': 'Extensão possível.',
        }
        artigo['sintese_artigo'] = {
            'revisao': self.p.revisao,
            'resumo': 'Síntese para leitura humana.',
            'lacunas_possiveis': ['Lacuna a investigar.'],
            'propostas_possiveis': ['Contribuição possível.'],
        }
        self.p.painel()
        nota = (self.root / 'vault/trabalhos/A.md').read_text(encoding='utf-8')
        self.assertIn('## Entendimento consolidado do trabalho', nota)
        self.assertIn('Síntese para leitura humana.', nota)
        self.assertIn('Lacuna a investigar.', nota)

    def test_relatorio_contem_proposta_completa_e_relacoes(self):
        a = self.artigo('A')
        b = self.artigo('B')
        a['referencias_openalex'] = [b['id_openalex']]
        self.p.estado['propostas'] = [{'id': 'p', 'titulo': 'Revogação eficiente', 'revisao': self.p.revisao}]
        motor.json_gravar(self.root / 'dados/propostas/p.json', {
            'fontes': ['A', 'B'], 'meu_trabalho': 'Implementar revogação incremental.',
            'interpretacao': 'A e B usam estratégias diferentes.',
            'alteracao_sobre_trabalhos_proximos': 'Modificar a política de B.', 'buscas': []})
        self.p.painel()
        rel = (self.root / 'vault/RELATORIO.md').read_text(encoding='utf-8')
        self.assertIn('Implementar revogação incremental.', rel)
        nota_a = (self.root / 'vault/trabalhos/A.md').read_text(encoding='utf-8')
        nota_b = (self.root / 'vault/trabalhos/B.md').read_text(encoding='utf-8')
        self.assertIn('Referencia: [B](B.md)', nota_a)
        self.assertIn('É citado por: [A](A.md)', nota_b)
        self.assertIn('A e B usam estratégias diferentes.', nota_a)

    def test_anotacoes_humanas_preservadas_ao_atualizar(self):
        a = self.artigo('A')
        a['pdf_local'] = 'pdfs/A.pdf'
        self.p.painel()
        nota = self.root / 'vault/trabalhos/A.md'
        nota.write_text('Minha observação pessoal.\n' + nota.read_text(encoding='utf-8') + '\nDecisão do orientador.', encoding='utf-8')
        self.p.painel()
        self.p.painel()
        texto = nota.read_text(encoding='utf-8')
        self.assertTrue(texto.startswith('Minha observação pessoal.'))
        self.assertTrue(texto.endswith('Decisão do orientador.'))
        self.assertEqual(texto.count('<!-- agente:inicio -->'), 1)
