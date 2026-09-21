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
para conferência e a redação deve ser reescrita e validada pelo pesquisador.

O fluxo de uso é simples:

1. Edite `vault/INSTRUCOES.md` com o tema, as perguntas e o modo de pesquisa.
2. Coloque trabalhos-base em `exemplos/` quando quiser que o agente os leia e use como sementes da pesquisa.
3. Configure a chave em `.env` e instale as dependências.
4. Rode `python agente.py` e acompanhe o terminal.
5. Leia os relatórios e revise as fontes e o texto produzido.
6. Rode novamente para ampliar o corpus e melhorar a redação.

O repositório inclui o estado de pesquisa, PDFs, exemplos, notas Markdown e
testes para que outra máquina receba o projeto no mesmo ponto. Segredos locais,
bytecode e ambientes virtuais instalados não entram no Git.

## Estrutura versionada

- `agente.py`: ponto de entrada e configuração editável. Cria `vault/INSTRUCOES.md` em clones novos.
- `motor.py`: orquestra execução, buscas acadêmicas, estado persistente, downloads permitidos, OpenRouter/Ollama, triagem e pré-leitura.
- `revisao.py`: leitura, fichamento, síntese, comparação entre trabalhos e geração de propostas.
- `apresentacao.py`: gera os arquivos Markdown visíveis em `vault/`.
- `tests/`: testes de regressão.
- `.env.example`: modelo de configuração local, sem chave.
- `.gitignore`: impede versionar `.env`, bytecode, caches e ambientes virtuais.

## Pastas do projeto

Estas pastas fazem parte do estado transportável do projeto e podem ser
versionadas:

- `exemplos/`: trabalhos fornecidos pelo pesquisador. São lidos integralmente
	como sementes e também orientam a forma da redação, mas não são usados como
	citações automáticas.
- `vault/`: instruções, relatórios, redação, notas Markdown e avaliações.
- `dados/`: estado interno, fichamentos, diagnósticos, propostas e histórico.
- `pdfs/`: PDFs/HTML baixados de fontes abertas ou colocados manualmente.
- `.obsidian/`: configuração do Obsidian, quando houver.

Como PDFs e estado de pesquisa podem aumentar o repositório, confirme a política
do seu servidor Git antes de publicar. Para esta cópia, eles são intencionais e
necessários para transportar o contexto entre máquinas.

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
python -m unittest discover -s tests -v
python agente.py --uma-vez
```

Na primeira execução, se `vault/INSTRUCOES.md` não existir, o agente cria um
arquivo inicial para você editar. Nesta versão, o arquivo já versionado em
`vault/` mantém as instruções e o contexto escolhidos pelo pesquisador.

## Instalação no Windows

```powershell
git clone <url-do-seu-repositorio> research-assistant
cd research-assistant
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
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

A configuração padrão em `vault/INSTRUCOES.md` usa um modelo principal fixo. Para custo zero e comportamento mais estável, use `modelo ia: ollama`. Para usar OpenRouter, informe um único modelo em `modelo ia:` ou use `modelo ia: openrouter` junto com `modelo openrouter:`. O Ollama continua como reserva técnica.

Se você colocou crédito no OpenRouter e quiser usar um modelo pago específico, edite `vault/INSTRUCOES.md`:

```md
- modelo ia: openrouter
- modelo openrouter: openai/gpt-oss-120b
- modelo ollama de reserva: qwen2.5:7b-instruct-q4_K_M
```

Os nomes exatos dos modelos mudam com o tempo. Use os slugs atuais mostrados pelo OpenRouter. Para controlar gasto e reduzir variação, crie uma chave dedicada, configure limite de uso e escolha apenas um modelo principal.

## Configurando IA local com Ollama

Instale o Ollama. O agente consulta os modelos instalados; se encontrar um modelo compatível, usa esse modelo. Se não houver nenhum modelo local adequado e o Ollama for necessário, ele tenta baixar automaticamente o modelo indicado em `vault/INSTRUCOES.md`.

Você também pode baixar manualmente antes de rodar:

```bash
ollama pull qwen2.5:7b-instruct-q4_K_M
ollama serve
```

Em outra janela:

```bash
python agente.py
```

Se `ollama serve` não estiver rodando, o agente tenta iniciar automaticamente. No Linux, se você instalou Ollama como serviço, normalmente ele já fica disponível em `http://localhost:11434`.

Para uma máquina com i9, 16 GB de RAM e GPU com 8 GB de VRAM, comece com um modelo 7B ou 8B quantizado. Se sobrar memória e a velocidade for aceitável, teste um 14B quantizado. Para este projeto, estabilidade e baixa alucinação importam mais que velocidade. Compare modelos olhando se eles retornam JSON válido, citam evidências corretamente e produzem propostas úteis no `RELATORIO.md`.

Exemplos para testar localmente:

```bash
ollama pull qwen2.5:7b-instruct-q4_K_M
ollama pull qwen2.5:14b-instruct-q4_K_M
```

Depois ajuste em `vault/INSTRUCOES.md`:

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

No `vault/INSTRUCOES.md`, a configuração recomendada é:

```md
- fonte acadêmica principal: openalex
- fontes acadêmicas auxiliares: semantic_scholar, crossref
- modelo ia: openrouter
- modelo ollama de reserva: qwen2.5:7b-instruct-q4_K_M
```

Se quiser testar uma IA remota fixa:

```md
- modelo ia: openrouter
- modelo openrouter: openai/gpt-oss-120b
- modelo ollama de reserva: qwen2.5:7b-instruct-q4_K_M
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

1. Lê `vault/INSTRUCOES.md` e o estado persistido em `dados/`.
2. Importa PDFs de `exemplos/` e `pdfs/`; os trabalhos-base de `exemplos/` são sementes prioritárias e têm leitura integral obrigatória.
3. Gera consultas a partir das variáveis, consultas manuais e ideias encontradas.
4. Busca resultados no OpenAlex por padrão; Crossref e Semantic Scholar são fallbacks configuráveis.
5. Deduplica por DOI ou título e faz triagem por título/resumo.
6. Tenta obter texto completo aberto por fontes permitidas, incluindo Unpaywall e Semantic Scholar.
7. Faz pré-leitura e depois fichamento por trechos, validando citações literais contra o texto original.
8. Consolida cada trabalho e compara as abordagens, limites, avaliações e possibilidades.
9. No modo `focada`, produz o mapa de fases e atualiza `vault/INTRODUCAO-E-FUNDAMENTACAO.md`.
10. No modo `geral`, organiza o estado da arte, hipóteses de lacunas e propostas de contribuição.
11. Registra fontes, consultas, tarefas e falhas em `dados/` para permitir retomada em outra máquina.
12. O pesquisador revisa o resultado, confere referências e pode ajustar as instruções antes da próxima rodada.

## Arquivos que você deve olhar durante o uso

- `vault/INSTRUCOES.md`: comandos e direção da pesquisa. Você edita.
- `vault/INTRODUCAO-E-FUNDAMENTACAO.md`: redação focada com links para as notas dos trabalhos citados.
- `vault/PROPOSTAS-DE-TRABALHO.md`: lista de propostas, lacunas, hipóteses, formas de avaliação e fontes.
- `vault/AVALIAR-PROPOSTAS.md`: avaliação das ideias para guiar próximas buscas. Você edita.
- `vault/trabalhos/`: notas dos trabalhos citados ou usados nas propostas. Cada nota deve ter síntese/fichamento e apontar para o anexo local quando houver.
- `pdfs/`: PDFs ou HTMLs dos textos completos disponíveis.
- `vault/RELATORIO.md` e `vault/METODOLOGIA-REVISAO.md`: arquivos operacionais/legados de rastreabilidade.

## Testes

```bash
python -m py_compile agente.py motor.py revisao.py apresentacao.py
python -m unittest discover -s tests -v
```

Rode os testes antes de mandar mudanças para o Git.

## Observações metodológicas

Este é um assistente de revisão e redação provisória. Ele não substitui a
revisão crítica do pesquisador nem a orientação. Citações e afirmações da IA
precisam ser conferidas nas fontes; lacunas, estado da arte e propostas não são
conclusões confirmadas. Trabalhos em `exemplos/` orientam o contexto e a forma,
mas a redação final deve ser autoral, citada e validada pelo pesquisador.

O agente não deve burlar restrições de acesso. Quando não consegue texto integral permitido, registra internamente e segue para outros trabalhos.
