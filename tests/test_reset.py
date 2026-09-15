import json
import tempfile
import types
import unittest
from pathlib import Path
import motor


class ResetTest(unittest.TestCase):
    def test_reset_repetido_isola_caches_e_retomada_mantem_execucao(self):
        with tempfile.TemporaryDirectory() as pasta:
            root = Path(pasta)
            dados = root / 'dados'
            dados.mkdir()
            instr = root / 'INSTRUCOES.md'
            instr.write_text('Minhas instruções.', encoding='utf-8')
            base = types.SimpleNamespace(ROOT=root, INSTRUCOES=instr,
                carregar_jsonl=lambda p: [json.loads(l) for l in p.read_text().splitlines() if l.strip()],
                carregar_instrucoes=lambda: {'artigos_por_ciclo_ia': 5, 'resultados_por_consulta': 10,
                                             'artigos_aprofundados': 8})
            def reset():
                (dados / 'artigos.jsonl').write_text('{"titulo":"velho"}\n')
                (dados / 'agente_estado.json').write_text('{"reiniciar_execucao":true,"propostas":["velha"]}')
                p = motor.Pesquisa(base, limpar=True)
                p.configurar()
                return p
            a = reset()
            self.assertEqual(a.artigos, [])
            self.assertEqual(a.estado['propostas'], [])
            self.assertNotIn('reiniciar_execucao', a.estado)
            b = motor.Pesquisa(base)
            b.configurar()
            self.assertEqual(a.revisao, b.revisao)
            self.assertEqual(a.estado['execucao'], b.estado['execucao'])
            c = reset()
            self.assertNotEqual(a.revisao, c.revisao)
            self.assertNotEqual(a.estado['execucao'], c.estado['execucao'])
            self.assertEqual(instr.read_text(encoding='utf-8'), 'Minhas instruções.')

    def test_execucao_existente_sem_reset_preservada(self):
        with tempfile.TemporaryDirectory() as pasta:
            root = Path(pasta)
            (root / 'dados').mkdir()
            estado = {'tarefas': {'ok': {'feito': True}}, 'consultas': {}, 'historico': [], 'propostas': []}
            (root / 'dados/agente_estado.json').write_text(json.dumps(estado))
            base = types.SimpleNamespace(ROOT=root, carregar_jsonl=lambda _: [{'titulo': 'existente'}])
            p = motor.Pesquisa(base)
            self.assertEqual(p.estado, estado)
            self.assertEqual(p.artigos, [{'titulo': 'existente'}])


if __name__ == '__main__':
    unittest.main()
