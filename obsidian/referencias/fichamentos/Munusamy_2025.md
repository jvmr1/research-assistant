---
nome_local: Munusamy_2025
openalex_id: https://openalex.org/W4412726368
doi: https://doi.org/10.1038/s41598-025-12225-x
ano: 2025
status: triagem_pendente
acesso_aberto: true
pdf_local: obsidian/referencias/pdfs/Munusamy_2025.pdf
tags: [blockchain, cidades-inteligentes, governanca-de-dados, interoperabilidade, iot, privacidade]
---
# Munusamy_2025

## Tags

#blockchain #cidades-inteligentes #governanca-de-dados #interoperabilidade #iot #privacidade
<!-- agente:inicio -->

## Leitura e relações atualizadas pelo agente

Fonte: https://doi.org/10.1038/s41598-025-12225-x

Triagem: revisar. O trabalho combina blockchain, computação de borda e técnicas de privacidade (SMPC, Differential Privacy) para melhorar a segurança e eficiência de aprendizado federado em ambientes sensíveis, o que se alinha aos interesses do grupo em sistemas distribuídos, blockchain e privacidade de dados. Contudo, o foco principal está na gestão de registros eletrônicos de saúde, sem abordar diretamente identidade digital auto‑soberana, controle de acesso baseado em atributos ou interoperabilidade entre serviços de cidades inteligentes. Por isso, embora seja relevante para a temática de segurança e privacidade em IoT/edge, não se enquadra como prioridade máxima para a linha de pesquisa em identidade e controle de acesso em cidades inteligentes, mas merece ser revisado para possíveis adaptações ou inspiração de técnicas.

[PDF local](../pdfs/Munusamy_2025.pdf)

### Relações bibliográficas verificadas nos metadados

Referencia: nenhum trabalho do acervo identificado.

É citado por: nenhum trabalho do acervo identificado.

### Como se correlaciona com os demais na análise

**Com  — Munusamy_2025: Desenvolver protótipo piloto em ambiente de saúde municipal usando EHR reais, medindo ener**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Desenvolver protótipo piloto em ambiente de saúde municipal usando EHR reais, medindo energia, latência e acurácia.

[Proposta completa nas anotações](../ANOTACOES.md)

**Com  — Munusamy_2025: Adaptar o consenso leve incorporando recompensas tokenizadas para incentivar a contribuiçã**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Adaptar o consenso leve incorporando recompensas tokenizadas para incentivar a contribuição de dispositivos IoT.

[Proposta completa nas anotações](../ANOTACOES.md)

**Com  — Munusamy_2025: Criar camada de interoperabilidade baseada em verifiable credentials que conecte o EPP‑BCF**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Criar camada de interoperabilidade baseada em verifiable credentials que conecte o EPP‑BCFL a sistemas SSI adotados por órgãos públicos.

[Proposta completa nas anotações](../ANOTACOES.md)

### Fichamento

Base: pdf; 16/16 trechos. Páginas sem texto extraível: []. Figuras e tabelas podem exigir conferência humana.

#### Página 1 — ficha 9c572813c3334a9c02c0

O artigo propõe o framework EPP-BCFL, que combina blockchain, aprendizado federado, SMPC e diferencial privacidade para reduzir custos computacionais e de comunicação, melhorar a precisão e proteger contra ataques de envenenamento em gestão de registros eletrônicos de saúde.

- O EPP-BCFL alcança alta acurácia e reduz latência e custo computacional. — citação conferida: Experimental evaluation on CIFAR-10 demonstrates 95.2% accuracy, a 43% reduction in communication latency, a 37% decrease in computational cost

Interpretação: A integração de blockchain com técnicas de privacidade avançadas parece mitigar os principais gargalos de desempenho e segurança do aprendizado federado, embora a validação ainda esteja restrita a um benchmark de visão computacional.

Dúvidas: Como o desempenho se comporta em dados reais de EHR com alta dimensionalidade? Qual o impacto de políticas de consentimento e regulatórias (HIPAA/GDPR) na implementação prática?

#### Página 2 — ficha 1f03669b04ec41d70341

O trabalho apresenta o framework Enhanced Privacy-Preserving Blockchain-Enabled Federated Learning (EPP-BCFL) para gestão segura e eficiente de registros eletrônicos de saúde (EHR). Combina aprendizado federado, analytics na borda e blockchain, usando mecanismos híbridos de privacidade (SMPC e Differential Privacy), consenso PoS+BFT leve e agregação adaptativa que considera qualidade dos dados, confiança dos nós e detecção de anomalias, visando reduzir sobrecarga computacional, latência e vulnerabilidades a ataques.

- FL facilitates collaborative model training across multiple healthcare organizations without sharing raw patient data. — citação conferida: Federated Learning (FL) facilitates collaborative model training across multiple healthcare organizations without sharing raw patient data.

Interpretação: O artigo propõe uma solução integrada que combina aprendizado federado, blockchain e analytics na borda, buscando superar as limitações de desempenho e segurança dos BCFL existentes ao introduzir privacidade híbrida e consenso leve, além de adaptar a agregação ao contexto dos nós.

Dúvidas: Como o framework lida com dados não-IID em larga escala? Qual o overhead real do consenso PoS+BFT em dispositivos IoMT? Existem métricas de energia consumida comparadas a abordagens tradicionais? Como a solução garante interoperabilidade com padrões de identidade digital (SSI) em cidades inteligentes?

#### Página 3 — ficha cc73fc3dc8e665986b0d

O trabalho apresenta o framework EPP-BCFL, que combina aprendizado federado, blockchain e técnicas de privacidade (SMPC, Differential Privacy, ZKP) para gerir registros eletrônicos de saúde. Destaca-se um consenso energeticamente eficiente que reduz latência em 43% e custo computacional em 37%, além de estratégias dinâmicas de agregação que dobram a velocidade de convergência. O sistema mantém alta acurácia (≈98,7%) e detecta anomalias em tempo real (~2,3 s).

- The framework achieved 95.2% accuracy with low communication overhead while defending against re-identification and inference attacks. — citação conferida: The framework achieved 95.2% accuracy with low communication overhead while defending against re-identification and inference attacks.

Interpretação: O EPP-BCFL demonstra que a combinação de blockchain, provas de conhecimento zero e privacidade diferencial pode melhorar significativamente a precisão, reduzir latência e custo computacional, ao mesmo tempo em que reforça a segurança e a privacidade em ambientes de aprendizado federado distribuído.

Dúvidas: Como o framework se comporta em cenários de alta heterogeneidade de dispositivos IoT típicos de cidades inteligentes? Qual o overhead adicional introduzido pelos ZKP em dispositivos extremamente limitados? Como garantir a interoperabilidade com padrões de identidade descentralizada (SSI) já adotados por órgãos públicos?

#### Página 4 — ficha 862bec4e31919ba54052

O trecho revisa literatura sobre aprendizado federado baseado em blockchain (BCFL), destacando contribuições como segurança aprimorada via criptografia homomórfica e provas de conhecimento zero, mas apontando limitações recorrentes de sobrecarga computacional/comunicação, desafios de escalabilidade e ausência de mecanismos de incentivo, especialmente em ambientes de recursos limitados como IoT, saúde e cidades inteligentes.

- Several frameworks extended this idea by implementing federated learning in UAV ecosystems, emphasizing both data protection and scalability. — citação conferida: Several frameworks extended this idea by implementing federated learning in UAV ecosystems, emphasizing both data protection and scalability.

Interpretação: O trabalho se insere em um cenário de BCFL onde a segurança é reforçada por blockchain, porém enfrenta os mesmos desafios de sobrecarga e escalabilidade descritos na literatura, indicando a necessidade de soluções que conciliem privacidade, eficiência e incentivos para adoção em ambientes de cidades inteligentes.

Dúvidas: Como o framework proposto lida com a falta de mecanismos de incentivo para participação dos dispositivos? Quais estratégias são previstas para reduzir a latência e o consumo energético em cenários de borda altamente dinâmicos? De que forma a heterogeneidade dos dados de saúde será tratada para evitar degradação da acurácia do modelo?

#### Página 5 — ficha 9eb08fc655dfd64eef4d

O trecho apresenta o framework EPP-BCFL, que combina blockchain e aprendizado federado com arquitetura em camadas, criptografia homomórfica, privacidade diferencial e agregação adaptativa para superar custos computacionais, sobrecarga de comunicação e falta de incentivos em ambientes de saúde. Identifica lacunas como suporte a dados heterogêneos de EHR, ausência de aprendizado federado vertical e coordenação interinstitucional, e propõe soluções técnicas para melhorar desempenho, privacidade e escalabilidade.

- BSDA achieves high throughput and low transaction latency — citação conferida: BSDA achieves high throughput and low transaction latency

Interpretação: O trabalho propõe uma arquitetura mais robusta e adaptável para aprendizado federado em saúde, mas reconhece que ainda há desafios de incentivos e de integração de dados heterogêneos, que são críticos para sua adoção em ambientes reais.

Dúvidas: Como o EPP-BCFL lida com a heterogeneidade de recursos computacionais entre dispositivos de borda? Qual o impacto real da criptografia homomórfica no consumo energético dos nós IoT?

#### Página 6 — ficha dda92be44322c7f098df

Trecho pulado por falha técnica repetida na extração da ficha. O texto original existe, mas a IA não retornou uma ficha utilizável.

Interpretação: Falha técnica de leitura deste trecho; seguir para os demais para não travar o trabalho.

Dúvidas: Conferir manualmente este trecho se ele for importante.

#### Página 7 — ficha a95c59f77a4eef2d3b24

O trecho descreve o fluxo hierárquico de dados e atualizações de modelo de nós de borda para o coordenador de FL e, finalmente, para a camada blockchain. A abordagem em camadas reforça privacidade, segurança e eficiência, combinando técnicas de preservação de privacidade, agregação adaptativa, consenso leve de blockchain e participação incentivada, configurando o EPP‑BCFL como solução otimizada para aprendizado federado baseado em blockchain.

- This layered approach enhances the privacy, security, and efficiency of federated learning — citação conferida: This layered approach enhances the privacy, security, and efficiency of federated learning

- The integration of privacy-preserving techniques, adaptive aggregation, lightweight blockchain consensus, and incentive-driven participation makes EPP-BCFL an optimized solution — citação conferida: The integration of privacy-preserving techniques, adaptive aggregation, lightweight blockchain consensus, and incentive-driven participation makes EPP-BCFL an optimized solution

Interpretação: O texto enfatiza a arquitetura em camadas e a combinação de técnicas de privacidade, agregação adaptativa e consenso leve como diferenciais do EPP‑BCFL, sugerindo que a participação incentivada é central para a eficácia do sistema.

Dúvidas: Quais são os detalhes específicos do mecanismo de incentivo (ex.: tokenomics, recompensas)? Qual algoritmo de consenso leve foi adotado (PoA, DAG, outro) e como ele se comporta em larga escala? Há métricas de latência e throughput reais em ambientes de borda de smart city?

#### Página 8 — ficha 827ddef7997e4cf9af2e

O trecho descreve como a camada de nós de borda, ao incorporar analytics locais, reduz riscos de privacidade, carga computacional e atrasos de comunicação, tornando o framework viável para implantação em larga escala. Análises estatísticas leves (Z‑score, PCA) e inferência rasa são usadas com custo O(M), adequado a dispositivos IoT limitados. Atualizações de modelo são protegidas por criptografia homomórfica, diferencial privacy e registradas na blockchain, garantindo integridade e auditabilidade.

- A divisão de responsabilidades entre camadas minimiza significativamente riscos de privacidade, encargos computacionais e atrasos de comunicação. — citação conferida: division of responsibilities among layers significantly minimizes privacy risks, computational burdens, and communication delays, making the framework suitable for large-scale deployment.

- Analytics de borda adiciona custo negligível (O(M)) em relação ao treinamento profundo, sendo adequado a dispositivos IoT com recursos limitados. — citação conferida: These methods add negligible cost (O(M)) relative to deep model training, making edge analytics suitable even for resource-constrained IoT devices.

Interpretação: A integração de analytics locais nos nós de borda, combinada com criptografia homomórfica, differential privacy e registro blockchain, fortalece a privacidade e a robustez do aprendizado federado, ao mesmo tempo que mantém a viabilidade em dispositivos IoT de baixa capacidade, aspecto crucial para aplicações em cidades inteligentes.

Dúvidas: Como o mecanismo de incentivo proposto pode ser implementado em cenários reais de smart city? Qual o impacto da latência da blockchain leve sobre a sincronização de modelos em milhares de nós distribuídos?

#### Página 9 — ficha ab12534778bbbaa32274

O trecho descreve o framework EPP-BCFL que utiliza armazenamento descentralizado de atualizações de modelo, contratos inteligentes e um consenso híbrido PoS+BFT para garantir auditabilidade, resistência a ataques e justiça na seleção de validadores, promovendo escalabilidade, segurança e robustez em ambientes de aprendizado federado distribuído.

Interpretação: O uso de armazenamento descentralizado e contratos inteligentes cria uma trilha de auditoria inviolável e protege contra ataques de envenenamento, enquanto o consenso híbrido PoS+BFT equilibra justiça e resistência a falhas, tornando o framework adequado para ambientes críticos como saúde e, potencialmente, cidades inteligentes.

Dúvidas: Como o mecanismo de stake será gerenciado em contextos de smart city onde os participantes podem não possuir tokens? Qual o impacto da latência de consenso híbrido em aplicações de tempo real de IoT? Existem planos para integrar mecanismos de revogação de credenciais em caso de comprometimento de nós?

#### Página 10 — ficha 4d4c6862c0c3b6563736

O algoritmo EPP-BCFL utiliza um protocolo de consenso leve PoS‑BFT para verificação segura e eficiente de atualizações de modelo em ambientes de borda. Reduz o conjunto de validadores a um pequeno subconjunto k ≪ N baseado em stake e atividade recente, diminuindo a sobrecarga de comunicação. O limiar BFT otimizado alcança consenso com mais de 2/3 dos validadores selecionados, mantendo tolerância a falhas bizantinas com menos mensagens, o que reduz latência e melhora a velocidade de processamento.

- The framework employs a lightweight PoS‑BFT consensus protocol to achieve secure, efficient model update verification. — citação conferida: lightweight Proof-of-Stake Byzantine Fault Tolerance (PoS-BFT) consensus protocol

- A reduced validator set—a small subset k ≪ N selected based on node stake and recent activity—minimizes communication overhead. — citação conferida: use of a reduced validator set—a small subset k ≪ N selected based on node stake and recent activity

Interpretação: A proposta enfatiza a redução de custos computacionais e de comunicação ao limitar o número de validadores, mantendo a descentralização e a tolerância a falhas, o que a torna adequada para ambientes de borda típicos de cidades inteligentes.

Dúvidas: Como será definido e atualizado o stake dos nós IoT em um contexto urbano dinâmico? Qual o impacto da escolha do limiar BFT (2/3) na resiliência contra ataques coordenados em redes altamente heterogêneas?

#### Página 11 — ficha 5f944c450563aa6f5f34

O trecho descreve o mecanismo híbrido PoS+BFT que usa pontuação de confiança composta para selecionar validadores, limitando stake para evitar centralização e incluindo fallback se mais de 1/3 dos nós forem maliciosos. O framework EPP-BCFL integra blockchain ao aprendizado federado, usando hash, criptografia, PoS e BFT, com DP aplicado antes de HE, e suporta treinamento assíncrono em dispositivos heterogêneos, mantendo complexidade computacional gerenciável.

- verification complexity remains O(1) per update — citação conferida: verification complexity remains O(1) per update, while overall consensus complexity is reduced to O(k²)

- Differential Privacy is applied prior to Homomorphic Encryption at the edge nodes — citação conferida: Differential Privacy (DP) is applied prior to Homomorphic Encryption (HE) at the edge nodes.

Interpretação: O texto apresenta um modelo de consenso híbrido que combina PoS e BFT para garantir eficiência (O(1) na verificação) e segurança (tolerância a falhas bizantinas). A inclusão de um limite de stake e de mecanismos de fallback busca prevenir a centralização e mitigar ataques quando a proporção de nós maliciosos ultrapassa 1/3. O framework EPP-BCFL incorpora privacidade diferencial antes da criptografia homomórfica, permitindo que dispositivos heterogêneos participem de aprendizado federado de forma assíncrona, mantendo a escalabilidade linear em relação ao número de nós.

Dúvidas: Como o limite de stake será definido e ajustado dinamicamente em ambientes de smart city? Qual o impacto prático da fase de fallback na latência do consenso? Como a combinação DP+HE afeta a precisão do modelo federado em cenários com dados altamente não‑IID?

#### Página 12 — ficha e905494cd75803376853

O trabalho apresenta o Efficient Privacy-Preserving BCFL Framework (EPP-BCFL), que combina aprendizado federado, MPC, diferencial de privacidade e blockchain com consenso PoS+BFT para garantir integridade e privacidade dos modelos. Avaliado com CIFAR-10 em cenário non‑IID, demonstra aumento de acurácia e redução de tempo de convergência à medida que o número de nós de borda cresce, embora use um dataset de visão computacional como proxy para EHRs.

- A acurácia do modelo aumenta com o número de nós de borda, atingindo 95.2% com 50 nós. — citação conferida: 50 95.2 94.0 93.3 93.6 10 300

Interpretação: Os resultados indicam que a combinação de blockchain com técnicas de privacidade pode melhorar a robustez e a precisão de aprendizado federado em ambientes distribuídos, embora a validação ainda dependa de datasets sintéticos.

Dúvidas: Como o desempenho do consenso PoS+BFT se comporta em redes com latência variável típica de cidades inteligentes? Quais são os impactos de usar dados reais de EHRs em termos de privacidade e carga computacional?

#### Página 13 — ficha 7a9a3a9facdb4bd65324

O estudo avalia o modelo federado global ao variar o número de nós de borda, mostrando aumento de acurácia de 88,5 % (10 nós) para 95,2 % (50 nós) e redução do tempo de convergência de 20 para 10 épocas. Também analisa o desempenho da blockchain, observando latência de transação de 50 ms a 150 ms e queda de throughput de 100 para 55 Tx/s ao crescer de 500 para 10 000 transações, com tempo de finalização de bloco dobrando.

- A acurácia do modelo federado melhora consistentemente de 88,5 % com 10 nós para 95,2 % com 50 nós. — citação conferida: accuracy of the federated model improves consistently from 88.5% with 10 nodes to 95.2% with 50 nodes

- A latência de transação da blockchain aumenta de 50 ms para 150 ms quando o número de transações cresce de 500 para 10 000, enquanto o throughput diminui de 100 Tx/sec para 55 Tx/sec. — citação conferida: transaction latency increases from 50 ms to 150 ms, while throughput decreases from 100 Tx/sec to 55 Tx/sec

Interpretação: Os resultados indicam que maior participação de nós de borda enriquece o conjunto de dados agregado, melhorando métricas de classificação e acelerando a convergência, ao mesmo tempo em que a escalabilidade da camada blockchain apresenta degradação de latência e throughput, refletindo o trade‑off entre número de atualizações e eficiência da rede.

Dúvidas: Como o aumento da latência e a redução do throughput da blockchain impactam a viabilidade de atualizações em tempo real em cenários críticos de saúde? Quais estratégias de otimização (e.g., sharding, off‑chain aggregation) poderiam mitigar esses efeitos sem comprometer a segurança?

#### Página 14 — ficha 07e650066580f7d54e02

O trabalho apresenta um mecanismo híbrido de privacidade que combina Computação Segura Multipartidária (MPC) e Privacidade Diferencial (DP), otimizado para reduzir a sobrecarga computacional e melhorar a precisão. Estudos de ablação mostram que a combinação sem otimização degrada desempenho, enquanto a solução proposta (EPP-BCFL) atinge 95,2% de acurácia, baixa sobrecarga de comunicação e alta resiliência a ataques, usando consenso PoS+BFT.

- O mecanismo híbrido combina MPC e DP para alcançar alto nível de privacidade. — citação conferida: hybrid privacy mechanism, which combines Secure Multiparty Computation (MPC) and Differential Privacy (DP)

Interpretação: A combinação otimizada de MPC e DP permite equilibrar privacidade e desempenho, superando abordagens que utilizam apenas uma técnica, e a escolha de consenso PoS+BFT contribui para a robustez contra ataques.

Dúvidas: Como o mecanismo híbrido se comporta em cenários com recursos de borda extremamente limitados? Qual seria o impacto de variar dinamicamente ε durante o treinamento em ambientes de saúde sensíveis?

#### Página 15 — ficha 86ce6df763778ca5cc24

O estudo avalia o impacto da heterogeneidade de dispositivos no framework EPP-BCFL, testando um servidor de borda de alto desempenho, um laptop intermediário e um dispositivo IoT limitado. Apesar das diferenças de recursos, a precisão permaneceu alta (desvio <1,2%) graças ao Mecanismo de Agregação Adaptativa. Também são apresentados resultados de precisão versus orçamento de privacidade e um estudo de ablação que mostra trade‑offs entre precisão e overhead de comunicação para diferentes configurações de privacidade.

- O framework EPP-BCFL manteve alta precisão em todos os dispositivos, com menos de 1.2% de desvio. — citação conferida: maintained high accuracy across all devices, with less than 1.2% deviation.

- A configuração combinada de DP + SMPC resultou em precisão de 89.1% com overhead de comunicação muito alto. — citação conferida: DP + SMPC (Combined) 89.1 Very High

Interpretação: Os resultados indicam que o mecanismo de agregação adaptativa consegue compensar disparidades de recursos computacionais, preservando a acurácia do modelo federado mesmo em dispositivos limitados, embora a combinação de DP e SMPC aumente significativamente o overhead de comunicação.

Dúvidas: Como o aumento de overhead de comunicação impacta a latência em redes de cidades inteligentes? Qual seria o efeito de otimizar o orçamento de privacidade (ε) em tempo real para diferentes tipos de dispositivos?

#### Página 16 — ficha f14e8f84b4b48f897caf

O trecho descreve como o framework EPP-BCFL ajusta pesos de dispositivos conforme qualidade dos dados, reduzindo a sobrecarga de comunicação via compressão (até 28% de ganho) sem degradar significativamente a acurácia (<1,5% de perda). Avalia a robustez contra ataques de envenenamento de dados, modelo e adversários FGSM, mostrando acurácias acima de 92% e tempos de resposta menores que os do FL baseline, mesmo com latência variável e dispositivos heterogêneos.

- Compression efficiency gain of up to 28% when scaling from 10 to 50 clients. — citação conferida: We observe a compression efficiency gain of up to 28% when scaling from 10 to 50 clients.

Interpretação: Os resultados indicam que a combinação de compressão adaptativa e o mecanismo AMA mantém a convergência e a acurácia mesmo em ambientes heterogêneos e sob condições de rede instáveis, reforçando a viabilidade do framework para aplicações críticas como gestão de registros de saúde eletrônicos.

Dúvidas: Como a compressão afeta a privacidade dos dados sensíveis em cenários de cidades inteligentes? Qual seria o impacto de aumentar a proporção de clientes adversários além de 20%?

<!-- agente:fim -->
