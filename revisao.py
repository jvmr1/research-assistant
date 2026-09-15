"""Leitura acadêmica, síntese e geração de propostas.

Responsabilidades deste arquivo:
- ler um trabalho aprovado por vez;
- reaproveitar fichas já produzidas quando possível;
- validar citações literais usadas pela IA;
- consolidar resumo, limitações e possibilidades de cada artigo;
- comparar trabalhos lidos para gerar hipóteses de lacunas e propostas;
- detalhar ideias com experimento, métricas, recursos e riscos.

A coleta, downloads e estado geral ficam em motor.py. A escrita dos arquivos
Markdown para o usuário fica em apresentacao.py.
"""
import json
import re
import time
import unicodedata

COLUNAS = ('problema', 'solucao', 'avaliacao', 'limites', 'possibilidades')


def texto(valor):
    if valor is None:
        return ''
    if isinstance(valor, str):
        return valor.strip()
    if isinstance(valor, list):
        return '; '.join(texto(v) for v in valor)
    if isinstance(valor, dict):
        return '; '.join(f'{k}: {texto(v)}' for k, v in valor.items())
    return str(valor)


def normalizar(s):
    s = unicodedata.normalize('NFKC', s).replace('\u00ad', '')
    s = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', s)
    return ' '.join(s.split())


def perfil_seguro(obj, material):
    """O mapa factual usa extratos; a criatividade fica em possibilidades."""
    obj = obj.get('perfil', obj) if isinstance(obj, dict) else {}
    campos = {''.join(c for c in unicodedata.normalize('NFD', k) if not unicodedata.combining(c)): v for k, v in obj.items()}
    base = normalizar(material)
    perfil = {}
    for c in COLUNAS:
        v = texto(campos.get(c))
        if c == 'possibilidades':
            perfil[c] = v[:600] or 'Ainda a explorar.'
        else:
            perfil[c] = v if v and len(v) <= 600 and normalizar(v) in base else 'Não identificado nas fichas/trechos disponíveis.'
    return perfil


def ficha_segura(obj, original):
    """Uma citação incorreta é descartada, sem jogar fora todo o fichamento."""
    resumo = texto(obj.get('resumo'))
    if not resumo:
        raise ValueError('Ficha sem conteúdo; ver resposta em dados/diagnosticos.')
    validas, avisos = [], []
    for e in obj.get('evidencias', []) if isinstance(obj.get('evidencias', []), list) else []:
        if not isinstance(e, dict):
            continue
        citacao, afirmacao = texto(e.get('citacao')), texto(e.get('afirmacao'))
        if citacao and afirmacao and len(citacao) <= 500 and normalizar(citacao) in normalizar(original):
            validas.append({'citacao': citacao, 'afirmacao': afirmacao})
        else:
            avisos.append('Citação não conferida descartada; a interpretação do trecho continua provisória.')
    return dict(obj, resumo=resumo, evidencias=validas, avisos=avisos,
                interpretacao=texto(obj.get('interpretacao')), duvidas=texto(obj.get('duvidas')))


def chamar(p, etapa, tarefa, dados, esquema=None):
    from motor import gerar_com_fallback, lento, json_gravar, chave, agora
    pasta = p.root / 'dados/diagnosticos'
    ident = chave([etapa, dados, time.time_ns()])
    registro = {'etapa': etapa, 'inicio': agora(), 'revisao': p.revisao, 'tarefa': tarefa, 'entrada': dados}
    try:
        obj = lento(gerar_com_fallback, p.modelos_ia(), p.instrucoes, tarefa, dados, esquema=esquema,
                    descricao=f"IA/{etapa}", intervalo=10)
        meta = p.registrar_meta_ia(obj)
        registro.update(resposta=obj, ia=meta, fim=agora())
        return obj
    except Exception as e:
        registro.update(erro=str(e), resposta_bruta=getattr(e, 'resposta_bruta', None), fim=agora())
        raise
    finally:
        json_gravar(pasta / f'{ident}.json', registro)


def consolidar_sintese_artigo(p, a, fichas, assinatura):
    """Consolida fichas em blocos para evitar estouro de contexto em artigos longos."""
    from motor import chave, ler_json, json_gravar
    itens = [{'pagina': f.get('pagina'), 'resumo': texto(f.get('resumo'))[:900],
              'interpretacao': texto(f.get('interpretacao'))[:700], 'duvidas': texto(f.get('duvidas'))[:400]}
             for _, f in sorted(fichas.items())]
    if not itens:
        raise ValueError('N?o h? fichas para consolidar.')
    if len(itens) <= 6:
        obj = chamar(p, 'sintese-artigo',
            'Consolide a leitura deste trabalho. JSON: resumo (at? 250 palavras), '
            'lacunas_possiveis (lista de strings) e propostas_possiveis (lista de strings). '
            'As duas listas s?o brainstorm derivado do trabalho, n?o alega??es comprovadas dos autores. '
            'N?o invente m?todos, resultados ou limita??es ausentes. Identifique quando a fonte ? HTML/PDF parcial.',
            {'titulo': a['titulo'], 'tipo_leitura': a['leitura_agente']['tipo'], 'fichas': itens})
        resumo = texto(obj.get('resumo'))
        if not resumo:
            raise ValueError('S?ntese final do trabalho vazia.')
        return {'revisao': p.revisao, 'assinatura': assinatura,
                'resumo': resumo[:3000],
                'lacunas_possiveis': [texto(x)[:800] for x in obj.get('lacunas_possiveis', []) if texto(x)][:8],
                'propostas_possiveis': [texto(x)[:800] for x in obj.get('propostas_possiveis', []) if texto(x)][:8]}
    parciais = []
    for inicio in range(0, len(itens), 6):
        bloco = itens[inicio:inicio + 6]
        cid = chave(['sintese-parcial', p.revisao, assinatura, inicio, bloco])
        cache = p.root / 'dados/sinteses' / f'{cid}.json'
        if cache.exists():
            parcial = ler_json(cache, {})
        else:
            parcial = chamar(p, 'sintese-parcial',
                'Consolide este bloco de fichas de um artigo. JSON: resumo (at? 140 palavras), '
                'lacunas_possiveis (lista curta) e propostas_possiveis (lista curta). N?o invente fatos; '
                'use apenas as fichas recebidas. As lacunas/propostas s?o brainstorm preliminar.',
                {'titulo': a['titulo'], 'tipo_leitura': a['leitura_agente']['tipo'], 'fichas': bloco})
            json_gravar(cache, parcial)
        parciais.append({
            'resumo': texto(parcial.get('resumo'))[:1200],
            'lacunas_possiveis': [texto(x)[:500] for x in parcial.get('lacunas_possiveis', []) if texto(x)][:5],
            'propostas_possiveis': [texto(x)[:500] for x in parcial.get('propostas_possiveis', []) if texto(x)][:5],
        })
    obj = chamar(p, 'sintese-artigo',
        'Consolide as s?nteses parciais deste trabalho. JSON: resumo (at? 250 palavras), '
        'lacunas_possiveis (lista de strings) e propostas_possiveis (lista de strings). '
        'As duas listas s?o brainstorm derivado do trabalho, n?o alega??es comprovadas dos autores. '
        'N?o invente m?todos, resultados ou limita??es ausentes. Identifique quando a fonte ? HTML/PDF parcial.',
        {'titulo': a['titulo'], 'tipo_leitura': a['leitura_agente']['tipo'], 'sinteses_parciais': parciais})
    resumo = texto(obj.get('resumo'))
    if not resumo:
        raise ValueError('S?ntese final do trabalho vazia.')
    return {'revisao': p.revisao, 'assinatura': assinatura,
            'resumo': resumo[:3000],
            'lacunas_possiveis': [texto(x)[:800] for x in obj.get('lacunas_possiveis', []) if texto(x)][:8],
            'propostas_possiveis': [texto(x)[:800] for x in obj.get('propostas_possiveis', []) if texto(x)][:8]}


def ler(p):
    from motor import chave, ler_json, json_gravar, log
    feitos = 0
    # Um trabalho é levado até o fim antes de escolher o seguinte.
    for a in [x for x in p.candidatos() if p.aprovado_preleitura(x) and x.get('sintese_artigo', {}).get('revisao') != p.revisao][:1]:
        try:
            trechos = p.trechos(a)
        except Exception as e:
            p.estado.setdefault('pendencias_pdf', {})[a['nome_local']] = str(e)[:300]
            continue
        if not trechos:
            a['leitura_agente'] = {'revisao': p.revisao, 'assinatura': '', 'feitos': 0,
                                  'total': 0, 'concluida': True, 'tipo': 'indisponivel',
                                  'paginas_sem_texto': []}
            a['sintese_artigo'] = {'revisao': p.revisao,
                                   'resumo': 'Texto integral e resumo não estavam disponíveis para leitura automática.',
                                   'lacunas_possiveis': [], 'propostas_possiveis': []}
            p.salvar()
            p.painel()
            return
        assinatura = chave(['revisao-exploratoria-v1', p.revisao, a['id_openalex'], trechos])
        pasta = p.root / 'dados/leituras' / assinatura
        legado = a.get('leitura_agente', {})
        assinaturas_compativeis = {
            chave([legado.get('revisao'), a['id_openalex'], trechos]),
            chave(['revisao-exploratoria-v1', legado.get('revisao'), a['id_openalex'], trechos]),
        }
        if legado.get('assinatura') in assinaturas_compativeis and legado['assinatura'] != assinatura:
            antiga = p.root / 'dados/leituras' / legado['assinatura']
            for i, t in enumerate(trechos):
                if (antiga / f'{i}.json').exists() and not (pasta / f'{i}.json').exists():
                    f = ler_json(antiga / f'{i}.json', {})
                    f['reaproveitada_de'] = legado['assinatura']
                    json_gravar(pasta / f'{i}.json', f)
        fichas = {i: ler_json(pasta / f'{i}.json', {}) for i, t in enumerate(trechos)
                  if t['texto'].strip() and (pasta / f'{i}.json').exists()}
        total = sum(bool(t['texto'].strip()) for t in trechos)
        if fichas and a.get('perfil_revisao', {}).get('assinatura') != assinatura:
            perfis = [f.get('perfil_acumulado') for f in fichas.values() if f.get('perfil_acumulado', {}).get('assinatura') == assinatura]
            if perfis:
                a['perfil_revisao'] = perfis[-1]
            else:
                # Recupera todas as fichas existentes em lotes, sem reler o PDF com a IA.
                memoria = {}
                antigas_fichas = list(fichas.values())
                for inicio in range(0, len(antigas_fichas), 6):
                    lote = antigas_fichas[inicio:inicio + 6]
                    dados = {'perfil_anterior': memoria, 'fichas': [{'resumo': f['resumo'], 'pagina': f.get('pagina')} for f in lote]}
                    pid = chave(['recuperar-perfil', assinatura, inicio, dados])
                    cache = p.root / 'dados/perfis' / f'{pid}.json'
                    if cache.exists():
                        memoria = ler_json(cache, {})
                        continue
                    def recuperar():
                        r = chamar(p, 'reaproveitar-leituras',
                            'Reorganize o entendimento já extraído destes trechos. JSON com problema, solucao, avaliacao, '
                            'limites, possibilidades. Nos primeiros QUATRO campos copie uma frase literal curta das fichas '
                            'ou do perfil anterior (até 500 caracteres); quando ausente, escreva Não informado. '
                            'Não transforme uma descrição de aplicação em avaliação experimental, nem foco do estudo em '
                            'limitação declarada. Em possibilidades você pode sugerir livremente uma extensão pequena. '
                            'Acumule o perfil anterior e não invente fatos.', dados)
                        r = perfil_seguro(r, '\n'.join(texto(v) for v in memoria.values()) + '\n' + '\n'.join(f['resumo'] for f in lote))
                        json_gravar(cache, r)
                        return r
                    r = p.tarefa(pid, recuperar)
                    if r is None:
                        break
                    memoria = r
                else:
                    a['perfil_revisao'] = dict(memoria, assinatura=assinatura, revisao=p.revisao)
                    p.salvar()
        for i, trecho in enumerate(trechos):
            if i in fichas or not trecho['texto'].strip():
                continue
            ident = chave(['ler', assinatura, i])
            pendente = p.estado['tarefas'].get(ident, {})
            if pendente.get('feito') or pendente.get('tentar_em', 0) > time.time():
                continue  # Um trecho problemático não impede a leitura das páginas seguintes.
            def acao():
                p.mensagem = f"Lendo {a['nome_local']}: {len(fichas)}/{total} trechos."
                log(p.mensagem)
                p.painel()
                anterior = a.get('perfil_revisao', {})
                if anterior.get('revisao') != p.revisao or anterior.get('assinatura') != assinatura:
                    anterior = {}
                obj = chamar(p, 'leitura',
                    'Leia este trecho e atualize o entendimento deste trabalho, usando o perfil anterior como memória. '
                    'JSON: resumo (até 100 palavras sobre o trecho), perfil (objeto com problema, solucao, avaliacao, '
                    'limites, possibilidades: nos primeiros quatro campos copie uma frase literal curta do trecho ou '
                    'do perfil anterior, até 500 caracteres; se ausente diga Não informado. Em possibilidades sugira extensões), '
                    'evidencias (até 2 objetos: afirmacao e citacao literal curta copiada do trecho no idioma original), '
                    'interpretacao e duvidas (strings). Cite somente o trecho novo. Não invente avaliações ausentes. '
                    'Possibilidades são ideias de extensão, não afirmações dos autores. Se não houver informação, diga não informado.',
                    {'titulo': a['titulo'], 'perfil_anterior': {c: anterior.get(c, '') for c in COLUNAS}, **trecho})
                obj = ficha_segura(obj, trecho['texto'])
                obj.update(id=ident, artigo=a['nome_local'], pagina=trecho['pagina'], tipo=trecho['tipo'])
                perfil = obj.get('perfil') if isinstance(obj.get('perfil'), dict) else {}
                acumulado = perfil_seguro(perfil, trecho['texto'] + '\n' + '\n'.join(texto(anterior.get(c)) for c in COLUNAS))
                for c in COLUNAS:
                    if acumulado[c].startswith('Não identificado') and anterior.get(c):
                        acumulado[c] = anterior[c]
                if not perfil:
                    acumulado['possibilidades'] = obj['resumo']
                acumulado = {c: (v[:600] + ' [síntese abreviada]' if len(v) > 600 else v) for c, v in acumulado.items()}
                obj['perfil_acumulado'] = dict(acumulado, revisao=p.revisao, assinatura=assinatura)
                json_gravar(pasta / f'{i}.json', obj)
                a['perfil_revisao'] = obj['perfil_acumulado']
                log('Entendimento provisório: ' + obj['resumo'][:250])
                if obj['avisos']:
                    log('Citação divergente descartada; leitura mantida como interpretação provisória.')
                return obj
            obj = p.tarefa(ident, acao)
            if obj:
                fichas[i] = obj
                feitos += 1
                a['ultima_leitura'] = time.time()
                a['leitura_agente'] = {'revisao': p.revisao, 'assinatura': assinatura,
                                      'feitos': len(fichas), 'total': total,
                                      'concluida': len(fichas) == total,
                                      'tipo': 'pdf' if a.get('pdf_local') else 'html' if a.get('texto_local') else 'resumo',
                                      'paginas_sem_texto': [t['pagina'] for t in trechos if not t['texto'].strip()]}
                p.salvar()
                p.painel()
        # Reconstrói o perfil se houve interrupção entre a ficha e o cadastro.
        if fichas and a.get('perfil_revisao', {}).get('assinatura') != assinatura:
            perfis = [f.get('perfil_acumulado') for f in fichas.values() if f.get('perfil_acumulado')]
            if perfis:
                a['perfil_revisao'] = perfis[-1]
        a['leitura_agente'] = {'revisao': p.revisao, 'assinatura': assinatura, 'feitos': len(fichas),
                              'total': total, 'concluida': len(fichas) == total,
                              'tipo': 'pdf' if a.get('pdf_local') else 'html' if a.get('texto_local') else 'resumo',
                              'paginas_sem_texto': [t['pagina'] for t in trechos if not t['texto'].strip()]}
        p.salvar()
        if a['leitura_agente']['concluida'] and a.get('sintese_artigo', {}).get('revisao') != p.revisao:
            ident = chave(['sintese-artigo', p.revisao, assinatura])
            def sintetizar():
                p.mensagem = f"Consolidando o resumo integral de {a['nome_local']}."
                log(p.mensagem)
                p.painel()
                a['sintese_artigo'] = consolidar_sintese_artigo(p, a, fichas, assinatura)
                p.salvar()
                return True
            p.tarefa(ident, sintetizar)
        p.painel()
        return


def matriz(p):
    linhas = []
    for a in p.artigos:
        if p.ignorado(a):
            continue
        perfil = a.get('perfil_revisao', {})
        leitura = a.get('leitura_agente', {})
        if perfil.get('revisao') != p.revisao or leitura.get('revisao') != p.revisao or not leitura.get('feitos'):
            continue
        linhas.append({'id': a['nome_local'], 'titulo': a['titulo'],
                       'escopo': {k: leitura[k] for k in ('tipo', 'feitos', 'total', 'concluida')},
                       **{c: texto(perfil.get(c, 'Não informado.'))[:450] for c in COLUNAS}})
    return linhas


def propor_por_artigo(p, linhas):
    from motor import chave, json_gravar, agora, log
    existentes = {m.get('id') for m in p.estado.get('propostas', [])}
    por_id = {l['id']: l for l in linhas}
    criadas = 0
    for a in p.artigos:
        nome = a.get('nome_local')
        if nome not in por_id:
            continue
        leitura = a.get('leitura_agente', {})
        if leitura.get('revisao') != p.revisao:
            continue
        feitos = leitura.get('feitos') or 0
        total = leitura.get('total') or 0
        minimo = min(4, max(1, total // 2)) if total else 1
        if not leitura.get('concluida') and feitos < minimo:
            continue
        sintese = a.get('sintese_artigo', {})
        perfil = a.get('perfil_revisao', {})
        ideias = []
        for item in sintese.get('propostas_possiveis', []) if sintese.get('revisao') == p.revisao else []:
            if texto(item):
                ideias.append(('proposta', texto(item)))
        for item in sintese.get('lacunas_possiveis', []) if sintese.get('revisao') == p.revisao else []:
            if texto(item):
                ideias.append(('lacuna', texto(item)))
        possibilidade = texto(perfil.get('possibilidades'))
        if possibilidade and 'Ainda a explorar' not in possibilidade and not ideias:
            ideias.append(('possibilidade', possibilidade))
        limite = texto(perfil.get('limites'))
        if limite and not limite.startswith('Não identificado') and not ideias:
            ideias.append(('limite', 'Investigar uma contribuição que trate: ' + limite))
        for indice, (tipo, ideia) in enumerate(ideias[:3]):
            pid = chave(['proposta-artigo-v1', p.revisao, nome, indice, ideia])
            if pid in existentes:
                continue
            titulo_base = ideia.split('.')[0].strip()[:90] or f'Ideia derivada de {nome}'
            titulo = f'{nome}: {titulo_base}'
            lacunas = sintese.get('lacunas_possiveis', []) if sintese.get('revisao') == p.revisao else []
            problema = texto(lacunas[0]) if lacunas else ''
            if not problema:
                problema = limite or ideia
            proposta = {
                'id': pid, 'revisao': p.revisao, 'gerado_em': agora(), 'modelo': 'síntese individual já extraída',
                'titulo': titulo, 'fontes': [nome], 'problema': problema,
                'hipotese_lacuna': problema, 'meu_trabalho': ideia,
                'interpretacao': 'Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.',
                'alteracao_sobre_trabalhos_proximos': ideia, 'modo': 'artigo',
                'buscas': [q for q in [
                    f'{a.get("titulo", "")} limitations future work',
                    f'{a.get("titulo", "")} smart cities IoT blockchain access control',
                ] if q.strip()][:2],
                'riscos': 'Ideia preliminar baseada em um único trabalho; pode ser enfraquecida ou já estar resolvida por trabalhos posteriores.',
                'duvidas_orientador': 'Vale aprofundar esta direção ou ela está ampla demais para uma dissertação?'
            }
            json_gravar(p.root / 'dados/propostas' / f'{pid}.json', proposta)
            json_gravar(p.root / 'dados/propostas' / f'{pid}-fontes.json',
                        {'fontes': [dict(por_id[nome], assinatura=leitura.get('assinatura'))],
                         'metodo': 'fichamento individual'})
            p.estado['propostas'].append({k: proposta[k] for k in ('id', 'revisao', 'titulo', 'fontes')})
            p.registrar_consultas(proposta['buscas'], 'proposta ' + pid)
            existentes.add(pid)
            criadas += 1
            log('Ideia preliminar registrada: ' + proposta['titulo'])
    if criadas:
        p.salvar()
    return criadas


def propor(p):
    from motor import chave, json_gravar, agora, log, ler_json
    linhas = matriz(p)
    if len(linhas) < 2:
        propor_por_artigo(p, linhas)
        return
    propostas_antes = len([m for m in p.estado.get('propostas', []) if m.get('revisao') == p.revisao])
    # Usa o conjunto de perfis, sem escolher pares arbitrários ou quatro páginas.
    # O limite explícito evita estourar o contexto de um modelo local.
    grupos, grupo, tamanho = [], [], 0
    for linha in linhas:
        custo = len(json.dumps(linha, ensure_ascii=False))
        if grupo and tamanho + custo > 10000:
            grupos.append(grupo)
            grupo, tamanho = [], 0
        grupo.append(linha)
        tamanho += custo
    if grupo:
        grupos.append(grupo)
    for indice, grupo in enumerate(grupos):
        if len(grupo) < 2:
            grupo = linhas[-2:]
        evidencias_lidas = sum(l['escopo']['feitos'] for l in grupo)
        anterior = p.estado.get('mapas_revisao', {}).get(str(indice), {})
        if anterior.get('revisao') == p.revisao and anterior.get('assinatura') == chave(grupo):
            continue
        # Reconsidera após novas leituras, não a cada passagem sem progresso.
        if anterior.get('revisao') == p.revisao and evidencias_lidas - anterior.get('trechos', 0) < 3 and not all(l['escopo']['concluida'] for l in grupo):
            continue
        ident = chave(['mapa', p.revisao, grupo])
        def acao():
            ids = [l['id'] for l in grupo]
            esquema = {'type': 'object', 'properties': {
                'panorama': {'type': 'string'},
                'ideias': {'type': 'array', 'maxItems': 3, 'items': {'type': 'object', 'properties': {
                    'titulo': {'type': 'string'}, 'oportunidade': {'type': 'string'}, 'contribuicao': {'type': 'string'},
                    'fontes': {'type': 'array', 'items': {'type': 'string', 'enum': ids}, 'minItems': 2}},
                    'required': ['titulo', 'oportunidade', 'contribuicao', 'fontes']}},
                'buscas': {'type': 'array', 'maxItems': 2, 'items': {'type': 'string'}}},
            'required': ['panorama', 'ideias']}
            p.mensagem = f'Construindo o estado da arte e ideias a partir de {len(grupo)} trabalhos.'
            log(p.mensagem)
            p.painel()
            obj = chamar(p, 'panorama-brainstorm',
                'Construa um panorama do conjunto: abordagens existentes, onde concordam, diferenças de avaliação '
                'e até onde os trabalhos chegam. Depois sugira até 3 ideias de mestrado que cruzem pelo menos dois trabalhos. '
                'É BRAINSTORM: aceite extensões pequenas, adaptações e comparações; não exija novidade comprovada nem '
                'projeto fechado. Não descarte uma ideia só por haver incertezas. Aponte o que o pesquisador poderia '
                'alterar sobre os trabalhos próximos. Cada ideia deve citar no campo fontes pelo menos dois IDs, explicando a lacuna pela comparação entre eles; se só houver ideia de artigo único, deixe ideias vazio para o fallback individual cuidar disso. Respeite o escopo parcial/resumo de cada leitura. '
                'JSON no esquema fornecido. Panorama até 200 palavras; cada ideia até 120 palavras. '
                'Fontes devem ser IDs fornecidos. Buscas são termos para aprofundar ou esclarecer as ideias.',
                {'trabalhos': grupo}, esquema)
            panorama = texto(obj.get('panorama'))
            if not panorama:
                raise ValueError('Panorama vazio; resposta salva nos diagnósticos.')
            p.estado.setdefault('mapas_revisao', {})[str(indice)] = {
                'revisao': p.revisao, 'assinatura': chave(grupo), 'trechos': evidencias_lidas,
                'panorama': panorama, 'fontes': ids, 'quando': agora()}
            for numero, ideia in enumerate(obj.get('ideias', []) if isinstance(obj.get('ideias'), list) else []):
                if not isinstance(ideia, dict):
                    continue
                fontes = [f for f in ideia.get('fontes', []) if isinstance(f, str) and f in ids]
                if len(fontes) < 2 or not texto(ideia.get('titulo')) or not texto(ideia.get('contribuicao')):
                    continue
                pid = chave([ident, numero])
                proposta = {'id': pid, 'revisao': p.revisao, 'gerado_em': agora(), 'modelo': ', '.join(p.modelos_ia()),
                            'titulo': texto(ideia['titulo']), 'fontes': list(dict.fromkeys(fontes)),
                            'problema': texto(ideia.get('oportunidade')), 'hipotese_lacuna': texto(ideia.get('oportunidade')),
                            'meu_trabalho': texto(ideia['contribuicao']), 'interpretacao': panorama,
                            'alteracao_sobre_trabalhos_proximos': texto(ideia['contribuicao']),
                            'modo': 'brainstorm', 'buscas': [q for q in obj.get('buscas', []) if isinstance(q, str)][:2]}
                json_gravar(p.root / 'dados/propostas' / f'{pid}.json', proposta)
                fontes_snapshot = []
                for l in grupo:
                    if l['id'] in fontes:
                        a = next(a for a in p.artigos if a['nome_local'] == l['id'])
                        fontes_snapshot.append(dict(l, assinatura=a['leitura_agente']['assinatura']))
                json_gravar(p.root / 'dados/propostas' / f'{pid}-fontes.json', {'fontes': fontes_snapshot, 'metodo': 'perfis acumulados'})
                p.estado['propostas'].append({k: proposta[k] for k in ('id', 'revisao', 'titulo', 'fontes')})
                p.registrar_consultas(proposta['buscas'], 'proposta ' + pid)
                log('Ideia registrada: ' + proposta['titulo'])
            p.salvar()
            return True
        if p.tarefa(ident, acao):
            propostas_agora = len([m for m in p.estado.get('propostas', []) if m.get('revisao') == p.revisao])
            if propostas_agora == propostas_antes:
                propor_por_artigo(p, linhas)
            return
    propostas_agora = len([m for m in p.estado.get('propostas', []) if m.get('revisao') == p.revisao])
    if propostas_antes == 0 and propostas_agora == propostas_antes:
        propor_por_artigo(p, linhas)


def detalhar(p):
    from motor import ler_json, chave, json_gravar, log
    for meta in p.estado['propostas']:
        if meta['revisao'] != p.revisao:
            continue
        path = p.root / 'dados/propostas' / f"{meta['id']}.json"
        obj = ler_json(path, {})
        if obj.get('modo') not in {'brainstorm', 'artigo'} or obj.get('detalhada'):
            continue
        ident = chave(['detalhar', meta['id']])
        def acao():
            log('Desenvolvendo a ideia: ' + obj['titulo'])
            fontes = ler_json(path.with_name(meta['id'] + '-fontes.json'), {})
            r = chamar(p, 'desenvolver-ideia',
                'Desenvolva esta sugestão de mestrado sem julgá-la como banca. JSON: experimento (o que implementar e '
                'com qual trabalho comparar), recursos (dados/ferramentas necessários, sem inventar disponibilidade), '
                'metricas e duvidas_orientador (strings, até 80 palavras cada). Se faltar informação, proponha opções. '
                'A ideia já está publicada; esta etapa só acrescenta um caminho possível.',
                {'ideia': obj['meu_trabalho'], 'fontes': fontes})
            for campo in ('experimento', 'recursos', 'metricas', 'duvidas_orientador'):
                if texto(r.get(campo)):
                    obj[campo] = texto(r[campo])
            obj['detalhada'] = any(texto(r.get(c)) for c in ('experimento', 'recursos', 'metricas'))
            if not obj['detalhada']:
                raise ValueError('Detalhamento vazio. A sugestão inicial permanece no relatório.')
            json_gravar(path, obj)
            return True
        if p.tarefa(ident, acao):
            return


def ciclo(p):
    p.configurar()
    p.mensagem = 'Preparando o próximo lote de trabalhos.'
    p.importar_pdfs()
    p.painel()
    lote = p.preparar_lote()
    if not lote:
        p.mensagem = 'Nenhum trabalho novo disponível agora; aguardando a próxima consulta.'
        p.salvar()
        p.painel()
        return
    if p.modelo_disponivel():
        p.triagem()
        artigos = [a for a in p.artigos if a['nome_local'] in lote['ids']]
        triagem_pronta = all(p.ignorado(a) or a.get('triagem_agente', {}).get('revisao') == p.revisao
                            for a in artigos)
        if not triagem_pronta:
            prontos = sum(p.ignorado(a) or a.get('triagem_agente', {}).get('revisao') == p.revisao
                         for a in artigos)
            p.mensagem = f"Lote {lote['numero']}: triagem {prontos}/{len(artigos)}."
            p.salvar()
            p.painel()
            return
        p.baixar()
        p.pre_leitura()
        pre_pronta = all(p.ignorado(a) or a.get('sintese_artigo', {}).get('revisao') == p.revisao or a.get('pre_leitura_agente', {}).get('revisao') == p.revisao
                         for a in artigos if a.get('triagem_agente', {}).get('classificacao') in {'priorizar', 'revisar', 'sem_resumo'})
        if not pre_pronta:
            prontos = sum(p.ignorado(a) or a.get('sintese_artigo', {}).get('revisao') == p.revisao or a.get('pre_leitura_agente', {}).get('revisao') == p.revisao
                         for a in artigos if a.get('triagem_agente', {}).get('classificacao') in {'priorizar', 'revisar', 'sem_resumo'})
            total_pre = sum(1 for a in artigos if a.get('triagem_agente', {}).get('classificacao') in {'priorizar', 'revisar', 'sem_resumo'})
            p.mensagem = f"Lote {lote['numero']}: pré-leitura {prontos}/{total_pre}."
            p.salvar()
            p.painel()
            return
        ler(p)
        propor(p)
        detalhar(p)
        interessantes = [a for a in artigos if not p.ignorado(a)
                          and a.get('triagem_agente', {}).get('classificacao') in {'priorizar', 'revisar', 'sem_resumo'}
                          and p.aprovado_preleitura(a)]
        concluidos = [a for a in interessantes
                      if a.get('leitura_agente', {}).get('revisao') == p.revisao
                      and a.get('leitura_agente', {}).get('concluida')
                      and a.get('sintese_artigo', {}).get('revisao') == p.revisao]
        if len(concluidos) == len(interessantes):
            p.concluir_lote()
            p.painel()
            pendentes = p.propostas_pendentes_avaliacao()
            if pendentes:
                p.estado['aguardando_avaliacao_propostas'] = {'revisao': p.revisao, 'quantidade': len(pendentes)}
                p.mensagem = f'Lote concluído com {len(pendentes)} proposta(s) pendente(s) de avaliação em vault/AVALIAR-PROPOSTAS.md. Edite o arquivo e reinicie para buscar na direção das favoritas.'
                p.salvar()
                p.painel()
                return
        erros = sum(bool(t.get('erro')) and not t.get('versao_anterior') for t in p.estado['tarefas'].values())
        p.mensagem = f"Lote {lote['numero']}: {len(concluidos)}/{len(interessantes)} trabalhos interessantes concluídos; " \
                     f"{sum(m['revisao'] == p.revisao for m in p.estado['propostas'])} sugestões; {erros} pendências técnicas."
    p.salvar()
    p.painel()

