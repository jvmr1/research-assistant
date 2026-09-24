import unittest

from src import contribuicao, maturacao


def proposta_valida():
    p = contribuicao.migrar_proposta({'titulo': 'Capacidade temporal derivada de VC', 'fontes': ['A', 'B', 'C']})
    p['problema_tecnico'] = {
        'estado_atual': 'Uma VC válida origina uma chave.', 'evento': 'A VC é revogada.',
        'problema': 'A chave antiga permanece.', 'consequencia_tecnica': 'O acesso pode continuar.',
        'componente_responsavel': 'Ponte VC-ABE.', 'propriedade_desejada': 'Revogação limitada por época.'}
    p['mecanismo_proposto'] = {
        'entrada': 'VC e finalidade', 'estado_mantido': 'época e status',
        'algoritmo_processo': 'Derivar componente criptográfico vinculado ao holder, finalidade e época.',
        'saida': 'capacidade temporal', 'estruturas_de_dados': ['registro de época'],
        'entidades': ['holder', 'issuer', 'autoridade ABE'], 'confianca': 'issuer autorizado',
        'eventos_de_atualizacao': ['revogação', 'mudança de época'], 'condicao_de_falha': 'chave antiga abre nova época'}
    p['diferencial_tecnico_candidato'] = (
        'O trabalho deriva capacidades CP-ABE temporárias de claims verificadas, vinculando cada componente ao holder, '
        'à finalidade e à época, e propaga a revogação da credencial para o reencapsulamento da chave de dados.')
    p['unidade_de_novidade'] = 'mecanismo'
    p['propriedades_contribuicao'] = [
        {'id': 'P1', 'descricao': 'atributos originados de VC'},
        {'id': 'P2', 'descricao': 'vínculo ao holder e finalidade'},
        {'id': 'P3', 'descricao': 'vínculo temporal e propagação de revogação'}]
    p['propriedade_avaliada'] = {'expressao': 'Revoked(VC,t) => not Decrypt(SK_old,C,t+Delta)',
                                 'metrica': 'janela de exposição',
                                 'criterio_refutacao': 'A hipótese falha se a chave antiga abrir a nova época.'}
    p['artefato_minimo'] = 'Protótipo de derivação e reencapsulamento da chave de dados.'
    p['experimento_decisivo'] = 'Revogar a VC, avançar a época e testar a chave antiga.'
    p['baselines'] = ['CP-ABE sem propagação de revogação']
    p['metricas_essenciais'] = ['janela de exposição', 'custo de reencapsulamento']
    p['fora_de_escopo'] = ['IoT físico', 'ZKP', 'criptografia homomórfica']
    return p


class ContribuicaoTest(unittest.TestCase):
    def test_proposta_generica_e_imatura(self):
        p = contribuicao.migrar_proposta({'titulo': 'Integrar SSI + CP-ABE', 'meu_trabalho': 'Integrar SSI com CP-ABE.'})
        self.assertTrue(contribuicao.validar_proposta(p))
        self.assertEqual(p['maturity_status'], 'immature')

    def test_exige_diferencial_tecnico(self):
        p = proposta_valida(); p['diferencial_tecnico_candidato'] = 'Usar blockchain.'
        self.assertTrue(any('diferencial' in e for e in contribuicao.validar_proposta(p)))

    def test_exige_propriedades_p1_pn(self):
        p = proposta_valida(); p['propriedades_contribuicao'] = []
        self.assertTrue(any('P1' in e for e in contribuicao.validar_proposta(p)))

    def test_strong_candidate_bloqueado_sem_anterioridade(self):
        self.assertEqual(contribuicao.limitar_novelty_status(proposta_valida(), 'strong_candidate'), 'insufficient_evidence')

    def test_colisao_gera_reformulacao_versionada(self):
        p = contribuicao.registrar_reformulacao(proposta_valida(), 'Paper X cobre P1-P3', 'Novo mecanismo técnico suficientemente delimitado.')
        self.assertEqual(p['proposal_version'], 2)
        self.assertEqual(len(p['reformulacoes']), 1)

    def test_numero_quantitativo_sem_fonte_rejeitado(self):
        p = proposta_valida(); p['experimento_decisivo'] = 'Reduzir latência em 30%.'
        self.assertTrue(any('quantitativa' in e for e in contribuicao.validar_proposta(p)))

    def test_trabalhos_proximos_e_evidencia_sao_obrigatorios(self):
        p = proposta_valida(); p['closest_prior_art'] = []
        self.assertFalse(contribuicao.evidencia_anterioridade_suficiente(p))

    def test_evidencia_de_cada_rodada(self):
        p = proposta_valida()
        p['anterioridade'] = {'rodadas': [{'tipo': str(i), 'status': 'concluida', 'queries': ['q'],
            'evidencias': [{'query': 'q', 'base': 'OpenAlex', 'numero_resultados': 1}]} for i in range(5)]}
        p['closest_prior_art'] = [{'identificador': str(i), 'fonte': 'OpenAlex', 'escopo_leitura': 'resumo'} for i in range(3)]
        self.assertTrue(contribuicao.evidencia_anterioridade_suficiente(p))

    def test_amplitude_penaliza_factibilidade(self):
        p = proposta_valida(); p['artefato_minimo'] = 'SSI ABE ZKP homomorphic encryption secret sharing blockchain IPFS IoT MQTT'
        self.assertEqual(contribuicao.avaliar_factibilidade(p)[0], 'very_high')

    def test_migracao_preserva_avaliacao_manual(self):
        p = contribuicao.migrar_proposta({'avaliacao_humana': 'muito_interessante', 'comentario_humano': 'manter'})
        self.assertEqual(p['avaliacao_humana'], 'muito_interessante')
        self.assertEqual(p['comentario_humano'], 'manter')

    def test_normaliza_resposta_tecnica_aninhada_e_aliases(self):
        resposta = {'contribuicao': {
            'diferencial_tecnico': 'Um mecanismo técnico detalhado ' * 8,
            'unidade_de_novidade': 'Primeira arquitetura que cobre o ciclo completo',
            'propriedades': [{'id': 'P1', 'descricao': 'Uma propriedade'}],
        }}
        obtida = maturacao.normalizar_resposta_tecnica(resposta)
        self.assertEqual(obtida['unidade_de_novidade'], 'arquitetura')
        self.assertIn('detalhado', obtida['diferencial_tecnico_candidato'])
        self.assertEqual(obtida['propriedades_contribuicao'][0]['id'], 'P1')

    def test_comparacao_anterioridade_nao_reenvia_rodadas_e_respeita_limite(self):
        p = proposta_valida()
        p['anterioridade'] = {'rodadas': [{'resultados': [{'resumo': 'x' * 5000}]}] * 5}
        candidatos = [{
            'titulo': f'Trabalho {i}', 'autores': ['Autor'], 'ano': 2025,
            'identificador': str(i), 'fonte': 'OpenAlex', 'query': 'consulta',
            'resumo': 'r' * 3000, 'escopo_leitura': 'resumo',
            'referencias': ['z' * 1000] * 10,
        } for i in range(20)]
        dados = maturacao.dados_comparacao_anterioridade(p, candidatos, limite=7000)
        serializado = __import__('json').dumps(dados, ensure_ascii=False)
        self.assertLessEqual(len(serializado), 7000)
        self.assertNotIn('anterioridade', dados['proposta'])
        self.assertNotIn('referencias', dados['candidatos'][0])
        self.assertLess(len(dados['candidatos']), len(candidatos))


    def test_revisao_manual_apos_duas_falhas_sai_da_fila_automatica(self):
        proposta = contribuicao.migrar_proposta({
            "titulo": "Recuperacao de credenciais SSI",
            "schema_version": 2,
            "maturity_status": "needs_manual_revision",
            "prior_art_comparison_attempts": 2,
            "prior_art_comparison_completed": True,
        })
        proposta["evidence_revision_cycles"] = 0
        self.assertTrue(maturacao.revisao_manual_terminal(proposta))

    def test_revisao_manual_legada_ainda_pode_ser_retomada_uma_vez(self):
        proposta = contribuicao.migrar_proposta({
            "titulo": "Proposta antiga ainda nao reanalisada",
            "maturity_status": "needs_manual_revision",
        })
        self.assertFalse(maturacao.revisao_manual_terminal(proposta))


if __name__ == '__main__':
    unittest.main()
