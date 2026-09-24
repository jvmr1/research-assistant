"""Pipeline incremental de problema, mecanismo e anterioridade de propostas."""
import json
import re

from src import contribuicao


def texto(v):
    if v is None:
        return ''
    if isinstance(v, str):
        return v.strip()
    if isinstance(v, list):
        return '; '.join(texto(x) for x in v)
    if isinstance(v, dict):
        return '; '.join(f'{k}: {texto(x)}' for k, x in v.items())
    return str(v)


def consultas_anterioridade(obj):
    props = [texto(x.get('descricao')) for x in obj.get('propriedades_contribuicao', []) if isinstance(x, dict)]
    dif = texto(obj.get('diferencial_tecnico_candidato') or obj.get('meu_trabalho'))
    termos = ' '.join(dict.fromkeys(re.findall(
        r'(?i)verifiable credentials?|\bVC\b|SSI|CP-ABE|attribute.based encryption|holder binding|purpose binding|epoch|revocation|derived key|capabilit\w+|DID|RBAC|OAuth|ACL',
        dif + ' ' + ' '.join(props))))
    return [
        ('combinacao_explicita', [dif[:240], termos]),
        ('sinonimos_tecnicos', [termos + ' verifiable claims decentralized credential short-lived derived key invalidation']),
        ('mecanismo_sem_contexto', [termos + ' cloud healthcare IIoT e-government confidential data sharing']),
        ('propriedades_individuais', [' '.join(props[i] for i in idx if i < len(props))[:260]
                                      for idx in ((0, 1, 2), (1, 3, 4), (0, 4, 5), (3, 5, 6))]),
        ('relacoes_dos_mais_proximos', [termos + ' related work references citations 2024 2025 2026']),
    ]


def proposta_compacta_para_prompt(obj):
    campos = ('id', 'titulo', 'meu_trabalho', 'problema', 'hipotese_lacuna',
              'alteracao_sobre_trabalhos_proximos', 'fontes', 'fatos',
              'diferencial_tecnico_candidato', 'unidade_de_novidade',
              'propriedades_contribuicao', 'propriedade_avaliada',
              'artefato_minimo', 'experimento_decisivo', 'fora_de_escopo',
              'validation_errors')
    compacto = {}
    for campo in campos:
        valor = obj.get(campo)
        if valor in (None, '', []):
            continue
        if isinstance(valor, str):
            valor = valor[:1200]
        elif isinstance(valor, list):
            valor = valor[:10]
        compacto[campo] = valor
    resultados = []
    for rodada in (obj.get('anterioridade') or {}).get('rodadas', []):
        for item in rodada.get('resultados', []):
            if len(resultados) >= 8:
                break
            resultados.append({
                'titulo': texto(item.get('titulo'))[:180],
                'ano': item.get('ano'),
                'identificador': texto(item.get('identificador'))[:120],
                'resumo': texto(item.get('resumo'))[:500],
                'escopo_leitura': item.get('escopo_leitura'),
            })
    if resultados:
        compacto['evidencias_anterioridade'] = resultados
    return compacto


def dados_comparacao_anterioridade(obj, candidatos, limite=10500):
    """Monta contexto pequeno e rastreável para comparar anterioridade.

    O objeto da proposta contém as rodadas e seus resultados. Reenviá-lo
    integralmente duplica os candidatos e estoura o limite global de contexto.
    """
    proposta = proposta_compacta_para_prompt(obj)
    proposta.pop('fatos', None)
    compactos = []
    for item in candidatos:
        candidato = {
            'titulo': texto(item.get('titulo'))[:240],
            'autores': item.get('autores', [])[:6] if isinstance(item.get('autores'), list) else texto(item.get('autores'))[:180],
            'ano': item.get('ano'),
            'identificador': texto(item.get('identificador'))[:180],
            'fonte': texto(item.get('fonte'))[:100],
            'query': texto(item.get('query'))[:220],
            'resumo': texto(item.get('resumo'))[:850],
            'escopo_leitura': texto(item.get('escopo_leitura'))[:40],
        }
        tentativa = {'proposta': proposta, 'candidatos': compactos + [candidato]}
        if len(json.dumps(tentativa, ensure_ascii=False)) > limite:
            break
        compactos.append(candidato)
    return {'proposta': proposta, 'candidatos': compactos}

def normalizar_resposta_tecnica(resposta):
    """Aceita as embalagens e aliases comuns devolvidos pelos modelos JSON."""
    if not isinstance(resposta, dict):
        return {}
    base = resposta
    for chave in ('contribuicao', 'contribuicao_principal'):
        if isinstance(resposta.get(chave), dict):
            base = resposta[chave]
            break
    normalizada = dict(base)
    aliases = {
        'diferencial_tecnico': 'diferencial_tecnico_candidato',
        'unidade_novidade': 'unidade_de_novidade',
        'propriedades': 'propriedades_contribuicao',
        'artefato': 'artefato_minimo',
        'experimento': 'experimento_decisivo',
        'metricas': 'metricas_essenciais',
    }
    for origem, destino in aliases.items():
        if normalizada.get(destino) in (None, '', []) and normalizada.get(origem) not in (None, '', []):
            normalizada[destino] = normalizada[origem]
    unidade = texto(normalizada.get('unidade_de_novidade')).lower()
    if unidade not in contribuicao.UNITS:
        for termo, categoria in (
            ('método experimental', 'método experimental'), ('modelo de estado', 'modelo de estado'),
            ('arquitet', 'arquitetura'), ('protocolo', 'protocolo'), ('algorit', 'algoritmo'),
            ('mecanismo', 'mecanismo'), ('política', 'política'), ('transforma', 'transformação')):
            if termo in unidade:
                normalizada['unidade_de_novidade'] = categoria
                break
    return normalizada


def tecnicalizar(p, obj):
    from src.revisao import chamar
    esquema = {'type': 'object', 'properties': {
        'problema_tecnico': {'type': 'object'}, 'mecanismo_proposto': {'type': 'object'},
        'diferencial_tecnico_candidato': {'type': 'string'},
        'unidade_de_novidade': {'type': 'string', 'enum': sorted(contribuicao.UNITS)},
        'propriedades_contribuicao': {'type': 'array', 'minItems': 3, 'items': {'type': 'object'}},
        'propriedade_avaliada': {'type': 'object'}, 'artefato_minimo': {'type': 'string'},
        'experimento_decisivo': {'type': 'string'}, 'baselines': {'type': 'array'},
        'metricas_essenciais': {'type': 'array'}, 'fora_de_escopo': {'type': 'array'},
        'pergunta_orientador': {'type': 'string'}},
        'required': ['problema_tecnico', 'mecanismo_proposto', 'diferencial_tecnico_candidato',
                     'unidade_de_novidade', 'propriedades_contribuicao', 'propriedade_avaliada',
                     'artefato_minimo', 'experimento_decisivo', 'baselines', 'metricas_essenciais', 'fora_de_escopo']}
    return chamar(p, 'maturacao-tecnica',
        'Transforme o brainstorm em contribuição técnica verificável. Não aceite integrar, combinar ou aplicar tecnologias como diferencial. '
        'problema_tecnico: estado_atual, evento, problema, consequencia_tecnica, componente_responsavel, propriedade_desejada. '
        'mecanismo_proposto: entrada, estado_mantido, algoritmo_processo, saida, estruturas_de_dados, entidades, confianca, eventos_de_atualizacao, condicao_de_falha, setup_e_chaves, dados_on_chain, dados_off_chain. '
        'Propriedades: objetos {id:P1, descricao:...}. propriedade_avaliada: expressao, metrica, criterio_refutacao. '
        'Uma contribuição principal e no máximo 2 ou 3 tecnologias centrais. Não invente números; o efeito quantitativo será determinado experimentalmente.',
        {'proposta_legada': proposta_compacta_para_prompt(obj)}, esquema)


def _normalizar(p, item, query, bases):
    resumo = p.b.resumo_invertido(item.get('abstract_inverted_index') or item.get('abstract'))
    autores = p.b.extrair_autores(item) if item.get('authorships') else []
    existente = next((a for a in p.artigos if p._chave_artigo(a) == p._chave_artigo(
        {'doi': item.get('doi'), 'titulo': item.get('title')})), None)
    escopo = 'resumo' if resumo and resumo != 'Resumo não disponível.' else 'titulo'
    if existente and existente.get('sintese_artigo', {}).get('resumo'):
        resumo = existente['sintese_artigo']['resumo']
        escopo = 'texto_integral' if existente.get('leitura_agente', {}).get('tipo') in {'pdf', 'html'} else 'resumo'
    return {'titulo': item.get('title') or '', 'autores': autores, 'ano': item.get('publication_year'),
            'doi': item.get('doi'), 'identificador': item.get('doi') or item.get('id') or '',
            'fonte': item.get('_fonte') or ', '.join(bases), 'query': query,
            'resumo': resumo[:1800], 'escopo_leitura': escopo,
            'referencias': item.get('referenced_works') or [], 'relacionados': item.get('related_works') or []}


def revisao_manual_terminal(obj):
    """Retira da fila a revisao manual que esgotou a automacao desta rodada."""
    return (
        obj.get("maturity_status") == "needs_manual_revision"
        and (
            int(obj.get("evidence_revision_cycles") or 0) >= 1
            or int(obj.get("prior_art_comparison_attempts") or 0) >= 2
        )
    )


def maturar_propostas(p):
    """Avança uma única etapa para manter retomada e respeitar rate limits."""
    from src.motor import ler_json, json_gravar, log, agora
    from src.revisao import chamar
    metas = [m for m in p.estado.get('propostas', [])
             if m.get('revisao') == p.revisao and m.get('avaliacao_humana') != 'descartar']
    visiveis = [m for m in metas if m.get('visivel_anotacoes')]
    if visiveis:
        metas = visiveis
    for meta in metas:
        if meta.get('revisao') != p.revisao or meta.get('avaliacao_humana') == 'descartar':
            continue
        path = p.root / 'dados/propostas' / f"{meta['id']}.json"
        obj = contribuicao.migrar_proposta(ler_json(path, {}))
        if (not obj.get('titulo') or obj.get('maturity_status') in {'mature', 'collision_exhausted'}
                or revisao_manual_terminal(obj)):
            continue
        erros_estrutura = contribuicao.validar_proposta(obj)
        if erros_estrutura:
            tentativas = int(obj.get('maturation_attempts') or 0)
            if tentativas >= 4:
                # Não transfere prematuramente para o pesquisador: primeiro
                # pesquisa trabalhos próximos e tenta novamente com evidências.
                obj['maturity_status'] = 'prior_art_search'
                obj['novelty_status'] = 'insufficient_evidence'
                obj['validation_errors'] = erros_estrutura
                json_gravar(path, obj); p.salvar()
            else:
                obj['maturation_attempts'] = tentativas + 1
                # Persiste antes da chamada: se uma biblioteca nativa derrubar o
                # trabalhador, o supervisor retoma sem repetir esta etapa para sempre.
                json_gravar(path, obj)
                p.salvar()
                resposta = normalizar_resposta_tecnica(tecnicalizar(p, obj))
                for campo, valor in resposta.items():
                    if campo in {'problema_tecnico', 'mecanismo_proposto', 'diferencial_tecnico_candidato', 'unidade_de_novidade',
                                 'propriedades_contribuicao', 'propriedade_avaliada', 'artefato_minimo', 'experimento_decisivo',
                                 'baselines', 'metricas_essenciais', 'fora_de_escopo', 'pergunta_orientador'} and valor not in (None, '', []):
                        obj[campo] = valor
                obj['implementation_risk'], obj['implementation_risk_justification'] = contribuicao.avaliar_factibilidade(obj)
                obj['validation_errors'] = contribuicao.validar_proposta(obj)
                obj['maturity_status'] = 'technical_definition' if not obj['validation_errors'] else 'immature'
                obj['ranking'] = contribuicao.ranking_explicado(obj)
                json_gravar(path, obj); p.salvar(); return True
        ant = obj.setdefault('anterioridade', {'rodadas': [], 'concluida': False})
        feitas = {r.get('tipo') for r in ant['rodadas'] if r.get('status') == 'concluida'}
        for tipo, queries in consultas_anterioridade(obj):
            if tipo in feitas:
                continue
            rodada = {'tipo': tipo, 'iniciada_em': agora(), 'queries': [q for q in queries if len(q.strip()) >= 12][:4], 'evidencias': [], 'resultados': []}
            for query in rodada['queries']:
                try:
                    resultados, bases = p.buscar_fontes_academicas(query, 1)
                    rodada['evidencias'].extend({'query': query, 'base': b, 'data': agora(), 'numero_resultados': len(resultados)} for b in bases)
                    rodada['resultados'].extend(_normalizar(p, x, query, bases) for x in resultados[:5])
                except Exception as erro:
                    rodada['evidencias'].append({'query': query, 'base': 'todas', 'data': agora(), 'numero_resultados': 0, 'erro': str(erro)[:300]})
            rodada.update(status='concluida', concluida_em=agora())
            ant['rodadas'].append(rodada); obj['maturity_status'] = 'prior_art_search'
            json_gravar(path, obj); p.salvar(); log(f'Anterioridade {tipo}: {len(rodada["resultados"])} resultado(s).'); return True
        ant['concluida'] = True
        candidatos, vistos = [], set()
        for rodada in ant['rodadas']:
            for item in rodada.get('resultados', []):
                ident = item.get('identificador') or item.get('titulo')
                if ident and ident not in vistos:
                    vistos.add(ident); candidatos.append(item)
        tentativas_comparacao = int(obj.get('prior_art_comparison_attempts') or 0)
        if tentativas_comparacao >= 2:
            obj['maturity_status'] = 'needs_manual_revision'
            obj['novelty_status'] = 'insufficient_evidence'
            obj['prior_art_comparison_error'] = obj.get('prior_art_comparison_error') or 'Comparação de anterioridade falhou duas vezes.'
            json_gravar(path, obj); p.salvar()
            log(f"Anterioridade de {obj.get('titulo', meta['id'])}: comparação suspensa após duas falhas; seguindo para outra proposta.")
            return True
        obj['prior_art_comparison_attempts'] = tentativas_comparacao + 1
        # Persiste antes da IA: queda nativa ou reinício não deve repetir
        # indefinidamente a mesma comparação.
        json_gravar(path, obj); p.salvar()
        try:
            resposta = chamar(p, 'comparacao-anterioridade',
                'Compare propriedade por propriedade. Nunca conclua por título; use resumo/síntese e marque desconhecido quando faltar texto. '
                'Retorne closest_prior_art (3 a 5 com titulo, autores, ano, identificador, fonte, mecanismo, propriedades_satisfeitas, propriedades_ausentes, proximidade, escopo_leitura), matriz_anterioridade, colisoes_encontradas, hipotese_lacuna e novelty_status. '
                'Nunca diga que não existe; diga que não foi identificado nas bases e consultas registradas.',
                dados_comparacao_anterioridade(obj, candidatos[:20]))
        except Exception as erro:
            obj['prior_art_comparison_error'] = str(erro)[:500]
            obj['maturity_status'] = 'prior_art_comparison_failed'
            obj['novelty_status'] = 'insufficient_evidence'
            json_gravar(path, obj); p.salvar()
            log(f"Falha na comparação de anterioridade ({obj['prior_art_comparison_attempts']}/2): {str(erro)[:220]}. O agente seguirá sem reiniciar em loop.")
            return True
        obj.pop('prior_art_comparison_error', None)
        obj['prior_art_comparison_completed'] = True
        for campo in ('closest_prior_art', 'matriz_anterioridade', 'colisoes_encontradas', 'hipotese_lacuna'):
            if resposta.get(campo) not in (None, ''):
                obj[campo] = resposta[campo]
        solicitado = texto(resposta.get('novelty_status'))
        obj['novelty_status'] = contribuicao.limitar_novelty_status(obj, solicitado)
        if solicitado == 'collision_found':
            tentativas_reformulacao = len(obj.get('reformulacoes') or [])
            if tentativas_reformulacao >= 2:
                obj['maturity_status'] = 'collision_exhausted'
                obj['retirada_automatica'] = True
                obj['motivo_retirada'] = 'Colisão técnica persistiu após duas reformulações e novas buscas de anterioridade.'
            else:
                reformulada = chamar(p, 'reformulacao-colisao',
                    'A proposta colidiu com trabalho anterior. Identifique o subconjunto já resolvido e reformule apenas com uma propriedade técnica ainda não tratada. Não acrescente tecnologias para fingir novidade. Retorne diferencial_tecnico_candidato.',
                    {'proposta': obj, 'colisoes': obj.get('colisoes_encontradas'), 'matriz': obj.get('matriz_anterioridade')})
                nova = texto(reformulada.get('diferencial_tecnico_candidato'))
                if nova:
                    obj = contribuicao.registrar_reformulacao(obj, obj.get('colisoes_encontradas'), nova)
                    obj['anterioridade'] = {'rodadas': [], 'concluida': False, 'reiniciada_apos_colisao': True}
                    obj['prior_art_comparison_attempts'] = 0
                    obj['prior_art_comparison_completed'] = False
                    obj['maturity_status'] = 'technical_definition'
        obj['validation_errors'] = contribuicao.validar_proposta(obj)
        if solicitado != 'collision_found':
            if not obj['validation_errors'] and obj['novelty_status'] != 'insufficient_evidence':
                obj['maturity_status'] = 'mature'
            elif obj['validation_errors'] and int(obj.get('evidence_revision_cycles') or 0) < 1:
                obj['evidence_revision_cycles'] = int(obj.get('evidence_revision_cycles') or 0) + 1
                obj['maturation_attempts'] = 0
                obj['maturity_status'] = 'immature'
            else:
                obj['maturity_status'] = 'needs_manual_revision'
        obj['ranking'] = contribuicao.ranking_explicado(obj)
        json_gravar(path, obj); p.salvar(); return True
    return False
