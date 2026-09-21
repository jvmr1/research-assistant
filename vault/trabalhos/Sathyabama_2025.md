---
nome_local: Sathyabama_2025
openalex_id: https://openalex.org/W4411852537
doi: https://doi.org/10.1038/s41598-025-04164-4
ano: 2025
status: triagem_pendente
acesso_aberto: true
pdf_local: pdfs/Sathyabama_2025.pdf
tags: [abe, blockchain, contratos-inteligentes, controle-de-acesso, criptografia, governanca-de-dados, interoperabilidade, iot, seguranca, sistemas-distribuidos]
---
# Sathyabama_2025

## Tags

#abe #blockchain #contratos-inteligentes #controle-de-acesso #criptografia #governanca-de-dados #interoperabilidade #iot #seguranca #sistemas-distribuidos

Enhancing anomaly detection and prevention in Internet of Things (IoT) using deep neural networks and blockchain based cyber security

<!-- agente:inicio -->

## Leitura e relações atualizadas pelo agente

Fonte: https://doi.org/10.1038/s41598-025-04164-4

Triagem: revisar. O trabalho aborda IoT, blockchain e segurança cibernética, temas centrais do escopo de pesquisa. Contudo, foca em detecção de anomalias via redes neurais profundas e uso de blockchain para integridade e resposta automática, sem tratar diretamente de identidade digital auto-soberana, controle de acesso baseado em atributos, interoperabilidade entre organizações ou contextos de cidades inteligentes. Por isso, não se enquadra como prioridade máxima, mas merece ser revisado para avaliar possíveis extensões ou combinações com abordagens de SSI, controle de acesso ou ABE que poderiam preencher lacunas identificadas no grupo de pesquisa.

[PDF local](../../pdfs/Sathyabama_2025.pdf)

### Relações bibliográficas verificadas nos metadados

Referencia: nenhum trabalho do acervo identificado.

É citado por: [Khayer_2025](Khayer_2025.md)

### Como se correlaciona com os demais na análise

**Com  — Sathyabama_2025: Explorar consenso leve (PoA, DAG) para reduzir latência; integrar verifiable credentials p**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Explorar consenso leve (PoA, DAG) para reduzir latência; integrar verifiable credentials para gerenciamento de identidade e revogação de dispositivos IoT; aplicar aprendizado federado para treinamento distribuído sem exposição de dados sensíveis; avaliar robustez contra ataques adversariais usando técnicas de defesa avançadas; otimizar modelos DNN com poda, quantização ou destilação para dispositivos de borda.

[Proposta completa no relatório](../RELATORIO.md)

**Com  — Sathyabama_2025: Avaliar desempenho de DNNs‑BCT com blockchains permissionados de baixa latência (ex**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Avaliar desempenho de DNNs‑BCT com blockchains permissionados de baixa latência (ex.: Hyperledger Fabric, Raft) em ambientes de edge computing

[Proposta completa no relatório](../RELATORIO.md)

**Com  — Sathyabama_2025: Desenvolver DNNs ultra‑leves ou aplicar aprendizado federado para reduzir consumo energéti**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Desenvolver DNNs ultra‑leves ou aplicar aprendizado federado para reduzir consumo energético nos nós de borda

[Proposta completa no relatório](../RELATORIO.md)

**Com  — Sathyabama_2025: Integrar técnicas de privacidade como homomorphic encryption ou zero‑knowledge proofs ao r**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Integrar técnicas de privacidade como homomorphic encryption ou zero‑knowledge proofs ao registro de dados na blockchain

[Proposta completa no relatório](../RELATORIO.md)

### Fichamento

Base: pdf; 16/16 trechos. Páginas sem texto extraível: []. Figuras e tabelas podem exigir conferência humana.

#### Página 1 — ficha 6a8f0b952a23d59feaeb

O artigo propõe um framework que combina Deep Neural Networks para detecção de anomalias e blockchain privado com smart contracts para garantir integridade, transparência e respostas automáticas a ameaças em ambientes IoT, alcançando 99,18% de acurácia e 15,42% de falsos positivos.

- O modelo DNN atinge taxa de falsos positivos de 15,42% e precisão de detecção de 99,18%. — citação conferida: With a low false-positive rate of 15.42% and a strong detection accuracy of 99.18%

Interpretação: A combinação de DNNs e blockchain oferece uma solução adaptativa que supera limitações de IDS baseados em regras, reduz falsos positivos e garante a integridade dos registros IoT, potencialmente viável para infraestruturas críticas de cidades inteligentes.

Dúvidas: Como o overhead de blockchain privado e smart contracts afeta a latência em redes IoT massivas? Qual o custo energético da execução contínua de DNNs em dispositivos de borda? Como garantir a privacidade dos dados sensíveis ao registrar informações na cadeia?

#### Página 2 — ficha b9c2f52d3610c303cb17

O artigo propõe a arquitetura DNNs‑BCT, que combina redes neurais profundas com blockchain privado para detectar anomalias em redes IoT em tempo real, reduzindo falsos positivos e aumentando a precisão. O blockchain garante integridade e resposta automática via contratos inteligentes, enquanto o DNN aprende padrões de ataque, inclusive zero‑day. Avaliações com datasets de benchmark mostram desempenho superior a IDS tradicionais. Futuras linhas incluem DNNs leves e aprendizado federado para dispositivos com recursos limitados.

- Every IoT device logs activities on a private blockchain network, ensuring secure communication and preventing unlawful access — citação conferida: Every IoT device logs activities on a private blockchain network, ensuring secure communication and preventing unlawful access

Interpretação: A combinação de IA avançada e blockchain oferece uma solução promissora para superar as limitações dos IDS baseados em assinaturas, proporcionando detecção adaptativa, integridade dos dados e respostas automáticas, embora dependa de recursos computacionais que podem ser restritos em dispositivos de borda.

Dúvidas: Como garantir a eficiência energética dos DNNs leves em dispositivos muito limitados? Qual o impacto da latência do blockchain permissionado em respostas em tempo real? Como o modelo lida com ataques adversariais direcionados ao próprio DNN? Quais são os custos de implantação e manutenção de uma rede blockchain privada em larga escala nas cidades inteligentes?

#### Página 3 — ficha eda521031516b8b36a16

O artigo propõe DNNs-BCT, que combina redes neurais profundas com blockchain para detecção de anomalias em IoT, usando edge computing para pré‑processamento, reduzindo custos computacionais, consumo de energia e latência em relação a soluções baseadas em Ethereum ou Bitcoin.

- DNNs-BCT reduces computational costs and latency compared to traditional blockchain solutions. — citação conferida: processing, reduced storage overhead, and efficient energy use for IoT environments, in contrast to traditional blockchain-based security solutions that depend on Ethereum or Bitcoin, which have high computational costs, energy consumption, and latency.

- Edge computing preprocesses data before DNN inference and blockchain logging, enabling real‑time anomaly detection. — citação conferida: DNNs-BCT uses edge computing to preprocess data before DNN inference and blockchain logging, greatly reducing bandwidth load and allowing for real-time anomaly detection.

Interpretação: O texto enfatiza que a combinação de DNNs com blockchain, apoiada por computação de borda, pode superar as limitações de energia e latência das abordagens tradicionais, tornando a detecção de anomalias viável para ambientes IoT restritos.

Dúvidas: Quais métricas específicas foram usadas para validar a eficiência de DNNs‑BCT? Como a solução lida com a atualização dos modelos DNN em dispositivos com recursos limitados? Existe avaliação de resistência a ataques adversariais direcionados ao modelo DNN?

#### Página 4 — ficha c3afa76dff606b4ad5e4

O trecho apresenta uma revisão de literatura que destaca a superação de obstáculos ao uso de deep learning em áreas como saúde e bioinformática, e descreve múltiplos estudos que combinam algoritmos bio‑inspirados, blockchain e redes neurais para otimizar coleta de dados, detecção de intrusões, confiabilidade de sensores e desempenho de IIoT. São citados critérios de avaliação (escalabilidade, flexibilidade, latência, métricas de classificação) e diversas propostas que melhoram confiabilidade, eficiência e segurança em ambientes distribuídos.

- Most articles are assessed based on scalability, flexibility, latency, Fscore, specificity, sensitivity, and accuracy. — citação conferida: most articles are assessed based on scalability, flexibility, latency, Fscore, specificity, sensitivity, and accuracy.

Interpretação: O trabalho se insere em uma tendência crescente de combinar deep learning e blockchain para melhorar a detecção de anomalias em IoT, adotando métricas de desempenho padrão da literatura (escalabilidade, latência, precisão). Os estudos citados reforçam a necessidade de soluções que conciliem segurança, confiabilidade e eficiência energética, apontando caminhos para aprimorar a proposta DNNs‑BCT.

Dúvidas: Como a DNNs‑BCT será avaliada em termos de escalabilidade e latência nos cenários de edge computing? Quais são os requisitos de recursos computacionais para a implementação prática em dispositivos IoT de baixa potência? Como a abordagem lida com revogação de credenciais e interoperabilidade entre diferentes organizações públicas e privadas?

#### Página 5 — ficha 380ae2aeb1551d28a123

O trecho discute a predominância de Python e CNNs em pesquisas de detecção de anomalias (AD) baseadas em DL, apontando lacunas em proteção de dados e estabilidade de modelos. Destaca a necessidade de IA mais transparente e melhor integração de dados. Apresenta diversas propostas de blockchain aplicadas ao IoT, como BDLT‑IoMT para segurança de dados e BAIoT‑EMS para gestão de PMEs, ressaltando ganhos de desempenho e redução de consumo computacional.

- some security issues, such as data protection and model stability, are under-explored in the current study. — citação conferida: The author believes some security issues, such as data protection and model stability, are under-explored in the current study.

- blockchain distributed ledger technology with the Internet of Medical Things (BDLT‑IoMT) for secure data processing. — citação conferida: Abdullah Ayub Khan et al. 41 suggested the blockchain distributed ledger technology with the Internet of Medical Things(BDLT-IoMT) for secure data processing.

Interpretação: O texto evidencia que, embora haja avanços no uso de DL e blockchain para detecção de anomalias em IoT, ainda faltam abordagens que garantam a proteção de dados e a estabilidade dos modelos, além de necessidade de maior transparência e integração de dados. As propostas de blockchain em diferentes domínios (IoMT, PMEs, fog/edge) sugerem um movimento rumo a soluções mais interoperáveis e eficientes.

Dúvidas: Como os DNNs são integrados ao ledger blockchain no contexto proposto? Quais métricas de precisão e latência foram avaliadas? Existe avaliação de consumo energético dos modelos leves sugeridos? Como a solução lida com revogação de credenciais em ambientes distribuídos?

#### Página 6 — ficha 72b8d0d4352f1ff971df

O artigo propõe o framework DNNs‑BCT, que combina uma arquitetura DNN leve com contratos inteligentes em blockchain para detectar e prevenir anomalias em redes IoT. Aponta limitações de técnicas existentes, como altas taxas de falsos positivos e sobrecarga computacional, e descreve como a integração proposta melhora a integridade dos dados, reduz a latência e aumenta a escalabilidade, especialmente em ambientes de recursos limitados.

- Existing IoT anomaly detection techniques often suffer from elevated false alarm rates, ineffective real-time threat categorization, and susceptibility to adversarial attacks. — citação conferida: Existing IoT anomaly detection techniques often suffer from elevated false alarm rates, ineffective real-time threat categorization, and susceptibility to adversarial attacks.

Interpretação: A proposta avança o estado da arte ao unir detecção de anomalias baseada em IA com garantias de integridade e resposta automática via blockchain, abordando tanto a precisão quanto a eficiência em ambientes IoT restritos.

Dúvidas: Como a solução lida com a heterogeneidade de dispositivos IoT de diferentes fabricantes? Qual o impacto real da latência introduzida pelos contratos inteligentes em cenários de tempo‑crítico? Existem testes de resistência a ataques adversariais específicos ao modelo DNN leve?

#### Página 7 — ficha f38e05006f7eed13c08c

O artigo propõe um módulo de Detecção de Anomalias baseado em DNN que analisa logs de tráfego IoT e classifica ameaças, enviando os resultados para uma rede blockchain para registro permanente e transparência. Contudo, o fluxo de dados que descreve armazenamento, verificação e uso das anomalias na blockchain não está detalhado, assim como a automação via contratos inteligentes. A combinação de IA preditiva com blockchain visa melhorar a segurança cibernética em IoT, reduzindo ataques e preservando a integridade dos dados.

- The Anomaly Detection module, which is based on DNN, scans IoT traffic logs and categorizes threats as normal or abnormal. — citação conferida: the Anomaly Detection module, which is based on DNN, scans IoT traffic logs and categorizes threats as normal or abnormal

- Combining the predictive capabilities of artificial intelligence with the trustless environment of blockchain enhances cybersecurity in IoT systems, thereby lowering probable attacks and maintaining data integrity. — citação conferida: Combining the predictive capabilities of artificial intelligence with the trustless environment of blockchain enhances cybersecurity in IoT systems, thereby lowering probable attacks and maintaining data integrity

Interpretação: O trabalho enfatiza a integração de DNNs para detecção de ameaças com registro imutável em blockchain, mas deixa em aberto como os logs são efetivamente armazenados, verificados e como contratos inteligentes respondem às anomalias, indicando uma lacuna de implementação prática.

Dúvidas: Como os resultados da detecção são codificados e inseridos na blockchain? Qual é a lógica dos contratos inteligentes para mitigação automática? Qual o impacto de latência e consumo de energia ao combinar DNNs em tempo real com operações de blockchain em dispositivos IoT de recursos limitados?

#### Página 8 — ficha cfe138fec6355151495f

O artigo propõe integrar redes neurais profundas (DNN) com blockchain para detectar e mitigar anomalias em dispositivos IoT em tempo real. As equações mostram a transição de dados processados para um sistema de redução de ameaças assegurado por blockchain, enquanto o DNN categoriza riscos. O blockchain fornece registro descentralizado, imutável e remediação automática. A arquitetura utiliza Hyperledger Fabric ou blockchains permissionados, aproveitando seu consenso de baixa latência (PBFT) para suportar ambientes de cidades inteligentes.

- O DNN aumenta a detecção de anomalias. — citação conferida: The DNN boosts the detection of anomalies nx [o − er′′]

- O blockchain garante registro descentralizado e remediação automática. — citação conferida: Blockchain guarantees safe, decentralized logging and automatic remediation

Interpretação: A combinação de DNN e blockchain visa criar um mecanismo de defesa em tempo real, onde a inteligência artificial identifica padrões anômalos e o ledger distribuído assegura a integridade e a ação corretiva automática, reduzindo a superfície de ataque em ambientes IoT de cidades inteligentes.

Dúvidas: Como o modelo lida com a sobrecarga computacional em dispositivos de borda? Qual o impacto do consenso PBFT na latência de resposta a anomalias? Há avaliação de escalabilidade em cenários multi‑organização?

#### Página 9 — ficha d91819e1051d377f0c40

O texto destaca o uso de Hyperledger Fabric como alternativa ao Ethereum PoW para IoT, recomendando blockchains leves com consenso PoA ou DAGs para reduzir custo computacional e energia. Apresenta equações que ilustram a integração de alertas de segurança com IA e blockchain, e relata que a solução alcança mais de 98% de acurácia na detecção de ameaças, incluindo DDoS e malware.

- Hyperledger Fabric is a great alternative to Ethereum’s energy-intensive Proof of Work (PoW) consensus. — citação conferida: Hyperledger Fabric is a great alternative to Ethereum’s energy-intensive Proof of Work (PoW) consensus.

- The solution achieves over 98% accuracy in identifying cyber threats, including DDoS assaults and malware injections. — citação conferida: it achieves over 98% accuracy in identifying cyber threats, including DDoS assaults and malware injections.

Interpretação: O trecho enfatiza a escolha de blockchains leves como Hyperledger Fabric com consenso PoA ou DAGs para reduzir custos computacionais em IoT, e destaca a alta precisão (≥98%) da detecção de ameaças usando DNNs, reforçando a proposta de combinar IA e blockchain para segurança autônoma e em tempo real.

Dúvidas: Como será realizada a análise de custo computacional para treinamento DNN e operações blockchain? Qual o impacto da latência dos consensos PoA/DAGs nas respostas em tempo real? Como a solução se comporta em dispositivos de borda com recursos limitados?

#### Página 10 — ficha 8d50265a63f95315ede0

O texto descreve o framework DNNs‑BCT que combina redes neurais profundas com blockchain para detectar anomalias em IoT. Utiliza funções de ativação avançadas, dropout e batch‑normalization, além de seleção de características (RFE, PCA, MI) extraídas de eventos de segurança blockchain, logs de dispositivos e tráfego de rede. Detecta exfiltração, DDoS, ataques Sybil e brute‑force. O pipeline inclui coleta e pré‑processamento de dados (75 % treino, 25 % teste) e treinamento de DNN para classificar o comportamento da rede como normal, benigno ou perigoso, gerando alertas em tempo real.

- O procedimento de seleção de características do framework DNNs‑BCT visa melhorar a precisão da detecção de anomalias com baixo custo computacional. — citação conferida: The DNNs-BCT framework’s feature selection procedure aims to improve anomaly detection accuracy with little computational cost.

- O modelo treinado classifica o comportamento da rede como normal, benigno ou anômalo, gerando alerta de risco de segurança. — citação conferida: The trained model sets network behavior as either normal, benign, or aberrant, either benign or dangerous.

Interpretação: O trecho evidencia que a proposta combina técnicas avançadas de deep learning e blockchain para criar um sistema de detecção de anomalias que prioriza eficiência computacional e capacidade de identificar múltiplas ameaças, reforçando a ideia de segurança descentralizada e auto‑aprendente para ambientes IoT.

Dúvidas: Não há detalhes sobre a avaliação empírica (métricas, benchmarks) nem sobre o impacto do custo computacional real em dispositivos de borda; também falta informação sobre como as credenciais verificáveis seriam integradas ao fluxo de detecção.

#### Página 11 — ficha 924bfebe39cd9fb52a6e

O trecho descreve como vulnerabilidades e falhas de segurança não descobertas em redes IoT podem ser transformadas em um framework de autenticação protegido por blockchain, combinando camadas de segurança Ba e mecanismos defensivos adaptativos Ka alimentados por IA. Destaca ainda o uso de smart contracts para mitigação automática de ameaças em tempo real, garantindo integridade dos dados e registro imutável.

- Automated threat mitigation via smart contracts — citação conferida: Automated threat mitigation via smart contracts

Interpretação: O autor propõe uma arquitetura que une IA para detecção de anomalias e blockchain para registro imutável e resposta automática via smart contracts, reforçando a segurança e a confiança em redes IoT.

Dúvidas: Como a solução lida com a sobrecarga computacional em dispositivos de borda? Qual o impacto do uso de smart contracts na latência de mitigação de ameaças?

#### Página 12 — ficha 7483b8ab98e681acd5bf

O trecho apresenta um método que converte vulnerabilidades de redes IoT, inclusive em monitoramento de tráfego marítimo, em camadas de autenticação protegidas por blockchain e controle de acesso descentralizado, combinados com modelos de IA para detecção de anomalias em tempo real. Equações demonstram a transição de falhas de segurança para um sistema multi‑nível que integra verificação comportamental, análise adaptativa e medidas híbridas, reforçando a proteção descentralizada dos dispositivos IoT.

- The Eq. 17 shows how possible data exposure networks may be transformed into a blockchain-protected authentication layer. — citação conferida: The Eq.  17 shows pde how possible data exposure networks may be transformed into a blockchain-protected authentication layer Ja [w − iu′′] and anomaly detection Va [w − syu′′] driven by artificial intelligence.

- Equation 18 depicts the move from possible security holes in IoT networks to a multi-level security system based on blockchain technology. — citação conferida: Equation 18 depicts the move from possible security holes in IoT networks ( psw [i − st′′]) to a multi-level security system based on blockchain technology.

Interpretação: Os autores propõem que, ao integrar blockchain e IA, vulnerabilidades de exposição de dados e falhas de segurança em redes IoT podem ser mitigadas por meio de autenticação descentralizada e detecção contínua de anomalias, criando um mecanismo de defesa em camadas que combina verificação comportamental e análises adaptativas.

Dúvidas: Como o modelo lida com a sobrecarga computacional em dispositivos de borda? Qual o impacto da latência introduzida pelos contratos inteligentes nas respostas em tempo real? Existem avaliações empíricas que quantifiquem a melhoria de segurança versus o custo de implementação?

#### Página 13 — ficha 2c128c266417e09fcd92

O artigo propõe uma arquitetura que combina blockchain e redes neurais profundas para detectar e prevenir anomalias em IoT, incluindo aplicações marítimas. O modelo DNN‑Blockchain alcança 99,18% de acurácia e reduz a taxa de falsos positivos para 15,42%, mas ainda enfrenta vulnerabilidades como ataques a contratos inteligentes e ataques de 51%. São sugeridas melhorias como verificação formal de contratos e algoritmos criptográficos leves.

Interpretação: A combinação de blockchain com DNN demonstra potencial para melhorar a segurança de IoT, especialmente ao reduzir falsos alarmes, porém a dependência de contratos inteligentes ainda expõe o sistema a vulnerabilidades conhecidas.

Dúvidas: Como a solução se comporta em ambientes de IoT com recursos extremamente limitados? Qual o impacto real de algoritmos criptográficos leves na segurança versus desempenho?

#### Página 14 — ficha 27ed43bd5cebc0425cce

O artigo relata que, ao empregar contratos inteligentes na blockchain, o sistema de segurança IoT reage automaticamente a ameaças, eliminando atrasos humanos e alcançando 95,25% de eficiência no tempo de reação, o que garante mitigação em tempo real e baixa latência na preservação da integridade dos dispositivos conectados.

- O sistema reage a ameaças em tempo real, eliminando atrasos humanos. — citação conferida: Smart contracts built within the Blockchain enable the system to react to threats automatically, therefore eliminating delays in human interaction.

Interpretação: A combinação de contratos inteligentes e DNN permite uma resposta quase instantânea a incidentes, reduzindo a janela de vulnerabilidade típica de intervenções manuais, embora a dependência de contratos inteligentes introduza novos vetores de risco.

Dúvidas: Como o modelo escala em ambientes com milhares de dispositivos IoT? Qual o overhead de execução dos contratos inteligentes em hardware de borda com recursos limitados?

#### Página 15 — ficha fa1d28ab2973e81e3722

O trecho descreve a integração de armazenamento off‑chain (IPFS ou nuvem) e otimização de contratos inteligentes para reduzir latência, além de usar edge computing para pré‑processar dados IoT. O método mantém alta precisão na mitigação de ameaças, alcançando 94,96% de escalabilidade, e propõe técnicas como batch de transações e compressão de logs para evitar o inchaço da blockchain.

- The framework ensures a 94.96% scalability. — citação conferida: 94.96% scalability

- Distributed storage alternatives like IPFS or cloud-based systems may be used off-chain to store less sensitive data, reducing transaction overhead. — citação conferida: Distributed storage alternatives like IPFS or cloud-based systems may be used off-chain to store less sensitive data, reducing transaction overhead

Interpretação: A proposta reforça a importância de combinar blockchain com computação de borda e armazenamento off‑chain para manter alta precisão de segurança ao mesmo tempo em que controla a latência e o tamanho da cadeia.

Dúvidas: Como a otimização dos contratos inteligentes será implementada na prática? Qual o impacto real da compressão de logs na detecção de anomalias? Existem métricas de comparação com soluções centralizadas para validar a melhoria de latência?

#### Página 16 — ficha bc7abe3f3b0020d4067b

O estudo apresenta uma arquitetura híbrida DNN‑Blockchain para segurança de redes IoT, destacando alta escalabilidade (94,96%), rapidez (95,25%) e descentralização (97,33%). Cada dispositivo registra atividades em uma blockchain privada, reduzindo pontos únicos de falha. Embora a detecção de anomalias alcance 99,18% de acurácia, os autores apontam a necessidade de análise de custo computacional e otimizações para dispositivos com recursos limitados.

- The method improves the system’s scalability by using decentralized computing methodologies and optimizing the allocation of resources. — citação conferida: The method improves the system’ s scalability by using decentralized computing methodologies and optimizing the allocation of resources in Eq. 24.

- The DNN detects abnormalities with 99.18% accuracy. — citação conferida: the DNN detects abnormalities with 99.18% accuracy.

Interpretação: Os autores demonstram que a combinação de DNN e blockchain pode oferecer alta escalabilidade e descentralização para IoT, mitigando pontos únicos de falha. Contudo, reconhecem que o custo computacional da treinamento e das operações blockchain pode ser um obstáculo para dispositivos de recursos limitados, exigindo otimizações de modelo e análise de viabilidade prática.

Dúvidas: Qual algoritmo de consenso foi adotado e como ele impacta a latência em ambientes de borda? Qual é o overhead energético real dos nós IoT ao registrar transações em blockchain privada? Como a solução se comporta frente a ataques adversariais sofisticados contra o modelo DNN?

<!-- agente:fim -->
