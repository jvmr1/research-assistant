# Agente de revisão exploratória para mestrado

Este projeto é um agente de garimpo e leitura de literatura acadêmica. A ideia é rodar por horas em um terminal, buscar trabalhos em bases abertas e processar um trabalho por vez: triar título/resumo, tentar obter texto completo permitido, fazer pré-leitura, fichar o texto relevante até o fim e alimentar um relatório com lacunas e propostas de contribuição antes de passar ao próximo trabalho.

O fluxo de uso é simples:

1. Edite `vault/INSTRUCOES.md`.
2. Rode `python agente.py`.
3. Acompanhe o terminal.
4. Leia `vault/RELATORIO.md`.
5. Avalie ideias em `vault/AVALIAR-PROPOSTAS.md`.
6. Rode novamente para o agente buscar mais perto do que você marcou como interessante.

O repositório versiona apenas código, testes e documentação. A base pessoal do Obsidian, PDFs baixados, caches, relatórios e estado de execução ficam fora do Git.

## Estrutura versionada

- `agente.py`: ponto de entrada e configuração editável. Cria `vault/INSTRUCOES.md` em clones novos.
- `motor.py`: orquestra execução, buscas acadêmicas, estado persistente, downloads permitidos, OpenRouter/Ollama, triagem e pré-leitura.
- `revisao.py`: leitura, fichamento, síntese, comparação entre trabalhos e geração de propostas.
- `apresentacao.py`: gera os arquivos Markdown visíveis em `vault/`.
- `tests/`: testes de regressão.
- `.env.example`: modelo de configuração local, sem chave.
- `.gitignore`: impede versionar base pessoal, PDFs, caches e chaves.

## Pastas geradas localmente

Estas pastas são criadas ou atualizadas durante a execução e ficam fora do Git:

- `vault/`: sua base Markdown/Obsidian, incluindo `INSTRUCOES.md`, `RELATORIO.md`, `AVALIAR-PROPOSTAS.md` e notas dos trabalhos.
- `dados/`: estado interno, caches de texto, diagnósticos, fichamentos e propostas em JSON.
- `pdfs/`: PDFs/HTML baixados de fontes abertas ou colocados manualmente.
- `.obsidian/`: configuração local do Obsidian.
- `backup-*` e `imagens/`: backups e capturas locais.

Se você quiser transportar a base entre Windows e Linux, sincronize essas pastas por fora do Git, por exemplo via Syncthing, Obsidian Sync, Dropbox, Google Drive ou cópia manual. O Git deve ficar só com o programa.

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

Na primeira execução, se `vault/INSTRUCOES.md` não existir, o agente cria um arquivo inicial para você editar.

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

1. Lê `vault/INSTRUCOES.md`.
2. Gera consultas a partir das variáveis de busca e consultas manuais.
3. Busca resultados no Semantic Scholar por padrão.
4. Deduplica por DOI ou título.
5. Faz triagem por título/resumo.
6. Tenta encontrar texto completo aberto pelo PDF do Semantic Scholar e por Unpaywall pelo DOI. CORE continua opcional quando configurado.
7. Baixa somente texto aberto permitido.
8. Descarta do grafo trabalhos sem texto integral útil, mantendo registro interno em JSON.
9. Faz pré-leitura de introdução/conclusão quando possível.
10. Lê integralmente um trabalho aprovado antes de passar para outro.
11. Registra fichamento e síntese do trabalho.
12. Atualiza estado da arte, lacunas e propostas no relatório.
13. Para quando houver propostas novas aguardando avaliação humana.
14. Na próxima execução, usa as avaliações positivas para puxar buscas próximas.

## Arquivos que você deve olhar durante o uso

- `vault/INSTRUCOES.md`: comandos e direção da pesquisa. Você edita.
- `vault/RELATORIO.md`: lacunas e propostas geradas. Você lê.
- `vault/AVALIAR-PROPOSTAS.md`: avaliação das ideias para guiar próximas buscas. Você edita.
- `vault/trabalhos/`: notas dos trabalhos com texto integral útil.

## Testes

```bash
python -m py_compile agente.py motor.py revisao.py apresentacao.py
python -m unittest discover -s tests -v
```

Rode os testes antes de mandar mudanças para o Git.

## Observações metodológicas

Este é um assistente de revisão exploratória e brainstorm. Ele não substitui a revisão crítica do pesquisador nem a orientação. As propostas são hipóteses: servem para encontrar direções promissoras, trabalhos próximos, lacunas possíveis e ideias de contribuição factíveis.

O agente não deve burlar restrições de acesso. Quando não consegue texto integral permitido, registra internamente e segue para outros trabalhos.
