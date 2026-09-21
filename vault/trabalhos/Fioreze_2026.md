---
nome_local: Exemplo_60479560a08f3b4cd724
openalex_id: exemplos:e9b4988e85f71af47b84
doi: 
ano: None
status: analisado_com_sintese
acesso_aberto: false
pdf_local: exemplos/dissertacao_wesleyFioreze_23_06_2026_anotada.pdf
tags: [abe, criptografia, criptografia-homomorfica, privacidade, ssi]
---
# Fioreze (2026)

## Tags

#abe #criptografia #criptografia-homomorfica #privacidade #ssi
<!-- agente:inicio -->

## Leitura e relações atualizadas pelo agente

Fonte: PDF de exemplo fornecido pelo pesquisador

Triagem: sem_resumo. Requer PDF para avaliar.

Pré-leitura: ler_integralmente — PDF da pasta exemplos/ usado como semente da pesquisa; leitura integral obrigatória para gerar nota limpa e alimentar o brainstorm de propostas.

### Entendimento consolidado do trabalho

**Síntese da leitura**

A dissertação de mestrado profissional de Wesley Novaes Fioreze Costa (UFSP, junho de 2026) propõe um framework que combina a blockchain permissionada Hyperledger Besu com criptografia baseada em atributos (ABE) para viabilizar o compartilhamento seguro, auditável e privado de dados IIoT em cidades inteligentes. A arquitetura incorpora identidade autossoberana (SSI), identificadores descentralizados (DID) e credenciais verificáveis (VC), suportados por contratos inteligentes e, potencialmente, por IPFS como camada de armazenamento descentralizado. O objetivo é eliminar intermediários centralizados, oferecendo controle granular de acesso, privacidade, auditabilidade e interoperabilidade entre organizações sem confiança prévia. O trabalho descreve fluxos de emissão, apresentação e verificação de credenciais, bem como a aplicação de políticas ABE para controle de acesso, mas reconhece lacunas em revogação de atributos, recuperação de credenciais perdidas, métricas de desempenho, escalabilidade e requisitos de interoperabilidade nas dimensões técnica, semântica, organizacional e legal. (fonte: PDF parcial)

**Problema**

superar a dependência de intermediários centralizados, oferecendo controle granular de acesso, privacidade, auditabilidade e interoperabilidade entre organizações sem relação prévia de confiança.

**Solução ou abordagem**

Não identificado nas fichas/trechos disponíveis.

**Avaliação**

Não identificado nas fichas/trechos disponíveis.

**Limitações observadas**

limitações (revogação de atributos e escopo da avaliação de escalabilidade criptográfica)

**Possibilidades de extensão**

Implementar um mecanismo de recuperação de credenciais baseado em secret sharing, permitindo que cidadãos restabeleçam o acesso perdido a credenciais verificáveis em ambientes de IoT urbano, com avaliação de usabilidade e segurança.

**Possíveis lacunas levantadas na leitura**

- Ausência de avaliação de desempenho e escalabilidade (throughput, latência, custo) do framework em cenários de alta frequência de dados IIoT.
- Falta de descrição de mecanismos de revogação de credenciais e de recuperação de acesso perdido para dispositivos ou cidadãos.
- Detalhamento insuficiente dos requisitos e estratégias de interoperabilidade entre organizações distintas, incluindo camadas semântica, organizacional e legal.
- Impacto de latência dos smart contracts e da verificação de políticas ABE em aplicações de tempo real.
- Integração prática entre DIDs/SSI e esquemas ABE/CP‑ABE não está descrita.
- Critérios para escolha da complexidade das políticas de acesso e seu impacto no overhead não são explicitados.
- Papel e implementação do IPFS no armazenamento e distribuição de credenciais não são detalhados.
- Escopo limitado à interoperabilidade técnica, sem considerar camadas semântica, organizacional e legal.

**Possíveis contribuições derivadas deste trabalho**

- Integrar listas de revogação distribuídas (CRL) ou esquemas de revogação baseados em blockchain para suportar a revogação de credenciais ABE.
- Desenvolver um protocolo de recuperação de credenciais usando secret sharing ou técnicas de identidade autossoberana (SSI) aplicadas a dispositivos IIoT.
- Realizar experimentos de benchmark que medem throughput, latência, consumo de recursos, comparando Hyperledger Besu com alternativas de camada 2 ou sidechains para reduzir custos operacionais.
- Definir um modelo de interoperabilidade baseado em padrões DID/VC que permita a troca de atributos de acesso entre organizações heterogêneas.
- Desenvolver um modelo híbrido que combine DIDs com CP‑ABE para controle de acesso baseado em atributos e revogação descentralizada.
- Implementar um mecanismo de recuperação de credenciais usando secret sharing integrado a smart contracts.
- Criar um benchmark que correlacione a complexidade das políticas ABE com latência e consumo de recursos em cenários IIoT.
- Utilizar IPFS como camada de armazenamento descentralizado para payloads criptografados de credenciais verificáveis.

[PDF local](../../exemplos/dissertacao_wesleyFioreze_23_06_2026_anotada.pdf)

### Relações bibliográficas verificadas nos metadados

Referencia: nenhum trabalho do acervo identificado.

É citado por: nenhum trabalho do acervo identificado.

### Como se correlaciona com os demais na análise

**Com  — Fioreze (2026): Investigar a integração de identidades auto‑soberanas (SSI/DIDs) com políticas de controle**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Investigar a integração de identidades auto‑soberanas (SSI/DIDs) com políticas de controle de acesso baseadas em ABE para ambientes IIoT; explorar credenciais verificáveis como mecanismo de autenticação de dispositivos IoT em cadeias de suprimentos; propor extensões que combinam criptografia homomórfica com smart contracts para auditoria de acesso sem revelar dados sensíveis; avaliar estratégias de revogação distribuída de credenciais em redes industriais sem intermediário central.

[Proposta completa no documento de propostas](../PROPOSTAS-DE-TRABALHO.md)

**Com  — Fioreze (2026): Integrar identidade autossoberana (SSI) e DIDs para dispositivos e cidadãos, usando wallet**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Integrar identidade autossoberana (SSI) e DIDs para dispositivos e cidadãos, usando wallets digitais e verifiable credentials nos fluxos de emissão, apresentação e verificação.

[Proposta completa no documento de propostas](../PROPOSTAS-DE-TRABALHO.md)

**Com  — Fioreze (2026): Implementar registro de revogação baseado em blockchain que suporte revogação seletiva bas**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Implementar registro de revogação baseado em blockchain que suporte revogação seletiva baseada em atributos e recuperação de credenciais perdidas, armazenando credenciais de recuperação em IPFS.

[Proposta completa no documento de propostas](../PROPOSTAS-DE-TRABALHO.md)

**Com  — Fioreze (2026): Explorar criptografia homomórfica para processamento de dados IIoT sem descriptografia, pr**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Explorar criptografia homomórfica para processamento de dados IIoT sem descriptografia, preservando a privacidade.

[Proposta completa no documento de propostas](../PROPOSTAS-DE-TRABALHO.md)

**Com  — Fioreze (2026): Integrar SSI/DIDs com criptografia baseada em atributos (ABE/CP‑ABE/KP‑ABE) para controle **

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Integrar SSI/DIDs com criptografia baseada em atributos (ABE/CP‑ABE/KP‑ABE) para controle de acesso seletivo, revogação distribuída e recuperação de credenciais em cenários IIoT.

[Proposta completa no documento de propostas](../PROPOSTAS-DE-TRABALHO.md)

**Com  — Fioreze (2026): Desenvolver e avaliar listas de revogação distribuídas (CRL) ou esquemas de revogação base**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Desenvolver e avaliar listas de revogação distribuídas (CRL) ou esquemas de revogação baseados em atributos dentro da blockchain.

[Proposta completa no documento de propostas](../PROPOSTAS-DE-TRABALHO.md)

**Com  — Fioreze (2026): Implementar módulos de recuperação de credenciais baseados em secret sharing integrados a **

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Implementar módulos de recuperação de credenciais baseados em secret sharing integrados a smart contracts.

[Proposta completa no documento de propostas](../PROPOSTAS-DE-TRABALHO.md)

**Com [[Gudipati_2025|Gudipati_2025]] — Framework híbrido VC‑ABE para controle de acesso cidadão em IoT urbano**

Interpretação da IA: A literatura sobre identidade autossoberana (SSI) em cidades inteligentes converge na necessidade de combinar credenciais verificáveis (VCs) com mecanismos criptográficos avançados para garantir privacidade, controle de acesso granular e interoperabilidade. Fioreze (2026) propõe um framework baseado em blockchain e criptografia baseada em atributos (ABE) para compartilhamento seguro de dados IIoT, destacando limitações em revogação e recuperação de credenciais. Gudipati (2025) apresenta VCs como facilitadoras da identidade digital, apontando desafios de adoção e sugerindo a integração com ABE para controle de acesso em IoT. O trabalho de S_2026 (2026) explora identidade blockchain em um sistema de segurança turística, mas não detalha SSI ou mecanismos de recuperação. Em conjunto, os estudos concordam que a descentralização e a criptografia são essenciais, diferem nas ênfases (dados industriais vs. identidade de usuários) e ainda não cobrem plenamente revogação escalável, recuperação de credenciais perdidas e a aplicação de ABE/VCs em serviços urbanos de larga escala.

Possível alteração a investigar: Combina o framework blockchain‑ABE de Fioreze (2026) com as Verifiable Credentials descritas por Gudipati (2025) para criar credenciais que suportam seleção de atributos e políticas de acesso baseadas em ABE. O modelo inclui um mecanismo de revogação baseado em lista de status na blockchain e recuperação de credenciais via secret sharing, abordando lacunas de revogação e perda de acesso ainda não tratadas em ambientes urbanos.

[Proposta completa no documento de propostas](../PROPOSTAS-DE-TRABALHO.md)

**Com [[S_2026|S_2026]] — Identidade SSI com ABE para privacidade de turistas em cidades inteligentes**

Interpretação da IA: A literatura sobre identidade autossoberana (SSI) em cidades inteligentes converge na necessidade de combinar credenciais verificáveis (VCs) com mecanismos criptográficos avançados para garantir privacidade, controle de acesso granular e interoperabilidade. Fioreze (2026) propõe um framework baseado em blockchain e criptografia baseada em atributos (ABE) para compartilhamento seguro de dados IIoT, destacando limitações em revogação e recuperação de credenciais. Gudipati (2025) apresenta VCs como facilitadoras da identidade digital, apontando desafios de adoção e sugerindo a integração com ABE para controle de acesso em IoT. O trabalho de S_2026 (2026) explora identidade blockchain em um sistema de segurança turística, mas não detalha SSI ou mecanismos de recuperação. Em conjunto, os estudos concordam que a descentralização e a criptografia são essenciais, diferem nas ênfases (dados industriais vs. identidade de usuários) e ainda não cobrem plenamente revogação escalável, recuperação de credenciais perdidas e a aplicação de ABE/VCs em serviços urbanos de larga escala.

Possível alteração a investigar: Estende o sistema de segurança turística baseado em blockchain de S_2026 (2026) incorporando carteiras SSI que utilizam credenciais verificáveis e criptografia baseada em atributos (ABE) conforme o framework de Fioreze. O objetivo é permitir divulgação seletiva de atributos turísticos (ex.: idade, nacionalidade) e oferecer recuperação de credenciais via secret sharing, suprindo a lacuna de privacidade e resiliência de identidade para visitantes urbanos.

[Proposta completa no documento de propostas](../PROPOSTAS-DE-TRABALHO.md)

**Com [[Gudipati_2025|Gudipati_2025]] — Registro descentralizado de revogação para credenciais SSI em serviços públicos**

Interpretação da IA: A literatura sobre identidade autossoberana (SSI) em cidades inteligentes converge na necessidade de combinar credenciais verificáveis (VCs) com mecanismos criptográficos avançados para garantir privacidade, controle de acesso granular e interoperabilidade. Fioreze (2026) propõe um framework baseado em blockchain e criptografia baseada em atributos (ABE) para compartilhamento seguro de dados IIoT, destacando limitações em revogação e recuperação de credenciais. Gudipati (2025) apresenta VCs como facilitadoras da identidade digital, apontando desafios de adoção e sugerindo a integração com ABE para controle de acesso em IoT. O trabalho de S_2026 (2026) explora identidade blockchain em um sistema de segurança turística, mas não detalha SSI ou mecanismos de recuperação. Em conjunto, os estudos concordam que a descentralização e a criptografia são essenciais, diferem nas ênfases (dados industriais vs. identidade de usuários) e ainda não cobrem plenamente revogação escalável, recuperação de credenciais perdidas e a aplicação de ABE/VCs em serviços urbanos de larga escala.

Possível alteração a investigar: Propõe um registro de revogação distribuído na blockchain que combina a abordagem de revogação limitada de Fioreze (2026) com as necessidades de gerenciamento de status de VCs apontadas por Gudipati (2025). O registro utiliza provas de conhecimento zero para atualizar o status sem revelar atributos, permitindo que entidades públicas verifiquem a validade das credenciais em tempo real, preenchendo a lacuna de revogação escalável em ambientes de administração municipal.

[Proposta completa no documento de propostas](../PROPOSTAS-DE-TRABALHO.md)

### Fichamento

Base: pdf; 16/16 trechos. Páginas sem texto extraível: []. Figuras e tabelas podem exigir conferência humana.

#### Página 1 — ficha b8fdb35fb7d73dc3651b

Dissertação de mestrado profissional intitulada "BLOCKCHAIN-ENABLED ABE FRAMEWORK FOR SECURE IIOT DATA SHARING ACROSS ORGANIZATIONS", apresentada por Wesley Novaes Fioreze Costa na Universidade Federal de São Paulo em junho de 2026, sob orientação do Prof. Dr. Arlindo Flávio Daconceição e co-orientação do Prof. Dr. Vladimir Rocha.

- O trabalho propõe um framework baseado em blockchain e ABE para compartilhamento seguro de dados IIoT. — citação conferida: BLOCKCHAIN-ENABLED ABE FRAMEWORK FOR SECURE IIOT DATA SHARING ACROSS ORGANIZATIONS

- O título indica foco em segurança de dados de Internet Industrial das Coisas entre organizações. — citação conferida: SECURE IIOT DATA SHARING ACROSS ORGANIZATIONS

Interpretação: O título da dissertação sugere que o autor investiga a combinação de tecnologia blockchain com criptografia baseada em atributos (ABE) como solução para proteger a troca de dados de IIoT entre diferentes organizações, possivelmente abordando questões de confidencialidade, integridade e controle de acesso.

Dúvidas: Quais são os requisitos de interoperabilidade considerados? Como o framework trata a revogação de credenciais e a recuperação de acesso perdido pelos dispositivos ou cidadãos?

#### Página 2 — ficha df91d89200211a73c761

Dissertação de mestrado profissional apresentada em junho de 2026 à Universidade Federal de São Paulo, sob orientação do Prof. Dr. Arlindo Flavio da Conceição, propõe um framework baseado em blockchain e criptografia baseada em atributos (ABE) para garantir o compartilhamento seguro de dados IIoT entre organizações.

- Problema de compartilhamento seguro de dados IIoT entre organizações. — citação conferida: SECURE IIOT DATA SHARING ACROSS ORGANIZATIONS

- Solução baseada em blockchain e ABE. — citação conferida: BLOCKCHAIN-ENABLED ABE FRAMEWORK

Interpretação: O trabalho visa combinar as propriedades de imutabilidade e consenso da blockchain com a flexibilidade de controle de acesso da criptografia baseada em atributos para proteger fluxos de dados industriais em ambientes colaborativos.

Dúvidas: Quais métricas de desempenho foram utilizadas para validar a escalabilidade do framework? Como o autor trata a revogação de credenciais e a recuperação de acesso perdido no contexto proposto?

#### Página 3 — ficha a9a4bdbb3703f579e472

O autor agradece aos pais, irmão, parceira, à Universidade Federal de São Paulo e aos orientadores Prof. Dr. Arlindo Flavio da Conceição e Prof. Dr. Vladimir Rocha pelo apoio ao desenvolvimento da dissertação.

- I would like to express my sincere gratitude to all the people who supported me directly and indirectly during the stages of this project. — citação conferida: I would like to express my sincere gratitude to all the people who supported me directly and indirectly during the stages of this project.

Interpretação: O trecho revela o reconhecimento pessoal e institucional do autor, indicando vínculo com a Universidade Federal de São Paulo e orientação de dois professores, o que reforça a validade acadêmica do trabalho, embora não aporte conteúdo técnico.

Dúvidas: Quais foram as contribuições específicas dos orientadores para o desenvolvimento do framework proposto? Como o apoio institucional influenciou a escolha das tecnologias (blockchain, ABE) empregadas na dissertação?

#### Página 4 — ficha 68313efcadd9a3f8c599

O trecho traz uma reflexão literária, comparando a jornada dos personagens a desafios de escuridão e perigo que, embora pareçam insuperáveis, acabam cedendo lugar a um novo dia de luz, simbolizando esperança e a persistência em lutar por algo bom.

- A escuridão eventualmente passa e um novo dia surge. — citação conferida: Even darkness must pass. A new day will come.

- Vale a pena lutar por algo bom no mundo. — citação conferida: That there is some good in this world, and it’s worth fighting for.

Interpretação: O texto usa a narrativa de superação para ilustrar que, apesar de desafios complexos (como segurança e privacidade em cidades inteligentes), a persistência e a busca por soluções éticas podem levar a resultados positivos.

Dúvidas: Como traduzir a ideia de “passar a sombra” em mecanismos técnicos de revogação e recuperação de credenciais em ambientes de identidade autossoberana?

#### Página 5 — ficha 0079d0dd65052d099f97

A dissertação propõe combinar contratos inteligentes na blockchain Hyperledger Besu com criptografia baseada em atributos (ABE) para viabilizar troca segura, auditável e privada de dados IIoT entre organizações sem confiança prévia, reduzindo a dependência de intermediários centralizados.

- The proposal explores the use of smart contracts on the Hyperledger Besu blockchain to formalize, manage, and audit access permissions — citação conferida: The proposal explores the use of smart contracts on the Hyperledger Besu blockchain

- Attribute-Based Encryption (ABE) ensures that shared data is accessible only to entities that meet predefined access policies — citação conferida: Attribute-Based Encryption (ABE) to ensure that shared data is accessible only to entities that meet predefined access policies

Interpretação: O trabalho demonstra que a combinação de blockchain e ABE pode suprir lacunas de confiança e granularidade de controle em ambientes IIoT multi‑organizacionais, oferecendo auditabilidade e privacidade sem depender de autoridades centrais.

Dúvidas: Como a solução lida com a escalabilidade dos contratos inteligentes em cenários de alta frequência de dados? Quais são os custos operacionais de manter a blockchain Hyperledger Besu em ambientes industriais?

#### Página 6 — ficha bc2ac1e718709f02917d

A dissertação investiga como viabilizar a troca segura de dados em ambientes IIoT distribuídos, combinando contratos inteligentes na blockchain Hyperledger Besu com criptografia baseada em atributos (ABE). O objetivo é superar a dependência de intermediários centralizados, oferecendo controle granular de acesso, privacidade, auditabilidade e interoperabilidade entre organizações sem relação prévia de confiança.

Interpretação: O trabalho demonstra que a combinação de blockchain permissionada e ABE pode oferecer um modelo descentralizado de governança de dados IIoT, atendendo a requisitos de privacidade e auditabilidade sem depender de autoridades centrais.

Dúvidas: Como a solução lida com a escalabilidade de verificação de políticas ABE em grandes redes de dispositivos? Qual o impacto de latência introduzido pelos smart contracts nas aplicações de tempo real?

#### Página 7 — ficha c9e2ca17df5f5709c61c

O trecho apresenta o índice de figuras da dissertação, destacando fluxos de ABE, contratos inteligentes, etapas da revisão de literatura, diagramas de componentes e métricas de desempenho, indicando foco em arquitetura baseada em criptografia e blockchain para ambientes IIoT.

- O trabalho inclui um fluxo de criptografia baseado em atributos. — citação conferida: 2.1 Attribute-Based Encryption Workflow

- São avaliados tempos de criptografia e overhead de payloads protegidos por ABE. — citação conferida: 6.1 Encryption time by message

Interpretação: A presença de figuras detalhando ABE, contratos inteligentes, diagramas de arquitetura e métricas de desempenho evidencia que a dissertação investiga profundamente a viabilidade técnica de combinar criptografia avançada e blockchain para garantir segurança, privacidade e eficiência em ambientes IIoT de cidades inteligentes.

Dúvidas: Como o fluxo de ABE será conectado ao modelo de identidade auto‑soberana (SSI) proposto? O estudo aborda mecanismos de recuperação de credenciais perdidas dentro do Smart contract Flow? Quais são os critérios para escolher a complexidade das políticas de acesso nas avaliações de overhead?

#### Página 8 — ficha 1a0ffc94a8e73a9b9bbd

O trecho apresenta a lista de tabelas da dissertação, destacando métodos OpenABE, associação de estágios DSR, questões de pesquisa, critérios de inclusão e exclusão, resultados de revisão sistemática sobre blockchain e ABE em IoT e privacidade de dados, representações de dados avaliadas e métricas de overhead de criptografia.

- O trabalho apresenta resultados de revisão sistemática da literatura sobre blockchain e ABE em IoT e privacidade de dados. — citação conferida: Systematic Literature Review Results: Blockchain and ABE Applications in IoT and Data Privacy

- A dissertação define questões de pesquisa específicas. — citação conferida: Research Questions

Interpretação: A presença de tabelas que descrevem questões de pesquisa, critérios de inclusão/exclusão e revisão sistemática indica que a dissertação segue uma metodologia rigorosa, centrada em blockchain e criptografia baseada em atributos para segurança e privacidade em ambientes IoT de cidades inteligentes.

Dúvidas: Quais são as questões de pesquisa detalhadas listadas na tabela? Como os critérios de inclusão/exclusão foram aplicados na revisão sistemática? De que forma os resultados de overhead influenciam propostas de SSI nas fases do ciclo de vida da credencial?

#### Página 9 — ficha 14ad5f8d2333a6f4764d

O trecho apresenta a lista de acrônimos utilizados na dissertação, incluindo termos‑chave como DID (Decentralized Identifier), ABE (Attribute‑Based Encryption) e CP‑ABE, que são relevantes para identidade autossoberana e controle de acesso em ambientes de IIoT e cidades inteligentes.

- DID–Decentralized Identifier — citação conferida: DID–Decentralized Identifier

- ABE–Attribute-Based Encryption — citação conferida: ABE–Attribute-Based Encryption

Interpretação: A presença desses acrônimos indica que a pesquisa considera tecnologias de identidade descentralizada e criptografia baseada em atributos como componentes centrais da solução proposta.

Dúvidas: Como os autores pretendem combinar DIDs com ABE/CP‑ABE nas fases de revogação e recuperação de credenciais? Qual o papel específico do IPFS no gerenciamento de credenciais?

#### Página 10 — ficha 688fca99a8d3b49f280a

O trecho apresenta um glossário de siglas usadas no trabalho, incluindo termos de identidade autossoberana (SSI), credenciais verificáveis (VC) e criptografia baseada em atributos (KP-ABE).

- O trabalho define abreviações para componentes de segurança e identidade. — citação conferida: SSI–Self-Sovereign Identity

- Credenciais verificáveis são consideradas como elemento central. — citação conferida: VC–Verifiable Credential

Interpretação: A presença de SSI, VC e KP‑ABE no glossário indica que o estudo contempla identidade descentralizada e criptografia baseada em atributos como pilares para segurança e privacidade em ambientes de cidades inteligentes.

Dúvidas: Como as siglas listadas são operacionalizadas na arquitetura proposta? Existe um fluxo concreto que combine SSI, VC e KP‑ABE? Quais mecanismos de revogação e recuperação de credenciais são previstos?

#### Página 11 — ficha d877c138cb472b13d5e7

O trecho apresenta o sumário da dissertação, indicando que o trabalho aborda interoperabilidade organizacional para compartilhamento seguro de dados, utilizando Criptografia Baseada em Atributos (ABE) e blockchain (Hyperledger Besu) com contratos inteligentes, dentro de um contexto de IIoT distribuído.

- Cross-Organizational Interoperability for Secure Data Sharing — citação conferida: Cross-Organizational Interoperability for Secure Data Sharing

- Attribute-Based Encryption (ABE) — citação conferida: Attribute-Based Encryption (ABE)

Interpretação: O sumário indica que a pesquisa foca em garantir a segurança e a interoperabilidade de dados entre organizações usando ABE e blockchain, sugerindo que essas tecnologias são centrais para a solução proposta.

Dúvidas: Quais são os critérios específicos de avaliação de desempenho da arquitetura proposta? Como a dissertação trata a revogação de credenciais em ambientes distribuídos?

#### Página 12 — ficha f0ca7e92707e06a1a1a8

O trecho apresenta a estrutura da dissertação, destacando capítulos de revisão sistemática da literatura, arquitetura proposta, tecnologias‑chave, ambiente experimental e resultados de desempenho criptográfico, incluindo avaliação de sobrecarga por tamanho de payload e complexidade de políticas de acesso.

- A revisão inclui abordagens específicas de privacidade e segurança. — citação conferida: 4.5.1 Specific approaches to privacy and security

- A arquitetura proposta é detalhada na seção de design. — citação conferida: 5.2 Proposed Architecture Design

Interpretação: O índice indica que o trabalho segue uma metodologia estruturada, iniciando com perguntas de pesquisa e critérios de inclusão/exclusão, avançando para a proposta de arquitetura e validação experimental, com foco em desempenho criptográfico e sobrecarga de políticas de acesso.

Dúvidas: Quais são os resultados específicos da avaliação de sobrecarga por tamanho de payload? Como as políticas de acesso complexas impactam a latência nas provas de conceito? Não há detalhes sobre a implementação prática de SSI/DIDs no contexto apresentado.

#### Página 13 — ficha 891eadf476bfcb3eaa58

O trecho apresenta a estrutura dos capítulos finais da dissertação, destacando seções sobre privacidade e controle de acesso, escalabilidade criptográfica e de volume de dados, discussão dos resultados, vantagens, limitações (revogação de atributos e escopo da avaliação de escalabilidade criptográfica), conclusões, contribuições, trabalhos futuros e artefatos de pesquisa.

- Uma limitação abordada é a revogação de atributos. — citação conferida: 7.3.1 Attribute Revocation

Interpretação: A dissertação avança ao discutir explicitamente questões de privacidade, controle de acesso e escalabilidade criptográfica, reconhecendo a revogação de atributos como desafio e apontando a necessidade de ampliar a avaliação de escalabilidade.

Dúvidas: Quais métricas específicas foram usadas para avaliar a escalabilidade criptográfica? Como o escopo limitado da avaliação impacta a generalização dos resultados para diferentes cenários de cidades inteligentes?

#### Página 14 — ficha 1a829c52c8c18208d854

O trecho introduz a evolução da Indústria 4.0 e o conceito de IIoT, destacando a importância da interoperabilidade técnica, semântica, organizacional e legal, conforme o EIF e a ISO 11354-1, e indica que a dissertação focará apenas na interoperabilidade técnica suportada por comunicação publish/subscribe.

- interoperability becomes a central concern — citação conferida: interoperability becomes a central concern.

- The European Interoperability Framework (EIF) organizes interoperability into technical, semantic, organizational, and legal layers — citação conferida: The European Interoperability Framework (EIF) organizes interoperability into technical, semantic, organizational, and legal layers (European Commission, 2017).

Interpretação: O autor contextualiza a necessidade de interoperabilidade nas IIoT como um desafio multidimensional, limitando o escopo da dissertação à camada técnica, o que indica uma oportunidade de ampliar a abordagem para incluir mecanismos de identidade descentralizada.

Dúvidas: Como a solução proposta de smart contracts se relaciona com a camada técnica de interoperabilidade descrita? Existe alguma consideração sobre a integração de SSI/DIDs nas comunicações publish/subscribe? Quais são as implicações das camadas semântica e organizacional não abordadas?

#### Página 15 — ficha 7072a39ef1e3f9edfeb1

O trecho destaca a necessidade de interoperabilidade orientada à governança e segurança para troca de dados entre domínios administrativos independentes, sem confiança prévia. Embora a interoperabilidade semântica esteja fora do escopo, a expansão dos dispositivos IoT (prevista em 29 bi até 2030) intensifica desafios de compartilhamento seguro, governança de acesso, privacidade e auditoria. Um cenário de cadeia de suprimentos ilustra a necessidade de controle de acesso granular, permitindo que organizações mantenham autonomia e evitem dependência de um intermediário centralizado.

- A necessidade de compartilhamento seguro de dados entre organizações requer controle de acesso granular. — citação conferida: This need for data sharing between organizations can be supported by mechanisms that ensure granular access control over shared data, without requiring all parties to depend on a single centralized authority.

- Previsões indicam 29 bilhões de dispositivos IoT conectados até 2030. — citação conferida: Recent forecasts indicate that the global number of IoT-connected devices will reach 29 billion by 2030 (ABUSERRIEH; ALALFI, 2024).

Interpretação: O autor enfatiza que, apesar do crescimento explosivo de dispositivos IoT, a falta de mecanismos de governança e controle de acesso granular impede a colaboração interorganizacional segura, exigindo soluções que preservem a autonomia de cada entidade sem depender de autoridades centrais.

Dúvidas: Quais são os requisitos específicos de desempenho para os mecanismos de controle de acesso granular em ambientes IIoT de alta frequência? Como a exclusão da interoperabilidade semântica afeta a aplicabilidade prática das propostas de controle de acesso?

#### Página 16 — ficha 4ffbd90c852d088d8add

Trecho pulado por falha técnica repetida na extração da ficha. O texto original existe, mas a IA não retornou uma ficha utilizável.

Interpretação: Falha técnica de leitura deste trecho; seguir para os demais para não travar o trabalho.

Dúvidas: Conferir manualmente este trecho se ele for importante.

<!-- agente:fim -->
