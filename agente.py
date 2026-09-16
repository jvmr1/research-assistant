"""Ponto de entrada e configuração editável do agente de revisão.

Este arquivo deve ser o primeiro lido por quem vai dar manutenção. Ele define
pastas, modelos padrão, consultas padrão, leitura de vault/INSTRUCOES.md e
funções simples para criar/atualizar notas Markdown de artigos. O fluxo pesado
fica em motor.py, revisao.py e apresentacao.py para evitar um agente.py enorme.

Execução normal: python agente.py
"""
from pathlib import Path
from datetime import datetime
import json
import re
import time

import requests


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "dados"
VAULT = ROOT / "vault"
ARTIGOS = VAULT / "trabalhos"
PDFS = ROOT / "pdfs"
INSTRUCOES = VAULT / "INSTRUCOES.md"
SESSOES = DATA / "sessoes"
PROPOSTAS = DATA / "propostas"
MODELO_OLLAMA = "qwen2.5:7b-instruct-q4_K_M"
MODELO_OPENROUTER = "openai/gpt-oss-120b"



CONSULTAS = [
    "smart cities interoperability digital identity",
    "self sovereign identity smart cities",
    "decentralized identity public sector interoperability",
    "verifiable credentials government data sharing",
    "privacy preserving interoperability government systems",
    "distributed data consistency smart cities",
]

INSTRUCOES_PADRAO = """# Instruções do agente

Edite este arquivo antes de rodar. Ele é seu painel principal de comando.
O agente nunca sobrescreve este arquivo automaticamente.

## Configuração

- ano mínimo: 2025
- resultados por consulta: 10
- trabalhos simultâneos: 1
- fonte acadêmica principal: openalex
- fontes acadêmicas auxiliares: semantic_scholar, crossref
- modelo ia: openrouter
- modelo openrouter: openai/gpt-oss-120b
- modelo ollama de reserva: qwen2.5:7b-instruct-q4_K_M

## Variáveis de busca

- domínio: smart cities, IoT, industrial IoT, cyber-physical systems
- tecnologia: blockchain, self-sovereign identity, decentralized identity, verifiable credentials, attribute-based encryption
- problema: authentication, access control, interoperability, privacy, data sharing, revocation, cross-organization security
- contexto: public sector, smart city services, edge computing, distributed systems

## Consultas iniciais

- smart cities IoT blockchain access control
- self sovereign identity smart cities interoperability
- decentralized identity verifiable credentials public sector
- attribute based encryption IoT data sharing blockchain
- blockchain enabled secure IIoT data sharing organizations
- authentication access control blockchain smart cities

## Critérios de interesse

Priorize trabalhos que ajudem a encontrar lacunas próximas ao grupo de pesquisa:
IoT, cidades inteligentes, sistemas distribuídos, blockchain, identidade digital,
SSI, controle de acesso, ABE, interoperabilidade, segurança e privacidade.

Aceite ideias exploratórias. Uma proposta pode ser uma combinação, adaptação,
avaliação ou extensão de trabalhos existentes, desde que fique claro quais
trabalhos sustentam a hipótese e o que ainda precisaria ser verificado.
"""


def garantir_instrucoes_iniciais():
    """Cria vault/INSTRUCOES.md em clones novos, sem tocar se o arquivo já existe."""
    if not INSTRUCOES.exists():
        INSTRUCOES.parent.mkdir(parents=True, exist_ok=True)
        INSTRUCOES.write_text(INSTRUCOES_PADRAO, encoding="utf-8")


def combinacoes_variaveis_busca(variaveis, limite=24):
    grupos = {k: [v for v in vals if v] for k, vals in (variaveis or {}).items() if vals}
    if not grupos:
        return []
    consultas = []
    dominios = grupos.get('dominio') or grupos.get('domínios') or grupos.get('tema') or []
    tecnologias = grupos.get('tecnologia') or grupos.get('tecnologias') or []
    problemas = grupos.get('problema') or grupos.get('problemas') or []
    contextos = grupos.get('contexto') or grupos.get('contextos') or []
    outros = [(k, v) for k, vals in grupos.items() for v in vals
              if k not in {'dominio', 'domínios', 'tema', 'tecnologia', 'tecnologias', 'problema', 'problemas', 'contexto', 'contextos'}]
    def add(partes):
        q = ' '.join(dict.fromkeys([x.strip() for x in partes if x and x.strip()]))
        if q and q not in consultas:
            consultas.append(q)
    for d in dominios or ['']:
        for t in tecnologias or ['']:
            for pr in problemas or ['']:
                add([d, t, pr] + contextos[:1])
                if len(consultas) >= limite:
                    return consultas
    for _, termo in outros:
        add([termo] + (dominios[:1] or []) + (problemas[:1] or []))
        if len(consultas) >= limite:
            return consultas
    return consultas


def carregar_instrucoes(caminho=INSTRUCOES):
    if not caminho.exists():
        return {"consultas": CONSULTAS}

    texto = caminho.read_text(encoding="utf-8-sig")
    consultas = []
    ano_minimo = 2025
    resultados_por_consulta = 10
    fonte_academica_principal = "openalex"
    fontes_academicas_auxiliares = ["semantic_scholar", "crossref"]
    modelo_ia = "ollama"
    modelo_openrouter = MODELO_OPENROUTER
    modelo_ollama = MODELO_OLLAMA
    artigos_por_ciclo_ia = 10
    lendo_consultas = False
    lendo_variaveis = False
    variaveis_busca = {}

    for linha in texto.splitlines():
        linha_limpa = linha.strip()

        if linha_limpa.startswith("# ") or linha_limpa.startswith("## "):
            secao = linha_limpa.lstrip("# ").lower()
            lendo_consultas = secao == "consultas iniciais"
            lendo_variaveis = secao in {"variáveis de busca", "variaveis de busca", "variaveis das buscas", "variáveis das buscas"}
            continue

        if linha_limpa.lower().startswith("- ano mínimo:"):
            ano_minimo = int(linha_limpa.split(":", 1)[1].strip())

        if linha_limpa.lower().startswith("- resultados por consulta:"):
            resultados_por_consulta = int(
                linha_limpa.split(":", 1)[1].strip()
            )

        if linha_limpa.lower().startswith("- fonte acadêmica principal:") or linha_limpa.lower().startswith("- fonte academica principal:"):
            fonte_academica_principal = linha_limpa.split(":", 1)[1].strip().lower().replace("-", "_")

        if linha_limpa.lower().startswith("- fontes acadêmicas auxiliares:") or linha_limpa.lower().startswith("- fontes academicas auxiliares:"):
            bruto = linha_limpa.split(":", 1)[1].strip().lower()
            if bruto in {"", "nenhuma", "nenhum", "não", "nao"}:
                fontes_academicas_auxiliares = ["semantic_scholar", "crossref"]
            else:
                fontes_academicas_auxiliares = [f.strip().replace("-", "_") for f in re.split(r"[,;]", bruto) if f.strip()]

        if linha_limpa.lower().startswith("- modelo ia:"):
            modelo_ia = linha_limpa.split(":", 1)[1].strip()

        if linha_limpa.lower().startswith("- modelo openrouter:"):
            modelo_openrouter = linha_limpa.split(":", 1)[1].strip()

        if (linha_limpa.lower().startswith("- modelo ollama:") or
            linha_limpa.lower().startswith("- modelo ollama de reserva:")):
            modelo_ollama = linha_limpa.split(":", 1)[1].strip()

        if (linha_limpa.lower().startswith("- modelos openrouter:") or
            linha_limpa.lower().startswith("- fila openrouter:")):
            bruto = linha_limpa.split(":", 1)[1].strip()
            primeiro = next((m.strip() for m in bruto.split(",") if m.strip()), "")
            if primeiro:
                modelo_openrouter = primeiro

        if linha_limpa.lower().startswith("- artigos analisados por ciclo:"):
            artigos_por_ciclo_ia = int(
                linha_limpa.split(":", 1)[1].strip()
            )

        if lendo_variaveis and linha_limpa.startswith("-") and ":" in linha_limpa:
            nome, bruto = linha_limpa[1:].split(":", 1)
            valores = [v.strip() for v in re.split(r"[,;]", bruto) if v.strip()]
            if valores:
                variaveis_busca[nome.strip().lower()] = valores

        if lendo_consultas and linha_limpa.startswith("-"):
            consulta = linha_limpa[1:].strip()
            if consulta:
                consultas.append(consulta)

    consultas_variaveis = combinacoes_variaveis_busca(variaveis_busca)
    consultas_finais = list(dict.fromkeys((consultas or []) + consultas_variaveis)) or CONSULTAS
    return {
        "consultas": consultas_finais,
        "variaveis_busca": variaveis_busca,
        "ano_minimo": ano_minimo,
        "resultados_por_consulta": resultados_por_consulta,
        "fonte_academica_principal": fonte_academica_principal,
        "fontes_academicas_auxiliares": fontes_academicas_auxiliares,
        "modelo_ia": modelo_ia,
        "modelo_openrouter": modelo_openrouter,
        "modelos_openrouter": [modelo_openrouter] if modelo_openrouter else [],
        "modelo_ollama": modelo_ollama,
        "artigos_por_ciclo_ia": artigos_por_ciclo_ia,
    }


def carregar_jsonl(caminho):
    if not caminho.exists():
        return []

    registros = []

    with caminho.open("r", encoding="utf-8-sig") as arquivo:
        for linha in arquivo:
            linha = linha.strip().lstrip("\ufeff")
            if linha:
                registros.append(json.loads(linha))

    return registros


def salvar_jsonl(caminho, registros):
    with caminho.open("w", encoding="utf-8") as arquivo:
        for registro in registros:
            arquivo.write(
                json.dumps(registro, ensure_ascii=False) + "\n"
            )


def limpar_nome(texto):
    texto = texto or "SemAutor"
    texto = re.sub(r"[^\w\s-]", "", texto, flags=re.UNICODE)
    texto = re.sub(r"\s+", "_", texto.strip())

    return texto[:80] or "SemAutor"


def obter_autor_principal(artigo):
    autores = artigo.get("authorships", [])

    if not autores and artigo.get("autores"):
        autor = artigo["autores"][0]
        return autor.get("nome", "SemAutor").split()[-1] if isinstance(autor, dict) else autor

    if not autores:
        return "SemAutor"

    autor = autores[0].get("author", {})
    nome = autor.get("display_name", "SemAutor")

    partes = nome.split()

    if not partes:
        return "SemAutor"

    return partes[-1]


def extrair_autores(artigo_openalex):
    autores = []

    for autoria in artigo_openalex.get("authorships", []):
        autor = autoria.get("author", {})
        nome = autor.get("display_name")

        if nome:
            autores.append({
                "nome": nome,
                "id_openalex": autor.get("id"),
                "instituicoes": [
                    instituicao.get("display_name")
                    for instituicao in autoria.get("institutions", [])
                    if instituicao.get("display_name")
                ],
            })

    return autores


def gerar_nome_local(artigo, artigos_existentes):
    sobrenome = limpar_nome(obter_autor_principal(artigo))
    ano = artigo.get("publication_year") or "SemAno"

    nome_base = f"{sobrenome}_{ano}"
    nome = nome_base
    contador = 2

    nomes_existentes = {
        artigo_existente.get("nome_local")
        for artigo_existente in artigos_existentes
    }

    while nome in nomes_existentes:
        nome = f"{nome_base}_{contador}"
        contador += 1

    return nome


def buscar_openalex(consulta, limite=10, ano_minimo=2025):
    url = "https://api.openalex.org/works"

    parametros = {
        "search": consulta,
        "per-page": limite,
        "sort": "relevance_score:desc",
        "filter": (
            f"from_publication_date:{ano_minimo}-01-01,"
            f"to_publication_date:{datetime.now().date().isoformat()}"
        ),
    }

    resposta = requests.get(
        url,
        params=parametros,
        timeout=60,
    )

    resposta.raise_for_status()

    return resposta.json()["results"]


def buscar_ids_citantes(artigo_openalex):
    url = artigo_openalex.get("cited_by_api_url")

    if not url:
        return []

    resposta = requests.get(
        url,
        params={
            "per-page": 200,
            "select": "id",
        },
        timeout=60,
    )
    resposta.raise_for_status()

    return [
        resultado.get("id")
        for resultado in resposta.json().get("results", [])
        if resultado.get("id")
    ]


def buscar_trabalho_openalex(identificador):
    resposta = requests.get(
        f"https://api.openalex.org/works/{identificador.rsplit('/', 1)[-1]}",
        timeout=60,
    )
    resposta.raise_for_status()
    return resposta.json()


def obter_relacoes_openalex(artigo_openalex):
    return {
        "referencias_openalex": [
            identificador
            for identificador in artigo_openalex.get("referenced_works", [])
            if identificador
        ],
        "citado_por_openalex": buscar_ids_citantes(artigo_openalex),
        "trabalhos_relacionados_openalex": [
            identificador
            for identificador in artigo_openalex.get("related_works", [])
            if identificador
        ],
    }


def resumo_invertido(indice):
    if not indice:
        return "Resumo não disponível."

    if isinstance(indice, str):
        return indice.strip() or "Resumo não disponível."

    palavras = []

    for palavra, posicoes in indice.items():
        for posicao in posicoes:
            palavras.append((posicao, palavra))

    palavras.sort()

    return " ".join(palavra for _, palavra in palavras)


def texto_resumo(artigo):
    return resumo_invertido(artigo.get("resumo"))




def pontuar_relevancia(artigo):
    texto = " ".join([
        artigo.get("titulo") or "",
        texto_resumo(artigo),
    ]).lower()
    grupos = {
        "cidades_inteligentes": ["smart cit", "smart urban", "cidade inteligente"],
        "iot": ["internet of things", "iot", "sensor", "edge computing"],
        "blockchain": ["blockchain", "smart contract", "distributed ledger"],
        "abe": ["attribute-based encryption", "attribute based encryption", "abe"],
        "interoperabilidade": ["interoperab", "data sharing", "data integration"],
        "privacidade": ["privacy", "confidentiality", "privacy-preserving"],
        "controle_acesso": ["access control", "authorization", "authentication"],
        "interscity": ["interscity"],
    }
    encontrados = [
        grupo
        for grupo, termos in grupos.items()
        if any(termo in texto for termo in termos)
    ]
    pontuacao = len(encontrados)

    if pontuacao >= 4:
        classificacao = "possivelmente_relevante"
    elif pontuacao >= 2:
        classificacao = "revisar_depois"
    else:
        classificacao = "baixa_relevancia_temática"

    return {
        "versao": 2,
        "metodo": "triagem_termos_titulo_resumo",
        "classificacao_sugerida": classificacao,
        "pontuacao": pontuacao,
        "dimensoes_encontradas": encontrados,
        "justificativa": (
            "Foram encontrados no título/resumo os termos associados às dimensões: "
            + (", ".join(encontrados) or "nenhuma dimensão principal")
            + "."
        ),
        "fatos": [
            f"O título do trabalho é: {artigo.get('titulo') or 'não disponível'}.",
            "O resumo contém termos associados às dimensões listadas acima.",
        ],
        "metodos": [],
        "limitacoes_declaradas": [],
        "temas": encontrados,
        "relacao_com_pesquisa": (
            "Relação preliminar inferida por termos; requer leitura do trabalho."
        ),
        "contraexemplos_a_investigar": [
            "Verificar se o trabalho trata apenas uma dimensão isolada."
        ],
        "confianca": "baixa",
        "limite": "Não substitui leitura do artigo completo nem decisão humana.",
    }




def formatar_lista(valores, vazio="Não identificado no título/resumo."):
    if not valores:
        return f"- {vazio}"
    return "\n".join(f"- {valor}" for valor in valores)


def atualizar_analise_nota(artigo):
    caminho = ARTIGOS / f"{artigo['nome_local']}.md"
    if not caminho.exists() or not artigo.get("analise"):
        return

    analise = artigo["analise"]
    conteudo = caminho.read_text(encoding="utf-8-sig")
    secao = f"""## Análise assistida

- **Classificação sugerida:** {analise.get('classificacao_sugerida', 'não definida')}
- **Confiança:** {analise.get('confianca', 'baixa')}
- **Método:** {analise.get('metodo', 'não informado')}
- **Pontuação temática:** {analise.get('pontuacao', 'não calculada')}

### Justificativa

{analise.get('justificativa', 'Triagem baseada nos termos encontrados.')}

### Fatos extraídos provisoriamente

{formatar_lista(analise.get('fatos'))}

### Métodos

{formatar_lista(analise.get('metodos'))}

### Limitações declaradas

{formatar_lista(analise.get('limitacoes_declaradas'))}

### Relação com o projeto

{analise.get('relacao_com_pesquisa', 'Ainda não avaliada.')}

### Contraexemplos a investigar

{formatar_lista(analise.get('contraexemplos_a_investigar'))}

### Limite da análise

{analise.get('limite', 'A análise não substitui leitura integral e validação humana.')}
"""
    conteudo, quantidade = re.subn(
        r"## Análise assistida\n\n.*?(?=\n## Análise\n)",
        secao + "\n",
        conteudo,
        count=1,
        flags=re.DOTALL,
    )
    if not quantidade:
        conteudo = conteudo.replace("## Análise\n", secao + "\n## Análise\n", 1)
    caminho.write_text(conteudo, encoding="utf-8")




def criar_tags(consulta, artigo=None):
    texto = " ".join([
        consulta or "",
        (artigo or {}).get("titulo", ""),
        texto_resumo(artigo or {}),
    ]).lower()
    temas = {
        "cidades-inteligentes": ["smart cit", "smart urban", "cidade inteligente"],
        "iot": ["internet of things", "iot", "sensor", "edge computing"],
        "sistemas-distribuidos": ["distributed system", "distributed data", "decentralized"],
        "interoperabilidade": ["interoperab", "data sharing", "data integration", "interconnection"],
        "blockchain": ["blockchain", "distributed ledger"],
        "contratos-inteligentes": ["smart contract"],
        "abe": ["attribute-based encryption", "attribute based encryption", " abe ", "ciphertext-policy"],
        "controle-de-acesso": ["access control", "authorization", "authentication"],
        "privacidade": ["privacy", "confidentiality", "privacy-preserving", "homomorphic encryption"],
        "seguranca": ["cybersecurity", "cyber security", "intrusion detection", "threat detection"],
        "governanca-de-dados": ["data governance", "data management", "data sharing"],
        "identidade-digital": ["digital identity", "decentralized identity", "identity management"],
        "ssi": ["self sovereign identity", "self-sovereign identity"],
        "credenciais-verificaveis": ["verifiable credential"],
        "cidades-digitais": ["digital twin", "urban digital"],
    }
    return sorted(
        tema for tema, termos in temas.items()
        if any(termo in texto for termo in termos)
    )


def links_para_corpus(identificadores, artigos_por_id, ignorar_id=None):
    return [
        artigos_por_id[identificador]["nome_local"]
        for identificador in identificadores
        if identificador != ignorar_id
        if identificador in artigos_por_id
    ]


def texto_relacoes(artigo, artigos_por_id):
    referencias = links_para_corpus(
        artigo.get("referencias_openalex", []),
        artigos_por_id,
        artigo.get("id_openalex"),
    )
    citantes = links_para_corpus(
        artigo.get("citado_por_openalex", []),
        artigos_por_id,
        artigo.get("id_openalex"),
    )
    relacionados = links_para_corpus(
        artigo.get("trabalhos_relacionados_openalex", []),
        artigos_por_id,
        artigo.get("id_openalex"),
    )

    def lista_links(nomes):
        if not nomes:
            return "- Nenhum trabalho relacionado presente no corpus."
        return "\n".join(f"- [[{nome}]]" for nome in sorted(set(nomes)))

    return (
        "### Referencia\n\n"
        f"{lista_links(referencias)}\n\n"
        "### E citado por\n\n"
        f"{lista_links(citantes)}\n\n"
        "### Trabalhos relacionados\n\n"
        f"{lista_links(relacionados)}"
    )


def criar_nota(artigo, artigos_por_id):
    nome_local = artigo["nome_local"]
    caminho = ARTIGOS / f"{nome_local}.md"

    tags = criar_tags(artigo["consulta"], artigo)
    resumo = resumo_invertido(artigo["resumo"])

    tags_yaml = "tags: [{}]".format(", ".join(tags))

    tags_texto = " ".join(
        f"#{tag}"
        for tag in tags
    )

    autores = artigo.get("autores", [])
    autores_texto = ", ".join(
        autor.get("nome", "SemAutor")
        for autor in autores
    ) or "Sem autores disponíveis"

    conteudo = f"""---
nome_local: {nome_local}
openalex_id: {artigo['id_openalex']}
doi: {artigo['doi']}
ano: {artigo['ano']}
status: triagem_pendente
acesso_aberto: {str(artigo['acesso_aberto']).lower()}
pdf_local: {artigo['pdf_local']}
{tags_yaml}
---

# {nome_local}

## Referência provisória

**Autor principal:** {obter_autor_principal(artigo)}

**Autores:** {autores_texto}

**Ano:** {artigo['ano']}

**Título:** {artigo['titulo']}

## Tags

{tags_texto}

## Metadados

- **OpenAlex:** {artigo['id_openalex']}
- **Fonte:** {artigo.get('fonte', 'OpenAlex')}
- **DOI:** {artigo['doi']}
- **URL:** {artigo['url']}
- **URL de acesso aberto:** {artigo['url_acesso_aberto']}
- **PDF online:** {artigo['url_pdf']}
- **PDF local:** {artigo['pdf_local']}
- **Acesso aberto:** {artigo['acesso_aberto']}

## Consulta que encontrou o artigo

{artigo['consulta']}

## Resumo disponível

{resumo}

## Artigos relacionados

{texto_relacoes(artigo, artigos_por_id)}

## Triagem

- **Classificação:** pendente.
- **Relevância:** ainda não avaliada.
- **Motivo da decisão:** ainda não avaliado.
- **Decisão humana:** ainda não registrada.
- **PDF lido:** não.

## Análise

### Fatos

Ainda não analisado.

### Interpretações

Ainda não analisado.

### Hipóteses

Ainda não analisado.

### Limitações identificadas

Ainda não analisado.

### Relações com outros artigos

As relações bibliográficas acima foram obtidas do OpenAlex. Relações sem nota local permanecem registradas apenas pelos identificadores no JSONL.

### Questões para investigar

Ainda não analisado.
"""

    caminho.write_text(conteudo, encoding="utf-8")


def atualizar_relacoes_nota(artigo, artigos_por_id):
    caminho = ARTIGOS / f"{artigo['nome_local']}.md"

    if not caminho.exists():
        return

    conteudo = caminho.read_text(encoding="utf-8-sig")
    nova_secao = "## Artigos relacionados\n\n" + texto_relacoes(
        artigo,
        artigos_por_id,
    )

    conteudo_atualizado, quantidade = re.subn(
        r"## Artigos relacionados\n\n.*?(?=\n## Triagem)",
        nova_secao + "\n",
        conteudo,
        count=1,
        flags=re.DOTALL,
    )

    if quantidade:
        caminho.write_text(conteudo_atualizado, encoding="utf-8")


def atualizar_triagem_nota(artigo):
    caminho = ARTIGOS / f"{artigo['nome_local']}.md"

    if not caminho.exists():
        return

    conteudo = caminho.read_text(encoding="utf-8-sig")
    autores = artigo.get("autores", [])
    autores_texto = ", ".join(
        autor.get("nome", "SemAutor")
        for autor in autores
    ) or "Sem autores disponíveis"
    conteudo_atualizado = re.sub(
        r"(?m)^status: novo$",
        "status: triagem_pendente",
        conteudo,
    )
    conteudo_atualizado = conteudo_atualizado.replace(
        "#status/novo",
        "#status/triagem-pendente",
    )
    conteudo_atualizado = re.sub(
        r"\*\*Autor principal:\*\* SemAutor",
        f"**Autor principal:** {obter_autor_principal(artigo)}",
        conteudo_atualizado,
        count=1,
    )

    if "**Autores:**" not in conteudo_atualizado:
        conteudo_atualizado = conteudo_atualizado.replace(
            f"**Autor principal:** {obter_autor_principal(artigo)}\n",
            f"**Autor principal:** {obter_autor_principal(artigo)}\n\n"
            f"**Autores:** {autores_texto}\n",
            1,
        )

    if "- **Classificação:**" not in conteudo_atualizado:
        conteudo_atualizado = conteudo_atualizado.replace(
            "## Triagem\n\n",
            "## Triagem\n\n"
            "- **Classificação:** pendente.\n"
            "- **Decisão humana:** ainda não registrada.\n"
            "- **PDF lido:** não.\n",
            1,
        )

    if conteudo_atualizado != conteudo:
        caminho.write_text(conteudo_atualizado, encoding="utf-8")


def atualizar_paineis(artigos, novos, consultas, modelo):
    contagens = {}

    for artigo in artigos:
        status = artigo.get("status", "sem_status")
        contagens[status] = contagens.get(status, 0) + 1

    fila_triagem = [
        artigo
        for artigo in artigos
        if artigo.get("status") == "triagem_pendente"
    ]
    links_triagem = "\n".join(
        f"- {artigo['nome_local']} - {artigo.get('titulo', '')}"
        for artigo in fila_triagem
    ) or "- Nenhum artigo aguardando triagem."

    sessoes = SESSOES / "ultima_coleta.md"
    sessoes.write_text(
        f"""---
tipo: sessao-de-coleta
executado_em: {datetime.now().isoformat()}
---

# Última coleta

## Consultas usadas

{chr(10).join(f'- {consulta}' for consulta in consultas)}

## Resultado

- Artigos novos nesta execução: {len(novos)}
- Artigos no corpus: {len(artigos)}
- Artigos com análise preliminar: {sum(1 for artigo in artigos if artigo.get('analise'))}
- Modelo de análise: {modelo} (com fallback determinístico se indisponível)
- Estados: {json.dumps(contagens, ensure_ascii=False)}

## Fila de triagem

{links_triagem}

## Próximo passo humano

Abra os artigos da fila, registre a classificação e o motivo da decisão.
Não apague artigos: marque-os como `irrelevante` quando essa for a decisão.
""",
        encoding="utf-8",
    )

    indice_propostas = PROPOSTAS / "00-indice-propostas.md"

    if not indice_propostas.exists():
        indice_propostas.write_text(
            """---
tipo: indice-de-propostas
status: em-construcao
---

# Propostas de trabalho

Ainda não há uma proposta validada. Este arquivo será atualizado quando
a evidência da literatura e a triagem humana permitirem formular uma
hipótese de contribuição.

## Estrutura de cada proposta

### Problema observado

Descrever o problema com referências e evidências.

### Fatos

O que os trabalhos efetivamente afirmam ou demonstram.

### Interpretação

Leitura comparativa dos fatos, sem apresentá-la como fato.

### Hipótese de lacuna

Ausência ou limitação observada, sempre acompanhada dos trabalhos
consultados e dos contraexemplos encontrados.

### Validação necessária

Como verificar se a hipótese é verdadeira.

### Proposta de contribuição

O que poderia ser construído, com escopo realista, dados disponíveis,
método, métricas e limitações.

### Trabalhos próximos

Trabalhos que chegaram perto e quais alterações seriam necessárias.

### Estado

`em-investigacao`
""",
            encoding="utf-8",
        )




if __name__ == "__main__":
    import sys
    from motor import principal
    principal(sys.modules[__name__])



