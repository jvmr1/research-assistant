---
nome_local: Tawfik_2025
openalex_id: https://openalex.org/W4413329862
doi: https://doi.org/10.1007/s10586-025-05308-x
ano: 2025
status: triagem_pendente
acesso_aberto: true
pdf_local: obsidian/referencias/pdfs/Tawfik_2025.pdf
tags: [blockchain, cidades-inteligentes, contratos-inteligentes, controle-de-acesso, iot, privacidade]
---
# Tawfik_2025

## Tags

#blockchain #cidades-inteligentes #contratos-inteligentes #controle-de-acesso #iot #privacidade
<!-- agente:inicio -->

## Leitura e relações atualizadas pelo agente

Fonte: https://doi.org/10.1007/s10586-025-05308-x

Triagem: revisar. O artigo aborda controle de acesso baseado em blockchain e preservação de privacidade, tópicos centrais para o grupo de pesquisa. Contudo, o domínio de aplicação é saúde (EHR), não cidades inteligentes ou IoT industrial, que são o foco principal da revisão. Ainda assim, a análise de arquiteturas permissionadas vs. permissionless, uso de smart contracts para autenticação e controle de acesso, e a discussão de técnicas criptográficas de privacidade podem oferecer insights metodológicos e arquiteturais úteis para adaptar soluções a ambientes de smart cities e IoT. Por isso, recomenda‑se revisar o trabalho para extrair possíveis abordagens transferíveis, mas não priorizá‑lo como fonte principal.

[PDF local](../../obsidian/referencias/pdfs/Tawfik_2025.pdf)

### Relações bibliográficas verificadas nos metadados

Referencia: nenhum trabalho do acervo identificado.

É citado por: nenhum trabalho do acervo identificado.

### Como se correlaciona com os demais na análise

**Com  — Tawfik_2025: Desenvolver benchmark experimental que mensure latência, throughput e consumo energético d**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Desenvolver benchmark experimental que mensure latência, throughput e consumo energético de contratos inteligentes em blockchains permissioned e permissionless para EHR.

[Proposta completa no relatório](../RELATORIO.md)

**Com  — Tawfik_2025: Criar um conjunto de métricas padronizadas (ex**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Criar um conjunto de métricas padronizadas (ex.: tempo de revogação, índice de privacidade, overhead de interoperabilidade) aplicáveis a soluções de controle de acesso.

[Proposta completa no relatório](../RELATORIO.md)

**Com  — Tawfik_2025: Elaborar um framework comparativo que avalie simultaneamente privacidade e segurança, inte**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Elaborar um framework comparativo que avalie simultaneamente privacidade e segurança, integrando análises de criptografia, accounting e compliance regulatório.

[Proposta completa no relatório](../RELATORIO.md)

### Fichamento

Base: pdf; 16/16 trechos. Páginas sem texto extraível: []. Figuras e tabelas podem exigir conferência humana.

#### Página 1 — ficha 731872fe2d0aa6d0a3c9

O artigo apresenta um levantamento abrangente sobre controle de acesso baseado em blockchain para registros eletrônicos de saúde (EHR), destacando que sistemas de e‑health tradicionais apresentam riscos de privacidade como acessos não autorizados. Propõe a integração de blockchain com técnicas de preservação de privacidade e contratos inteligentes para melhorar transparência, integridade e disponibilidade, além de automatizar autenticação e controle de acesso. A revisão inclui 45 trabalhos selecionados, analisa plataformas, protocolos de consenso e técnicas criptográficas, e discute estudos de caso reais, apontando desafios e direções futuras.

Interpretação: O estudo demonstra que a combinação de blockchain com técnicas criptográficas pode mitigar os principais riscos de privacidade nos sistemas de saúde eletrônicos, oferecendo um caminho promissor para controle de acesso automatizado e auditável.

Dúvidas: Quais são as limitações práticas de escalabilidade e latência ao aplicar contratos inteligentes em ambientes de saúde com alta taxa de transações? Como os requisitos regulatórios (ex.: GDPR, HIPAA) influenciam a escolha de plataformas permissionadas versus permissionless?

#### Página 2 — ficha 178303345bbd3bb29308

O texto descreve a transição dos sistemas de saúde tradicionais para e‑health, destacando a importância dos registros eletrônicos (EHR) e os desafios de interoperabilidade e privacidade. Aponta incidentes de vazamento de dados e apresenta o blockchain como solução potencial para controle de acesso, oferecendo transparência, descentralização e resistência a adulterações, especialmente em ambientes permissioned.

- privacy is a major concern in shared environments — citação conferida: Privacy is a major concern in shared environments and must be carefully considered.

- blockchain can play a key role in access control — citação conferida: Blockchain technology can play a key role in access control by recording and verifying access-related information through a decentralized ledger.

Interpretação: O trecho reforça que, apesar dos benefícios dos EHRs, a falta de padrões comuns e as ameaças à privacidade limitam sua adoção, e que o blockchain surge como infraestrutura promissora para garantir controle de acesso auditável e resistente a falhas centralizadas.

Dúvidas: Quais são os custos de desempenho e consumo de energia ao empregar blockchains permissioned em ambientes de edge computing? Como garantir a escalabilidade do registro de auditoria de acesso em redes de grande porte?

#### Página 3 — ficha 15878b05c8879d1ac8ee

O trecho descreve a importância de contabilizar atividades de usuários em sistemas de saúde para auditoria e conformidade, destacando que autenticação, autorização e accounting são essenciais para controle de acesso a prontuários eletrônicos. A pesquisa classifica métodos de controle de acesso baseados em blockchain em permissivos e permissionados, analisa técnicas de privacidade, plataformas, protocolos de consenso e contratos inteligentes, e aponta desafios de privacidade e direções futuras.

- Accounting involves tracking and logging user activity within the healthcare system, including who accessed patient data, when it was accessed, and what actions were taken. — citação conferida: Accounting: Accounting involves tracking and logging user activity within the healthcare system, including who accessed patient data, when it was accessed, and what actions were taken.

- The survey categorizes recent EHR access control methods based on blockchain into two categories: permissionless and permissioned. — citação conferida: The survey’s main contributions are: 1. The categorization of recent EHR access control methods based on blockchain into two categories: permissionless and permissioned.

Interpretação: O documento enfatiza que, além da criptografia, a rastreabilidade (accounting) é crucial para garantir a conformidade e a confiança nos sistemas de saúde baseados em blockchain, oferecendo um panorama estruturado das soluções existentes.

Dúvidas: Quais são as métricas específicas usadas para avaliar a escalabilidade e a revogabilidade nas soluções de controle de acesso apresentadas? Como os métodos de accounting podem ser adaptados para dispositivos de IoT com recursos limitados em ambientes de smart city?

#### Página 4 — ficha 2a14312fc2791ef41be4

O trecho revisa diversas pesquisas sobre o uso de blockchain em sistemas de saúde, destacando requisitos, aplicações, limitações e direções futuras. Evidenciam-se desafios de interoperabilidade, segurança, privacidade, escalabilidade e consumo de energia, bem como o potencial da blockchain para melhorar a proteção de dados sensíveis por meio de gerenciamento descentralizado e mecanismos de criptografia robustos.

Interpretação: O texto indica que, embora haja um crescente número de estudos sobre blockchain na saúde, ainda persistem lacunas críticas relacionadas à interoperabilidade, privacidade e eficiência, sugerindo a necessidade de pesquisas que adaptem essas soluções ao contexto de cidades inteligentes e IoT.

Dúvidas: Quais métricas específicas de privacidade foram propostas nos trabalhos citados? Como os autores avaliam a viabilidade prática das soluções de blockchain em ambientes de saúde reais? Há evidências empíricas de implementação em larga escala?

#### Página 5 — ficha d62d99f39b030d90c814

O artigo apresenta uma revisão sistemática de trabalhos que utilizam blockchain para controle de acesso e preservação de privacidade em saúde, categorizando métodos em blockchains permissionless e permissioned, avaliando fatores críticos de privacidade e segurança, e apontando a falta de comparações holísticas como lacuna que preenchem.

- O estudo categoriza métodos de controle de acesso em blockchains permissionless e permissioned. — citação conferida: we systematically categorize access control methods into permissionless and permissioned blockchains

Interpretação: O trabalho destaca que, apesar do crescente interesse em blockchain para saúde, ainda há ausência de análises comparativas abrangentes que considerem simultaneamente privacidade e segurança, e preenche essa lacuna ao oferecer uma taxonomia detalhada dos métodos de controle de acesso.

Dúvidas: Quais critérios específicos foram usados para avaliar os fatores críticos de privacidade e segurança? Como a revisão trata a escalabilidade e consumo de energia dos diferentes tipos de blockchain? Há evidências empíricas que sustentem a eficácia das soluções propostas?

#### Página 6 — ficha 993a27f7c6b13a9cfd37

A Tabela 1 apresenta uma comparação entre o presente levantamento e demais surveys na área de saúde, listando autores, ano de publicação, principais contribuições (frameworks EHR, tipos de blockchain, protocolos de consenso, técnicas de privacidade, controle de acesso) e o período coberto por cada estudo, evidenciando a abrangência e as lacunas abordadas pelo trabalho em relação a revisões anteriores de 2019 a 2024.

- Table 1 A comparison between this survey and other surveys in the healthcare domain — citação conferida: Table 1 A comparison between this survey and other surveys in the healthcare domain

- Review of blockchain applications in healthcare, focusing on blockchain interoperability and security solutions — citação conferida: Review blockchain applications in healthcare, focusing on blockchain interoperability and security solutions

Interpretação: A tabela demonstra que o estudo atual amplia o escopo das revisões anteriores ao combinar múltiplas dimensões (tipos de blockchain, consenso, privacidade, controle de acesso) e ao cobrir um período mais recente, indicando uma visão mais integrada das soluções de blockchain para saúde.

Dúvidas: Quais critérios específicos foram usados para classificar os tipos de blockchain e as técnicas de privacidade nos surveys comparados? Como o presente survey trata de questões de escalabilidade e consumo de energia em relação aos trabalhos listados?

#### Página 7 — ficha 09da3e158d7cbf0dc2c4

O trecho descreve como funções de hash e assinaturas digitais garantem a integridade e a segurança dos blocos em uma blockchain, destacando a dificuldade de modificar blocos devido ao encadeamento de hashes e às propriedades de resistência a ataques, além de mencionar variações de tamanho de bloco entre diferentes implementações.

- Funções de hash garantem a integridade dos dados no bloco. — citação conferida: Any modification to the data within a block results in a different hash value, immediately signaling tampering.

Interpretação: O trecho reforça que a segurança de blockchains depende fortemente de mecanismos criptográficos como hash e assinaturas digitais, o que é crucial para garantir a integridade e a resistência a ataques em sistemas de controle de acesso distribuídos.

Dúvidas: Como as limitações de tamanho de bloco impactam a performance de redes IoT de borda em cidades inteligentes? De que forma diferentes protocolos de consenso influenciam a privacidade dos dados compartilhados?

#### Página 8 — ficha 2edee90eeafd3c049d27

O trecho descreve a estrutura de blocos, o papel dos nós e os mecanismos criptográficos que garantem a integridade e a resistência a adulterações em blockchains. Apresenta a arquitetura descentralizada, a ausência de ponto único de falha e a classificação das redes em permissionless (públicas) e permissioned (privadas ou consórcio), destacando que blockchains públicas oferecem alta descentralização, porém enfrentam desafios de escalabilidade e privacidade.

- A blockchain is secured using a combination of hashing and, in many implementations, digital signatures. — citação conferida: A block is secured using a combination of hashing and, in many implementations, digital signatures [ 32].

Interpretação: O texto reforça que a segurança das blockchains provém de técnicas criptográficas e da replicação distribuída, e que a escolha entre redes permissionless e permissioned influencia diretamente questões de privacidade, escalabilidade e controle de acesso, aspectos críticos para aplicações em saúde e cidades inteligentes.

Dúvidas: Quais são os requisitos de desempenho específicos (latência, throughput) para blockchains permissioned em ambientes de IoT de borda? Como integrar de forma prática SSI e ABE em blockchains existentes sem comprometer a eficiência?

#### Página 9 — ficha 44ca747a234ee9a11aa2

O trecho descreve os diferentes tipos de blockchain (públicas, privadas e consórcios), destacando que blockchains de consórcio são permissionadas e governadas por múltiplas organizações. Apresenta ainda os elementos-chave da tecnologia, como transparência, integridade e uso de Merkle trees, e compara características como identidade dos participantes, necessidade de autenticação e throughput.

- Transparency is one of the main advantages of blockchain, particularly in applications that require trust and accountability. — citação conferida: Transparency is one of the main advantages of blockchain, particularly in applications that require trust and accountability.

Interpretação: O texto enfatiza que a escolha entre blockchains públicas, privadas ou de consórcio impacta diretamente aspectos críticos como privacidade, escalabilidade e segurança, sendo essencial para setores sensíveis como saúde e cidades inteligentes.

Dúvidas: Como garantir a privacidade dos dados sensíveis em blockchains de consórcio sem sacrificar a transparência? Qual o custo de desempenho ao integrar ABE em blockchains permissioned para controle de acesso granular?

#### Página 10 — ficha 20d10b3f17b2af1b3918

O texto descreve o uso de árvores de Merkle para verificação eficiente de transações, a disponibilidade proporcionada pela descentralização da blockchain que elimina pontos únicos de falha, e o papel dos contratos inteligentes na automação de controle de acesso e proteção de privacidade em sistemas de saúde.

- Merkle trees enable efficient and secure verification of individual transactions. — citação conferida: Merkle trees enable efﬁcient and secure veriﬁcation of individual transactions.

Interpretação: O trecho destaca como estruturas de Merkle e contratos inteligentes podem suprir a necessidade de integridade, disponibilidade e controle de acesso em ambientes de saúde distribuídos, reforçando a proposta de usar blockchain para garantir segurança e privacidade.

Dúvidas: Como garantir a privacidade dos dados de saúde ao usar provas de Merkle públicas? Qual o overhead de desempenho ao integrar contratos inteligentes com ABE para controle de acesso granular?

#### Página 11 — ficha 304dd68ee204ebbf7aff

O trecho descreve como contratos inteligentes permitem codificar políticas de controle de acesso, registrar auditorias e garantir integridade e transparência em blockchains públicas como Ethereum e Hyperledger. Também apresenta os protocolos de consenso (PoW e PoS), destacando a alta segurança e descentralização do PoW, mas apontando seu alto consumo de energia e limitada escalabilidade.

- Smart contracts can be used to implement blockchain-based systems for access control. — citação conferida: Rules can be encoded to enforce specific access control policies using smart contracts for different users or groups.

- Proof of Work (PoW) offers decentralization and high security, but its primary drawback is the substantial amount of power required for mining blocks and its limited scalability. — citação conferida: its primary drawback is the substantial amount of power required for mining blocks and its limited scalability.

Interpretação: O texto evidencia que contratos inteligentes são instrumentos chave para automatizar políticas de acesso e gerar trilhas de auditoria, ao mesmo tempo que a escolha do protocolo de consenso impacta diretamente a viabilidade de implantação em cenários de IoT e cidades inteligentes devido a questões de energia e escalabilidade.

Dúvidas: Como garantir a privacidade dos dados de saúde ao usar contratos inteligentes públicos? Qual é o custo operacional de migrar de PoW para PoS em redes de saúde distribuídas? Como integrar SSI de forma padronizada com diferentes plataformas de blockchain (Ethereum, Hyperledger) em ambientes de smart city?

#### Página 12 — ficha 713de1b7659a294885e0

O trecho descreve diversos protocolos de consenso blockchain (PoS, DPoS, PoAc, PBFT, DBFT, PoA, PoET, PoV, PoC), destacando suas vantagens como alta taxa de transferência, eficiência energética e escalabilidade, bem como limitações como consumo de energia, risco de centralização e necessidade de hardware especializado. Cada mecanismo apresenta trade‑offs entre desempenho, segurança e descentralização, relevantes para aplicações distribuídas em IoT e cidades inteligentes.

- PoS provides a fast block creation time, high throughput, independence from specialized hardware, and energy efficiency. — citação conferida: PoS provides a fast block creation time, high throughput, independence from specialized hardware, and energy efﬁciency.

- PoA is suitable for distributed applications because it does not require high power consumption, generates blocks at predetermined intervals for increased transaction rates, and offers better scalability. — citação conferida: PoA is suitable for distributed applications because it does not require high power consumption, generates blocks at predetermined intervals for increased transaction rates, and offers better scalability.

Interpretação: O texto evidencia que a escolha do mecanismo de consenso deve equilibrar desempenho, consumo energético e grau de descentralização, aspectos críticos para garantir segurança e eficiência em infraestruturas de IoT e smart cities.

Dúvidas: Qual o impacto prático da centralização parcial em DPoS e DBFT em ambientes de cidades inteligentes? Como o custo de hardware especializado exigido por PoET afeta sua viabilidade em dispositivos de borda?

#### Página 13 — ficha 726e8cb5353080b1a7c5

O trecho discute a preservação de privacidade, controle de acesso e buscas seguras em dados criptografados, destacando o protocolo Proof of Authentication (PoAh) como solução leve para dispositivos IoT de recursos limitados. Aponta vantagens de baixa energia e riscos de centralização, além de analisar a importância da escolha de plataformas blockchain (Bitcoin, Ethereum, Hyperledger, etc.) e de protocolos de consenso para atender a requisitos de escalabilidade, segurança e eficiência.

- Proof of Authentication (PoAh) is a lightweight blockchain authentication protocol for resource-constrained devices in IoT and edge computing. — citação conferida: Proof of Authentication (PoAh) [ 69] is a lightweight blockchain authentication protocol for resource-constrained devices in IoT and edge computing.

- Consensus protocols vary in performance efficiency, security guarantees, and levels of decentralization. — citação conferida: These protocols vary in performance efficiency, security guarantees, and levels of decentralization, as outlined in Table 3.

Interpretação: O texto enfatiza que, embora protocolos como PoAh ofereçam eficiência energética para IoT, a dependência de nós confiáveis introduz riscos de centralização, o que requer cuidadosa seleção de plataformas e consensos adequados ao contexto de cidades inteligentes.

Dúvidas: Como equilibrar a necessidade de baixa latência em edge computing com a mitigação de riscos de centralização? Quais métricas específicas de desempenho são mais críticas ao comparar PoAh com outros protocolos leves em ambientes de smart city?

#### Página 14 — ficha 3af7ccda92e4d3b48ecd

A Tabela 3 apresenta uma comparação de protocolos de consenso (PoW, PoS, DPoS, PoAc, PBFT, DBFT, PoA), indicando ano, tipo de blockchain, técnica de mineração, plataforma, grau de descentralização, throughput estimado, latência, consumo de energia, vantagens e desvantagens. Evidencia-se a variedade de trade‑offs entre segurança, desempenho e consumo energético, destacando limitações como alta energia ou risco de centralização.

- PoW tem alto consumo de energia. — citação conferida: High power consumption.

- PoS oferece alta taxa de transferência e eficiência energética. — citação conferida: High throughput. Energy efﬁciency.

Interpretação: O trecho evidencia que protocolos mais antigos como PoW sacrificam eficiência energética, enquanto protocolos mais recentes como PoS melhoram throughput e consumo, porém introduzem riscos de centralização.

Dúvidas: Como balancear a descentralização e a eficiência energética em redes de cidades inteligentes? Qual o impacto da latência reduzida de PBFT em aplicações de tempo‑crítico?

#### Página 15 — ficha 35f0219cbf71b4b1cc85

O trecho apresenta quatro protocolos de consenso (PoET, PoV, PoC e PoAh) detalhando ano, tipo de blockchain, plataforma, descentralização, taxa de transferência, latência, consumo de energia, vantagens e desvantagens. PoET oferece baixa energia, alta taxa e baixa latência, mas depende de hardware Intel, comprometendo a descentralização. PoV tem controle de votação, mas pode reduzir a descentralização e aumentar latência com mais nós. PoC garante privacidade na busca por palavras‑chave, porém não suporta buscas conjuntivas. PoAh consome pouca energia, adequado a dispositivos limitados, porém requer nós autenticadores que podem gerar tráfego adicional.

- PoET tem consumo de energia muito baixo. — citação conferida: Very Low

- PoAh consome muito pouca energia, sendo adequado para dispositivos com recursos limitados. — citação conferida: Consuming very little power. Suitable for devices with limited resources

Interpretação: Os protocolos analisados buscam equilibrar desempenho (throughput, latência) e eficiência energética, porém introduzem novos desafios de descentralização e complexidade de implementação, especialmente quando dependem de hardware especializado ou de autoridades de votação.

Dúvidas: Qual o impacto real da dependência de Intel SGX na descentralização de redes públicas de cidades inteligentes? Como a introdução de nós autenticadores no PoAh afeta a escalabilidade em grandes implantações de IoT?

#### Página 16 — ficha b6328a1cc2f36fb1b031

O trecho descreve como técnicas criptográficas avançadas, como Secure Multi‑Party Computation (SMPC) e Homomorphic Encryption, são integradas ao blockchain para melhorar controle de acesso, privacidade e segurança de registros eletrônicos de saúde. Apresenta definições, modelos de segurança, tipos de adversários e aplicações, destacando ainda as limitações de desempenho do SMPC.

- SMPC permite cálculo conjunto sem revelar entradas privadas. — citação conferida: SMPC enables computations over encrypted data without exposing individual inputs, making it ideal for privacy-preserving blockchain applications.

Interpretação: O texto enfatiza que, embora o blockchain ofereça transparência, a privacidade dos dados de saúde ainda depende de técnicas criptográficas avançadas. SMPC e homomorphic encryption são apresentadas como soluções promissoras, porém com custos de desempenho que precisam ser mitigados para adoção prática.

Dúvidas: Como reduzir a sobrecarga de comunicação do SMPC em dispositivos IoT limitados? Quais protocolos de consenso são mais compatíveis com SMPC em ambientes de edge computing? Existem implementações de homomorphic encryption otimizadas para sensores de baixa potência?

<!-- agente:fim -->
