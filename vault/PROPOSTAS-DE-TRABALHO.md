# Possíveis propostas de trabalho

Atualizado: 2026-09-21T07:21:38

Linha atual: segurança em cidades inteligentes com identidade autosoberana, com atenção a criptografia baseada em atributos e/ou homomórfica quando a lacuna justificar.

Use `AVALIAR-PROPOSTAS.md` para marcar `muito_interessante`, `gostei`, `neutra` ou `descartar`; o agente usa esse feedback nas próximas buscas.



## 1. [[trabalhos/Cardoso_2024|Cardoso (2024)]]: Integrar identidades autossoberanas (SSI) e credenciais verificáveis ao modelo baseado em 

**Ideia do trabalho**

Integrar identidades autossoberanas (SSI) e credenciais verificáveis ao modelo baseado em Hyperledger Fabric.

**Lacuna explorada**

Ausência de requisitos funcionais e não funcionais detalhados para o modelo.

**Como desenvolver e avaliar**

descricao: Implementar um módulo de identidade autossoberana (SSI) baseado em DID e credenciais verificáveis sobre uma rede Hyperledger Fabric. O módulo deve suportar emissão, apresentação, verificação, revogação e recuperação de credenciais usando criptografia de atributos (ABE) e, opcionalmente, criptografia homomórfica para consultas de dados IoT. Comparar o desempenho e a privacidade do sistema proposto com (i) o modelo de gestão de identidades para cidades inteligentes baseado em blockchain descrito por [[trabalhos/Cardoso_2024|Cardoso (2024)]] e (ii) a solução padrão de identidade do Hyperledger Fabric que utiliza certificados X.509.; fases: Emissão de credenciais SSI via Hyperledger Fabric CA + Aries/Indy; Apresentação e verificação em serviços de IoT de cidade inteligente (ex.: sensores de tráfego); Revogação de credenciais usando listas de revogação distribuídas (CRL) e protocolos de atualização de DID; Recuperação de acesso perdido via chaves de recuperação criptograficamente protegidas; Processamento de dados agregados com criptografia homomórfica para análise de mobilidade

**Recursos, ferramentas e dados possíveis**

dados: Conjunto de dados de tráfego urbano aberto (ex.: Open Traffic Data – disponível em data.gov.br); Logs de transações simuladas de serviços públicos (gerados via script de carga); Metadados de identidade sintéticos (gerados conforme o padrão W3C DID); ferramentas: Hyperledger Fabric v2.5 (disponível no GitHub oficial); Hyperledger Aries Framework Go (para agentes SSI); Hyperledger Indy (para armazenamento de DIDs e credenciais); Biblioteca de ABE – Charm-Crypto (Python) ou libfenc (C); Biblioteca de criptografia homomórfica – Microsoft SEAL (C++); Docker Compose para orquestração de nós Fabric e agentes SSI; Prometheus + Grafana para coleta de métricas; infraestrutura: Cluster de 3 máquinas virtuais (2 CPU, 8 GB RAM cada) em um provedor de nuvem pública (ex.: AWS, GCP) – recursos padrão disponíveis; Repositório Git para código‑fonte e scripts de experimentos

**Métricas de avaliação**

Latência média (ms) para emissão, apresentação e verificação de credenciais; Throughput (transações/segundo) da rede Fabric com e sem módulo SSI; Consumo de memória e CPU dos nós Fabric e dos agentes SSI durante carga sustentada; Tempo de propagação de revogação (ms) até que todos os nós reconheçam a credencial revogada; Taxa de sucesso na recuperação de acesso perdido (percentual); Precisão e tempo de consultas homomórficas sobre dados agregados (erro relativo, ms); Indicadores de privacidade – entropia de atributos divulgados vs. atributos requeridos

**Riscos, limites e incertezas**

Ideia preliminar baseada em um único trabalho; pode ser enfraquecida ou já estar resolvida por trabalhos posteriores.

**Perguntas para reunião com orientador**

Qual estratégia de armazenamento de DIDs (Indy vs. Fabric ledger) oferece melhor escalabilidade em cenários de milhares de cidadãos?; Deveríamos usar ABE baseada em CP‑ABE ou KP‑ABE para controle de acesso a sensores IoT, considerando a complexidade de gerenciamento de chaves?; Qual abordagem de revogação (CRL distribuída, status de credencial on‑chain ou protocolos de atualização de DID) minimiza latência sem sobrecarregar a rede?; É viável integrar criptografia homomórfica para análises de mobilidade em tempo real sem comprometer a latência exigida pelos serviços de trânsito?; Como garantir interoperabilidade entre o módulo SSI e sistemas legados que ainda utilizam certificados X.509 no Fabric?; Qual conjunto de métricas de privacidade (ex.: diferencial de privacidade, entropia) é mais adequado para avaliar a exposição de atributos nas credenciais?; Qual carga de trabalho (número de transações simultâneas, tamanho das credenciais) deve ser adotada para refletir um cenário realista de cidade inteligente?

**Fontes que sustentam**

- [[trabalhos/Cardoso_2024|Cardoso (2024)]] — André Luiz Almeida Cardoso

**Tags temáticas**

#abe #criptografia #criptografia-homomorfica #privacidade #ssi

**Próximas buscas sugeridas**

- André Luiz Almeida Cardoso limitations future work
- André Luiz Almeida Cardoso smart cities IoT blockchain access control



## 2. [[trabalhos/Cardoso_2024|Cardoso (2024)]]: Aplicar criptografia baseada em atributos (ABE) para controle de acesso seletivo e divulga

**Ideia do trabalho**

Aplicar criptografia baseada em atributos (ABE) para controle de acesso seletivo e divulgação mínima de atributos.

**Lacuna explorada**

Ausência de requisitos funcionais e não funcionais detalhados para o modelo.

**Como desenvolver e avaliar**

Problema específico: em cidades inteligentes, sensores IoT e serviços públicos exigem controle de acesso granular que preserve a privacidade dos cidadãos, mas os modelos atuais baseados apenas em blockchain não garantem divulgação mínima de atributos. Hipótese: a combinação de Self‑Sovereign Identity (SSI) com criptografia baseada em atributos (ABE) permite que o cidadão autorize o acesso a dados IoT usando credenciais verificáveis que revelam apenas os atributos necessários, reduzindo a superfície de ataque e facilitando a revogação seletiva. Arquitetura/artefato: um protótipo de carteira digital SSI que emite Verifiable Credentials (VCs) contendo políticas ABE; um serviço de verificação que, ao receber uma apresentação, descodifica a política e aplica a decriptação ABE para liberar o recurso IoT. Etapas: (1) modelar o ciclo de vida da credencial (emissão, apresentação, verificação, revogação, recuperação); (2) implementar a carteira usando Hyperledger Aries e integrar biblioteca CP‑ABE (ex.: libfenc); (3) criar um sandbox de sensores IoT simulados (Smart City Lab) que requer atributos como "residente", "classe de tarifa"; (4) comparar contra baseline que usa apenas VC sem ABE. Cenário de avaliação: testes em ambiente de simulação de tráfego urbano com 10 000 solicitações de acesso, medindo latência, taxa de sucesso de verificação e vazamento de atributos.

**Recursos, ferramentas e dados possíveis**

Ferramentas: Hyperledger Aries/Indy para SSI, libfenc ou Charm‑Crypto para CP‑ABE, Docker para orquestração, Node.js/Express para APIs de verificação, PostgreSQL para armazenamento de revogação. Dados/Simuladores: Smart City Lab (simulador de sensores de tráfego, iluminação e coleta de resíduos) disponível em repositório público; conjuntos de atributos sintéticos baseados em perfis de residentes (ex.: idade, zona, nível de renda). Padrões: W3C Verifiable Credentials, Decentralized Identifiers (DID), OpenID Connect para integração com serviços municipais. Bibliotecas: did‑jwt‑vc, jsonld‑signatures, Open Policy Agent (OPA) para políticas de acesso. Todas as ferramentas citadas são de código aberto e documentadas, sem necessidade de licenças proprietárias.

**Métricas de avaliação**

Desempenho: latência média da verificação (ms), throughput (solicitações/s) e consumo de memória da carteira SSI durante sessões prolongadas. Segurança: número de tentativas de acesso não autorizadas detectadas, taxa de sucesso de ataques de replay e análise de superfície de ataque (atributos expostos). Privacidade: quantidade de atributos revelados por transação (medida em bits) comparada ao baseline sem ABE; índice de anonimato (k‑anonymity) dos logs de acesso. Usabilidade/Interoperabilidade: tempo de emissão e recuperação de credenciais (segundos), taxa de falha de interoperabilidade entre diferentes provedores de identidade (ex.: Aries vs. DIF), e avaliação qualitativa de usuários (escala Likert) sobre clareza do consentimento de atributos.

**Riscos, limites e incertezas**

Ideia preliminar baseada em um único trabalho; pode ser enfraquecida ou já estar resolvida por trabalhos posteriores.

**Perguntas para reunião com orientador**

1. O escopo de atributos (ex.: residência, classe tarifária) é suficiente para demonstrar controle seletivo ou devemos incluir atributos sensíveis (ex.: saúde) para ampliar a relevância? 2. Qual baseline acadêmico seria mais adequado: um modelo SSI puro baseado em blockchain (ex.: [[trabalhos/Cardoso_2024|Cardoso (2024)]]) ou um sistema de controle de acesso ABE sem SSI? 3. Existe disponibilidade de um dataset real de sensores IoT de cidades brasileiras que possamos usar em vez de simuladores? 4. Qual a profundidade esperada para a avaliação de revogação de credenciais (tempo de propagação, impacto na latência)? 5. Devemos priorizar a implementação de políticas OPA ou usar políticas estáticas codificadas? 6. Há necessidade de validar a solução com usuários finais (cidadãos) ou basta avaliação técnica? 7. Como alinhar a proposta com requisitos da LGPD e possíveis auditorias de privacidade?

**Fontes que sustentam**

- [[trabalhos/Cardoso_2024|Cardoso (2024)]] — André Luiz Almeida Cardoso

**Tags temáticas**

#abe #criptografia #criptografia-homomorfica #privacidade #ssi

**Próximas buscas sugeridas**

- André Luiz Almeida Cardoso limitations future work
- André Luiz Almeida Cardoso smart cities IoT blockchain access control



## 3. [[trabalhos/Cardoso_2024|Cardoso (2024)]]: Desenvolver mecanismos de revogação distribuída (registradores on‑chain) e protocolos de r

**Ideia do trabalho**

Desenvolver mecanismos de revogação distribuída (registradores on‑chain) e protocolos de recuperação social ou baseada em chaves distribuídas.

**Lacuna explorada**

Ausência de requisitos funcionais e não funcionais detalhados para o modelo.

**Como desenvolver e avaliar**

Problema específico: em cidades inteligentes, a revogação de credenciais SSI e a recuperação de acesso perdido por cidadãos são pouco estudadas, sobretudo em ambientes distribuídos onde os registradores on‑chain podem ser vulneráveis a atrasos ou falhas de consenso. Hipótese: um mecanismo de revogação distribuída baseado em registradores on‑chain combinados a protocolos de recuperação social (p. ex., delegação de chaves a contatos de confiança) ou a esquemas de chaves distribuídas (threshold‑cryptography) melhora a disponibilidade de serviços e reduz o risco de perda permanente de identidade, sem comprometer a privacidade. Arquitetura/artefato: extensão do modelo de gestão de identidades proposto por [[trabalhos/Cardoso_2024|Cardoso (2024)]] – que já usa blockchain para registro de identidades – incorporando um contrato inteligente de revogação que aceita provas de perda (ex.: assinatura de múltiplos guardiões) e um módulo de recuperação que gera chaves de recuperação via Shamir Secret Sharing. Etapas: (1) análise do modelo de [[trabalhos/Cardoso_2024|Cardoso (2024)]]; (2) design do contrato de revocação e do protocolo de recuperação; (3) implementação em uma rede de teste Ethereum (Goerli) usando Solidity; (4) integração com um wallet SSI (ex.: DIF Universal Resolver) e com um simulador de serviços IoT de cidade inteligente; (5) avaliação comparativa contra baseline sem revogação (modelo original) e contra soluções centralizadas de revogação. Cenário de avaliação: usuários simulados (n=200) interagem com serviços de estacionamento e coleta de resíduos; métricas de tempo de revogação, taxa de sucesso de recuperação e consumo de gas são coletados.

**Recursos, ferramentas e dados possíveis**

Ferramentas: Solidity para contratos inteligentes, Hardhat ou Truffle para deployment, Goerli testnet (ou local Ganache) como blockchain pública; biblioteca DID‑Auth (ex.: did‑jwt) para geração e verificação de credenciais verificáveis; Hyperledger Aries/Indy para wallet SSI; biblioteca de secret sharing (ex.: sss‑js) para recuperação distribuída; simulador de IoT urbano (ex.: CityPulse ou OpenIoT) para gerar fluxos de dados de sensores. Dados: conjuntos de atributos de cidadãos (nome, CPF, atributos de residência) e de sensores (localização, tipo de serviço) disponíveis em repositórios públicos de cidades inteligentes (ex.: Open Data Porto Alegre). Padrões: W3C Verifiable Credentials, Decentralized Identifiers (DID), W3C DID‑Auth, OIDC‑4‑VP. Bibliotecas criptográficas: libsodium para ABE (ex.: cp‑abe‑js) e Microsoft SEAL (via WebAssembly) para criptografia homomórfica, caso se deseje avaliar processamento de dados privados. Todas as ferramentas citadas são de código aberto e disponíveis em repositórios públicos; não foram criadas fontes fictícias.

**Métricas de avaliação**

Desempenho: tempo médio (ms) para registrar revogação no contrato inteligente, tempo de geração e verificação de credenciais pós‑revogação, consumo de gas (ETH) por operação de revogação e recuperação. Segurança: taxa de falsos positivos/negativos na detecção de perda de chave, resistência a ataques de replay e de negação de serviço (DoS) nos registradores on‑chain. Privacidade: grau de anonimato mantido (medido por entropia de atributos divulgados) e avaliação de vazamento de metadados durante o protocolo de recuperação (ex.: número de guardiões revelados). Usabilidade/Interoperabilidade: número de serviços IoT que aceitam credenciais revogadas/reemitidas sem reconfiguração, taxa de sucesso de usuários finais ao recuperar acesso usando apenas contatos de confiança, e compatibilidade com padrões DID e VC (verificação de conformidade com testes de interoperabilidade do W3C).

**Riscos, limites e incertezas**

Ideia preliminar baseada em um único trabalho; pode ser enfraquecida ou já estar resolvida por trabalhos posteriores.

**Perguntas para reunião com orientador**

1. Qual nível de tolerância a latência é aceitável para revogação de credenciais em serviços críticos (ex.: controle de tráfego) e como podemos validar isso em ambiente de teste? 2. Quantos guardiões (threshold) seriam suficientes para equilibrar segurança contra ataques de engenharia social e usabilidade para o cidadão? 3. Deveríamos priorizar sidechains ou soluções de rollup para reduzir custos de gas, e quais trade‑offs de segurança isso implica? 4. Como integrar o módulo de recuperação com wallets SSI existentes (ex.: Aries) sem exigir alterações significativas nos padrões DID? 5. Existe algum benchmark público de ABE ou homomorphic encryption em dispositivos IoT que possamos usar como baseline para comparar o overhead introduzido? 6. Quais métricas de privacidade (ex.: entropia de atributos) são mais relevantes para o orientador ao avaliar a eficácia do protocolo de recuperação?

**Fontes que sustentam**

- [[trabalhos/Cardoso_2024|Cardoso (2024)]] — André Luiz Almeida Cardoso

**Tags temáticas**

#abe #criptografia #criptografia-homomorfica #privacidade #ssi

**Próximas buscas sugeridas**

- André Luiz Almeida Cardoso limitations future work
- André Luiz Almeida Cardoso smart cities IoT blockchain access control



## 4. [[trabalhos/Maia_2025|Maia (2025)]]: Incorporar revocation registries baseados em blockchain para revogação em tempo real

**Ideia do trabalho**

Incorporar revocation registries baseados em blockchain para revogação em tempo real

**Lacuna explorada**

Mecanismos concretos de revogação de credenciais em larga escala e em tempo real

**Como desenvolver e avaliar**

Problema específico: em ambientes de cidades inteligentes, credenciais digitais emitidas por identidades autosoberanas (SSI) podem ser comprometidas ou perder validade, gerando risco de acessos não autorizados, fraudes e ataques de negação de serviço, conforme apontado no TCC de [[trabalhos/Maia_2025|Maia (2025)]]. Hipótese: a integração de um registro de revogação (revocation registry) baseado em blockchain permitirá revogar credenciais em tempo real, reduzindo a janela de exploração de credenciais comprometidas sem impactar significativamente a latência das operações de emissão e verificação. Arquitetura/artefato: um módulo de revogação implementado como contrato inteligente em uma rede permissionada (ex.: Hyperledger Fabric) conectado ao middleware InterSCity via Resource Adaptor; as credenciais são Verifiable Credentials (VC) armazenadas em wallets SSI dos cidadãos. Etapas: (1) modelagem do esquema de revogação (bitmap ou Merkle tree); (2) desenvolvimento do contrato inteligente; (3) extensão do fluxo de emissão/apresentação para consultar o registro antes da aceitação; (4) testes de carga simulando milhares de solicitações de revogação e verificação; (5) comparação com baseline sem revogação (modelo proposto no TCC). Cenário de avaliação: ambiente de teste com sensores IoT simulados (e.g., CityPulse) e usuários virtuais que emitem, perdem e recuperam credenciais, medindo latência, taxa de sucesso de revogação e impacto na experiência do usuário.

**Recursos, ferramentas e dados possíveis**

Ferramentas: Hyperledger Fabric (para blockchain permissionada), Aries Framework Go (para SSI e VC), Docker/Kubernetes (orquestração de microsserviços), InterSCity platform (para integração IoT), Postman (testes de API). Dados/Simuladores: datasets públicos de tráfego urbano (ex.: Open Data Porto Alegre) e geradores de carga como Locust para simular milhares de requisições de emissão e revogação. Padrões e bibliotecas: W3C Verifiable Credentials, Decentralized Identifiers (DID) Core, OpenID Connect for Verifiable Presentations, libp2p (para comunicação P2P), Crypto++ (para ABE e homomorphic encryption caso se deseje estender). Todas as ferramentas citadas são de código aberto e disponíveis em repositórios públicos; não há indicação de disponibilidade de datasets específicos de revogação, portanto será necessário gerar dados sintéticos baseados nos cenários descritos no TCC de 2025.

**Métricas de avaliação**

Desempenho: latência média (ms) das operações de emissão, apresentação e verificação com e sem consulta ao registro de revogação; throughput (transações por segundo) suportado pelo contrato inteligente. Segurança: taxa de falsos positivos/negativos na detecção de credenciais revogadas; análise de vulnerabilidades do contrato (ex.: reentrancy). Privacidade: avaliação do vazamento de atributos ao consultar o registro (medido por entropia de informação revelada). Usabilidade/Interoperabilidade: tempo de resposta percebido pelo usuário final (tempo de carregamento da wallet); compatibilidade com padrões W3C VC/DID testada em diferentes wallets (ex.: Trinsic, Veramo). Cada métrica será coletada em múltiplas execuções para cálculo de intervalos de confiança (95%).

**Riscos, limites e incertezas**

Ideia preliminar baseada em um único trabalho; pode ser enfraquecida ou já estar resolvida por trabalhos posteriores.

**Perguntas para reunião com orientador**

1. Qual a tolerância de latência aceitável para processos de revogação em serviços críticos de cidades inteligentes (ex.: controle de tráfego, energia)? 2. Deveríamos priorizar uma rede permissionada (ex.: Hyperledger) ou explorar soluções públicas (ex.: Ethereum) considerando requisitos de governança? 3. Como validar a interoperabilidade do registro de revogação com diferentes wallets SSI já existentes no mercado? 4. Qual abordagem de estrutura de revogação (bitmap vs. Merkle tree) oferece melhor trade‑off entre tamanho do registro e velocidade de consulta? 5. É viável incluir ABE ou criptografia homomórfica no mesmo contrato inteligente ou devemos tratá‑los como módulos externos ao blockchain? 6. Que critérios de auditoria de segurança do contrato inteligente são recomendados para garantir que a revogação não introduza novas vulnerabilidades?

**Fontes que sustentam**

- [[trabalhos/Maia_2025|Maia (2025)]] — Danilo_TCC_final

**Tags temáticas**

#abe #criptografia #criptografia-homomorfica #privacidade #ssi

**Próximas buscas sugeridas**

- Danilo_TCC_final limitations future work
- Danilo_TCC_final smart cities IoT blockchain access control



## 5. [[trabalhos/Maia_2025|Maia (2025)]]: Desenvolver protocolos de recuperação de credenciais usando secret sharing, agentes de con

**Ideia do trabalho**

Desenvolver protocolos de recuperação de credenciais usando secret sharing, agentes de confiança ou chaves distribuídas

**Lacuna explorada**

Mecanismos concretos de revogação de credenciais em larga escala e em tempo real

**Como desenvolver e avaliar**

Problema específico: cidadãos de cidades inteligentes perdem o acesso às suas credenciais digitais (verifiable credentials) e não há mecanismo confiável de recuperação que preserve a soberania da identidade e a privacidade dos atributos. Hipótese: a combinação de Self‑Sovereign Identity (SSI) com esquemas de secret sharing (ex.: Shamir) e agentes de confiança distribuídos permite a recuperação segura de credenciais sem revelar atributos sensíveis e sem depender de um provedor central. Arquitetura/artefato: um protótipo de wallet SSI baseado em Hyperledger Aries que incorpora um módulo de recuperação. O módulo divide a chave‑mestra da wallet em n fragmentos, distribuídos entre agentes de confiança (ex.: prefeitura, provedor de serviços IoT, e um nó de blockchain). Em caso de perda, o cidadão solicita a recomposição mediante prova de posse de atributos (zero‑knowledge). Etapas: (1) modelagem do ciclo de vida da credencial (emissão, apresentação, verificação, transmissão, processamento, armazenamento, revogação, recuperação); (2) implementação do módulo de secret sharing e protocolos de consenso para recomposição; (3) integração com o modelo de controle de acesso proposto por [[trabalhos/Maia_2025|Maia (2025)]], que já usa blockchain e SSI para autenticação; (4) definição de cenários de teste (emissão de credencial para acesso a sensores de trânsito, revogação por violação de política, recuperação após perda de dispositivo). Baseline: solução de recuperação baseada em recuperação de senha tradicional (centralizada) e a abordagem de [[trabalhos/Maia_2025|Maia (2025)]] que não contempla recuperação. Cenário de avaliação: ambiente de simulação InterSCity com 1 000 cidadãos virtuais, 200 sensores IoT e 5 agentes de confiança, medindo latência de recomposição, taxa de sucesso e vazamento de atributos. Esta proposta é uma inferência exploratória a partir do trabalho de Danilo, que não trata recuperação de credenciais.

**Recursos, ferramentas e dados possíveis**

Ferramentas: Hyperledger Aries/Indy para wallet SSI, Hyperledger Fabric ou Ethereum para contratos inteligentes de revogação, biblioteca de secret sharing (ex.: sss-js ou Shamir‑Secret‑Sharing em Go), framework de simulação InterSCity (disponível no repositório da comunidade). Dados/simuladores: datasets de tráfego urbano públicos (ex.: Open Data São Paulo) para gerar atributos de credenciais, e geradores de carga (Locust) para simular 1 000 usuários. Padrões: W3C Verifiable Credentials, Decentralized Identifiers (DID), OAuth 2.0‑DID‑Auth, e ISO/IEC 24760‑2 (identidade digital). Bibliotecas: Aries Cloud Agent‑Python, DID‑Comm, libp2p para comunicação P2P entre agentes de confiança, e libs de criptografia homomórfica (Microsoft SEAL) caso se deseje processamento privativo de atributos. Todas as ferramentas citadas são de código aberto e já disponíveis em repositórios públicos; não foram criadas novas ferramentas.

**Métricas de avaliação**

Desempenho: latência média (ms) da recomposição da chave‑mestra, throughput (recomposições/s) sob carga de 100 solicitações simultâneas, consumo de recursos (CPU/memória) nos agentes de confiança. Segurança: taxa de sucesso de ataques de reconstrução por adversário com menos de n‑1 fragmentos, resistência a replay e DoS medidos por número de solicitações rejeitadas. Privacidade: quantidade de atributos expostos durante o protocolo de recuperação (medido em bits), avaliação de vazamento usando métricas de informação mutua. Usabilidade/Interoperabilidade: tempo de configuração da wallet pelo cidadão, número de passos necessários para iniciar a recuperação, compatibilidade com wallets existentes (ex.: Trinsic, Veramo) testada via DID‑Comm. Cada métrica será comparada entre o protótipo proposto e o baseline centralizado, permitindo quantificar ganhos e trade‑offs.

**Riscos, limites e incertezas**

Ideia preliminar baseada em um único trabalho; pode ser enfraquecida ou já estar resolvida por trabalhos posteriores.

**Perguntas para reunião com orientador**

1. Qual o número ideal de fragmentos (n) e o limiar (k) para equilibrar segurança e usabilidade no contexto de cidades inteligentes? 2. Como garantir que os agentes de confiança cumpram políticas de retenção e destruição de fragmentos conforme LGPD/ GDPR? 3. Existe algum padrão emergente para recuperação de credenciais SSI que deveríamos alinhar, ou devemos propor um novo? 4. Qual baseline de recuperação centralizada seria mais adequado para comparação (ex.: recuperação por e‑mail, por suporte técnico)? 5. Como integrar o módulo de recuperação ao fluxo de revogação já implementado no TCC de [[trabalhos/Maia_2025|Maia (2025)]] sem introduzir vulnerabilidades de replay? 6. Quais métricas de usabilidade são mais relevantes para cidadãos não técnicos em ambientes urbanos? 7. Há disponibilidade de datasets de incidentes de perda de credenciais que possamos usar para validar cenários realistas?

**Fontes que sustentam**

- [[trabalhos/Maia_2025|Maia (2025)]] — Danilo_TCC_final

**Tags temáticas**

#abe #criptografia #criptografia-homomorfica #privacidade #ssi

**Próximas buscas sugeridas**

- Danilo_TCC_final limitations future work
- Danilo_TCC_final smart cities IoT blockchain access control



## 6. [[trabalhos/Maia_2025|Maia (2025)]]: Integrar criptografia baseada em atributos (ABE) ou criptografia homomórfica nos fluxos de

**Ideia do trabalho**

Integrar criptografia baseada em atributos (ABE) ou criptografia homomórfica nos fluxos de emissão, verificação e processamento de dados sensíveis

**Lacuna explorada**

Mecanismos concretos de revogação de credenciais em larga escala e em tempo real

**Como desenvolver e avaliar**

Problema específico: nos fluxos de emissão, apresentação e processamento de credenciais verificáveis em cidades inteligentes, ainda não há mecanismos que garantam controle de acesso baseado em atributos ou processamento de dados sensíveis sem revelar conteúdo, o que pode levar a acessos não autorizados e vazamento de informações pessoais. Hipótese: a integração de criptografia baseada em atributos (ABE) e criptografia homomórfica (HE) ao ciclo de vida das credenciais SSI reduzirá o risco de exposição de dados e permitirá políticas de acesso mais granulares, sem degradar significativamente a latência das operações. Arquitetura/artefato: um middleware estendido sobre a pilha InterSCity que conecta carteiras digitais (W3C VC/DID) a sensores IoT via um Resource Adaptor; o middleware incorpora um módulo ABE para encriptação de atributos nas credenciais e um módulo HE para permitir consultas agregadas sobre dados criptografados. Etapas: (1) modelar políticas de acesso em ABE; (2) implementar wrappers ABE/HE em agentes Aries; (3) adaptar contratos inteligentes para revogação baseada em atributos; (4) executar cenários de emissão, verificação e processamento de dados IoT; (5) comparar com baseline do modelo de [[trabalhos/Maia_2025|Maia (2025)]] que usa apenas blockchain e SSI. Cenário de avaliação: ambiente de teste com o simulador InterSCity, 10.000 dispositivos IoT simulados, medindo latência, throughput e taxa de sucesso de revogação. Fonte: [[trabalhos/Maia_2025|Maia (2025)]] descreve o modelo base e sugere a integração de ABE/HE como possibilidade exploratória.

**Recursos, ferramentas e dados possíveis**

Ferramentas: Hyperledger Indy/Aries para identidade descentralizada, Aries Cloud Agent‑Python, blockchain Ethereum ou Hyperledger Fabric para contratos inteligentes, bibliotecas de ABE como Charm‑Crypto (cp‑abe) e de HE como Microsoft SEAL ou PALISADE. Dados/simuladores: InterSCity (simulador de cidades inteligentes) com cenários de tráfego de sensores IoT, datasets sintéticos de consumo de energia e mobilidade urbana disponíveis no repositório da própria plataforma. Padrões: W3C Verifiable Credentials, Decentralized Identifiers (DID), OAuth 2.0 / OIDC para integração de serviços, ISO/IEC 24760 para identidade digital. Bibliotecas auxiliares: libp2p para comunicação P2P, Docker/Kubernetes para orquestração de microsserviços. Todas as ferramentas citadas são de código aberto e documentadas; nenhuma foi criada especificamente para este estudo, portanto a disponibilidade depende de versões estáveis já publicadas.

**Métricas de avaliação**

Desempenho: latência média (ms) nas fases de emissão, apresentação e verificação de credenciais; throughput (credenciais/s) sob carga de 10 k dispositivos; uso de CPU/memória dos módulos ABE/HE. Segurança: taxa de falsos positivos/negativos em detecção de acessos não autorizados; tempo de revogação de credenciais (ms) comparado ao baseline. Privacidade: medida de vazamento de atributos (entropia residual) antes e depois da aplicação de ABE/HE; número de consultas agregadas possíveis sem descriptografia. Usabilidade/Interoperabilidade: número de passos necessários ao cidadão para autorizar acesso via carteira digital; compatibilidade com padrões VC/DID (conformidade W3C); taxa de sucesso de integração com serviços existentes do InterSCity. Cada métrica será coletada em múltiplas execuções para cálculo de intervalos de confiança de 95 %.

**Riscos, limites e incertezas**

Ideia preliminar baseada em um único trabalho; pode ser enfraquecida ou já estar resolvida por trabalhos posteriores.

**Perguntas para reunião com orientador**

1. Qual o nível de granularidade de políticas de acesso baseado em atributos que o orientador considera suficiente para validar a proposta? 2. O uso de HE deve ser limitado a consultas agregadas ou também a operações de classificação de dados sensíveis? 3. É viável usar o simulador InterSCity como ambiente de avaliação final ou seria necessário um deployment piloto em uma zona de teste real? 4. Qual baseline de comparação seria mais adequado: o modelo de [[trabalhos/Maia_2025|Maia (2025)]] ou algum trabalho recente de SSI sem ABE/HE encontrado em OpenAlex? 5. Existem restrições de hardware (ex.: dispositivos IoT de baixa potência) que devemos considerar ao escolher entre bibliotecas ABE/HE? 6. Como medir de forma objetiva o impacto na usabilidade da carteira digital para o cidadão ao introduzir processos de descriptografia de atributos?

**Fontes que sustentam**

- [[trabalhos/Maia_2025|Maia (2025)]] — Danilo_TCC_final

**Tags temáticas**

#abe #criptografia #criptografia-homomorfica #privacidade #ssi

**Próximas buscas sugeridas**

- Danilo_TCC_final limitations future work
- Danilo_TCC_final smart cities IoT blockchain access control



## 7. [[trabalhos/Fioreze_2026|Fioreze (2026)]]: Investigar a integração de identidades auto‑soberanas (SSI/DIDs) com políticas de controle

**Ideia do trabalho**

Investigar a integração de identidades auto‑soberanas (SSI/DIDs) com políticas de controle de acesso baseadas em ABE para ambientes IIoT; explorar credenciais verificáveis como mecanismo de autenticação de dispositivos IoT em cadeias de suprimentos; propor extensões que combinam criptografia homomórfica com smart contracts para auditoria de acesso sem revelar dados sensíveis; avaliar estratégias de revogação distribuída de credenciais em redes industriais sem intermediário central.

**Lacuna explorada**

Traditional solutions tend to depend on centralized intermediaries

**Como desenvolver e avaliar**

Problema específico: A governança e a segurança da interoperabilidade de dados IIoT ainda dependem de intermediários centralizados, limitando a granularidade de controle de acesso e a revogação eficiente ([[trabalhos/Fioreze_2026|Fioreze (2026)]]). Hipótese: A combinação de identidades auto‑soberanas (SSI/DIDs) com políticas de controle de acesso baseadas em Attribute‑Based Encryption (ABE) permite que dispositivos e cidadãos autenticados provem atributos seletivamente, reduzindo a necessidade de autoridades centrais e melhorando a revogação distribuída. Arquitetura/artefato: Um protótipo composto por (i) camada de identidade SSI usando Hyperledger Indy/DIDs, (ii) motor de ABE (OpenABE) para gerar chaves de política, (iii) blockchain permissionada (Hyperledger Fabric) para registro de credenciais verificáveis e smart contracts que executam auditoria homomórfica (Microsoft SEAL) sem expor dados brutos, e (iv) módulo de revogação baseada em accumulator de credenciais. Etapas: 1) modelagem de políticas de acesso para um caso‑de‑uso de cadeia de suprimentos IIoT; 2) implementação da emissão de credenciais verificáveis vinculadas a DIDs; 3) integração do motor ABE para criptografia de atributos nos payloads IoT; 4) desenvolvimento de smart contracts que realizam consultas homomórficas sobre logs de acesso; 5) teste de revogação via accumulator distribuído. Baseline: O framework blockchain‑enabled ABE descrito na dissertação de [[trabalhos/Fioreze_2026|Fioreze (2026)]], que não inclui SSI nem homomorphic auditing. Cenário de avaliação: Simulação de 1 000 dispositivos IIoT em um ambiente de fábrica digital usando o simulador iot‑sim, medindo latência de autenticação, throughput de transações, taxa de sucesso de revogação e nível de privacidade (atributos revelados).

**Recursos, ferramentas e dados possíveis**

Ferramentas: Hyperledger Indy/Aries para gestão de DIDs e credenciais verificáveis; Hyperledger Fabric para blockchain permissionada; OpenABE (biblioteca C++) para criptografia baseada em atributos; Microsoft SEAL (C++) para operações homomórficas; Docker/Kubernetes para orquestração de micro‑serviços. Dados/Simuladores: iot‑sim (simulador de dispositivos IIoT) e CityPulse (dataset de fluxos de sensores urbanos) para gerar tráfego de mensagens. Padrões: W3C Verifiable Credentials, Decentralized Identifiers (DID) Core Specification, ISO/IEC 24760‑2 (identidade digital). Bibliotecas auxiliares: Aries Cloud Agent‑Python, Fabric SDK Go/Node, Open Policy Agent (OPA) para definição de políticas ABE, Prometheus/Grafana para coleta de métricas. Todas as ferramentas citadas são de código aberto e disponíveis em repositórios públicos, sem necessidade de licenças proprietárias.

**Métricas de avaliação**

Desempenho: latência média (ms) da emissão e apresentação de credenciais, throughput (transações/s) da blockchain, tempo de execução de consultas homomórficas. Segurança: número de tentativas de ataque de replay ou spoofing mitigadas, taxa de detecção de chaves comprometidas, robustez da revogação (tempo até a invalidação efetiva). Privacidade: percentual de atributos revelados versus atributos necessários (medida de seletividade), entropia de dados expostos nos logs auditados. Usabilidade/Interoperabilidade: tempo de onboarding de novos dispositivos (s), conformidade com W3C VC/DID (percentual de mensagens válidas), compatibilidade com padrões de troca de dados IIoT (OPC-UA, MQTT). Cada métrica será coletada em cenários controlados e comparada ao baseline da solução ABE‑only de [[trabalhos/Fioreze_2026|Fioreze (2026)]] para quantificar ganhos ou trade‑offs introduzidos pela camada SSI e pela auditoria homomórfica.

**Riscos, limites e incertezas**

Ideia preliminar baseada em um único trabalho; pode ser enfraquecida ou já estar resolvida por trabalhos posteriores.

**Perguntas para reunião com orientador**

1) Qual o nível de profundidade esperado para a integração SSI/DIDs no protótipo: apenas emissão de VCs ou também fluxo completo de descoberta e negociação de DIDs entre dispositivos? 2) O avaliador prefere comparar nosso artefato com o framework ABE‑only de [[trabalhos/Fioreze_2026|Fioreze (2026)]] ou com soluções comerciais de identidade IoT (ex.: Azure IoT Hub) como baseline adicional? 3) Até que ponto devemos investir em auditoria homomórfica: demonstração de prova de conceito simples ou avaliação de desempenho realista em escala de milhares de transações? 4) Existem restrições de infraestrutura (ex.: disponibilidade de clusters Kubernetes ou hardware de aceleração) que devemos considerar ao planejar os experimentos? 5) Como abordar a questão de conformidade regulatória (LGPD, GDPR) no contexto de revogação distribuída e auditoria sem revelar dados sensíveis? Estas perguntas orientarão a definição do escopo e dos entregáveis da próxima reunião.

**Fontes que sustentam**

- [[trabalhos/Fioreze_2026|Fioreze (2026)]] — dissertacao_wesleyFioreze_23_06_2026_anotada

**Tags temáticas**

#abe #criptografia #criptografia-homomorfica #privacidade #ssi

**Próximas buscas sugeridas**

- dissertacao_wesleyFioreze_23_06_2026_anotada limitations future work
- dissertacao_wesleyFioreze_23_06_2026_anotada smart cities IoT blockchain access control



## Trabalhos acadêmicos recentes que merecem leitura/checagem

Estes trabalhos apareceram nas buscas acadêmicas ou no acervo e foram classificados como `revisar`. Eles ajudam a entender o que a área está discutindo agora.



- `Addula_2025` — A Novel Permissioned Blockchain Approach for Scalable and Privacy-Preserving IoT Authentication. Pré-leitura: manter_como_contexto. Motivo: O artigo aborda blockchain permissionada e criptografia homomórfica para autenticação de dispositivos IoT em larga escala, tópicos relevantes para segurança e privacidade em ambientes de cidades inteligentes. Contudo, o foco está em identidade de dispositivos e não em identidade autossoberana de cidadãos, credenciais verificáveis ou ciclos de vida 

- `Ahsan_2025` — A Comprehensive Survey on the Requirements, Applications, and Future Challenges for Access Control Models in IoT: The State of the Art. Pré-leitura: pendente. Motivo: O artigo apresenta um levantamento abrangente sobre modelos de controle de acesso em IoT, tema que se relaciona com a segurança e privacidade em serviços de cidades inteligentes. Contudo, o foco da pesquisa de mestrado está na identidade autossoberana (SSI), credenciais verificáveis e mecanismos criptográficos avançados (ABE, criptografia homomórfi

- `Alanzi_2025` — Blockchain-Based Identity Management System Prototype for Enhanced Privacy and Security. Pré-leitura: pendente. Motivo: O artigo apresenta um protótipo de sistema de gerenciamento de identidade descentralizado baseado em blockchain, abordando privacidade, segurança e desempenho com uso de IPFS e ECIES. Embora trate de identidade descentralizada, não está explicitamente inserido no contexto de cidades inteligentes, nem menciona identidade autossoberana (SSI), credenc

- `Anthony_2025` — Implementing Digital Sovereignty to Accelerate Smarter Mobility Solutions in Local Communities. Pré-leitura: pendente. Motivo: O artigo aborda soberania digital e controle de dados de cidadãos em serviços de mobilidade urbana, temas alinhados ao contexto de cidades inteligentes e à preocupação com privacidade, segurança e confiança. Contudo, não menciona identidade autossoberana, credenciais verificáveis, DIDs, ABE ou criptografia homomórfica, que são o foco central da rev

- `Aydeger_2025` — Enhancing Electric Vehicle Security and Privacy through Decentralized Identity Management. Pré-leitura: descartar_sem_texto_integral. Motivo: O artigo aborda a integração de Self‑Sovereign Identity (SSI) baseada em blockchain para melhorar a segurança e a privacidade em sistemas de carregamento de veículos elétricos, o que se enquadra nos domínios de cidades inteligentes, IoT e identidade descentralizada listados nas variáveis de busca. Embora o foco seja em veículos e infraestrutura de 

- `Babel_2025` — Self-sovereign identity and digital wallets. Pré-leitura: ler_integralmente. Motivo: O trabalho aborda identidade autossoberana (SSI) e carteiras digitais, tópicos centrais para a identidade do cidadão. Contudo, o título e o resumo não mencionam explicitamente aplicações em cidades inteligentes, serviços públicos, IoT ou compartilhamento de dados interorganizacional, que são requisitos essenciais do escopo da revisão focada. Assim,
