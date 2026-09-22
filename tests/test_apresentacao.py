import test_motor
import unittest
from pathlib import Path
from src import motor


class ApresentacaoTest(unittest.TestCase):
    setUp = test_motor.PesquisaTest.setUp
    artigo = test_motor.PesquisaTest.artigo
    def test_area_do_obsidian_nao_exibe_memoria_interna_da_ia(self):
        a = self.artigo('A')
        a['pdf_local'] = 'obsidian/referencias/pdfs/A.pdf'
        self.p.painel()
        entradas = {p.name for p in (self.root / 'obsidian').iterdir()}
        self.assertIn('ANOTACOES.md', entradas)
        self.assertNotIn('ANOTACOES-DA-IA.md', entradas)
        self.assertTrue((self.root / 'dados/anotacoes-ia.md').exists())

    def test_artigo_sem_texto_nao_cria_nota_no_grafo(self):
        self.artigo('A')
        self.p.painel()
        self.assertFalse((self.root / 'obsidian/referencias/fichamentos/A.md').exists())
        self.assertFalse((self.root / 'obsidian/TRABALHOS-SEM-PROPOSTA.md').exists())

    def test_relatorio_principal_nao_lista_acervo(self):
        self.artigo('A')
        self.p.painel()
        rel = (self.root / 'dados/anotacoes-ia.md').read_text(encoding='utf-8')
        self.assertNotIn('## Trabalhos do acervo', rel)
        self.assertNotIn('TRABALHOS-SEM-PROPOSTA.md', rel)
        self.assertNotIn('INSTRUCOES.md', rel)
        self.assertNotIn('AVALIAR-PROPOSTAS.md', rel)

    def test_tags_do_trabalho_usam_frontmatter_inline(self):
        a = self.artigo('A')
        a['pdf_local'] = 'obsidian/referencias/pdfs/A.pdf'
        self.p.estado['propostas'] = [{'id': 'p', 'titulo': 'Ideia', 'revisao': self.p.revisao, 'fontes': ['A']}]
        motor.json_gravar(self.root / 'dados/propostas/p.json', {'fontes': ['A'], 'meu_trabalho': 'Ideia', 'buscas': []})
        self.base.ARTIGOS.mkdir(parents=True, exist_ok=True)
        (self.base.ARTIGOS / 'A.md').write_text(
            '---\ntags:\n  - artigo\n  - status/novo\n---\n# A\n\n## Tags\n\n#artigo #status/novo\n',
            encoding='utf-8',
        )
        self.p.painel()
        nota = (self.root / 'obsidian/referencias/fichamentos/A.md').read_text(encoding='utf-8')
        self.assertRegex(nota, r'(?m)^tags: \[[^\n]*\]$')
        self.assertNotRegex(nota, r'(?m)^  - (artigo|status/novo)$')

    def test_tags_sao_recriadas_quando_nota_nao_tem_frontmatter(self):
        a = self.artigo('A')
        a['titulo'] = 'Blockchain access control for IoT'
        a['pdf_local'] = 'obsidian/referencias/pdfs/A.pdf'
        self.p.estado['propostas'] = [{'id': 'p', 'titulo': 'Ideia', 'revisao': self.p.revisao, 'fontes': ['A']}]
        motor.json_gravar(self.root / 'dados/propostas/p.json', {'fontes': ['A'], 'meu_trabalho': 'Ideia', 'buscas': []})
        self.base.ARTIGOS.mkdir(parents=True, exist_ok=True)
        (self.base.ARTIGOS / 'A.md').write_text('# A\n\nTexto antigo.\n', encoding='utf-8')
        self.p.painel()
        nota = (self.root / 'obsidian/referencias/fichamentos/A.md').read_text(encoding='utf-8')
        self.assertTrue(nota.startswith('---\n'))
        self.assertRegex(nota, r'(?m)^tags: \[[^\n]*(iot|blockchain)[^\n]*(iot|blockchain)[^\n]*\]$')
        self.assertIn('## Tags', nota)
        self.assertIn('#iot', nota)

    def test_ficha_json_vazia_nao_quebra_painel(self):
        a = self.artigo('A')
        a['pdf_local'] = 'obsidian/referencias/pdfs/A.pdf'
        self.p.estado['propostas'] = [{'id': 'p', 'titulo': 'Ideia', 'revisao': self.p.revisao, 'fontes': ['A']}]
        motor.json_gravar(self.root / 'dados/propostas/p.json', {'fontes': ['A'], 'meu_trabalho': 'Ideia', 'buscas': []})
        a['leitura_agente'] = {
            'revisao': self.p.revisao, 'assinatura': 'assinatura', 'feitos': 1,
            'total': 1, 'concluida': False, 'tipo': 'pdf', 'paginas_sem_texto': []
        }
        pasta = self.root / 'dados/leituras/assinatura'
        pasta.mkdir(parents=True)
        (pasta / '0.json').write_text('', encoding='utf-8')
        self.p.painel()
        nota = (self.root / 'obsidian/referencias/fichamentos/A.md').read_text(encoding='utf-8')
        self.assertIn('Ficha 0 indisponível', nota)

    def test_nota_exibe_entendimento_consolidado_do_trabalho(self):
        artigo = self.artigo('A')
        self.p.estado['propostas'] = [{'id': 'p', 'titulo': 'Ideia', 'revisao': self.p.revisao, 'fontes': ['A']}]
        motor.json_gravar(self.root / 'dados/propostas/p.json', {'fontes': ['A'], 'meu_trabalho': 'Ideia', 'buscas': []})
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
        nota = (self.root / 'obsidian/referencias/fichamentos/A.md').read_text(encoding='utf-8')
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
        rel = (self.root / 'dados/anotacoes-ia.md').read_text(encoding='utf-8')
        self.assertIn('Implementar revogação incremental.', rel)
        self.assertIn('> [!abstract]- Revogação eficiente — comparativa; 2 trabalho(s)', rel)
        self.assertIn('> Implementar revogação incremental.', rel)
        self.assertNotIn('<details', rel)
        self.assertNotIn('<summary', rel)
        nota_a = (self.root / 'obsidian/referencias/fichamentos/A.md').read_text(encoding='utf-8')
        nota_b = (self.root / 'obsidian/referencias/fichamentos/B.md').read_text(encoding='utf-8')
        self.assertIn('Referencia: [B](B.md)', nota_a)
        self.assertIn('É citado por: [A](A.md)', nota_b)
        self.assertIn('A e B usam estratégias diferentes.', nota_a)

    def test_proposta_descartada_some_do_relatorio_e_do_grafo(self):
        a = self.artigo('A')
        a['pdf_local'] = 'obsidian/referencias/pdfs/A.pdf'
        self.p.estado['propostas'] = [{'id': 'p', 'titulo': 'Ideia ruim', 'revisao': self.p.revisao, 'fontes': ['A']}]
        motor.json_gravar(self.root / 'dados/propostas/p.json', {
            'fontes': ['A'], 'meu_trabalho': 'Ideia ruim', 'avaliacao_humana': 'descartar', 'buscas': []})
        self.p.painel()
        rel = (self.root / 'dados/anotacoes-ia.md').read_text(encoding='utf-8')
        self.assertNotIn('Ideia ruim', rel)
        self.assertFalse((self.root / 'obsidian/referencias/fichamentos/A.md').exists())

    def test_anotacoes_humanas_preservadas_ao_atualizar(self):
        a = self.artigo('A')
        a['pdf_local'] = 'obsidian/referencias/pdfs/A.pdf'
        self.p.estado['propostas'] = [{'id': 'p', 'titulo': 'Ideia', 'revisao': self.p.revisao, 'fontes': ['A']}]
        motor.json_gravar(self.root / 'dados/propostas/p.json', {'fontes': ['A'], 'meu_trabalho': 'Ideia', 'buscas': []})
        self.p.painel()
        nota = self.root / 'obsidian/referencias/fichamentos/A.md'
        nota.write_text('Minha observação pessoal.\n' + nota.read_text(encoding='utf-8') + '\nDecisão do orientador.', encoding='utf-8')
        self.p.painel()
        self.p.painel()
        texto = nota.read_text(encoding='utf-8')
        self.assertTrue(texto.startswith('Minha observação pessoal.'))
        self.assertTrue(texto.endswith('Decisão do orientador.'))
        self.assertEqual(texto.count('<!-- agente:inicio -->'), 1)
