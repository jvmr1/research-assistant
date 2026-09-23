"""Geração dos arquivos Markdown visíveis para o pesquisador.

Responsabilidades deste arquivo:
- atualizar obsidian/ANOTACOES.md com propostas e feedback humano;
- atualizar dados/anotacoes-ia.md com rastreabilidade e memória operacional;
- atualizar obsidian/TRABALHO.md com a redação acadêmica em andamento;
- manter em obsidian/referencias/fichamentos/ somente o resumo e as evidências do próprio artigo;
    conexões, lacunas e propostas ficam em ANOTACOES.md ou TRABALHO.md.

Este arquivo deve só apresentar o estado já calculado. Ele não deve buscar
artigos, chamar modelos de IA ou decidir relevância científica.
"""
import json
import re
from urllib.parse import quote


INICIO = '<!-- agente:inicio -->'
FIM = '<!-- agente:fim -->'
BLOCO_PROPOSTAS_INICIO = '<!-- agente:propostas:inicio -->'
BLOCO_PROPOSTAS_FIM = '<!-- agente:propostas:fim -->'
BLOCO_IA_INICIO = '<!-- agente:memoria-ia:inicio -->'
BLOCO_IA_FIM = '<!-- agente:memoria-ia:fim -->'
BLOCO_TRABALHO_INICIO = '<!-- agente:trabalho:inicio -->'
BLOCO_TRABALHO_FIM = '<!-- agente:trabalho:fim -->'
BLOCO_DIALOGO_INICIO = '<!-- agente:dialogo:inicio -->'
BLOCO_DIALOGO_FIM = '<!-- agente:dialogo:fim -->'
ARQUIVOS_LEGADOS_OBSIDIAN = [
    'INSTRUCOES.md',
    'AVALIAR-PROPOSTAS.md',
    'PROPOSTAS-DE-TRABALHO.md',
    'METODOLOGIA-REVISAO.md',
    'RELATORIO.md',
    'INTRODUCAO-E-FUNDAMENTACAO.md',
]
CAMPOS = {
    'problema': 'Problema observado', 'fatos': 'Fatos sustentados nos trabalhos',
    'interpretacao': 'Interpretação feita', 'hipotese_lacuna': 'Hipótese de lacuna',
    'meu_trabalho': 'O que seria o meu trabalho de mestrado',
    'alteracao_sobre_trabalhos_proximos': 'Trabalhos próximos e o que eu alteraria',
    'experimento': 'Como desenvolver e avaliar', 'recursos': 'Recursos necessários',
    'metricas': 'Métricas', 'riscos': 'Riscos e limites',
    'contraexemplos_a_buscar': 'O que pode contradizer a hipótese',
    'duvidas_orientador': 'Questões para discutir com o orientador',
}


def ler(path, padrao):
    if not path.exists():
        return padrao
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError):
        return padrao


def valor_markdown(valor):
    """Converte respostas da IA para texto antes de escrever Markdown.

    Algumas respostas chegam como dict/list mesmo quando o prompt pediu string.
    O relatorio nao deve quebrar por isso; ele registra o conteudo em forma legivel.
    """
    if valor is None:
        return ''
    if isinstance(valor, str):
        return valor.strip()
    if isinstance(valor, list):
        return '; '.join(valor_markdown(v) for v in valor if valor_markdown(v))
    if isinstance(valor, dict):
        partes = []
        for k, v in valor.items():
            tv = valor_markdown(v)
            if tv:
                partes.append(f'{k}: {tv}')
        return '; '.join(partes)
    return str(valor)


def link(nome, prefixo='referencias/fichamentos/'):
    return f'[{nome}]({prefixo}{quote(nome)}.md)'


def garantir_frontmatter_e_secao_tags(conteudo, artigo, tags):
    if not conteudo.startswith('---\n'):
        pos = conteudo.find('\n---\n')
        if pos >= 0:
            prefixo = conteudo[:pos + 1]
            return prefixo + garantir_frontmatter_e_secao_tags(conteudo[pos + 1:], artigo, tags)
    tags_yaml = 'tags: [{}]'.format(', '.join(tags))
    linhas_yaml = [
        '---',
        f"nome_local: {artigo.get('nome_local', '')}",
        f"openalex_id: {artigo.get('id_openalex', '')}",
        f"doi: {artigo.get('doi', '')}",
        f"ano: {artigo.get('ano', '')}",
        f"status: {artigo.get('status', 'triagem_pendente')}",
        f"acesso_aberto: {str(artigo.get('acesso_aberto', False)).lower()}",
        f"pdf_local: {artigo.get('pdf_local', '')}",
        tags_yaml,
        '---',
        '',
    ]
    if re.match(r'\A---\n', conteudo):
        conteudo = re.sub(r'(?ms)^tags:.*?(?=^---$|^# )', tags_yaml + '\n', conteudo, count=1)
        if not re.search(r'(?m)^tags:', conteudo.split('---', 2)[1] if conteudo.count('---') >= 2 else ''):
            conteudo = re.sub(r'\A---\n', '---\n' + tags_yaml + '\n', conteudo, count=1)
    else:
        conteudo = '\n'.join(linhas_yaml) + conteudo.lstrip()
    tags_texto = ' '.join(f'#{tag}' for tag in tags) or 'Nenhum tema identificado'
    if re.search(r'(?ms)^## Tags\n\n', conteudo):
        conteudo = re.sub(r'(?ms)^## Tags\n\n.*?(?=\n## |<!-- agente:inicio -->|\Z)', f'## Tags\n\n{tags_texto}\n', conteudo, count=1)
    else:
        conteudo = re.sub(r'(?m)^# .*$\n', lambda m: m.group(0) + f'\n## Tags\n\n{tags_texto}\n', conteudo, count=1)
    return conteudo


def deve_ter_nota_markdown(artigo, revisao, fontes_relevantes):
    """Controla quais trabalhos entram no grafo do Obsidian.

    O obsidian é a interface de leitura do pesquisador, não o log completo do
    funil. Trabalhos sem proposta ficam apenas em dados/*.json/jsonl.
    """
    nome = artigo.get('nome_local')
    if nome in fontes_relevantes:
        return True
    return (
        artigo.get('fonte') == 'PDF de exemplo fornecido pelo pesquisador'
        and artigo.get('sintese_artigo', {}).get('revisao') == revisao
    )


def proposta_descartada(meta, obj):
    valor = (obj or {}).get('avaliacao_humana') or (meta or {}).get('avaliacao_humana') or ''
    return str(valor).strip().lower() == 'descartar'


def referencias_citadas_no_obsidian(root):
    """IDs de fichamentos citados nas anotações ou no trabalho atual."""
    citadas = set()
    for rel in ('obsidian/ANOTACOES.md', 'obsidian/TRABALHO.md'):
        path = root / rel
        if not path.exists():
            continue
        texto = path.read_text(encoding='utf-8-sig')
        citadas.update(re.findall(r'referencias/fichamentos/([^\]|)#]+)', texto))
        citadas.update(re.findall(r'\[\[referencias/fichamentos/([^\]|#]+)', texto))
    return {nome[:-3] if nome.endswith('.md') else nome for nome in citadas}


def referencias_ativas(root, propostas, redacao=None):
    """Referências que devem permanecer visíveis no Obsidian."""
    ativas = {
        fonte
        for meta, obj in propostas
        if not proposta_descartada(meta, obj)
        for fonte in (obj.get('fontes', meta.get('fontes', [])) if obj else meta.get('fontes', []))
    }
    if isinstance(redacao, dict):
        ativas.update(f for f in redacao.get('fontes_usadas', []) if isinstance(f, str))
        for fase in redacao.get('mapa_fases', []) if isinstance(redacao.get('mapa_fases'), list) else []:
            if isinstance(fase, dict):
                ativas.update(f for f in fase.get('fontes', []) if isinstance(f, str))
    ativas.update(referencias_citadas_no_obsidian(root))
    return ativas


def link_ou_nome(nome, root):
    path = root / 'obsidian/referencias/fichamentos' / f'{nome}.md'
    return link(nome) if path.exists() else f'`{nome}`'


def bloco_callout_dobravel(titulo, linhas, tipo='abstract'):
    """Cria callout dobravel nativo do Obsidian preservando Markdown interno."""
    titulo = str(titulo).replace('\n', ' ').strip()
    saida = [f'> [!{tipo}]- {titulo}']
    for linha in linhas:
        texto = str(linha)
        if texto == '':
            saida.append('>')
        else:
            for sublinha in texto.splitlines() or ['']:
                saida.append('> ' + sublinha)
    return saida


def atualizar_bloco_preservando_texto(path, inicio, fim, cabecalho, linhas_bloco):
    """Atualiza um bloco gerado sem apagar as anotações livres do pesquisador."""
    bloco = '\n'.join([inicio, *linhas_bloco, fim]).rstrip() + '\n'
    if path.exists():
        conteudo = path.read_text(encoding='utf-8-sig')
    else:
        conteudo = cabecalho.rstrip() + '\n\n'
    padrao = re.escape(inicio) + r'.*?' + re.escape(fim)
    if re.search(padrao, conteudo, flags=re.S):
        novo = re.sub(padrao, bloco.rstrip(), conteudo, count=1, flags=re.S)
    else:
        novo = conteudo.rstrip() + '\n\n' + bloco
    return novo.rstrip() + '\n'


def migrar_anotacoes_do_pesquisador(root):
    """Cria o arquivo único do pesquisador reunindo conteúdo útil legado."""
    path = root / 'obsidian/ANOTACOES.md'
    if path.exists():
        return
    partes = [
        '# Anotações',
        '',
        'Este é o arquivo principal para conversar com a IA sobre a pesquisa. Escreva aqui o rumo desejado, decisões, dúvidas e feedback sobre propostas.',
        '',
        'A IA preserva estas anotações livres e atualiza apenas os blocos marcados por comentários HTML.',
    ]
    for nome in ['INSTRUCOES.md', 'AVALIAR-PROPOSTAS.md', 'PROPOSTAS-DE-TRABALHO.md']:
        legado = root / 'obsidian' / nome
        if legado.exists():
            partes += ['', f'## Conteúdo migrado de `{nome}`', '', legado.read_text(encoding='utf-8-sig').strip()]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(partes).rstrip() + '\n', encoding='utf-8')


def limpar_arquivos_legados_obsidian(root):
    for nome in ARQUIVOS_LEGADOS_OBSIDIAN:
        (root / 'obsidian' / nome).unlink(missing_ok=True)


def avaliacoes_existentes(path):
    conteudo_nota = path.read_text(encoding='utf-8') if path.exists() else ''
    dados = {}
    atual = None
    for linha in conteudo_nota.splitlines():
        if linha.startswith('id:'):
            atual = linha.split(':', 1)[1].strip()
            dados.setdefault(atual, {})['id'] = atual
        elif atual and linha.startswith('avaliacao:'):
            dados[atual]['avaliacao'] = linha.split(':', 1)[1].strip()
        elif atual and linha.startswith('comentario:'):
            dados[atual]['comentario'] = linha.split(':', 1)[1].strip()
    return dados


def atualizar_avaliacao_propostas(root, propostas, revisao, agora_func, artigos=None):
    path = root / 'obsidian/ANOTACOES.md'
    legado = root / 'obsidian/AVALIAR-PROPOSTAS.md'
    antigas = avaliacoes_existentes(path)
    antigas.update(avaliacoes_existentes(legado))
    linhas = [
        '## Propostas',
        f'Atualizado: {agora_func()}',
        'Cada proposta fica em um toggle. Abra, revise resumo/trabalhos/descrição e edite `avaliacao:` e `comentario:` no final do próprio item.',
        'Valores úteis para `avaliacao:`: `pendente`, `muito_interessante`, `gostei`, `neutra`, `descartar`.',
    ]
    atuais = [(m, o) for m, o in propostas
              if m.get('revisao') == revisao and not proposta_descartada(m, o)]
    if artigos is not None:
        linhas += ['', *linhas_lista_propostas(root, propostas, revisao, artigos, agora_func, antigas)]
    elif not atuais:
        linhas.append('Ainda não há propostas nesta orientação.')
    gravar = __import__('src.motor', fromlist=['gravar']).gravar
    cabecalho = (
        '# Anotações\n\n'
        'Este é o arquivo principal de conversa com a IA. Escreva livremente fora dos blocos automáticos.\n'
    )
    gravar(path, atualizar_bloco_preservando_texto(path, BLOCO_PROPOSTAS_INICIO, BLOCO_PROPOSTAS_FIM, cabecalho, linhas))


def atualizar_lista_propostas(root, propostas, revisao, artigos, agora_func):
    """Mantida por compatibilidade: as propostas agora ficam nas anotações."""
    atualizar_avaliacao_propostas(root, propostas, revisao, agora_func, artigos)


def linhas_lista_propostas(root, propostas, revisao, artigos, agora_func, antigas=None):
    """Gera a visão curta das propostas para o bloco do pesquisador."""
    atuais = [(m, o) for m, o in propostas
              if m.get('revisao') == revisao and not proposta_descartada(m, o)]
    antigas = antigas or {}
    linhas = []
    if not atuais:
        linhas.append('Ainda não há propostas ativas para a orientação atual. Quando houver propostas antigas sem detalhamento suficiente, o agente deve reler a memória interna, fichamentos e fontes para desenvolver melhor antes de levar ao trabalho.')
    for indice, (meta, obj) in enumerate(atuais, 1):
        obj = obj or {}
        titulo = meta.get('titulo', 'Proposta sem título')
        fontes = obj.get('fontes', meta.get('fontes', []))
        antigo = antigas.get(meta.get('id'), {})
        avaliacao = antigo.get('avaliacao') or obj.get('avaliacao_humana') or 'pendente'
        comentario = antigo.get('comentario') or obj.get('comentario_humano') or ''
        tags = sorted({tag for fonte in fontes for tag in __import__('src.agente', fromlist=['criar_tags']).criar_tags(artigos.get(fonte, {}).get('consulta', ''), artigos.get(fonte, {}))})
        resumo = valor_markdown(obj.get('meu_trabalho') or obj.get('hipotese_lacuna') or 'Detalhes ainda incompletos no relatório.')
        trabalhos = '\n'.join(f'- {link_ou_nome(fonte, root)} — {artigos.get(fonte, {}).get("titulo", fonte)}' for fonte in fontes) or '- Nenhuma fonte informada.'
        linhas += [
            '<details>',
            f'<summary>{indice}. {titulo}</summary>',
            '',
            '### Resumo',
            resumo,
            '',
            '### Trabalhos-base e fontes usadas',
            trabalhos,
            '',
            '### Descrição detalhada da proposta',
            '**Ideia do trabalho**',
            resumo,
            '',
            '**Lacuna explorada**',
            valor_markdown(obj.get('hipotese_lacuna') or 'Ainda não registrada.'),
            '',
            '**Problema observado**',
            valor_markdown(obj.get('problema') or 'Ainda não detalhado.'),
            '',
            '**Fatos sustentados nos trabalhos**',
            valor_markdown(obj.get('fatos') or 'Ainda não detalhado.'),
            '',
            '**Interpretação feita**',
            valor_markdown(obj.get('interpretacao') or 'Ainda não detalhada.'),
            '',
            '**Trabalhos próximos e o que eu alteraria**',
            valor_markdown(obj.get('alteracao_sobre_trabalhos_proximos') or 'Ainda não detalhado.'),
            '',
            '**Como desenvolver e avaliar**',
            valor_markdown(obj.get('experimento') or 'Ainda não detalhado.'),
            '',
            '**Recursos, ferramentas e dados possíveis**',
            valor_markdown(obj.get('recursos') or 'Ainda não detalhado.'),
            '',
            '**Métricas de avaliação**',
            valor_markdown(obj.get('metricas') or 'Ainda não detalhado.'),
            '',
            '**Riscos, limites e incertezas**',
            valor_markdown(obj.get('riscos') or 'Ainda não detalhado.'),
            '',
            '**Perguntas para reunião com orientador**',
            valor_markdown(obj.get('duvidas_orientador') or 'Ainda não detalhado.'),
            '',
            '**Tags temáticas**',
            ' '.join(f'#{tag}' for tag in tags) or 'Nenhuma tag temática identificada.',
            '',
            '**Próximas buscas sugeridas**',
            '\n'.join(f'- {q}' for q in obj.get('buscas', [])) or '- Nenhuma busca sugerida.',
            '',
            '### Avaliação do pesquisador',
            f'id: {meta.get("id")}',
            f'avaliacao: {avaliacao}',
            f'comentario: {comentario}',
            'fontes: ' + (', '.join(fontes) if fontes else 'não informadas'),
            '',
            '</details>',
            '',
        ]
    candidatos = []
    for artigo in artigos.values():
        triagem = artigo.get('triagem_agente', {})
        if triagem.get('revisao') != revisao or triagem.get('classificacao') not in {'priorizar', 'revisar', 'sem_resumo'}:
            continue
        if artigo.get('sintese_artigo', {}).get('revisao') == revisao:
            continue
        candidatos.append(artigo)
    if candidatos:
        linhas += [
            '## Trabalhos acadêmicos recentes que merecem leitura/checagem',
            'Estes trabalhos apareceram nas buscas acadêmicas ou no acervo e ainda estão em análise. Eles podem orientar a pesquisa, mas só viram referências após texto disponível, leitura e decisão de relevância.',
            '',
        ]
        for artigo in sorted(candidatos, key=lambda a: a.get('nome_local', ''))[:12]:
            linhas += [
                f"- `{artigo.get('nome_local')}` — {artigo.get('titulo', '')}. "
                f"Pré-leitura: {artigo.get('pre_leitura_agente', {}).get('decisao', 'pendente')}. "
                f"Motivo: {valor_markdown(artigo.get('triagem_agente', {}).get('justificativa', ''))[:350]}"
            ]
    ativas = referencias_ativas(root, atuais, ler(root / 'dados/redacao-focada.json', {}))
    bases = [a for a in artigos.values() if a.get('fonte') == 'PDF de exemplo fornecido pelo pesquisador']
    analisadas_sem_uso = [
        a for a in artigos.values()
        if a.get('sintese_artigo', {}).get('revisao') == revisao
        and a.get('nome_local') not in ativas
        and a.get('fonte') != 'PDF de exemplo fornecido pelo pesquisador'
    ]
    if analisadas_sem_uso:
        linhas += ['', '## Referências analisadas sem uso ativo',
                   'Estes trabalhos têm leitura/fichamento, mas ainda não sustentam proposta ativa nem trecho aprovado do trabalho. Se uma proposta for marcada como `descartar`, o agente registra as fontes em `dados/` para evitar repetir a direção. A remoção física de PDFs deve ser feita só com confirmação explícita.', '']
        for artigo in sorted(analisadas_sem_uso, key=lambda a: a.get('nome_local', ''))[:20]:
            linhas.append(f"- `{artigo.get('nome_local')}` — {artigo.get('titulo', '')}")
    if bases:
        linhas += ['', '## Trabalhos-base preservados',
                   'Estes trabalhos foram fornecidos como sementes pelo pesquisador e permanecem na base mesmo quando não sustentam uma proposta ativa.', '']
        for artigo in sorted(bases, key=lambda a: a.get('nome_local', '')):
            linhas.append(f"- `{artigo.get('nome_local')}` — {artigo.get('titulo', artigo.get('nome_local'))}")

    consultas = []
    redacao = ler(root / 'dados/redacao-focada.json', {})
    consultas.extend(redacao.get('consultas_novas', []) if isinstance(redacao.get('consultas_novas', []), list) else [])
    for item in propostas:
        obj = ler(root / 'dados/propostas' / f"{item[0].get('id')}.json", {})
        consultas.extend(obj.get('buscas', []) if isinstance(obj.get('buscas', []), list) else [])
    if consultas:
        linhas += ['', '## Consultas acadêmicas para a próxima rodada',
                   'Consultas geradas a partir das anotações, do trabalho atual e da memória da IA. Os resultados ainda precisam de triagem e não são referências aprovadas.',
                   '\n'.join(f'- {q}' for q in dict.fromkeys(consultas) if q)]
    return linhas


def atualizar_redacao_focada(p, agora_func):
    if p.cfg.get('modo_pesquisa') != 'focada':
        return
    from src.motor import gravar
    redacao = p.estado.get('redacao_focada', {})
    destino = p.root / 'obsidian/TRABALHO.md'
    if redacao.get('status') == 'aguardando_fontes' or not redacao.get('introducao'):
        return
    linhas = [
        BLOCO_TRABALHO_INICIO,
        '## Atualização assistida pela IA',
        f'Atualizado: {agora_func()}',
        '> Rascunho produzido pela IA a partir das fontes lidas. As marcações com IDs reais, como `[Papatheodorou_2025]`, e a lista de fontes permitem conferência; a redação ainda exige revisão humana.',
    ]
    if redacao.get('status') == 'aguardando_fontes' or not redacao.get('introducao'):
        linhas += ['', 'Ainda não há fichas suficientes para redigir. O agente continuará após concluir a leitura de fontes alinhadas ao escopo focado.']
    else:
        linhas += ['', f"Status: `{redacao.get('status', 'rascunho')}`.", '### Introdução']
        for secao in redacao.get('introducao', []):
            if isinstance(secao, dict):
                linhas += [secao.get('texto', '')]
            else:
                linhas += [str(secao)]
        linhas += ['### Fundamentação teórica']
        for secao in redacao.get('fundamentacao_teorica', []):
            if isinstance(secao, dict):
                linhas += [f"### {secao.get('titulo', 'Subseção')}", secao.get('texto', '')]
            else:
                linhas += [str(secao)]
        linhas += ['## Mapa do ciclo de vida e pontos de atenção']
        for fase in redacao.get('mapa_fases', []):
            linhas += ['', f"### {fase.get('fase', 'Fase não identificada')}",
                       '**Ações do cidadão**', fase.get('acoes_cidadao', 'Não identificado nas fontes lidas.'),
                       '**Ações das entidades administrativas**', fase.get('acoes_entidades', 'Não identificado nas fontes lidas.'),
                       '**Riscos de segurança e privacidade**', fase.get('riscos', 'Não identificado nas fontes lidas.'),
                       '**Estado da arte**', fase.get('estado_da_arte', 'Não identificado nas fontes lidas.'),
                       '**Lacunas ou melhorias a investigar**', fase.get('lacunas', 'Não identificado nas fontes lidas.'),
                       '**Fontes da fase**', ', '.join(f'[{f}]' for f in fase.get('fontes', [])) or 'Nenhuma fonte associada.']
        linhas += ['', '### Fontes usadas',
                   '\n'.join(f'- {link(nome)}' for nome in redacao.get('fontes_usadas', [])) or '- Nenhuma fonte validada.']
    linhas.append(BLOCO_TRABALHO_FIM)
    bloco = '\n\n'.join(linhas) + '\n'
    atual = destino.read_text(encoding='utf-8-sig') if destino.exists() else ''
    padrao = re.escape(BLOCO_TRABALHO_INICIO) + r'.*?' + re.escape(BLOCO_TRABALHO_FIM)
    if re.search(padrao, atual, flags=re.S):
        novo = re.sub(padrao, bloco.rstrip(), atual, count=1, flags=re.S)
    else:
        separador = '\n\n' if atual.rstrip() else ''
        novo = atual.rstrip() + separador + bloco
    if novo != atual:
        gravar(destino, novo)


def atualizar_dialogo_pesquisa(p, agora_func):
    if p.cfg.get('modo_pesquisa') != 'focada':
        return
    from src.motor import gravar
    redacao = p.estado.get('redacao_focada', {})
    atual = p.b.ANOTACOES_PESQUISADOR.read_text(encoding='utf-8-sig') if p.b.ANOTACOES_PESQUISADOR.exists() else '# Anotações\n'
    respostas = {
        titulo.strip(): resposta.strip()
        for titulo, resposta in re.findall(
            r'(?ms)^####\s+\d+\.\s+(.*?)\n.*?^resposta_pesquisador:\s*(.*?)\s*(?=^####\s+\d+\.\s+|^###\s+|<!-- agente:dialogo:fim -->)',
            atual)
    }
    linhas = ['## Diálogo de pesquisa da IA',
              f'Atualizado: {agora_func()}',
              'Este bloco é produzido pela IA. O pesquisador deve responder aos achados e marcar cada ação como `aprovar`, `rejeitar` ou `revisar`. Nada aqui é aprovação automática.']
    achados = redacao.get('achados_em_analise', [])
    if achados:
        linhas += ['', '### Achados em análise']
        for indice, item in enumerate(achados, 1):
            titulo = item.get('titulo', 'Achado sem título')
            linhas += [f'#### {indice}. {titulo}',
                       f'consulta: {item.get("consulta", "")}',
                       f'resumo: {item.get("resumo", "")}',
                       f'acao_pesquisador: {item.get("acao_pesquisador", "revisar")}',
                       'resposta_pesquisador: ' + respostas.get(titulo, '')]
    else:
        linhas += ['', 'Ainda não há achados novos aguardando resposta.']
    aprovadas = redacao.get('decisoes_aprovadas', [])
    if aprovadas:
        linhas += ['', '### Decisões aprovadas consideradas pela IA',
                   '\n'.join(f'- {item}' for item in aprovadas)]
    novo = atualizar_bloco_preservando_texto(
        p.b.ANOTACOES_PESQUISADOR,
        BLOCO_DIALOGO_INICIO,
        BLOCO_DIALOGO_FIM,
        '# Anotações\n\nEste é o arquivo principal de conversa com a IA.',
        linhas,
    )
    if len(novo) + 100 < len(atual):
        raise ValueError('Atualização da IA reduziria ANOTACOES.md inesperadamente; escrita cancelada.')
    if novo != atual:
        gravar(p.b.ANOTACOES_PESQUISADOR, novo)


def atualizar(p):
    from src.motor import gravar, agora
    root = p.root
    migrar_anotacoes_do_pesquisador(root)
    atualizar_redacao_focada(p, agora)
    atualizar_dialogo_pesquisa(p, agora)
    artigos = {a['nome_local']: a for a in p.artigos}
    ids = {a['id_openalex']: a['nome_local'] for a in p.artigos}
    todas_propostas = [(meta, ler(root / 'dados/propostas' / f"{meta['id']}.json", {}))
                       for meta in p.estado['propostas']]
    propostas = [(meta, obj) for meta, obj in todas_propostas if not proposta_descartada(meta, obj)]
    leituras = [a.get('leitura_agente', {}) for a in p.artigos
                if a.get('leitura_agente', {}).get('revisao') == p.revisao]
    feitos = sum(l.get('feitos', 0) for l in leituras)
    total = sum(l.get('total', 0) for l in leituras)
    titulo_relatorio = ('Estado da arte e redação da pesquisa focada'
                        if p.cfg.get('modo_pesquisa') == 'focada'
                        else 'Lacunas e propostas para meu mestrado')
    linhas = [f'# {titulo_relatorio}', f'Atualizado: {agora()}',
              f'**Andamento:** {p.mensagem}',
              f'Acervo: {len(artigos)} trabalhos. Sinteses uteis: {sum(a.get("sintese_artigo", {}).get("revisao") == p.revisao for a in artigos.values())}. Leitura planejada: {feitos}/{total} trechos.',
              ('O documento de redação focada acompanha a introdução e a fundamentação teórica. As lacunas continuam sendo hipóteses e precisam de verificação.'
               if p.cfg.get('modo_pesquisa') == 'focada'
               else 'As propostas abaixo são hipóteses de contribuição. Novidade e viabilidade ainda precisam ser verificadas.')]
    atuais = [(m, o) for m, o in propostas if m['revisao'] == p.revisao]
    antigas = [(m, o) for m, o in propostas if m['revisao'] != p.revisao]
    linhas += ['## Propostas para a orientação atual']
    if not atuais:
        linhas += ['Ainda não há propostas registradas para esta orientação. Assim que um trabalho interessante tiver fichamento suficiente, o agente deve registrar ideias preliminares; leituras posteriores podem reforçar, contradizer ou substituir essas ideias.']
    def proposta(meta, obj):
        titulo = meta.get('titulo', 'Proposta sem título')
        fontes_resumo = obj.get('fontes', meta.get('fontes', [])) if obj else meta.get('fontes', [])
        tipo = 'comparativa' if len(fontes_resumo or []) >= 2 else 'individual'
        titulo_callout = f'{titulo} — {tipo}; {len(fontes_resumo or [])} trabalho(s)'
        corpo = []
        if not obj:
            return bloco_callout_dobravel(titulo_callout, ['Registro detalhado indisponível; não é possível reconstruir esta proposta.'])
        metodo = ('Fichamento individual de um trabalho; hipótese inicial a confrontar nas próximas leituras.'
                  if obj.get('modo') == 'artigo'
                  else 'Comparação de perfis acumulados de trabalhos lidos; não é uma revisão exaustiva.')
        corpo += [f"Gerada em {obj.get('gerado_em', 'não informado')}. Modelo: {obj.get('modelo', 'não informado')}.",
                  '**Como a pesquisa chegou a esta hipótese**',
                  metodo]
        fontes = ler(root / 'dados/propostas' / f"{meta['id']}-fontes.json", {}).get('fontes', [])
        for fonte in fontes:
            a = artigos.get(fonte['id'], {})
            escopo = fonte.get('escopo', {})
            corpo += [f"- {link(fonte['id'])}: {fonte.get('titulo', '')}. Base da leitura: {escopo.get('tipo', 'não informada')}; "
                      f"{escopo.get('feitos', '?')}/{escopo.get('total', '?')} trechos. Consulta original: {a.get('consulta', 'PDF fornecido localmente')}."]
        if not fontes:
            corpo += ['Trabalhos: ' + ', '.join(link(n) for n in obj.get('fontes', []))]
        for campo, titulo in CAMPOS.items():
            padrao = 'Caminho experimental ainda em desenvolvimento.' if campo == 'experimento' and obj.get('modo') == 'brainstorm' else 'Ainda não registrado.'
            corpo += [f'**{titulo}**', str(obj.get(campo, padrao))]
        corpo += ['**Evidências usadas nesta comparação**']
        selecionadas = set(obj.get('evidencias_usadas', []))
        for fonte in fontes:
            for ficha in fonte.get('fichas_amostradas', []):
                if ficha['id'] in selecionadas:
                    corpo += [f"- {link(fonte['id'])}, página {ficha.get('pagina') or 'resumo'}, ficha `{ficha['id']}`: {ficha.get('resumo', '')}"]
                    for e in ficha.get('evidencias', []):
                        corpo += [f"  - Afirmação da IA: {e['afirmacao']} — citação conferida: {e['citacao']}"]
        corpo += ['**Buscas sugeridas para confrontar a hipótese**', '\n'.join('- ' + q for q in obj.get('buscas', [])) or 'Nenhuma.']
        posteriores = [h for h in p.estado['historico'] if h.get('origem') == 'proposta ' + meta['id']]
        corpo += ['**Checagens posteriores**']
        if not posteriores:
            corpo += ['Ainda nao executadas. A hipotese ainda nao foi confrontada por buscas adicionais.']
        for h in posteriores:
            quantidade = len(h.get('resultados', []) or [])
            detalhe = f"{quantidade} resultado(s) registrado(s) na metodologia/rastreabilidade." if quantidade else h.get('erro', 'Nenhum resultado.')
            corpo += [f"- {h['quando']} - {h['consulta']}: {h['status']}. {detalhe}"]
        return bloco_callout_dobravel(titulo_callout, corpo)
    for meta, obj in atuais:
        linhas += proposta(meta, obj)
    if antigas:
        linhas += ['## Propostas de orientações anteriores']
        for meta, obj in antigas:
            linhas += proposta(meta, obj)

    redacao = ler(root / 'dados/redacao-focada.json', {})
    fontes_relevantes = referencias_ativas(root, propostas, redacao)
    (root / 'obsidian/TRABALHOS-SEM-PROPOSTA.md').unlink(missing_ok=True)
    atualizar_avaliacao_propostas(root, propostas, p.revisao, agora, artigos)

    metodologia = ['# Metodologia e rastreabilidade da revisão', f'Atualizado: {agora()}',
                   f'Orientação analisada: `{p.revisao}`',
                   '## Objetivo e escopo',
                   'Identificar trabalhos recentes sobre o tema definido em ANOTACOES.md, selecionar os que merecem aprofundamento, extrair evidências e formular hipóteses de lacuna com propostas de contribuição ainda não validadas.',
                   '## Consultas e fontes',
                   'As consultas são as registradas em ANOTACOES.md e as consultas posteriores geradas para confrontar hipóteses. A descoberta usa OpenAlex, Semantic Scholar e Crossref; o sistema registra quais fontes responderam a cada busca. O texto completo é procurado em versões abertas indicadas pelas fontes, em PDF ou HTML/XML.',
                   '### Consultas registradas']
    for ident, consulta in p.estado.get('consultas', {}).items():
        if consulta.get('revisao') == p.revisao:
            metodologia.append(f"- `{consulta.get('consulta', '')}` — origem: {consulta.get('origem', 'não informada')}; página atual: {consulta.get('pagina', 1)}")
    metodologia += ['## Seleção e análise',
                     'O fluxo reproduz uma revisão em funil: (1) definição de variáveis e consultas; (2) identificação por fontes acadêmicas; (3) deduplicação por DOI ou título; (4) triagem de título e resumo; (5) pré-leitura de introdução/conclusão ou resumo para confirmar alinhamento; (6) leitura integral dos aprovados; (7) extração de evidências; (8) comparação e síntese de lacunas; (9) propostas de contribuição como hipóteses a validar.',
                     '1. Resultados são deduplicados por DOI ou título normalizado.',
                     '2. A IA faz triagem de título e resumo em `priorizar`, `revisar`, `baixa` ou `sem_resumo`; a triagem não é decisão definitiva.',
                     '3. São tentados textos completos abertos dos trabalhos priorizados/revisados. Quando não há texto completo, o resumo é usado na pré-leitura como evidência limitada.',
                     '4. Antes da leitura integral, a IA avalia introdução e conclusão quando extraíveis para decidir `ler_integralmente`, `ler_com_resumo`, `manter_como_contexto`, `descartar` ou `precisa_texto_melhor`.',
                     '5. O texto aprovado é dividido em trechos. A IA produz fichas com resumo, interpretação, dúvidas e citações literais conferidas no trecho original. Propostas preliminares podem ser geradas a partir do fichamento de um único trabalho. Com novas leituras, elas podem ser reforçadas, contraditas, substituídas ou virar propostas comparativas do estado da arte.',
                     '6. A próxima busca só é liberada quando não há trabalho pendente no acervo. Cada trabalho é levado até um destino claro — descartado, sem texto integral, contexto ou lido/sintetizado — antes de o agente escolher outro. Assim o acervo cresce por trabalhos processados, não por coleta contínua sem síntese.',
                     '## Tags de busca',
                     'Tags derivadas das consultas: ' + ', '.join(sorted({tag for consulta in p.cfg.get('consultas', []) for tag in p.b.criar_tags(consulta)})),
                     '## Contagem do fluxo',
                     f'- Registros no acervo após deduplicação: {len(artigos)}.',
                     f'- Trabalhos com triagem concluída: {sum(a.get("triagem_agente", {}).get("revisao") == p.revisao for a in artigos.values())}.',
                     f'- Trabalhos selecionados para aprofundamento: até {p.cfg.get("artigos_aprofundados", "não informado")}.',
                     f'- Trabalhos com pré-leitura concluída: {sum(a.get("pre_leitura_agente", {}).get("revisao") == p.revisao for a in artigos.values())}.',
                     f'- Leituras aprofundadas concluídas: {sum(a.get("leitura_agente", {}).get("revisao") == p.revisao and a.get("leitura_agente", {}).get("concluida") for a in artigos.values())}.',
                     f'- Propostas geradas: {sum(m.get("revisao") == p.revisao for m, _ in propostas)}.',
                     '## Registros das buscas']
    for h in p.estado['historico']:
        fontes = ', '.join(h.get('fontes', ['OpenAlex']))
        resultados = [ids[u] if u in ids else u for u in h.get('resultados', [])]
        metodologia.append(f"- {h['quando']} — fontes: {fontes}; página: {h.get('pagina', 1)}; consulta: **{h['consulta']}**; origem: {h['origem']}; {h['status']}. " + (', '.join(resultados) or h.get('erro', 'Nenhum resultado.')))
    metodologia += ['## Limitações',
                    'A disponibilidade de texto completo depende de acesso aberto. A análise pode ser baseada apenas no resumo. PDFs sem texto extraível, figuras e tabelas podem exigir conferência humana. As propostas são hipóteses exploratórias: não comprovam novidade, ausência de trabalhos ou viabilidade.',
                    '## Pendências']
    erros = [t['erro'] for t in p.estado['tarefas'].values() if t.get('erro')]
    erros += [f'PDF {n}: {e}' for n, e in p.estado.get('pendencias_pdf', {}).items()]
    metodologia += list(dict.fromkeys(erros))[-20:] or ['Nenhuma pendência técnica registrada.']
    memoria_ia = [
        '# Anotações da IA',
        f'Atualizado: {agora()}',
        'Este arquivo é memória operacional do agente. Ele registra rastreabilidade, decisões técnicas e propostas completas para continuidade entre execuções/modelos.',
        '',
        BLOCO_IA_INICIO,
        *linhas,
        '',
        *metodologia,
        BLOCO_IA_FIM,
    ]
    gravar(root / 'dados/anotacoes-ia.md', '\n\n'.join(memoria_ia).rstrip() + '\n')

    for nome, a in artigos.items():
        path = root / 'obsidian/referencias/fichamentos' / f'{nome}.md'
        if not deve_ter_nota_markdown(a, p.revisao, fontes_relevantes):
            if path.exists():
                path.unlink()
            continue
        if path.exists():
            original = path.read_text(encoding='utf-8')
        else:
            original = "# " + nome + "\n\n" + str(a.get('titulo', nome)) + "\n"
        leitura = a.get('leitura_agente', {})
        sintese = a.get('sintese_artigo', {})
        triagem = a.get('triagem_agente', {})
        pre = a.get('pre_leitura_agente', {})
        if p.ignorado(a):
            status_atual = 'irrelevante'
        elif sintese.get('revisao') == p.revisao:
            status_atual = 'analisado_com_sintese'
        elif leitura.get('revisao') == p.revisao and leitura.get('concluida'):
            status_atual = 'leitura_concluida'
        elif leitura.get('revisao') == p.revisao and leitura.get('feitos'):
            status_atual = 'em_leitura'
        elif pre.get('revisao') == p.revisao:
            status_atual = 'preleitura_' + pre.get('decisao', 'sem_decisao')
        elif triagem.get('revisao') == p.revisao:
            status_atual = 'triado_' + triagem.get('classificacao', 'sem_classificacao')
        else:
            status_atual = a.get('status', 'triagem_pendente')
        tags = p.b.criar_tags(a.get('consulta', ''), a)
        original = garantir_frontmatter_e_secao_tags(original, a, tags)
        original = re.sub(r'(?m)^status:.*$', f'status: {status_atual}', original, count=1)
        triagem_bloco = (
            '## Triagem\n\n'
            f"- **Classificação:** {triagem.get('classificacao', 'pendente')}.\n"
            f"- **Relevância:** {triagem.get('justificativa', 'ainda não avaliada')}.\n"
            f"- **Motivo da decisão:** {triagem.get('justificativa', 'ainda não avaliado')}.\n"
            "- **Decisão humana:** ainda não registrada.\n"
            f"- **Pré-leitura:** {pre.get('decisao', 'pendente')} — {pre.get('justificativa', 'ainda não avaliada')}.\n"
            f"- **PDF/texto lido:** {'sim' if leitura.get('feitos') else 'não'}.\n"
            f"- **Status automático:** {status_atual}."
        )
        original = re.sub(r'(?ms)^## Triagem\n\n.*?(?=\n## |\Z)', triagem_bloco + '\n', original, count=1)
        analise_bloco = (
            '## Análise\n\n'
            'A análise do trabalho fica no bloco "Leitura do trabalho" abaixo. '
            'Conexões com outros trabalhos, lacunas e propostas ficam nas anotações do pesquisador, não neste fichamento.'
        )
        original = re.sub(r'(?ms)^## An[áa]lise\n\n.*?(?=\n## |\Z)', analise_bloco + '\n', original, count=1)
        gerado = [INICIO, '## Leitura do trabalho',
                  f"Fonte: {a.get('url') or a.get('fonte', 'PDF local')}",
                  'Esta nota resume exclusivamente o trabalho e suas evidências. '
                  'Conexões com a pesquisa ficam em `ANOTACOES.md`.']
        perfil = a.get('perfil_revisao', {})
        if perfil.get('revisao') == p.revisao or sintese.get('revisao') == p.revisao:
            gerado += ['### Resumo do trabalho']
            if sintese.get('resumo'):
                gerado += ['**Síntese da leitura**', sintese['resumo']]
            campos_perfil = {
                'problema': 'Problema', 'solucao': 'Solução ou abordagem',
                'avaliacao': 'Avaliação', 'limites': 'Limitações observadas',
            }
            for campo, titulo in campos_perfil.items():
                valor = perfil.get(campo)
                if valor:
                    gerado += [f'**{titulo}**', str(valor)]
        if a.get('pdf_local'):
            alvo = a['pdf_local'].replace(chr(92), '/')
            if alvo.startswith('obsidian/referencias/'):
                alvo = alvo[len('obsidian/referencias/'):]
            if alvo.startswith('obsidian/'):
                alvo = alvo[len('obsidian/'):]
            gerado += [f"[PDF local](../{quote(alvo)})"]
        elif a.get('texto_local'):
            alvo = a['texto_local'].replace(chr(92), '/')
            if alvo.startswith('obsidian/referencias/'):
                alvo = alvo[len('obsidian/referencias/'):]
            if alvo.startswith('obsidian/'):
                alvo = alvo[len('obsidian/'):]
            gerado += [f"[Texto local](../{quote(alvo)})"]
        leitura = a.get('leitura_agente', {})
        if leitura.get('assinatura'):
            gerado += ['### Fichamento', f"Base: {leitura.get('tipo')}; {leitura.get('feitos')}/{leitura.get('total')} trechos. "
                       f"Páginas sem texto extraível: {leitura.get('paginas_sem_texto', [])}. Figuras e tabelas podem exigir conferência humana."]
            for ficha_path in sorted((root / 'dados/leituras' / leitura['assinatura']).glob('*.json'), key=lambda p: int(p.stem)):
                f = ler(ficha_path, {})
                if not f:
                    gerado += [f"#### Ficha {ficha_path.stem} indisponível", "Arquivo de ficha vazio ou inválido; o agente irá refazer este trecho quando a leitura for retomada."]
                    continue
                gerado += [f"#### Página {f.get('pagina') or 'resumo'} — ficha {f['id']}", f['resumo']]
                gerado += [f"- {e['afirmacao']} — citação conferida: {e['citacao']}" for e in f.get('evidencias', [])]
                gerado += ['Interpretação: ' + str(f.get('interpretacao', '')), 'Dúvidas: ' + str(f.get('duvidas', ''))]
        gerado += [FIM]
        bloco = '\n\n'.join(gerado)
        if INICIO in original and FIM in original:
            conteudo_final = re.sub(re.escape(INICIO) + '.*?' + re.escape(FIM), lambda _: bloco, original, count=1, flags=re.S)
        else:
            conteudo_final = original.rstrip() + '\n\n' + bloco + '\n'
        if conteudo_final != original:
            gravar(path, conteudo_final)
    limpar_arquivos_legados_obsidian(root)
