"""Regras verificáveis para maturar contribuições científicas.

O modelo de linguagem propõe conteúdo; este módulo impõe os requisitos que
não podem depender da obediência do modelo: estrutura, evidência mínima,
rastreabilidade, factibilidade e proibição de metas quantitativas sem fonte.
Os campos são adicionados aos JSONs legados, sem remover os campos antigos.
"""
from __future__ import annotations

from copy import deepcopy
from datetime import datetime
import re


SCHEMA_VERSION = 2
NOVELTY_STATUSES = {
    "collision_found", "likely_incremental", "plausible_gap",
    "strong_candidate", "insufficient_evidence",
}
GENERIC_PATTERNS = (
    r"\bintegrar\b.{0,35}\b(com|e)\b",
    r"\bcombinar\b.{0,35}\btecnolog",
    r"\bcombina[cç][aã]o de\b.{0,100}\b(com|e)\b",
    r"\bintegra[cç][aã]o de\b.{0,100}\b(com|e)\b",
    r"\bcriar (um|uma) (framework|arquitetura)\b",
    r"\b(aplicar|utilizar|usar) (blockchain|ssi|abe)\b",
    r"\b(aumentar|melhorar|garantir|tornar) (a )?(segurança|privacidade|interoperabilidade|escalabilidade)\b",
)
TECHNOLOGIES = (
    "ssi", "self-sovereign", "abe", "cp-abe", "kp-abe", "zkp",
    "zero-knowledge", "homomorphic", "homomórf", "secret sharing",
    "blockchain", "ipfs", "iot", "mqtt", "hyperledger",
)
UNITS = {
    "algoritmo", "protocolo", "mecanismo", "modelo de estado",
    "transformação", "política", "arquitetura", "método experimental",
}


def agora():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def texto(valor):
    if valor is None:
        return ""
    if isinstance(valor, str):
        return valor.strip()
    if isinstance(valor, list):
        return "; ".join(texto(v) for v in valor)
    if isinstance(valor, dict):
        return "; ".join(f"{k}: {texto(v)}" for k, v in valor.items())
    return str(valor)


def migrar_proposta(proposta):
    """Acrescenta o envelope v2 sem apagar nenhum dado legado."""
    p = deepcopy(proposta or {})
    if p.get("schema_version", 1) >= SCHEMA_VERSION:
        return p
    versao = int(p.get("proposal_version") or 1)
    p.update({
        "schema_version": SCHEMA_VERSION,
        "proposal_version": versao,
        "maturity_status": "immature",
        "problema_tecnico": p.get("problema_tecnico") or {
            "estado_atual": "", "evento": "", "problema": texto(p.get("problema")),
            "consequencia_tecnica": "", "componente_responsavel": "",
            "propriedade_desejada": "",
        },
        "mecanismo_proposto": p.get("mecanismo_proposto") or {
            "entrada": "", "estado_mantido": "", "algoritmo_processo": "",
            "saida": "", "estruturas_de_dados": [], "entidades": [],
            "confianca": "", "eventos_de_atualizacao": [], "condicao_de_falha": "",
            "setup_e_chaves": "", "dados_on_chain": "", "dados_off_chain": "",
        },
        "diferencial_tecnico_candidato": texto(p.get("diferencial_tecnico_candidato") or p.get("alteracao_sobre_trabalhos_proximos")),
        "unidade_de_novidade": texto(p.get("unidade_de_novidade")),
        "propriedades_contribuicao": p.get("propriedades_contribuicao") or [],
        "closest_prior_art": p.get("closest_prior_art") or [],
        "matriz_anterioridade": p.get("matriz_anterioridade") or [],
        "colisoes_encontradas": p.get("colisoes_encontradas") or [],
        "reformulacoes": p.get("reformulacoes") or [],
        "historico_versoes": p.get("historico_versoes") or [{
            "proposal_version": versao,
            "quando": agora(),
            "descricao": texto(p.get("meu_trabalho") or p.get("titulo")),
            "origem": "migração compatível do formato legado",
        }],
        "anterioridade": p.get("anterioridade") or {"rodadas": [], "concluida": False},
        "novelty_status": "insufficient_evidence",
        "propriedade_avaliada": p.get("propriedade_avaliada") or {"expressao": "", "metrica": "", "criterio_refutacao": ""},
        "artefato_minimo": texto(p.get("artefato_minimo")),
        "experimento_decisivo": texto(p.get("experimento_decisivo") or p.get("experimento")),
        "baselines": p.get("baselines") or [],
        "metricas_essenciais": p.get("metricas_essenciais") or [],
        "fora_de_escopo": p.get("fora_de_escopo") or [],
        "implementation_risk": p.get("implementation_risk") or "",
        "implementation_risk_justification": texto(p.get("implementation_risk_justification")),
        "novelty_risk": texto(p.get("novelty_risk") or p.get("riscos")),
        "pergunta_orientador": texto(p.get("pergunta_orientador") or p.get("duvidas_orientador")),
        "ranking": p.get("ranking") or {},
    })
    return p


def tecnologias_centrais(proposta):
    base = " ".join((
        texto(proposta.get("diferencial_tecnico_candidato")),
        texto(proposta.get("mecanismo_proposto")),
        texto(proposta.get("artefato_minimo")),
    )).lower()
    return sorted({t for t in TECHNOLOGIES if t in base})


def avaliar_factibilidade(proposta):
    tecnologias = tecnologias_centrais(proposta)
    quantidade = len(tecnologias)
    risco = "low" if quantidade <= 2 else "medium" if quantidade == 3 else "high" if quantidade <= 5 else "very_high"
    justificativa = (
        f"Foram identificadas {quantidade} tecnologias centrais ({', '.join(tecnologias) or 'nenhuma explicitada'}). "
        "Para uma dissertação com 18 meses e dedicação parcial, a proposta deve manter uma contribuição principal "
        "e no máximo duas ou três tecnologias indispensáveis; as demais devem ser infraestrutura ou trabalho futuro."
    )
    return risco, justificativa


def numeros_sem_evidencia(proposta):
    """Detecta metas numéricas; anos, IDs P1 e nota de ranking não contam."""
    campos = (
        "diferencial_tecnico_candidato", "hipotese_lacuna", "artefato_minimo",
        "experimento_decisivo", "metricas_essenciais",
    )
    base = " ".join(texto(proposta.get(c)) for c in campos)
    padrao = re.compile(r"(?<!P)\b\d+(?:[.,]\d+)?\s*(?:%|ms|s\b|segundos?|minutos?|MB|GB|x\b)", re.I)
    encontrados = padrao.findall(base)
    evidencias = proposta.get("evidencias_quantitativas") or []
    return [] if evidencias else encontrados


def validar_proposta(proposta):
    """Retorna erros determinísticos que impedem uma proposta madura."""
    p = migrar_proposta(proposta)
    erros = []
    problema = p.get("problema_tecnico") or {}
    obrigatorios = ("estado_atual", "evento", "problema", "consequencia_tecnica", "componente_responsavel", "propriedade_desejada")
    faltantes = [c for c in obrigatorios if not texto(problema.get(c))]
    if faltantes:
        erros.append("problema_tecnico incompleto: " + ", ".join(faltantes))
    mecanismo = p.get("mecanismo_proposto") or {}
    campos_mecanismo = ("entrada", "estado_mantido", "algoritmo_processo", "saida", "entidades", "confianca", "eventos_de_atualizacao", "condicao_de_falha")
    faltantes = [c for c in campos_mecanismo if not texto(mecanismo.get(c))]
    if faltantes:
        erros.append("mecanismo_proposto incompleto: " + ", ".join(faltantes))
    diferencial = texto(p.get("diferencial_tecnico_candidato"))
    if len(diferencial) < 120 or any(re.search(pat, diferencial, re.I) for pat in GENERIC_PATTERNS):
        erros.append("diferencial técnico ausente, genérico ou pouco específico")
    unidade = texto(p.get("unidade_de_novidade")).lower()
    if unidade not in UNITS:
        erros.append("unidade_de_novidade inválida ou ausente")
    props = p.get("propriedades_contribuicao") or []
    if len(props) < 3 or any(not isinstance(x, dict) or not re.fullmatch(r"P\d+", texto(x.get("id"))) or not texto(x.get("descricao")) for x in props):
        erros.append("são necessárias ao menos três propriedades estruturadas P1...Pn")
    falsificavel = p.get("propriedade_avaliada") or {}
    if not all(texto(falsificavel.get(c)) for c in ("expressao", "metrica", "criterio_refutacao")):
        erros.append("propriedade falsificável incompleta")
    if numeros_sem_evidencia(p):
        erros.append("meta quantitativa sem fonte, requisito ou experimento piloto")
    return erros


def evidencia_anterioridade_suficiente(proposta):
    ant = proposta.get("anterioridade") or {}
    rodadas = {r.get("tipo") for r in ant.get("rodadas", []) if r.get("status") == "concluida" and r.get("queries")}
    proximos = proposta.get("closest_prior_art") or []
    fontes_ok = [x for x in proximos if x.get("identificador") and x.get("fonte") and x.get("escopo_leitura") not in {None, "", "titulo"}]
    evidencias = [e for r in ant.get("rodadas", []) for e in r.get("evidencias", []) if e.get("query") and e.get("base") and "numero_resultados" in e]
    return len(rodadas) >= 5 and len(fontes_ok) >= 3 and len(evidencias) >= 5


def limitar_novelty_status(proposta, solicitado):
    solicitado = solicitado if solicitado in NOVELTY_STATUSES else "insufficient_evidence"
    if validar_proposta(proposta):
        return "insufficient_evidence"
    if solicitado == "strong_candidate" and not evidencia_anterioridade_suficiente(proposta):
        return "insufficient_evidence"
    if solicitado in {"plausible_gap", "likely_incremental"} and not evidencia_anterioridade_suficiente(proposta):
        return "insufficient_evidence"
    return solicitado


def registrar_reformulacao(proposta, motivo, nova_descricao):
    p = migrar_proposta(proposta)
    anterior = texto(p.get("diferencial_tecnico_candidato") or p.get("meu_trabalho"))
    p["proposal_version"] = int(p.get("proposal_version") or 1) + 1
    registro = {
        "quando": agora(), "proposal_version": p["proposal_version"],
        "antes": anterior, "colisao": texto(motivo), "depois": texto(nova_descricao),
    }
    p.setdefault("reformulacoes", []).append(registro)
    p.setdefault("historico_versoes", []).append({
        "proposal_version": p["proposal_version"], "quando": registro["quando"],
        "descricao": registro["depois"], "origem": "reformulação após colisão",
    })
    p["diferencial_tecnico_candidato"] = registro["depois"]
    p["novelty_status"] = "insufficient_evidence"
    return p


def ranking_explicado(proposta):
    risco, justificativa = avaliar_factibilidade(proposta)
    p = migrar_proposta(proposta)
    criterios = {
        "A_clareza_problema": (4 if not any("problema_tecnico" in e for e in validar_proposta(p)) else 1, "Problema técnico estruturado em estado, evento, consequência e propriedade."),
        "B_forca_lacuna": (5 if p.get("novelty_status") == "strong_candidate" else 3 if p.get("novelty_status") == "plausible_gap" else 1, "Depende da checagem documentada de anterioridade."),
        "C_especificidade_diferencial": (4 if len(texto(p.get("diferencial_tecnico_candidato"))) >= 120 else 1, "Avalia se há mecanismo/propriedade, não mera combinação de tecnologias."),
        "D_avaliacao_experimental": (4 if texto((p.get("propriedade_avaliada") or {}).get("criterio_refutacao")) else 1, "Exige propriedade falsificável e experimento decisivo."),
        "E_alinhamento_bases": (min(5, max(1, len(p.get("fontes") or []))), "Proporcional aos trabalhos-base efetivamente associados."),
        "F_factibilidade_18_meses": ({"low": 5, "medium": 4, "high": 2, "very_high": 1}[risco], justificativa),
        "G_implementacao": ({"low": 5, "medium": 4, "high": 2, "very_high": 1}[risco], "Menos tecnologias centrais e artefato mínimo delimitado recebem melhor avaliação."),
        "H_risco_colisao": (4 if p.get("novelty_status") in {"plausible_gap", "strong_candidate"} else 2, "Baseado na matriz e nos trabalhos mais próximos, não na quantidade de tecnologias."),
        "I_publicacao": (4 if p.get("novelty_status") in {"plausible_gap", "strong_candidate"} else 2, "Estimativa condicionada à confirmação da lacuna e ao resultado experimental."),
        "J_utilidade_smart_city": (3, "Utilidade contextual não substitui novidade técnica."),
    }
    return {"criterios": {k: {"nota": n, "justificativa": j} for k, (n, j) in criterios.items()},
            "total": sum(n for n, _ in criterios.values()), "maximo": 50}

