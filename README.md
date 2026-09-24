# Assistente de Pesquisa Acadêmica

Este projeto ajuda um pesquisador a sair de uma ideia, de instruções e de
alguns trabalhos-base para uma revisão organizada e um primeiro texto acadêmico.
Ele busca trabalhos em bases acadêmicas abertas, lê os textos disponíveis,
compara ideias, registra evidências e produz uma versão inicial de introdução,
fundamentação teórica, estado da arte e possíveis lacunas.

O sistema é uma ferramenta de apoio à pesquisa, não um gerador de trabalho
pronto. O pesquisador deve revisar o texto, conferir cada referência no trabalho
original, corrigir interpretações e decidir o que pode ser aproveitado. O texto
gerado não deve ser apresentado como autoria automática nem como substituto da
leitura, da orientação ou da contribuição intelectual do pesquisador. A proposta
é ajudar a começar e organizar a escrita, não plagiar: as fontes são registradas
para conferência e a redação deve ser revisada e validada pelo pesquisador.

O fluxo de uso é simples:

1. Edite `obsidian/ANOTACOES.md` como um caderno do pesquisador: tema, perguntas, decisões, dúvidas, feedback e ideias soltas.
2. Coloque trabalhos-base em `obsidian/referencias/pdfs/` quando quiser que o agente os leia e use como sementes da pesquisa.
3. Configure a chave em `.env` e instale as dependências.
4. Rode `python agente.py` e acompanhe o terminal.
5. Leia `obsidian/TRABALHO.md`, as propostas no próprio arquivo de anotações e os fichamentos em `obsidian/referencias/fichamentos/`.
6. Rode novamente para ampliar o corpus e melhorar a redação.

O repositório foi pensado para carregar o código genérico, testes e a estrutura
mínima do Obsidian. O acervo real da pesquisa — PDFs, fichamentos, anotações,
texto em construção e memória da IA — fica local ou em armazenamento privado.
Segredos locais, bytecode e ambientes virtuais instalados não entram no Git.

## Estrutura versionada

- `agente.py`: atalho de execução na raiz. Mantém o comando simples: `python agente.py`.
- `src/agente.py`: configuração, constantes, leitura das anotações e utilitários de metadados.
- `src/motor.py`: orquestra execução, buscas acadêmicas, estado persistente, downloads permitidos, OpenRouter/Ollama, triagem e pré-leitura.
- `src/revisao.py`: leitura, fichamento, síntese, comparação entre trabalhos e geração de propostas.
- `src/apresentacao.py`: gera os arquivos Markdown visíveis em `obsidian/`.
- `tests/`: testes de regressão.
- `.env.example`: modelo de configuração local, sem chave.
- `.gitignore`: impede versionar `.env`, bytecode, caches e ambientes virtuais.

## Pastas do projeto

Estas pastas existem no projeto, mas o Git versiona apenas templates e arquivos
`.gitkeep` para preservar a estrutura limpa:

- `obsidian/`: pasta que você abre no Obsidian. Localmente contém `ANOTACOES.md`, `TRABALHO.md` e a biblioteca de referências. No Git entram apenas `ANOTACOES.example.md`, `TRABALHO.example.md` e a estrutura vazia.
- `obsidian/referencias/pdfs/`: repositório local dos textos completos usados como base da pesquisa, em PDF, HTML ou outro formato aberto. Conteúdo ignorado pelo Git.
- `obsidian/referencias/fichamentos/`: fichamentos locais, um Markdown por trabalho de referência. Conteúdo ignorado pelo Git.
- `dados/`: estado interno local para a IA retomar execuções: leituras, diagnósticos, propostas, histórico e `anotacoes-ia.md`. Conteúdo ignorado pelo Git.

Se quiser transportar sua pesquisa pessoal entre máquinas, sincronize `obsidian/` e `dados/` por um repositório privado separado, backup criptografado ou nuvem privada. O repositório público fica limpo e reutilizável.

## Ambiente virtual

Use uma venv local para instalar as dependências sem misturar com o Python do sistema.

No Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

No Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Depois de ativar a venv, rode os comandos do projeto normalmente com `python`.

## Instalação no Linux

Use Python 3.11 ou superior.

```bash
git clone <url-do-seu-repositorio> research-assistant
cd research-assistant
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
cp obsidian/ANOTACOES.example.md obsidian/ANOTACOES.md
cp obsidian/TRABALHO.example.md obsidian/TRABALHO.md
python -m unittest discover -s tests -v
python agente.py --uma-vez
```

Na primeira execução, se `obsidian/ANOTACOES.md` não existir, o agente também
consegue criar um arquivo inicial. Os templates versionados existem para deixar
o ponto de partida claro em uma instalação limpa.

## Instalação no Windows

```powershell
git clone <url-do-seu-repositorio> research-assistant
cd research-assistant
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
Copy-Item obsidian/ANOTACOES.example.md obsidian/ANOTACOES.md
Copy-Item obsidian/TRABALHO.example.md obsidian/TRABALHO.md
python -m unittest discover -s tests -v
python agente.py --uma-vez
```

## Configurando IA remota com OpenRouter

Crie uma chave no OpenRouter e coloque em `.env`:

```env
OPENROUTER_API_KEY=cole_sua_chave_aqui
UNPAYWALL_EMAIL=seu-email@exemplo.com
SEMANTIC_SCHOLAR_API_KEY=opcional
CORE_API_KEY=opcional
```

Ou configure só no terminal:

```bash
export OPENROUTER_API_KEY="cole_sua_chave_aqui"
python agente.py
```

No Windows PowerShell:

```powershell
$env:OPENROUTER_API_KEY = "cole_sua_chave_aqui"
python agente.py
```

A configuração padrão em `obsidian/ANOTACOES.md` usa OpenRouter quando houver chave e mantém Ollama como reserva. A lista do OpenRouter é uma fila configurável de slugs reais, não uma garantia de “melhores modelos”; esses slugs mudam com o tempo e devem ser escolhidos pelo pesquisador conforme custo, qualidade e disponibilidade.

A escolha local via Ollama segue esta prioridade:

1. modelo explicitado em `obsidian/ANOTACOES.md`;
2. modelo registrado em `dados/modelos.json`, útil para guardar o resultado de benchmark da máquina;
3. melhor modelo já instalado no Ollama segundo uma heurística simples;
4. download do modelo de reserva, se não houver nenhum modelo local instalado.

Assim, se uma máquina foi testada e o melhor equilíbrio foi `qwen3:8b`, registre isso uma vez e o agente passa a respeitar essa decisão. O arquivo `dados/modelos.json` é local/ignorado pelo Git porque depende do hardware. Exemplo:

```json
{
  "modelo_ollama": "qwen3:8b",
  "observacao": "Escolhido por benchmark local nesta máquina."
}
```

Confira o nome exato com `ollama list`. Se você escreveu informalmente `qwen3.8b`, o agente tenta casar com `qwen3:8b`, mas o ideal é usar o nome exibido pelo Ollama.

Se você colocou crédito no OpenRouter e quiser usar um modelo pago específico, edite `obsidian/ANOTACOES.md`:

```md
- modelo ia: openrouter
- modelo openrouter: openai/gpt-oss-120b
- modelo ollama de reserva: qwen3:8b
```

Os nomes exatos dos modelos mudam com o tempo. Use os slugs atuais mostrados pelo OpenRouter. Para controlar gasto e reduzir variação, crie uma chave dedicada, configure limite de uso e escolha apenas um modelo principal.

## Configurando IA local com Ollama

Instale o Ollama. O agente consulta os modelos instalados; se encontrar o modelo preferido, usa exatamente ele. Se o preferido não estiver instalado, escolhe o melhor instalado por heurística, privilegiando modelos de conversa/instrução e famílias como Qwen, Llama, Mistral, Gemma e Phi. Se não houver nenhum modelo local e o Ollama for necessário, ele tenta baixar automaticamente o modelo indicado em `obsidian/ANOTACOES.md` ou em `dados/modelos.json`.

Você também pode baixar manualmente antes de rodar:

```bash
ollama pull qwen3:8b
ollama serve
```

Em outra janela:

```bash
python agente.py
```

Se `ollama serve` não estiver rodando, o agente tenta iniciar automaticamente. No Linux, se você instalou Ollama como serviço, normalmente ele já fica disponível em `http://localhost:11434`.

Para uma máquina com i9, 16 GB de RAM e GPU com 8 GB de VRAM, comece com um modelo 7B ou 8B quantizado. Se sobrar memória e a velocidade for aceitável, teste um 14B quantizado. Para este projeto, estabilidade e baixa alucinação importam mais que velocidade. Compare modelos olhando se eles retornam JSON válido, citam evidências corretamente e produzem propostas úteis em `obsidian/ANOTACOES.md`.

Exemplos para testar localmente:

```bash
ollama pull qwen3:8b
ollama pull qwen2.5:14b-instruct-q4_K_M
```

Depois ajuste em `obsidian/ANOTACOES.md`:

```md
- modelo ia: ollama
- modelo ollama de reserva: qwen2.5:14b-instruct-q4_K_M
```

## Busca acadêmica estável

A fonte acadêmica principal é o OpenAlex, porque costuma responder de forma mais estável e traz metadados de acesso aberto. Semantic Scholar e Crossref ficam como auxiliares: se uma fonte der limite, timeout ou falhar, o agente tenta a próxima. Unpaywall não muda a seleção de trabalhos; ele só tenta encontrar uma cópia open access pelo DOI.

Se você tiver uma chave do Semantic Scholar, coloque-a em `.env` como
`SEMANTIC_SCHOLAR_API_KEY`. O agente envia a chave no header `x-api-key` e
serializa as chamadas ao Semantic Scholar para respeitar o limite de 1
requisição por segundo, cumulativo entre endpoints.

No `obsidian/ANOTACOES.md`, a configuração recomendada é:

```md
- fonte acadêmica principal: openalex
- fontes acadêmicas auxiliares: semantic_scholar, crossref
- modelo ia: openrouter
- modelo ollama de reserva: qwen3:8b
```

Se quiser testar uma IA remota fixa:

```md
- modelo ia: openrouter
- modelo openrouter: openai/gpt-oss-120b
- modelo ollama de reserva: qwen3:8b
```

## Como rodar

Execução normal de até 8 horas:

```bash
python agente.py
```

Rodar por 12 horas:

```bash
python agente.py --duracao-horas 12
```

Executar só um ciclo, útil para teste:

```bash
python agente.py --uma-vez
```

Recomeçar a execução mantendo arquivos do projeto, mas zerando o estado ativo:

```bash
python agente.py --limpar
```

Use `Ctrl+C` para pausar. Rodar o mesmo comando depois retoma o estado salvo.

## Fluxo do agente

1. Lê `obsidian/ANOTACOES.md` e o estado persistido em `dados/`.
2. Importa textos completos de `obsidian/referencias/pdfs/`; trabalhos-base indicados em `ANOTACOES.md` são sementes prioritárias e têm leitura integral obrigatória.
3. Gera consultas a partir das variáveis, consultas manuais e ideias encontradas.
4. Busca resultados no OpenAlex por padrão; Crossref e Semantic Scholar são fallbacks configuráveis.
5. Deduplica por DOI ou título e faz triagem por título/resumo.
6. Tenta obter texto completo aberto por fontes permitidas, incluindo Unpaywall e Semantic Scholar.
7. Faz pré-leitura e depois fichamento por trechos, validando citações literais contra o texto original.
8. Consolida cada trabalho e compara as abordagens, limites, avaliações e possibilidades.
9. No modo `focada`, produz o mapa de fases e atualiza `obsidian/TRABALHO.md`.
10. No modo `geral`, organiza o estado da arte, hipóteses de lacunas e propostas de contribuição.
11. Registra fontes, consultas, tarefas e falhas em `dados/` para permitir retomada em outra máquina.
12. No início de cada rodada, a IA lê novamente `ANOTACOES.md`, `TRABALHO.md`, `dados/anotacoes-ia.md` e os fichamentos já produzidos; só relê PDFs quando o fluxo indicar que falta evidência.
13. A IA gera consultas adicionais para esclarecer pontos das anotações. Os resultados aparecem como achados em análise nas anotações; somente trabalhos aprovados e fichados entram na biblioteca de referências.
14. O pesquisador revisa o resultado, confere referências e pode ajustar as instruções antes da próxima rodada.

Em `ANOTACOES.md`, texto fora dos blocos automáticos é tratado como anotação do
pesquisador. Achados da IA aparecem em `<!-- agente:dialogo:inicio -->`; responda
em `resposta_pesquisador:` com `aprovar`, `rejeitar` ou `revisar`. A IA não deve
tratar uma sugestão própria como aprovação e não pode apagar texto existente de
`ANOTACOES.md` ou `TRABALHO.md`.

## Arquivos que você deve olhar durante o uso

- `obsidian/ANOTACOES.md`: caderno local do pesquisador e principal arquivo de interação com a IA. Você escreve orientações livres, acompanha achados e responde com `aprovar`, `rejeitar` ou `revisar` para guiar próximas buscas.
- `obsidian/TRABALHO.md`: texto acadêmico em construção, hoje com introdução, fundamentação e mapa conceitual citando as notas dos trabalhos.
- `obsidian/referencias/fichamentos/`: uma nota por trabalho, contendo somente o resumo, o perfil factual e as evidências do próprio PDF. Conexões entre trabalhos, lacunas e propostas ficam em `obsidian/ANOTACOES.md`; afirmações já consolidadas entram em `obsidian/TRABALHO.md`.
- `obsidian/referencias/pdfs/`: textos completos disponíveis, baixados de fontes abertas ou colocados manualmente.
- `dados/anotacoes-ia.md`: memória operacional e rastreabilidade do agente. Em geral você não precisa abrir este arquivo.

## Testes

```bash
python -m py_compile agente.py src/agente.py src/motor.py src/revisao.py src/apresentacao.py
python -m unittest discover -s tests -v
```

Rode os testes antes de mandar mudanças para o Git.

## Observações metodológicas

Este é um assistente de revisão e redação provisória. Ele não substitui a
revisão crítica do pesquisador nem a orientação. Citações e afirmações da IA
precisam ser conferidas nas fontes; lacunas, estado da arte e propostas não são
conclusões confirmadas. Trabalhos em `obsidian/referencias/pdfs/` orientam o contexto e a forma,
mas a redação final deve ser autoral, citada e validada pelo pesquisador.

O agente não deve burlar restrições de acesso. Quando não consegue texto integral permitido, registra internamente e segue para outros trabalhos.
## Rigor na maturação de propostas

Uma ideia gerada pelo agente é inicialmente um brainstorm, não uma contribuição científica. Antes de ganhar um estado de novidade, ela precisa registrar problema técnico, mecanismo, unidade de novidade, propriedades P1...Pn, propriedade falsificável, artefato mínimo e experimento decisivo. O agente executa cinco rodadas de anterioridade (combinação explícita, sinônimos, mecanismo fora do domínio, combinações de propriedades e relações dos trabalhos próximos) em Semantic Scholar, OpenAlex e Crossref.

O resultado usa `collision_found`, `likely_incremental`, `plausible_gap`, `strong_candidate` ou `insufficient_evidence`. O código impede `strong_candidate` sem rastreabilidade das buscas e ao menos três trabalhos próximos examinados além do título. Colisões devem provocar reformulação e nova busca. Metas numéricas sem literatura, requisito ou piloto são rejeitadas. O pesquisador continua responsável por conferir textos, referências e a alegação de novidade antes de usar o material academicamente.
