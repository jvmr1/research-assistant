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


def ler_json_seguro(path, padrao):
    from motor import ler_json, log
    try:
        return ler_json(path, padrao)
    except json.JSONDecodeError:
        log(f"Ficha JSON inválida ignorada para retomada: {path}")
        return padrao


def ficha_json_invalida(path):
    if not path.exists():
        return False
    try:
        json.loads(path.read_text(encoding='utf-8'))
        return False
    except (OSError, json.JSONDecodeError):
        return True


def quarentenar_ficha_invalida(p, assinatura, indice, path):
    from motor import chave, log
    destino = p.root / 'dados/leituras_corrompidas' / assinatura / f'{indice}-{int(time.time())}.json'
    destino.parent.mkdir(parents=True, exist_ok=True)
    try:
        path.replace(destino)
    except OSError:
        path.unlink(missing_ok=True)
    p.estado.get('tarefas', {}).pop(chave(['ler', assinatura, indice]), None)
    log(f"Ficha inválida movida para quarentena e trecho liberado para releitura: {path}")


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
                    f = ler_json_seguro(antiga / f'{i}.json', {})
                    if not f:
                        continue
                    f['reaproveitada_de'] = legado['assinatura']
                    json_gravar(pasta / f'{i}.json', f)
        for i, t in enumerate(trechos):
            ficha_path = pasta / f'{i}.json'
            if t['texto'].strip() and ficha_json_invalida(ficha_path):
                quarentenar_ficha_invalida(p, assinatura, i, ficha_path)
        fichas = {i: ficha for i, t in enumerate(trechos)
                  if t['texto'].strip() and (pasta / f'{i}.json').exists()
                  for ficha in [ler_json_seguro(pasta / f'{i}.json', {})] if ficha}
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
            if not (pasta / f'{i}.json').exists() and p.estado['tarefas'].get(ident, {}).get('feito'):
                p.estado['tarefas'].pop(ident, None)
                p.salvar()
                log(f"Ficha ausente apesar de tarefa marcada como concluída; liberando releitura do trecho {i + 1}/{total}.")
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
            if not obj:
                tarefa = p.estado.get('tarefas', {}).get(ident, {})
                erro = tarefa.get('erro', '')
                erro_modelo = any(x in erro for x in (
                    'localhost:11434/api/generate', 'api/generate', 'Nenhum modelo respondeu',
                    'modelo local', 'Ollama', 'OPENROUTER_API_KEY', 'nao retornou um objeto JSON',
                    'não retornou um objeto JSON', 'Modelo indisponivel', 'Modelo indisponível'))
                if tarefa.get('tentar_em') and erro_modelo:
                    p.mensagem = f"Leitura pausada por indisponibilidade de modelo; retomada programada para depois."
                    p.estado['pausa_modelo_ate'] = tarefa.get('tentar_em')
                    p.salvar()
                    p.painel()
                    return
                if tarefa.get('definitivo') or ('Ficha sem conteúdo' in erro):
                    obj = {
                        'id': ident,
                        'artigo': a['nome_local'],
                        'pagina': trecho['pagina'],
                        'tipo': trecho['tipo'],
                        'resumo': 'Trecho pulado por falha técnica repetida na extração da ficha. O texto original existe, mas a IA não retornou uma ficha utilizável.',
                        'evidencias': [],
                        'interpretacao': 'Falha técnica de leitura deste trecho; seguir para os demais para não travar o trabalho.',
                        'duvidas': 'Conferir manualmente este trecho se ele for importante.',
                        'avisos': ['falha_tecnica_ficha'],
                        'perfil_acumulado': dict(a.get('perfil_revisao', {}), revisao=p.revisao, assinatura=assinatura),
                    }
                    json_gravar(pasta / f'{i}.json', obj)
                    log(f"Trecho {i + 1}/{total} pulado após falha técnica repetida; seguindo leitura de {a['nome_local']}.")
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
    from motor import ler_json
    linhas = []
    for a in p.artigos:
        if p.ignorado(a):
            continue
        perfil = a.get('perfil_revisao', {})
        leitura = a.get('leitura_agente', {})
        if perfil.get('revisao') != p.revisao or leitura.get('revisao') != p.revisao or not leitura.get('feitos'):
            continue
        fichas = []
        pasta = p.root / 'dados/leituras' / leitura.get('assinatura', '')
        for path in sorted(pasta.glob('*.json'), key=lambda x: int(x.stem) if x.stem.isdigit() else 10**9):
            ficha = ler_json_seguro(path, {})
            if ficha.get('resumo') and ficha.get('evidencias'):
                fichas.append({k: ficha.get(k) for k in ('id', 'pagina', 'resumo', 'evidencias')})
            if len(fichas) >= 4:
                break
        linhas.append({'id': a['nome_local'], 'titulo': a['titulo'],
                       'escopo': {k: leitura[k] for k in ('tipo', 'feitos', 'total', 'concluida')},
                       'fichas_amostradas': fichas,
                       **{c: texto(perfil.get(c, 'Não informado.'))[:450] for c in COLUNAS}})
    return linhas


def exemplos_de_redacao(p):
    """Fornece apenas estrutura e estilo dos trabalhos-exemplo, nunca evidência."""
    pasta = p.root / 'exemplos'
    if not pasta.exists():
        return []
    try:
        from pypdf import PdfReader
    except ImportError:
        return []
    exemplos = []
    for caminho in sorted(pasta.glob('*.pdf'))[:3]:
        try:
            texto_pdf = '\n'.join((pagina.extract_text() or '') for pagina in PdfReader(caminho).pages)
        except Exception:
            continue
        normalizado = ' '.join(texto_pdf.split())
        marcadores = [
            trecho for trecho in (
                '1 Introdução', '1.1 Justificativa', '1.2 Objetivos',
                '2 Fundamentação Teórica', '3 Trabalhos Relacionados',
            ) if trecho.lower() in normalizado.lower()
        ]
        exemplos.append({
            'arquivo': caminho.name,
            'paginas': len(PdfReader(caminho).pages),
            'estrutura_identificada': marcadores,
            'trecho_apenas_para_estilo': normalizado[:3500],
        })
    return exemplos


def secoes_redacao(valor, titulo_padrao):
    if isinstance(valor, list):
        resultado = []
        for item in valor:
            if isinstance(item, dict):
                titulo = texto(item.get('titulo') or titulo_padrao)
                corpo = texto(item.get('texto') or item.get('conteudo') or item.get('paragrafos'))
                fontes = item.get('fontes', [])
            else:
                titulo, corpo, fontes = titulo_padrao, texto(item), []
            if corpo:
                resultado.append({'titulo': titulo, 'texto': corpo, 'fontes': fontes if isinstance(fontes, list) else []})
        return resultado
    if texto(valor):
        return [{'titulo': titulo_padrao, 'texto': texto(valor), 'fontes': []}]
    return []


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
            fichas_evidencia = por_id[nome].get('fichas_amostradas', [])
            proposta['evidencias_usadas'] = [f['id'] for f in fichas_evidencia[:3]]
            fatos = [e.get('afirmacao') for f in fichas_evidencia[:3] for e in f.get('evidencias', [])
                     if isinstance(e, dict) and texto(e.get('afirmacao'))]
            proposta['fatos'] = '; '.join(dict.fromkeys(fatos)) or 'Nenhuma evidência literal validada foi selecionada.'
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
                'Desenvolva esta sugestão em nível de reunião com orientador, como brainstorm profundo e útil. '
                'Não escreva só uma frase. JSON com strings: experimento, recursos, metricas, riscos e duvidas_orientador. '
                'Em experimento, detalhe: problema específico, hipótese, arquitetura/artefato a implementar, etapas, baseline '
                'ou trabalhos de comparação, e cenário de avaliação. Em recursos, liste ferramentas, dados/simuladores, padrões '
                'e bibliotecas possíveis, sem inventar disponibilidade. Em métricas, inclua desempenho, segurança, privacidade, '
                'usabilidade/interoperabilidade quando couber. Em riscos, explique o que pode inviabilizar ou reduzir a novidade. '
                'Em dúvidas, escreva perguntas concretas para levar à reunião. Use as fontes fornecidas e deixe claro quando for '
                'inferência exploratória. Cada campo deve ter entre 120 e 250 palavras quando houver informação suficiente.',
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


def redigir_pesquisa_focada(p):
    """Gera uma redação provisória rastreável para o modo de pesquisa focada."""
    from motor import chave, agora, json_gravar, log

    if p.cfg.get('modo_pesquisa') != 'focada':
        return False
    corpus = [linha for linha in matriz(p) if linha.get('fichas_amostradas')]
    if not corpus:
        p.estado.setdefault('redacao_focada', {})['status'] = 'aguardando_fontes'
        return False
    assinatura = chave(corpus)
    anterior = p.estado.get('redacao_focada', {})
    if (anterior.get('assinatura') == assinatura
            and anterior.get('versao') == 3
            and isinstance(anterior.get('introducao'), list)
            and isinstance(anterior.get('fundamentacao_teorica'), list)
            and len(anterior['introducao']) >= 3
            and len(anterior['fundamentacao_teorica']) >= 4):
        return False
    ident = chave(['redacao-focada-v3', p.revisao, assinatura])

    def acao():
        log('Escrevendo introdução e fundamentação teórica provisórias.')
        esquema = {
            'type': 'object',
            'properties': {
                'introducao': {'type': 'array', 'items': {'type': 'string'}, 'minItems': 5},
                'fundamentacao_teorica': {'type': 'array', 'items': {'type': 'object', 'properties': {
                    'titulo': {'type': 'string'}, 'texto': {'type': 'string'},
                    'fontes': {'type': 'array', 'items': {'type': 'string'}}},
                    'required': ['titulo', 'texto', 'fontes']}, 'minItems': 5},
                'mapa_fases': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'fase': {'type': 'string'},
                            'acoes_cidadao': {'type': 'string'},
                            'acoes_entidades': {'type': 'string'},
                            'riscos': {'type': 'string'},
                            'estado_da_arte': {'type': 'string'},
                            'lacunas': {'type': 'string'},
                            'fontes': {'type': 'array', 'items': {'type': 'string'}},
                        },
                        'required': ['fase', 'acoes_cidadao', 'acoes_entidades', 'riscos', 'estado_da_arte', 'lacunas', 'fontes'],
                    },
                },
                'fontes_usadas': {'type': 'array', 'items': {'type': 'string'}},
            },
            'required': ['introducao', 'fundamentacao_teorica', 'mapa_fases', 'fontes_usadas'],
        }
        r = chamar(p, 'redacao-focada',
            'Escreva uma seção acadêmica desenvolvida, não um resumo. Use os trabalhos-exemplo apenas para aprender '
            'estrutura, extensão, profundidade e modo de referenciar; eles NÃO são fontes do tema e não podem ser citados. '
            'A introdução deve ter 5 a 8 parágrafos substanciais, cobrindo contexto de cidades inteligentes, problema, '
            'motivação, justificativa, objetivo geral, objetivos específicos e organização do texto. A fundamentação deve '
            'ter pelo menos 6 subseções nomeadas, cada uma com 2 a 4 parágrafos: (1) cidades inteligentes e atores, '
            '(2) identidade digital e SSI, (3) DID e credenciais verificáveis, (4) autenticação e controle de acesso, '
            '(5) segurança e privacidade no ciclo de dados, (6) interoperabilidade e governança, (7) revogação e '
            'recuperação de acesso. Compare conceitos e abordagens, explicando limites e relações, em vez de listar definições. '
            'Use citações autor-data somente quando o trabalho fornecido trouxer autor e ano; caso contrário cite o '
            'identificador real do trabalho entre colchetes, por exemplo [Papatheodorou_2025]. NUNCA escreva '
            '[ID_EXATO], [ID] ou qualquer marcador genérico. Cada afirmação factual precisa de uma fonte real; se '
            'nenhuma ficha sustentar a afirmação, escreva “não identificado nas fontes lidas”. '
            'Depois faça exatamente 7 itens no mapa: emissão, apresentação/verificação, transmissão, processamento, '
            'armazenamento, revogação e recuperação de acesso. Em cada item use 2 a 4 frases por campo para ações do cidadão '
            'e entidades administrativas, riscos, estado da arte e lacunas. Use somente os '
            'trabalhos fornecidos. Insira citações no texto como [ID_EXATO] e liste em fontes_usadas somente IDs '
            'fornecidos. Não invente autores, anos, resultados ou consenso: quando a fonte não sustentar algo, escreva '
            '“não identificado nas fontes lidas” e trate lacunas como hipóteses. A redação é um rascunho de trabalho, '
            'não uma afirmação de novidade comprovada. JSON no esquema fornecido. '
            'EXEMPLOS DE FORMA, NÃO FONTES: ' + json.dumps(exemplos_de_redacao(p), ensure_ascii=False),
            {'objetivo': p.instrucoes, 'trabalhos': corpus}, esquema)
        if '[ID_EXATO]' in json.dumps(r, ensure_ascii=False) or '[ID]' in json.dumps(r, ensure_ascii=False):
            raise ValueError('A redação contém marcador de citação genérico; a tarefa será refeita com IDs reais.')
        ids = {linha['id'] for linha in corpus}
        fontes = [f for f in r.get('fontes_usadas', []) if isinstance(f, str) and f in ids]
        introducao = secoes_redacao(r.get('introducao'), 'Introdução')
        fundamentacao = secoes_redacao(r.get('fundamentacao_teorica'), 'Fundamentação teórica')
        if len(introducao) < 3 or len(fundamentacao) < 4:
            raise ValueError('A redação focada não trouxe introdução e fundamentação completas.')
        fases = []
        for fase in r.get('mapa_fases', []) if isinstance(r.get('mapa_fases'), list) else []:
            if not isinstance(fase, dict) or not texto(fase.get('fase')):
                continue
            item = dict(fase)
            item['fontes'] = [f for f in item.get('fontes', []) if isinstance(f, str) and f in ids]
            fases.append(item)
        resultado = {'versao': 3, 'revisao': p.revisao, 'assinatura': assinatura, 'gerado_em': agora(),
                     'status': 'rascunho_em_revisao', 'introducao': introducao,
                     'fundamentacao_teorica': fundamentacao,
                     'mapa_fases': fases, 'fontes_usadas': fontes}
        p.estado['redacao_focada'] = resultado
        json_gravar(p.root / 'dados/redacao-focada.json', resultado)
        p.salvar()
        return True

    return bool(p.tarefa(ident, acao))


def ciclo(p):
    p.configurar()
    pausa_modelo_ate = p.estado.get('pausa_modelo_ate', 0)
    if pausa_modelo_ate and pausa_modelo_ate > time.time():
        restante = int(pausa_modelo_ate - time.time())
        p.mensagem = f"Modelos de IA indisponíveis; retomada em {max(1, restante)} s."
        p.salvar()
        p.painel()
        return
    p.estado.pop('pausa_modelo_ate', None)
    p.mensagem = 'Preparando o próximo trabalho.'
    p.importar_pdfs()
    p.painel()
    lote = p.preparar_lote()
    if not lote:
        p.mensagem = 'Nenhum trabalho novo disponível agora; aguardando a próxima consulta.'
        p.salvar()
        p.painel()
        return

    artigos = [a for a in p.artigos if a['nome_local'] in lote['ids']]
    artigo = artigos[0] if artigos else None
    if not artigo:
        p.concluir_lote()
        return

    if p.modelo_disponivel():
        p.triagem()
        triagem = artigo.get('triagem_agente', {})
        if not (p.ignorado(artigo) or triagem.get('revisao') == p.revisao):
            p.mensagem = f"Trabalho {lote['numero']}: triagem de título/resumo em andamento — {artigo['nome_local']}."
            p.salvar()
            p.painel()
            return

        if p.trabalho_fechado_no_ciclo(artigo):
            p.concluir_lote()
            p.painel()
            return

        p.baixar()
        p.pre_leitura()
        pre = artigo.get('pre_leitura_agente', {})
        if triagem.get('classificacao') in {'priorizar', 'revisar', 'sem_resumo'} and pre.get('revisao') != p.revisao:
            p.mensagem = f"Trabalho {lote['numero']}: buscando/confirmando texto completo e pré-leitura — {artigo['nome_local']}."
            p.salvar()
            p.painel()
            return

        if p.trabalho_fechado_no_ciclo(artigo):
            p.concluir_lote()
            p.painel()
            return

        ler(p)
        pausa_modelo_ate = p.estado.get('pausa_modelo_ate', 0)
        if pausa_modelo_ate and pausa_modelo_ate > time.time():
            p.salvar()
            p.painel()
            return
        propor(p)
        detalhar(p)
        redigir_pesquisa_focada(p)

        if p.trabalho_fechado_no_ciclo(artigo):
            p.concluir_lote()
            p.painel()
            pendentes = p.propostas_pendentes_avaliacao()
            if pendentes:
                p.estado['aguardando_avaliacao_propostas'] = {'revisao': p.revisao, 'quantidade': len(pendentes)}
                p.mensagem = f'Trabalho concluído com {len(pendentes)} proposta(s) pendente(s) de avaliação em vault/AVALIAR-PROPOSTAS.md. Edite o arquivo quando quiser guiar as próximas buscas.'
                p.salvar()
                p.painel()
                return

        leitura = artigo.get('leitura_agente', {})
        erros = sum(bool(t.get('erro')) and not t.get('versao_anterior') for t in p.estado['tarefas'].values())
        p.mensagem = (
            f"Trabalho {lote['numero']}: {artigo['nome_local']} — "
            f"triagem={triagem.get('classificacao', 'pendente')}; "
            f"pré-leitura={pre.get('decisao', 'pendente')}; "
            f"leitura={leitura.get('feitos', 0)}/{leitura.get('total', 0)}; "
            f"{sum(m['revisao'] == p.revisao for m in p.estado['propostas'])} sugestões; "
            f"{erros} pendências técnicas."
        )
    p.salvar()
    p.painel()
