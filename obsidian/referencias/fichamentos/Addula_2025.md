---
nome_local: Addula_2025
openalex_id: https://openalex.org/W4411266576
doi: https://doi.org/10.63180/jcsra.thestap.2025.4.3
ano: 2025
status: triagem_pendente
acesso_aberto: true
pdf_local: obsidian/referencias/pdfs/Addula_2025.pdf
tags: [abe, blockchain, controle-de-acesso, criptografia, criptografia-homomorfica, governanca-de-dados, interoperabilidade, iot, privacidade, sistemas-distribuidos]
---
# Addula_2025

## Tags

#abe #blockchain #controle-de-acesso #criptografia #criptografia-homomorfica #governanca-de-dados #interoperabilidade #iot #privacidade #sistemas-distribuidos
<!-- agente:inicio -->

## Leitura e relações atualizadas pelo agente

Fonte: https://doi.org/10.63180/jcsra.thestap.2025.4.3

Triagem: revisar. O artigo aborda blockchain permissionada e criptografia homomórfica para autenticação de dispositivos IoT em larga escala, tópicos relevantes para segurança e privacidade em ambientes de cidades inteligentes. Contudo, o foco está em identidade de dispositivos e não em identidade autossoberana de cidadãos, credenciais verificáveis ou ciclos de vida de credenciais humanas. Assim, pode servir como referência complementar para discussões sobre infraestrutura blockchain e técnicas criptográficas (ABE, homomorphic encryption) que podem ser adaptadas ao contexto de SSI, mas não atende diretamente aos critérios centrais da revisão focada. Por isso, recomenda-se revisá‑lo para extrair insights técnicos, mas não priorizá‑lo como fonte principal.

[PDF local](../pdfs/Addula_2025.pdf)

### Relações bibliográficas verificadas nos metadados

Referencia: nenhum trabalho do acervo identificado.

É citado por: [Li_2025](Li_2025.md)

### Como se correlaciona com os demais na análise

**Com  — Addula_2025: Desenvolver um protocolo de revogação baseado em blocos de status que minimize comunicação**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Desenvolver um protocolo de revogação baseado em blocos de status que minimize comunicação adicional e preserve anonimato

[Proposta completa nas anotações](../ANOTACOES.md)

**Com  — Addula_2025: Benchmarkar a criptografia homomórfica (incluindo FHE) em hardware IoT de recursos limitad**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Benchmarkar a criptografia homomórfica (incluindo FHE) em hardware IoT de recursos limitados para quantificar energia e latência

[Proposta completa nas anotações](../ANOTACOES.md)

**Com  — Addula_2025: Realizar testes de desempenho em ambientes de edge computing com latência variável para va**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Realizar testes de desempenho em ambientes de edge computing com latência variável para validar robustez do framework

[Proposta completa nas anotações](../ANOTACOES.md)

### Fichamento

Base: pdf; 16/16 trechos. Páginas sem texto extraível: []. Figuras e tabelas podem exigir conferência humana.

#### Página 1 — ficha df6bffac640d82c70f15

O artigo propõe um framework de autenticação IoT baseado em blockchain permissionada, combinando armazenamento otimizado, mecanismo de autenticação leve e criptografia homomórfica para proteger dados antes da nuvem. Visa melhorar a escalabilidade e reduzir a sobrecarga de armazenamento, oferecendo maior privacidade e confiança em ambientes IoT de grande escala, avaliado por simulações comparativas.

- A maioria das pesquisas existentes foca vulnerabilidades específicas, deixando de lado privacidade e confiança. — citação conferida: Most existing research on decentralized IoT applications tends to address specific vulnerabilities, with relatively few techniques dedicated to managing privacy and trust issues.

- O estudo introduz criptografia homomórfica para proteger dados IoT antes da nuvem. — citação conferida: we introduce, for the first time, the integration of homomorphic encryption to secure IoT data at the user end before uploading it to the cloud.

Interpretação: O trabalho combina blockchain permissionada e criptografia avançada para superar limitações de escalabilidade e privacidade típicas de soluções IoT descentralizadas, sugerindo que a abordagem pode ser adaptada a infraestruturas de cidades inteligentes onde o volume de dispositivos e a sensibilidade dos dados são críticos.

Dúvidas: Como o modelo lida com a revogação de credenciais de dispositivos comprometidos? Qual é o impacto de usar criptografia homomórfica na latência de comunicação em tempo real?

#### Página 2 — ficha 5f602c19ab7e3def8b54

O artigo apresenta um modelo híbrido de blockchain combinado com criptografia homomórfica para autenticação escalável e preservação de privacidade em IoT industrial, especialmente em ambientes de saúde. Destaca a vulnerabilidade de arquiteturas centralizadas, a necessidade de segurança em redes 6G e propõe um framework de confiança que utiliza aprendizado profundo leve para autenticação biométrica, suportando milhares de sensores.

- Blockchain technology has emerged as a promising solution to many of the IoT security challenges — citação conferida: Blockchain technology has emerged as a promising solution to many of the IoT security challenges [11].

- A key innovation in the proposed model is the integration of homomorphic encryption — citação conferida: A key innovation in the proposed model is the integration of homomorphic encryption —introduced here for the first time.

Interpretação: O uso combinado de blockchain híbrido e criptografia homomórfica visa superar as limitações de privacidade e confiança das arquiteturas centralizadas, permitindo processamento de dados criptografados na nuvem sem expor informações sensíveis.

Dúvidas: Como o modelo lida com a revogação de credenciais em tempo real? Qual o impacto de homomorphic encryption no consumo de energia dos dispositivos IoT de baixa potência? Como a solução se comporta em cenários de múltiplas organizações com políticas de acesso divergentes?

#### Página 3 — ficha 64aba68c5f6981536bcb

O texto revisa diversas abordagens de segurança para IoT, destacando o uso de blockchain e contratos inteligentes para gerenciamento de recursos, autenticação e controle de acesso. Aponta soluções como o protocolo Trust‑Aware Blockchain Seamless Authentication (TAB‑SAPP) e a Segurança de Camada Física (PLS) como alternativas leves. Também discute desafios de privacidade, regulamentação e a necessidade de criptografia eficiente para dispositivos restritos, especialmente em contextos médicos e de cidades inteligentes.

Interpretação: O trecho evidencia um movimento crescente para combinar blockchain com técnicas leves (PLS, biometria, ABE) a fim de atender às restrições de recursos dos dispositivos IoT, ao mesmo tempo em que busca cumprir exigências de privacidade e regulamentação, especialmente em aplicações críticas como saúde e cidades inteligentes.

Dúvidas: Como o TAB‑SAPP lida com a revogação de credenciais em ambientes distribuídos? Qual o impacto de delegar PoW a servidores de borda na latência de autenticação? Existem métricas comparativas entre PLS e criptografia tradicional em termos de consumo energético em sensores médicos?

#### Página 4 — ficha 7effbc03f18051519c19

O trecho descreve o uso de biometria de veia digital (FV) como método de autenticação robusto para IoT, destacando sua resistência a falsificações e a geração de chaves criptográficas a partir de características biométricas. Em seguida, apresenta a estrutura de blockchain como ledger descentralizado, imutável e transparente, adequado para gerenciamento seguro de dados em ambientes como saúde IoT, embora ressalte desafios de sobrecarga de comunicação e computação.

- Finger vein (FV) recognition stands out as one of the most secure biometric approaches. — citação conferida: Among these methods, finger vein (FV) recognition stands out as one of the most secure biometric approaches.

Interpretação: O texto amplia o escopo do trabalho ao sugerir que a combinação de biometria de veia digital com blockchain pode atender à necessidade de autenticação segura e privacidade em IoT, especialmente em contextos críticos como saúde. Contudo, destaca que a sobrecarga de comunicação/computação ainda é um obstáculo a ser mitigado, indicando a importância de otimizações para ambientes de borda.

Dúvidas: Como a proposta original lida com a sobrecarga computacional introduzida pela biometria FV? O framework já contempla mecanismos de revogação de credenciais biométricas? Há planos para validar a solução em cenários reais de cidades inteligentes?

#### Página 5 — ficha a8dfb592fcf8fdfaf689

O trecho descreve como a integração de contratos inteligentes em blockchains permissionadas permite a autenticação em tempo real de dados IoT, garantindo integridade e mitigando falsificação, acesso não autorizado e replay attacks. Após a verificação, os dados são criptografados com homomorphic encryption e enviados ao cloud, possibilitando análises sem revelar o conteúdo. O fluxo inclui coleta, verificação, criptografia e classificação via SVM.

- Smart contracts automatically validate, log, and manage data transactions, thereby providing a secure, immutable, and transparent mechanism for handling IoT data. — citação conferida: These smart contracts automatically validate, log, and manage data transactions, thereby providing a secure, immutable, and transparent mechanism for handling IoT data.

- Data are encrypted using homomorphic encryption and securely outsourced to the cloud. — citação conferida: the data are encrypted using homomorphic encryption and securely outsourced to the cloud.

Interpretação: O autor propõe um fluxo de dados IoT que combina verificação por contratos inteligentes e privacidade via homomorphic encryption, permitindo análises avançadas sem comprometer a confidencialidade, o que reforça a governança de dados em ambientes distribuídos.

Dúvidas: Como é medido o overhead de execução dos contratos inteligentes em tempo real? Qual o custo computacional da homomorphic encryption para dispositivos de borda? Existem testes de escalabilidade com milhares de dispositivos?

#### Página 6 — ficha 292ee3366641932d6bfc

O artigo apresenta um algoritmo para criar, atualizar e revogar registros de saúde pessoal em uma blockchain permissionada. O processo inicia com a autenticação via assinatura digital de chave pública, verifica duplicidade, registra operações como blocos imutáveis e utiliza um bloco de status "REVOKED" para revogação, preservando o histórico. O algoritmo é descrito como leve, adequado a dispositivos IoT com recursos limitados e integrável a contratos inteligentes para validação automática e políticas de segurança.

Interpretação: O trabalho propõe um mecanismo de controle de acesso baseado em blockchain que combina autenticação forte e registro imutável, atendendo às restrições de recursos típicas de dispositivos IoT, ao mesmo tempo que preserva a auditabilidade e a integridade dos dados sensíveis.

Dúvidas: Como o algoritmo lida com a escalabilidade em redes IoT de grande porte? Qual o overhead de comunicação e armazenamento ao adicionar blocos de revogação em dispositivos com memória limitada?

#### Página 7 — ficha 66308cb5e07c3e45f374

O trecho descreve procedimentos de atualização e revogação de registros em uma blockchain permissionada, e apresenta o Algoritmo 2, que valida atributos de usuários usando chaves mestras, grupos bilineares (G1, G2) e assinaturas digitais. O algoritmo incorpora criptografia homomórfica, permitindo cálculos sobre dados criptografados sem necessidade de descriptografia, reforçando a privacidade e a segurança em ambientes IoT sensíveis, como registros de saúde.

Interpretação: A inclusão de validação de atributos baseada em criptografia avançada e o uso de criptografia homomórfica reforçam tanto o controle de acesso quanto a confidencialidade dos dados, atendendo a requisitos críticos de privacidade em IoT de cidades inteligentes.

Dúvidas: • Qual é o custo computacional e de energia da criptografia homomórfica em dispositivos IoT de baixa potência?
• Como o modelo lida com a gestão e distribuição segura das chaves mestras em ambientes distribuídos?
• Existem limitações práticas na revogação de credenciais usando blocos de revogação descritos?

#### Página 8 — ficha 2dbba22f4a1d8872543c

O trabalho propõe um método de autenticação IoT que combina verificação de atributos contra políticas de acesso, criptografia homomórfica dos atributos armazenados em blockchain e seleção de cluster head baseada na energia da bateria. Também descreve a criptografia de registros médicos usando FHE, visando privacidade e eficiência energética.

Interpretação: A inclusão de criptografia homomórfica permite que atributos sensíveis sejam processados sem descriptografia, reforçando a privacidade. A escolha do cluster head por energia prolonga a vida útil da rede, mas pode introduzir variabilidade no caminho de comunicação. O uso de FHE para EMR demonstra viabilidade em cenários de saúde, sugerindo aplicação similar em outros domínios de IoT.

Dúvidas: Como o esquema de criptografia homomórfica afeta o tempo de verificação de atributos em tempo real? Qual o custo de armazenamento dos atributos criptografados na blockchain para grandes escalas de dispositivos? O algoritmo de seleção de cluster head considera mobilidade ou falhas de nós? Há avaliação de resistência a ataques de replay ou falsificação de atributos?

#### Página 9 — ficha 2536ded837b6511aeece

O trabalho propõe o uso de Fully Homomorphic Encryption (FHE) para criptografar dados de dispositivos IoMT, permitindo seu armazenamento e processamento seguro na nuvem, e emprega contratos inteligentes multi‑assinatura para autenticação de chaves privadas, visando confidencialidade, privacidade e prevenção de acessos não autorizados em ambientes industriais.

- FHE permite realizar computações sobre dados criptografados sem necessidade de descriptografia. — citação conferida: FHE provides maximum flexibility for supporting diverse and complex operations over encrypted data

Interpretação: O artigo demonstra que a combinação de criptografia homomórfica total com contratos inteligentes pode atender aos requisitos de privacidade e integridade de dados em IoMT, ao mesmo tempo em que oferece mecanismos de autenticação robustos para ambientes industriais.

Dúvidas: Como o custo computacional do FHE impacta a latência em aplicações de tempo real? Qual é o desempenho dos contratos multi‑assinatura em dispositivos de borda com recursos limitados?

#### Página 10 — ficha ed74cb77be163298e930

O trecho descreve o framework Trust-Aware Blockchain-based Smart Authentication and Privacy Preservation (TAB‑SAPP) que usa contratos inteligentes, ECDSA, hash Keccak e assinaturas de múltiplas partes para registrar, autenticar e operar dispositivos IoT em ambientes industriais, garantindo confidencialidade, integridade e anonimato via ECC e ring signatures.

Interpretação: O trabalho propõe uma arquitetura baseada em blockchain permissionada que centraliza funções críticas de segurança em contratos inteligentes, usando criptografia leve (ECC, ring signatures) para atender às restrições de recursos dos dispositivos IoT, ao mesmo tempo que introduz mecanismos de anonimato e verificação coletiva.

Dúvidas: Como o custo de gas e o tempo de execução dos contratos escalam com o número crescente de dispositivos? Qual o impacto da manutenção dinâmica da whitelist em termos de latência e consistência distribuída? O uso de ring signatures compromete a rastreabilidade necessária para auditorias regulatórias?

#### Página 11 — ficha c619b3f943ea6dbaa468

O artigo apresenta um método que combina criptografia de curva elíptica (ECC) com ring signatures dentro de uma blockchain permissionada (Hyperledger Fabric) para autenticação escalável e privacidade em IoT industrial. O sistema foi avaliado com AVISPA e METRE, demonstrando resistência a ataques de colusão e phishing, e mostrou melhoria no processo de autenticação ao integrar velocidade de mobilidade, reduzindo tempo de criptografia em comparação a modelos tradicionais.

- A integração de blockchain com velocidade de mobilidade melhora o processo de autenticação. — citação conferida: integration leverages the immutable and decentralized attributes of blockchain to enhance the reliability and security of authentication, while the inclusion of mobility speed ensures real-time responsiveness

Interpretação: A proposta demonstra que a união de ECC, ring signatures e blockchain pode oferecer autenticação robusta e de baixo custo computacional para IoT, especialmente em ambientes industriais onde a mobilidade dos dispositivos é alta.

Dúvidas: Como a velocidade de mobilidade afeta a latência em redes de borda? Qual o overhead adicional ao escalar o número de nós além dos testados? Como garantir a revogação de credenciais em um esquema baseado em ring signatures?

#### Página 12 — ficha dc47276240ccc7fe54f8

O trecho descreve que o framework proposto, baseado em blockchain com criptografia otimizada, mantém latência menor que modelos de referência e escala eficientemente com mais nós, oferecendo eficiência e robustez para ambientes IoT críticos.

- O framework mantém latência menor que os modelos de referência. — citação conferida: maintains lower latency levels when compared to the benchmark models

- A solução escala efetivamente com um número maior de nós. — citação conferida: scaling effectively with a higher number of nodes

Interpretação: Os resultados indicam que a integração de blockchain com mecanismos de criptografia otimizados reduz atrasos na autenticação, tornando o modelo adequado para aplicações IoT que exigem respostas em tempo real.

Dúvidas: Quais são os custos computacionais e de energia associados ao uso de assinaturas em anel e criptografia otimizada em dispositivos de borda? Como o modelo lida com a revogação de credenciais em ambientes distribuídos?

#### Página 13 — ficha 82542f090696b18ba08a

O estudo apresenta um framework permissionado baseado em blockchain que utiliza criptografia homomórfica totalmente otimizada e algoritmos criptográficos leves, demonstrando escalabilidade superior e tempos de criptografia menores à medida que aumenta o número de nós IoT. Avaliações comparativas mostram maior resistência a ataques (colusão, phishing, replay, man‑in‑the‑middle) em relação a modelos de referência, indicando adequação para comunicação segura em tempo real em ambientes de alta densidade, como cidades inteligentes e saúde.

- the proposed framework outperforms benchmark models in multiple aspects of attack resistance — citação conferida: Table 2. Comparative Analysis of Attack Resistance

Interpretação: Os resultados indicam que a combinação de blockchain permissionada, criptografia homomórfica e smart contracts multissignature reduz significativamente o tempo de criptografia e aumenta a resistência a ataques, tornando o modelo viável para IoT massiva em cidades inteligentes.

Dúvidas: Como o framework se comporta sob condições de alta latência de rede típica de edge computing? Qual o custo computacional da criptografia homomórfica em dispositivos IoT com recursos restritos? Como garantir a revogação de credenciais sem comprometer a privacidade?

#### Página 14 — ficha d448200db68c9ee0a533

O estudo apresenta um framework de autenticação que preserva a privacidade para IoT industrial, integrando avaliação de hash e verificação MAC para reduzir sobrecarga computacional e de comunicação, suportando grandes implantações e garantindo proteção de identidade via blockchain permissionada, embora dependa de um único mecanismo de blockchain.

- O framework integra avaliação de hash e verificação MAC para minimizar sobrecarga computacional e de comunicação. — citação conferida: integrates hash evaluation and MAC verification to minimize computational and communication overhead

Interpretação: O artigo demonstra que a combinação de hash, MAC e blockchain permissionada pode atender às exigências de autenticação em larga escala para IoT industrial, reduzindo latência e mantendo a privacidade, porém a solução ainda carece de flexibilidade devido ao uso de um único tipo de blockchain.

Dúvidas: Como a introdução de algoritmos de consenso afetará a latência e a leveza da autenticação? Qual seria o impacto da integração de deep learning sobre os requisitos de recursos nos dispositivos de borda?

#### Página 15 — ficha 1b7d15939d9e55a44fb2

O trecho apresenta apenas a referência bibliográfica do artigo, indicando o Journal of Cyber Security and Risk Auditing, volume 2025, número 4, e o ISSN da publicação.

- O artigo está publicado no Journal of Cyber Security and Risk Auditing, volume 2025, número 4. — citação conferida: Journal of Cyber Security and Risk Auditing Vol.2025, No.4

Interpretação: O trecho não contém conteúdo técnico ou descritivo do trabalho, limitando‑se a informações de publicação.

Dúvidas: Não há informações sobre problema, solução, avaliação ou limites no trecho fornecido.

#### Página 16 — ficha b215fd9447590448d50b

O artigo apresenta uma abordagem permissionada baseada em blockchain para autenticação IoT escalável e com preservação de privacidade. Os autores, Dr. Santosh Reddy Addula e Dr. Aitizaz Ali, possuem ampla experiência em IA, ML, IoT, segurança cibernética e blockchain, reforçando a credibilidade da proposta. O trabalho integra avaliação de hash e verificação MAC, mantendo latência inferior aos modelos de referência.

- Os autores têm experiência em blockchain, IoT e segurança cibernética. — citação conferida: research focuses on Artificial Intelligence, Machine Learning, IoT, Cybersecurity, Blockchain

- Um dos autores atua como revisor de revistas renomadas em IoT e segurança. — citação conferida: He was the Reviewer of IEEE Internet of Things Journal, IEEE Transactions on Network Science and Engineering, IEEE Access

Interpretação: O trecho acrescenta informações biográficas que confirmam a expertise dos autores nas áreas centrais do trabalho (IoT, blockchain, segurança), mas não traz novos detalhes técnicos sobre a solução proposta.

Dúvidas: Faltam informações sobre a arquitetura específica da blockchain permissionada, métricas detalhadas de desempenho e como a privacidade é garantida além da verificação de hash e MAC.

<!-- agente:fim -->
