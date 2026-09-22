---
nome_local: Asaithambi_2025
openalex_id: https://openalex.org/W4410037339
doi: https://doi.org/10.1038/s41598-025-00337-3
ano: 2025
status: triado_baixa
acesso_aberto: true
pdf_local: obsidian/referencias/pdfs/Asaithambi_2025.pdf
tags: [blockchain, contratos-inteligentes, controle-de-acesso, governanca-de-dados, interoperabilidade, iot, privacidade, sistemas-distribuidos]
---
# Asaithambi_2025

## Tags

#blockchain #contratos-inteligentes #controle-de-acesso #governanca-de-dados #interoperabilidade #iot #privacidade #sistemas-distribuidos
<!-- agente:inicio -->

## Leitura e relações atualizadas pelo agente

Fonte: https://doi.org/10.1038/s41598-025-00337-3

Triagem: baixa. O trabalho trata de uma arquitetura de computação de borda assistida por blockchain para o Industrial Internet of Things (IIoT), focando em autenticação de dispositivos, integridade de dados e eficiência de consenso (PoAh). Embora envolva IoT e blockchain, não aborda identidade autossoberana (SSI), credenciais verificáveis, controle de acesso baseado em atributos, criptografia homomórfica ou outros mecanismos de privacidade e interoperabilidade relevantes ao escopo da revisão (cidades inteligentes, serviços públicos digitais, ações de cidadãos ou entidades administrativas). Portanto, o artigo tem pouca relevância direta para o objetivo da pesquisa focada.

[PDF local](../../obsidian/referencias/pdfs/Asaithambi_2025.pdf)

### Relações bibliográficas verificadas nos metadados

Referencia: nenhum trabalho do acervo identificado.

É citado por: nenhum trabalho do acervo identificado.

### Como se correlaciona com os demais na análise

**Com  — Asaithambi_2025: Realizar experimentos de benchmark comparando PoAh com outros consensos leves (e**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Realizar experimentos de benchmark comparando PoAh com outros consensos leves (e.g., PoS, PBFT) em termos de latência, energia e consumo computacional.

[Proposta completa no relatório](../RELATORIO.md)

**Com  — Asaithambi_2025: Desenvolver módulo de revogação baseado em smart contracts que suporte atualização dinâmic**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Desenvolver módulo de revogação baseado em smart contracts que suporte atualização dinâmica de reputação e remoção de nós comprometidos, integrando credenciais verificáveis (SSI).

[Proposta completa no relatório](../RELATORIO.md)

**Com  — Asaithambi_2025: Integrar protocolos de identidade auto‑soberana (SSI) e verifiable credentials à camada de**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Integrar protocolos de identidade auto‑soberana (SSI) e verifiable credentials à camada de autenticação da arquitetura.

[Proposta completa no relatório](../RELATORIO.md)

### Fichamento

Base: pdf; 16/16 trechos. Páginas sem texto extraível: []. Figuras e tabelas podem exigir conferência humana.

#### Página 1 — ficha 458e1cc4f946bb50f100

O artigo propõe uma arquitetura de computação de borda assistida por blockchain para IIoT, introduzindo um mecanismo seguro de compartilhamento de dados e autenticação de ponta a ponta baseada na reputação da blockchain e contratos inteligentes. Um consenso de Prova de Autenticação (PoAh) é usado para validar nós e rastrear atividades, reduzindo o tempo de autenticação e aumentando a taxa de resposta, conforme estudo experimental.

- End-to-end authentication is developed based on the blockchain’s reputation — citação conferida: End-to-end authentication is developed based on the blockchain’s reputation

- the proposed architecture lowers the authentication time and obtains a high response rate — citação conferida: the proposed architecture lowers the authentication time and obtains a high response rate

Interpretação: O trabalho demonstra que combinar blockchain com computação de borda pode melhorar a segurança e a eficiência da autenticação em ambientes IIoT, oferecendo rastreabilidade e controle de acesso via contratos inteligentes.

Dúvidas: Quais são os custos computacionais e de energia do consenso PoAh em dispositivos de borda? Como a solução lida com revogação de credenciais ou nós comprometidos? Há avaliação de interoperabilidade com padrões de identidade digital existentes?

#### Página 2 — ficha 7a9f5dac96afa43d0dc9

O trecho descreve que o armazenamento centralizado de dados em IoT representa um grande obstáculo de segurança, favorecendo ataques. Propõe‑se usar edge computing para processar dados próximo à fonte, reduzindo latência e consumo de banda, e blockchain como ledger distribuído que garante integridade e transparência. Destaca‑se que edge computing melhora a resposta em tempo real e que blockchain oferece resistência a adulterações, sendo adequado a múltiplos setores, inclusive industrial.

- Centralized data storage is a big obstacle. — citação conferida: Centralized data storage is a big obstacle.

Interpretação: O texto enfatiza que a centralização dos dados em IoT aumenta vulnerabilidades e propõe a combinação de edge computing e blockchain para melhorar segurança, latência e privacidade, deslocando o processamento para a borda e usando um ledger distribuído resistente a adulterações.

Dúvidas: Qual algoritmo de consenso específico é adotado na blockchain proposta? Como o modelo trata a revogação de credenciais e a gestão de identidade? Há avaliação empírica da escalabilidade e da sobrecarga introduzida pela integração edge‑blockchain?

#### Página 3 — ficha 4641a8464bde80281737

O trecho descreve como algoritmos de consenso (Proof of Capacity, Proof of Stake, Proof of Burn, PBFT) garantem a confiabilidade da blockchain, destacando o papel dos smart contracts na automação e segurança das transações. São ressaltados os atributos de descentralização, imutabilidade e transparência, bem como os desafios de latência, consumo energético e baixa taxa de transferência ao aplicar blockchain em IoT. Também são apresentados requisitos de confiança para sistemas IoT de borda, como precisão, segurança e acessibilidade.

- Consensus algorithms play a crucial role in establishing the trustworthiness of every node in the blockchain. — citação conferida: consensus algorithms play a crucial role in establishing the trustworthiness of every node in the blockchain

Interpretação: O texto enfatiza que a segurança e a confiança em sistemas IoT de borda podem ser reforçadas por blockchain, mas alerta para os custos de desempenho e energia associados a algoritmos de consenso tradicionais.

Dúvidas: Quais algoritmos de consenso são mais adequados para dispositivos IoT com recursos limitados? Como equilibrar transparência e privacidade ao usar criptografia avançada na borda?

#### Página 4 — ficha 6f92d6b0e0fd3e875838

O artigo propõe uma arquitetura privada baseada em blockchain para IIoT com computação de borda, enfatizando leveza, escalabilidade e extensibilidade. Destaca requisitos de confiabilidade, diversidade, recursos limitados e flexibilidade. Introduz nós pequenos com máquinas virtuais para criptografia assimétrica e um mecanismo PoAh para autenticação de dispositivos, abordando gestão de confiança, compartilhamento seguro de dados e registro de dispositivos.

- A arquitetura utiliza nós pequenos com máquinas virtuais para criptografia assimétrica em tempo real. — citação conferida: first step is implementing small nodes that use virtual machines to conduct asymmetric cryptography in real time.

Interpretação: O trabalho foca na integração de blockchain com computação de borda para IIoT, buscando superar limitações de recursos e garantir confiança, mas ainda não demonstra avaliação prática ou métricas detalhadas.

Dúvidas: Como o PoAh se compara a outros algoritmos de consenso em termos de latência e consumo energético? Qual o plano para validar a arquitetura em ambientes reais de cidades inteligentes?

#### Página 5 — ficha 412f5bd069b9b1628282

O trecho revisa diversas propostas que combinam blockchain e computação de borda para IIoT, destacando arquiteturas de gestão baseadas em contratos inteligentes, sistemas de confiança como BlockEdge e TrustChain, e mecanismos de controle de acesso em ambientes genéricos de IoT. Aponta que, apesar dos avanços, ainda há limitações de escalabilidade, consumo energético e interoperabilidade que precisam ser superadas para adoção em larga escala.

- a blockchain-based management architecture is suggested in 22. — citação conferida: a blockchain-based management architecture is suggested in 22.

- BlockEdge builds a trust rating system. — citação conferida: BlockEdge builds a trust rating system.

Interpretação: O texto indica que a combinação de blockchain com computação de borda pode melhorar a confiança e a segurança em IIoT, mas ainda enfrenta desafios de desempenho e interoperabilidade que precisam ser abordados.

Dúvidas: Quais métricas específicas foram usadas para medir a redução do tempo de autenticação? Como a proposta lida com a heterogeneidade de dispositivos em ambientes de cidades inteligentes?

#### Página 6 — ficha 14d52368ad56e6db4023

O texto descreve desafios de dispositivos IoT de baixa potência ao executar consenso blockchain, propõe uma blockchain leve com estrutura EOG e consenso PoS aprimorado para borda, e discute a integração de computação de borda (MEC) para suportar essas soluções, apontando limitações de dependência de infraestrutura e conectividade.

- Dispositivos IoT de baixa potência têm dificuldade com as exigências de consenso blockchain. — citação conferida: Low-power IoT devices may need help to handle the high processing demands of blockchain consensus methods

- A blockchain proposta utiliza um processo de consenso PoS aprimorado para dispositivos de borda com bateria limitada. — citação conferida: enhanced PoS consensus process tailored for edge devices with limited battery life

Interpretação: O trabalho avança ao propor uma blockchain leve com estrutura de dados EOG e consenso PoS otimizado, permitindo que dispositivos de borda com recursos restritos participem de redes IIoT, embora dependa fortemente da disponibilidade de servidores MEC, o que pode limitar sua adoção em áreas com infraestrutura fraca.

Dúvidas: Como a solução lida com a revogação de credenciais em ambientes com conectividade intermitente? Qual o impacto real do armazenamento de blocos expirados na latência de transações? Como garantir a segurança dos nós MEC que atuam como servidores de autenticação?

#### Página 7 — ficha a7f50a9fec316c8b79fd

O artigo propõe uma arquitetura que combina computação de borda com blockchain para IIoT, onde servidores de borda executam tarefas em containers, armazenam dados de identificação de usuários e dispositivos na blockchain e utilizam contratos inteligentes para registrar e autenticar IDs, proporcionando baixa latência, expansão dinâmica e controle de integridade.

- User and device registration are the final stages of the registration process, which is designed to be user-friendly and straightforward. — citação conferida: User and device registration are the final stages of the registration process, which is designed to be user-friendly and straightforward.

- Edge servers may be quickly added to and deleted from the platform, ensuring expansion and reliability. — citação conferida: Since the edge servers are arranged as a changing system, they may be quickly added to and deleted from the platform. As a result, edge computing platforms’ expansion and reliability are assured.

Interpretação: O texto detalha como a blockchain funciona como camada de confiança para registro, autenticação e certificação de usuários e dispositivos, enquanto a computação de borda fornece processamento próximo ao dado, reduzindo latência. A arquitetura permite escalabilidade dinâmica dos servidores de borda e utiliza contratos inteligentes para validar identidades, reforçando a integridade e a reputação do serviço.

Dúvidas: Como o protocolo PoAh se compara em termos de consumo energético a outros consensos leves? Qual o impacto da dependência de servidores MEC em áreas com conectividade limitada? Como a solução lida com revogação de certificados de identidade em caso de comprometimento? Existe avaliação de desempenho em cenários de alta mobilidade de dispositivos IoT?

#### Página 8 — ficha 162adf038a6b0b7f4e10

O artigo apresenta uma arquitetura de computação de borda assistida por blockchain para IIoT, detalhando quatro smart contracts (identidade, submissão, verificação e crédito) e um novo mecanismo de consenso chamado Proof-of-Authentication, projetado para dispositivos com recursos limitados, usando criptografia ElGamal e valores de confiança para validar blocos.

- Proof-of-Authentication is proposed as a novel consensus mechanism. — citação conferida: This study proposes a novel consensus mechanism, called Proof-of-Authentication, to create a distributed ledger that is durable and compact for endpoints with limited resources.

- Four smart contracts document and validate the data analysis procedure. — citação conferida: The four smart contracts document and validate the data analysis procedure, further enhancing the system’s security.

Interpretação: A proposta combina blockchain com computação de borda, usando contratos inteligentes para gerenciar identidade, submissão, verificação e reputação, enquanto o consenso PoAh reduz a carga computacional em dispositivos IoT limitados, reforçando segurança e confiança na troca de dados críticos.

Dúvidas: Como o PoAh se comporta em cenários de alta latência de rede? Qual o impacto da confiança inicial (tr = 10) nos nós em ambientes dinâmicos? Os contratos inteligentes suportam integração com credenciais verificáveis (VCs) de SSI? Há avaliação de escalabilidade quando o número de nós cresce significativamente?

#### Página 9 — ficha 4183f2720ed51377e624

Os autores apresentam uma arquitetura de computação de borda assistida por blockchain para IIoT, implementada em Hyperledger Fabric com consenso PoAh. Simulações em MATLAB mostram alta eficiência, confiabilidade e baixo custo, usando containers Docker e VMs conectadas por LAN de 1 Mbps. O tempo de autenticação aumenta conforme o número de nós (de 5 a 50), mas permanece eficiente. Os custos de cálculo e comunicação são detalhados, reforçando a viabilidade econômica da solução.

- O sistema proposto é altamente custo‑efetivo. — citação conferida: The proposed system, evaluated using MATLAB and Hyperledger Fabric, is not only efficient and reliable but also highly cost-effective.

- Os tempos de autenticação aumentam com o número de pares. — citação conferida: Figure 4 illustrates that authentication times grow for varying numbers of peers deployed as terminal counts rise from five to fifty.

Interpretação: Os resultados indicam que a combinação de PoAh e Hyperledger Fabric oferece uma solução prática e econômica para autenticação em IIoT, embora a latência aumente com a escala, sugerindo necessidade de otimizações para grandes implantações.

Dúvidas: Como o desempenho e o custo‑benefício se comportam em cenários reais com conectividade intermitente e recursos de MEC limitados?

#### Página 10 — ficha eb376b0b3a1aee39020e

O artigo apresenta o algoritmo de consenso PoAh, projetado para ser menos intensivo em recursos e energia, atendendo a dispositivos IIoT com restrições. Experimentos em bancada e simulações mostram que o tempo de autenticação cresce conforme o número de nós aumenta, conforme ilustrado na Figura 4. Custos de comunicação e blockchain são detalhados em uma tabela, indicando tempos de geração de valores aleatórios, hash, emparelhamento criptográfico, verificação de nó e implantação do PoAh.

- O algoritmo PoAh oferece autenticação menos intensiva em recursos e energia. — citação conferida: The PoAh algorithm implements a less resource- and energy-intensive authentication approach.

- O tempo de autenticação aumenta com o número de nós na arquitetura proposta. — citação conferida: Fig. 4. The authentication time of proposed architecture with different nodes.

Interpretação: O trecho reforça que o consenso PoAh foi concebido para ambientes IIoT com restrição de recursos, proporcionando autenticação mais leve e demonstrando que o tempo de autenticação escala com o número de nós, o que é crítico para a viabilidade em redes de borda extensas.

Dúvidas: Como o PoAh se comporta em termos de segurança contra ataques de Sybil ou replay em ambientes altamente dinâmicos? Qual é o impacto real do consumo energético nos dispositivos de baixa potência ao longo de longos períodos de operação?

#### Página 11 — ficha 87663cda143089a73c92

O artigo apresenta o algoritmo PoAh, um consenso leve que reduz o consumo de recursos e o tempo de execução em comparação ao PoW e PoS, tornando‑se adequado para dispositivos IIoT de baixa potência em cenários de cidades inteligentes. Testes em bancada com seis nós demonstram que PoAh valida blocos rapidamente, mantendo a segurança ao integrar a criptografia do PoW.

- PoAh offers a key advantage of reduced execution time without compromising on security. — citação conferida: PoW , which takes about 10 min to validate a single block, is simply not practical for IoT use.

Interpretação: O estudo demonstra que o consenso PoAh pode superar as limitações de energia e tempo dos algoritmos tradicionais, oferecendo uma solução viável para a integração de blockchain em dispositivos IIoT de baixa potência, especialmente em ambientes de cidades inteligentes onde a conectividade pode ser limitada.

Dúvidas: Como o PoAh se comporta em escalas muito maiores que o testbed de seis nós? Qual o impacto da dependência de servidores MEC na robustez da solução em áreas com conectividade intermitente?

#### Página 12 — ficha 2f798e15eaed86a1aeda

O trecho descreve o consenso PoAh combinado com ECDSA, que melhora a segurança contra ataques de 51% e conexões instáveis em redes IIoT, detalha a rastreabilidade de mensagens ilegais e apresenta avaliação de desempenho de processos industriais, como tempo de inscrição de usuários (815‑1571 ms) e captura de dados de sensores (≈1908 ms).

- PoAh mitigates 51% attack through dynamic trust values. — citação conferida: the dynamic nature of trust values effectively addresses PoW’s vulnerability to a 51% assault

- User enrollment time remains under 1 s even with 50 users. — citação conferida: The first group’s execution time records a minimum of 815 milliseconds and a high of 1571 milliseconds

Interpretação: O consenso PoAh, ao combinar ECDSA e valores de confiança dinâmicos, parece oferecer resistência a ataques de maioria e melhorar a confiabilidade em redes IIoT com conectividade irregular, ao mesmo tempo em que mantém tempos de operação aceitáveis para processos industriais críticos.

Dúvidas: Como o PoAh se comporta em ambientes com alta latência de rede ou perda de pacotes? Qual o impacto de escalonar para milhares de dispositivos IoT em termos de consumo energético e gerenciamento de chaves?

#### Página 13 — ficha 7d62414c2f12918e3c57

O trabalho apresenta uma arquitetura de computação de borda assistida por blockchain para IIoT, que inclui coleta de dados de sensores e um processo de autorização em três etapas (submissão de transação, autenticação e concessão de acesso). Os tempos de execução são inferiores a 875 ms para a maioria dos grupos de registros e 1612 ms em média para o maior lote, indicando desempenho satisfatório.

- A autorização de pessoas para visualizar as informações coletadas pelo sensor é uma função crucial adicional. — citação conferida: The authorization of people to view the information collected by the sensor is an additional crucial function.

- O tempo total de execução foi inferior a 875 ms para a maioria dos grupos de registros. — citação conferida: the total execution time was less than 875 ms

Interpretação: Os resultados indicam que a arquitetura proposta consegue atender aos requisitos de latência para coleta e acesso a dados de sensores em ambientes industriais, embora o tempo aumente para lotes maiores, sugerindo necessidade de otimizações para alta carga.

Dúvidas: Como o mecanismo de autorização se comporta sob alta concorrência de solicitações? Qual o impacto da variabilidade de conectividade de borda nos tempos de autenticação e concessão de acesso?

#### Página 14 — ficha 4aee7ffe466649e1508a

O estudo implementou uma rede de teste com laptops, PCs e um servidor cloud usando Golang e Node.js para avaliar o consenso PoAh. Foram introduzidos atrasos de propagação de 35–55 ms. Os resultados mostraram que a taxa de transferência aumenta com a largura da arquitetura e o tamanho dos blocos, atingindo 225 tps, muito superior ao Bitcoin (7 tps) e Ethereum (27 tps).

- Our blockchain achieves 225 tps, a significant improvement over Bitcoin and Ethereum — citação conferida: Our blockchain achieves 225 tps, a significant improvement over Bitcoin and Ethereum, which achieves 7 tps and 27 tps respectively.

- As the width of the PoAh architecture grows, throughput rises with a fixed block size — citação conferida: As the width of the PoAh architecture grows, throughput rises with a fixed block size, as seen in Fig. 8.

Interpretação: Os experimentos indicam que a arquitetura PoAh escala bem em largura e tamanho de bloco, proporcionando alta taxa de transações comparada a blockchains públicas.

Dúvidas: Como a latência introduzida (35–55 ms) afeta a consistência e a segurança da cadeia? Qual o comportamento da arquitetura em cenários com conectividade intermitente? O mecanismo PoAh resiste a ataques de 51% em redes maiores?

#### Página 15 — ficha b690824cdae3dbd03efc

O estudo apresenta uma arquitetura de computação de borda assistida por blockchain que atinge 1273 tps, reduz latência e protege contra ataques de replay e man‑in‑the‑middle. O desempenho é satisfatório até ~100 nós de borda, mas decai acima desse número devido ao consenso.

- Alto rendimento da blockchain — citação conferida: maximum throughput of 1273 tps, a substantial improvement over Bitcoin and Ethereum

Interpretação: Os resultados indicam que a combinação de blockchain privada leve (PoAh) com computação de borda pode melhorar significativamente a eficiência e a segurança de IIoT, porém a escalabilidade do consenso se torna um gargalo crítico quando o número de nós de borda ultrapassa cerca de 100.

Dúvidas: Como a arquitetura se comportaria em cenários com milhares de nós distribuídos geograficamente? Qual seria o impacto de integrar SSI ou ABE sobre a latência e o consumo de recursos?

#### Página 16 — ficha 1dc02ab0c7a154099cf5

O trecho apresenta uma lista extensa de referências relacionadas a blockchain, edge computing e IoT industrial, incluindo trabalhos sobre mecanismos de consenso leves (Poah), frameworks como BlockEdge, e soluções de privacidade e controle de acesso, além das informações de autoria, financiamento e declaração de conflitos de interesse do artigo.

- Poah é um algoritmo de consenso novel para blockchains privadas escaláveis em grandes frameworks IoT. — citação conferida: Puthal, D., Mohanty, S. P ., Y anambaka, V . P . & Kougianos, E. Poah: A novel consensus algorithm for fast scalable private blockchain for large-scale iot frameworks. arXiv preprint. arXiv:2001.07297 (2020).

- BlockEdge propõe um framework blockchain-edge para redes industriais IoT. — citação conferida: Kumar, T. et al. BlockEdge: blockchain-edge framework for industrial IoT networks. IEEE Access 8, 154166–154185 (2020).

Interpretação: A presença dessas referências indica que o trabalho se apoia em literatura recente sobre consenso leve, integração blockchain-edge e privacidade, reforçando a relevância da proposta no contexto de cidades inteligentes e IIoT.

Dúvidas: Como a arquitetura proposta difere ou complementa o framework BlockEdge? Qual o papel específico do Poah na solução apresentada? Há detalhes sobre a implementação de credenciais verificáveis ou ABE que ainda não foram descritos?

<!-- agente:fim -->
