---
nome_local: Papatheodorou_2025
openalex_id: https://openalex.org/W4411154141
doi: https://doi.org/10.3390/app15126437
ano: 2025
status: triagem_pendente
acesso_aberto: true
pdf_local: pdfs/Papatheodorou_2025.pdf
tags: [blockchain, cidades-inteligentes, contratos-inteligentes, controle-de-acesso, criptografia, identidade-digital, interoperabilidade, privacidade, sistemas-distribuidos, ssi]
---
# Papatheodorou_2025

## Tags

#blockchain #cidades-inteligentes #contratos-inteligentes #controle-de-acesso #criptografia #identidade-digital #interoperabilidade #privacidade #sistemas-distribuidos #ssi
<!-- agente:inicio -->

## Leitura e relações atualizadas pelo agente

Fonte: https://doi.org/10.3390/app15126437

Triagem: priorizar. O trabalho apresenta um sistema SSI baseado em blockchain (BSC) que inclui emissão, revogação, compartilhamento e controle de acesso de credenciais, alinhado aos padrões DID/W3C. Aborda aspectos críticos para o ciclo de vida da credencial (emissão, revogação, auditoria) e menciona aplicação em contextos municipais ou governamentais, o que o torna diretamente relevante para a revisão focada em identidade autossoberana em cidades inteligentes. Embora não detalhe todas as fases (ex.: processamento ou recuperação pós-perda), fornece base tecnológica, métricas de desempenho e comparações com outras soluções SSI, servindo como fonte importante para mapear requisitos de segurança, privacidade e interoperabilidade. Portanto, deve ser priorizado para inclusão na revisão.

[PDF local](../../pdfs/Papatheodorou_2025.pdf)

### Relações bibliográficas verificadas nos metadados

Referencia: nenhum trabalho do acervo identificado.

É citado por: nenhum trabalho do acervo identificado.

### Como se correlaciona com os demais na análise

**Com  — Papatheodorou_2025: Realizar testes de carga simulando milhares de dispositivos IoT para medir latência, throu**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Realizar testes de carga simulando milhares de dispositivos IoT para medir latência, throughput e comportamento sob alta concorrência

[Proposta completa no relatório](../RELATORIO.md)

**Com  — Papatheodorou_2025: Comparar alternativas de armazenamento descentralizado (ex**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Comparar alternativas de armazenamento descentralizado (ex.: Filecoin, Arweave) quanto à disponibilidade, latência e custos

[Proposta completa no relatório](../RELATORIO.md)

**Com  — Papatheodorou_2025: Desenvolver e validar um protocolo de revogação instantânea usando eventos de contrato int**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Desenvolver e validar um protocolo de revogação instantânea usando eventos de contrato inteligente e notificações off‑chain

[Proposta completa no relatório](../RELATORIO.md)

**Com  — Papatheodorou_2025: Realizar testes de carga simulando milhares de usuários simultâneos para medir latência e **

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Realizar testes de carga simulando milhares de usuários simultâneos para medir latência e throughput

[Proposta completa no relatório](../RELATORIO.md)

**Com  — Papatheodorou_2025: Implementar camada de armazenamento híbrido que combine IPFS com provedores de backup desc**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Implementar camada de armazenamento híbrido que combine IPFS com provedores de backup descentralizado

[Proposta completa no relatório](../RELATORIO.md)

**Com  — Papatheodorou_2025: Desenvolver protocolo de revogação off‑chain com atualização de status via eventos de cont**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Desenvolver protocolo de revogação off‑chain com atualização de status via eventos de contrato inteligente

[Proposta completa no relatório](../RELATORIO.md)

### Fichamento

Base: pdf; 16/16 trechos. Páginas sem texto extraível: []. Figuras e tabelas podem exigir conferência humana.

#### Página 1 — ficha a539adb6247c318d5314

O artigo apresenta o YouGovern, um sistema SSI baseado em blockchain (Binance Smart Chain) que segue os padrões W3C DID, usando contratos inteligentes para controle de acesso e armazenamento descentralizado via IPFS e Web3.Storage. O sistema permite registro, compartilhamento e revogação de identidades com privacidade e auditabilidade, suportando permissões baseadas em papéis e rotação de chaves. Avaliações de desempenho mostram latência média de registro de 0,94 s e pico de 12,5 transações por segundo, destacando melhorias em revogação e custos operacionais em relação a soluções como Sovrin e uPort.

- O controle centralizado permite que entidades modifiquem ou revoguem privilégios de identidade sem consentimento, gerando riscos de privacidade. — citação conferida: centralized control also means that these entities have the power to modify, revoke, or misuse identity privileges, often without the user’s consent or knowledge, posing significant risks to privacy and autonomy

- YouGovern apresenta latência de registro de DID de 0,94 s e taxa máxima de 12,5 transações por segundo. — citação conferida: Results indicate an average DID registration latency of 0.94 s and a peak throughput of 12.5 transactions per second.

Interpretação: O trabalho demonstra que uma arquitetura SSI baseada em BSC pode oferecer registro rápido e throughput adequado para aplicações de cidades inteligentes, ao mesmo tempo que melhora a revogação e reduz custos operacionais em comparação com soluções existentes.

Dúvidas: Como o sistema se comporta em cenários de alta concorrência realista? Qual o impacto da dependência de serviços externos como Web3.Storage na disponibilidade e soberania dos dados?

#### Página 2 — ficha d1741ae45168524d94a2

O trecho discute os riscos da centralização da web, como censura e bloqueios governamentais, e destaca a crescente demanda por privacidade. Apresenta a Self‑Sovereign Identity (SSI) como identidade distribuída, independente de autoridade central, e descreve como a blockchain pode ampliar o controle do usuário sobre identificadores e dados. Também menciona a possibilidade de integrar SSI a sistemas oficiais como eID, eIDAS e ePassport, apontando desafios de adoção em soluções baseadas em blockchain.

Interpretação: O texto reforça a necessidade de modelos descentralizados como SSI para mitigar riscos de censura e controle centralizado, apontando ainda para a integração com identidades oficiais.

Dúvidas: Como o YouGovern lida com revogação de credenciais? Qual o impacto de usar a Binance Smart Chain em ambientes de cidades inteligentes com restrições de latência?

#### Página 3 — ficha 774154c2c04bbfd4c100

O trecho descreve que o problema central é a ausência de sistemas de identidade controlados pelo usuário, escaláveis, econômicos e compatíveis com infraestruturas descentralizadas, e propõe projetar, implementar e avaliar um SSI descentralizado que suporte credenciais verificáveis, controle de acesso com preservação de privacidade e interoperabilidade baseada em padrões.

- The central problem addressed by this work is the lack of user-controlled identity systems that are scalable, cost-effective, and compatible with decentralized infrastructure. — citação conferida: The central problem addressed by this work is the lack of user-controlled identity systems that are scalable, cost-effective, and compatible with decentralized infrastructure.

- This paper aims to design, implement, and evaluate a decentralized self-sovereign identity system that supports verifiable credentials, privacy-preserving access control, and standards-based interoperability. — citação conferida: This paper aims to design, implement, and evaluate a decentralized self-sovereign identity system that supports verifiable credentials, privacy-preserving access control, and standards-based interoperability.

Interpretação: O autor enfatiza a evolução dos modelos de identidade, culminando em SSI baseado em blockchain como solução para eliminar autoridades centralizadas, melhorar privacidade e garantir integridade via criptografia de chave pública. O foco está em criar um sistema que seja ao mesmo tempo descentralizado, interoperável e capaz de suportar credenciais verificáveis, atendendo a requisitos de cidades inteligentes.

Dúvidas: • Quais mecanismos de revogação de credenciais são propostos ou planejados?
• Como a solução lida com a descoberta (discoverability) de DIDs em ambientes heterogêneos?
• Há avaliação de custos operacionais (gas fees) na Binance Smart Chain?
• O trabalho contempla testes de interoperabilidade com padrões governamentais (eIDAS, ePassport)?
• Qual é a estratégia para garantir a escalabilidade em cenários de alta densidade de dispositivos IoT?

#### Página 4 — ficha a83782b652687938c8ae

O artigo apresenta o YouGovern, um protótipo de SSI baseado na Binance Smart Chain que integra DIDs, contratos inteligentes e armazenamento descentralizado (IPFS/Web3.Storage). O objetivo é demonstrar que um framework SSI totalmente descentralizado pode operar em uma blockchain semi‑descentralizada, mantendo custos baixos e aderindo às especificações W3C, sem introduzir novos algoritmos criptográficos.

Interpretação: O trabalho demonstra a viabilidade prática de um SSI totalmente descentralizado usando BSC, priorizando interoperabilidade e usabilidade sem propor inovações criptográficas, o que o posiciona como um ponto de partida para aplicações governamentais e civis.

Dúvidas: Quais são os impactos de usar BSC em termos de soberania de dados comparado a blockchains públicas mais descentralizadas? Como a solução lida com a revogação de credenciais em tempo real? Há avaliação de custos operacionais em cenários de grande escala (milhares de usuários).

#### Página 5 — ficha 923ed73b629f6f49d9d7

O trecho descreve a abordagem distribuída baseada em blockchain para SSI, destacando que os dados não ficam em servidor central, mas são armazenados em um ledger público e distribuído entre nós que atuam como servidores. Cada nó verifica transações, garantindo integridade e imutabilidade, o que confere confiança ao registro de credenciais. O texto enfatiza que a blockchain funciona simultaneamente como rede e banco de dados, facilitando a construção de aplicações SSI descentralizadas, exemplificando com a Binance Smart Chain (BSC).

- Blockchain provides a decentralized storage and network for SSI applications. — citação conferida: Blockchain solves these issues, and it is a safer option to create an SSI identity application

- All nodes on the blockchain act simultaneously to ensure the security of the public ledger data. — citação conferida: both the network nodes act simultaneously to ensure the security of all public ledger data

Interpretação: O autor argumenta que a natureza distribuída e imutável da blockchain elimina a dependência de servidores centrais, aumentando a confiança e a segurança nas transações de identidade, o que é particularmente relevante para ambientes de cidades inteligentes onde a disponibilidade e a integridade dos dados são críticas.

Dúvidas: Como a solução lida com a revogação de credenciais em um ledger imutável? Qual o custo energético da BSC comparado a outras plataformas em cenários de grande volume de transações IoT?

#### Página 6 — ficha 20dc2e00021188b98e4e

O trecho descreve o uso de contratos inteligentes na Binance Smart Chain (BSC) escritos em Solidity, que hospedam a lógica de negócios da aplicação YouGovern, permitindo a leitura/escrita de dados e a execução automática de acordos sem intermediários. São apresentados exemplos de aplicação em compra de carro, apostas e aluguel, ilustrando como os contratos garantem cumprimento de condições pré‑definidas, reduzindo custos e necessidade de terceiros.

- Smart contracts are written in the BSC and coded with a specific programming language known as Solidity — citação conferida: Smart contracts are written in the BSC and coded with a specific programming language known as Solidity [33].

- Smart contracts are like a web-based microservice — citação conferida: A smart contract is like a web-based microservice.

Interpretação: O texto enfatiza que a lógica de negócios da solução SSI YouGovern está encapsulada em contratos inteligentes na BSC, usando Solidity para automatizar acordos e controle de acesso, eliminando a necessidade de intermediários e reduzindo custos operacionais.

Dúvidas: Como a latência dos contratos na BSC impacta aplicações de tempo‑crítico em IoT? Qual o custo de gas para operações frequentes de registro e revogação de credenciais? Existem mecanismos de fallback caso o contrato falhe ou seja comprometido?

#### Página 7 — ficha c0b45c04f7729b48dcfd

O trecho descreve duas categorias de contas na Binance Smart Chain (BSC): Externally Owned Accounts (EOAs), que são contas de usuário associadas a um par de chaves criptográficas e identificadas por um endereço de carteira, e Contract Accounts, que são contratos inteligentes controlados por EOAs e executados pela EVM. Explica ainda que aplicações descentralizadas (dApps) utilizam esses contratos para compartilhar dados em redes P2P, permitindo que usuários atualizem informações pessoais sem servidores centralizados, e contextualiza a importância da identidade digital em plataformas digitais.

- Externally Owned Accounts (EOAs) are considered user-type accounts (for users) and are linked to a cryptographic key pair created upon account creation. — citação conferida: Externally Owned Accounts (EOAs) are considered user-type accounts (for users) and are linked to a cryptographic key pair created upon account creation.

- A smart contract is a kind of account that is controlled and operated by an EOA. — citação conferida: A smart contract is a kind of account that is controlled and operated by an EOA.

Interpretação: O texto esclarece a arquitetura de contas na BSC, distinguindo entre contas de usuário (EOAs) que detêm chaves privadas e contratos inteligentes que executam lógica de negócio. Essa separação permite que dApps operem de forma descentralizada, usando EOAs para autorizar transações e contratos para gerenciar identidade e controle de acesso, o que é relevante para soluções de SSI em cidades inteligentes.

Dúvidas: Como garantir a proteção da chave privada das EOAs em dispositivos IoT com recursos limitados? Qual o impacto de usar BSC, com seu modelo de consenso, na latência de autenticação em cenários de edge computing?

#### Página 8 — ficha 7f43233eae4de9168f4a

O trecho descreve que as estruturas SSI atuais carecem de mediador, operando apenas em arranjos pessoa‑a‑pessoa, e compara duas soluções – uPort (BSC) e Sovrin (Hyperledger Indy) – detalhando armazenamento de identidade, recuperação social, custos, segurança, privacidade e acessibilidade.

- uPort has been built on the BSC public blockchain without authorization. — citação conferida: uPort has been built on the BSC public blockchain without authorization

Interpretação: O texto evidencia que, embora existam soluções SSI baseadas em blockchain (uPort, Sovrin), ainda há lacunas em termos de mediação, gerenciamento de agentes/guardians e custos operacionais, o que abre espaço para pesquisas que integrem essas tecnologias a contextos de cidades inteligentes e IoT.

Dúvidas: Como a ausência de um mediador afeta a segurança e a privacidade em ambientes de IoT críticos? Quais são os impactos de usar BSC versus Hyperledger Indy em termos de latência e custo para dispositivos de borda?

#### Página 9 — ficha 92ae5546348ab727de60

O artigo compara uPort e Sovrin quanto à disponibilidade, transparência, portabilidade, interoperabilidade e escalabilidade, apontando limitações de escalabilidade nas blockchains públicas (≈15 tps) e a necessidade de mediadores. Introduz o esquema DNS‑IdM, que usa contratos inteligentes para gerenciar identidades de forma descentralizada, oferecendo proteção de privacidade e evitando ameaças tradicionais. Destaca ainda os princípios de SSI de Allen e a classificação da Sovrin Foundation, ressaltando questões como controle, consentimento e direito ao esquecimento.

- Scalability is limited. The public Ethereum blockchain elaborates around 15 transactions per second. — citação conferida: Scalability is limited. The public Ethereum blockchain elaborates around 15 transactions per second.

Interpretação: O trabalho evidencia que, apesar dos avanços de uPort e Sovrin, ainda há lacunas críticas em escalabilidade e na presença de um agente mediador, o que compromete a interoperabilidade em ambientes de cidades inteligentes. O esquema DNS‑IdM surge como uma proposta alternativa que combina contratos inteligentes e um modelo de identidade semelhante ao DNS, potencialmente mitigando algumas dessas limitações.

Dúvidas: Como o DNS‑IdM se comporta em termos de latência e throughput comparado ao uPort em redes de edge computing? Quais são os requisitos de segurança para um agente mediador leve que possa operar entre dispositivos IoT e as blockchains públicas?

#### Página 10 — ficha c9b29da43ee2c6dc7851

O trecho descreve como o DNS‑IdM permite que clientes controlem seus atributos de identidade e como o YouGovern propõe um SSI modular, de baixo custo e com controle de acesso usando BSC, contratos inteligentes baseados em papéis e armazenamento híbrido, apontando limitações de soluções existentes como uPort, Sovrin e Microsoft ION.

- DNS‑IdM gives clients the ability to control their identification details. — citação conferida: DNS–IdM gives clients the ability to control their identification details.

Interpretação: O texto enfatiza que, embora existam soluções SSI como uPort, Sovrin e ION, elas ainda carecem de revogação, controle de acesso granular e integração com sistemas de armazenamento descentralizado. O YouGovern surge como proposta que combina blockchain BSC, contratos inteligentes baseados em papéis e armazenamento híbrido para suprir essas lacunas, e sugere ainda que tecnologias emergentes como SBC podem ser incorporadas para ambientes de IoT de baixa potência.

Dúvidas: Como o YouGovern implementa a revogação de credenciais? Qual é o overhead de usar armazenamento híbrido (on‑chain + IPFS) em termos de latência e custo? De que forma o consenso SBC pode ser integrado ao protocolo SSI proposto? Existem métricas de escalabilidade para milhares de dispositivos edge?

#### Página 11 — ficha f948153867c936b8c019

O trecho descreve o modelo de caso de uso do YouGovern, onde o usuário entra com MetaMask, registra seu endereço na blockchain, carrega arquivos no IPFS e armazena o hash no contrato inteligente. Outros usuários podem solicitar acesso ao arquivo via transação; o proprietário aprova ou rejeita e, se aprovado, o solicitante baixa o dado.

- User signs in or signs up with his MetaMask account, and his address is recorded in the blockchain — citação conferida: A user first signs in or signs up with his MetaMask account, and his address is recorded in the blockchain

- The hash of the uploaded file is stored in a smart contract and other users can request access via a transaction — citação conferida: There is also an option to upload a file to IPFS, in which the hash of the file is internally stored in a smart contract. Now, other users can send a request to see that data by sending a request transaction from a function.

Interpretação: O modelo de caso de uso demonstra como o YouGovern implementa controle de acesso descentralizado a dados pessoais armazenados em IPFS, usando solicitações de transação para aprovação pelo proprietário, reforçando a proposta de identidade auto‑soberana e gerenciamento de permissões na blockchain.

Dúvidas: Como o sistema revoga acessos concedidos após mudanças de endereço ou políticas? Qual o impacto de múltiplas solicitações simultâneas no desempenho medido (12,5 tps)? Existe suporte para agentes/guardians no fluxo de consentimento descrito?

#### Página 12 — ficha 1030c744b85cd2c56cec

O trecho descreve os casos de uso essenciais do YouGovern, onde usuários se cadastram via MetaMask, armazenam dados na blockchain e no IPFS, e podem conceder ou revogar acesso a outros usuários por meio de contratos inteligentes. Autoridades verificam credenciais consultando o registro DID e o hash de conteúdo no IPFS. O fluxo inclui solicitação, aprovação/rejeição e download de arquivos, com papéis de autoridade definidos por endereços confiáveis.

- Usuários podem solicitar ver os dados de outro usuário — citação conferida: Users can request to see another user data

- O proprietário dos dados pode aceitar ou rejeitar a solicitação — citação conferida: he can accept or reject that request

Interpretação: O sistema YouGovern combina identidade auto-soberana com controle de acesso granular, permitindo que usuários gerenciem quem pode visualizar ou baixar seus dados armazenados de forma descentralizada, enquanto autoridades confiáveis validam credenciais via DID e IPFS.

Dúvidas: Como o modelo de autoridade baseado em endereços verificados lida com a delegação de confiança entre diferentes entidades governamentais? Qual o impacto de múltiplas solicitações concorrentes no desempenho do armazenamento híbrido?

#### Página 13 — ficha 232d5732acb7bfb458f2

O YouGovern foi implementado na Binance Smart Chain usando contratos inteligentes, registro de DIDs, armazenamento descentralizado via IPFS/Web3.Storage e interface web com MetaMask; as interações são expostas por API RESTful e o ambiente de desenvolvimento inclui Truffle Suite, Solidity e Node.js.

- User interactions—such as identity registration, credential issuance, or access revocation—are initiated from the browser interface and signed via MetaMask. — citação conferida: User interactions—such as identity registration, credential issuance, or access revocation—are initiated from the browser interface and signed via MetaMask.

Interpretação: O trecho detalha a arquitetura e o ambiente de desenvolvimento do YouGovern, evidenciando a combinação de armazenamento on‑chain e off‑chain e a exposição de APIs RESTful para gerenciamento de DIDs.

Dúvidas: Como são garantidas as propriedades de privacidade dos dados armazenados no IPFS? Qual o impacto de usar Ganache para simular condições de rede na avaliação de desempenho real? Existe suporte a múltiplas cadeias além da BSC?

#### Página 14 — ficha 19ac43dabd82bc557a83

O trecho descreve a implementação da interface do YouGovern, destacando o uso de React.js, integração com MetaMask e armazenamento descentralizado via IPFS. Detalha a implantação de smart contracts na BSC, com definição de papéis e permissões usando OpenZeppelin para controle de acesso baseado em funções, e otimizações para reduzir custos de gas. A UI visa ser intuitiva, permitindo que usuários gerenciem identidades sem depender de servidores terceiros, reforçando privacidade e controle de dados.

Interpretação: A implementação enfatiza a descentralização tanto na camada de identidade (via blockchain) quanto na de armazenamento (via IPFS), reforçando a privacidade do usuário e reduzindo dependência de infraestruturas centralizadas, ao mesmo tempo que adota boas práticas de segurança com OpenZeppelin e MetaMask.

Dúvidas: Como a integração com IPFS afeta o tempo de resposta das operações de identidade? Qual o custo de gas ao escalar o número de papéis e permissões definidas nos contratos? Existe plano para suportar revogação automática de credenciais sem agentes externos?

#### Página 15 — ficha 53d9d1b98e4a08aebbfb

O trecho descreve como o YouGovern combina IPFS com Web3.Storage (Filecoin) para garantir persistência dos dados de identidade, inclui testes automatizados e auditorias de segurança dos contratos inteligentes, e implementa revogação, rotação de chaves e controle de acesso via funções de smart contract protegidas por OpenZeppelin ReentrancyGuard.

- The platform provides revocation and key rotation mechanisms compliant with the W3C DID specification. — citação conferida: To comply with the W3C DID specification, YouGovern includes mechanisms for revocation and key rotation.

Interpretação: O texto evidencia que o YouGovern reforça a disponibilidade dos dados de identidade ao adotar armazenamento híbrido e consolida a segurança ao empregar testes automatizados, auditorias e proteções contra reentrância, além de oferecer funcionalidades de revogação e controle de acesso diretamente nos contratos inteligentes.

Dúvidas: Não há detalhes sobre o desempenho do acesso a credenciais após a integração com Web3.Storage nem sobre a escalabilidade das funções de controle de acesso em cenários de alta concorrência.

#### Página 16 — ficha fdc2a995058cf670f6bf

O trecho apresenta trechos de código que implementam revogação de DIDs, rotação de chaves e controle de acesso no sistema YouGovern, descreve seu deployment na Binance Smart Chain e a integração com IPFS para armazenamento de dados, além de mencionar monitoramento contínuo de desempenho e segurança.

- O sistema inclui função para revogar DIDs e rotacionar chaves. — citação conferida: function revokeDID(address user) public onlyOwner { didRecords[user].active = false; emit DIDRevoked(user); }

- O controle de acesso é gerenciado por um mapeamento de permissões entre usuários e verificadores. — citação conferida: mapping(address => mapping(address => bool)) public accessPermissions; function grantAccess(address verifier) public { accessPermissions[msg.sender][verifier] = true; emit AccessGranted(msg.sender, verifier); }

Interpretação: O trecho demonstra que o YouGovern já incorpora mecanismos de revogação de identidade e controle de acesso simples via smart contracts, reforçando a proposta de SSI baseada em blockchain e indicando que a infraestrutura está pronta para extensões de segurança avançada.

Dúvidas: Como a revogação de DIDs impacta a latência e o custo de transação em cenários de alta frequência? Qual a estratégia de recuperação de credenciais caso o agente/guardian ainda não esteja implementado?

<!-- agente:fim -->
