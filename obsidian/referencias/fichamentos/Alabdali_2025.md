---
nome_local: Alabdali_2025
openalex_id: https://openalex.org/W4409968817
doi: https://doi.org/10.1038/s41598-025-97030-2
ano: 2025
status: triagem_pendente
acesso_aberto: true
pdf_local: obsidian/referencias/pdfs/Alabdali_2025.pdf
tags: [blockchain, cidades-inteligentes, controle-de-acesso, iot]
---
# Alabdali_2025

## Tags

#blockchain #cidades-inteligentes #controle-de-acesso #iot
<!-- agente:inicio -->

## Leitura e relações atualizadas pelo agente

Fonte: https://doi.org/10.1038/s41598-025-97030-2

Triagem: baixa. O trabalho foca em classificação de resíduos sólidos usando IA, IoT e blockchain para melhorar a gestão de resíduos em cidades inteligentes. Embora envolva blockchain e IoT, não aborda identidade autossoberana, credenciais verificáveis, controle de acesso baseado em atributos, criptografia homomórfica ou outras tecnologias centrais ao objetivo da pesquisa focada, que é mapear o ciclo de vida das credenciais de identidade do cidadão e seus riscos de segurança e privacidade. Portanto, tem baixa relevância para o escopo de revisão proposto.

[PDF local](../pdfs/Alabdali_2025.pdf)

### Relações bibliográficas verificadas nos metadados

Referencia: nenhum trabalho do acervo identificado.

É citado por: nenhum trabalho do acervo identificado.

### Como se correlaciona com os demais na análise

**Com  — Alabdali_2025: Realizar estudo de custo‑benefício comparando blockchains públicas, privadas, híbridas e c**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Realizar estudo de custo‑benefício comparando blockchains públicas, privadas, híbridas e consensos leves (DAG, BFT) para gestão de resíduos.

[Proposta completa nas anotações](../ANOTACOES.md)

**Com  — Alabdali_2025: Medir e modelar o overhead de latência introduzido por diferentes algoritmos de consenso e**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Medir e modelar o overhead de latência introduzido por diferentes algoritmos de consenso em cenários de borda.

[Proposta completa nas anotações](../ANOTACOES.md)

**Com  — Alabdali_2025: Desenvolver e testar um esquema de revogação de credenciais baseado em SSI ou ABE adaptado**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Desenvolver e testar um esquema de revogação de credenciais baseado em SSI ou ABE adaptado a sensores de recursos limitados, com atualização automática de políticas.

[Proposta completa nas anotações](../ANOTACOES.md)

### Fichamento

Base: pdf; 15/15 trechos. Páginas sem texto extraível: []. Figuras e tabelas podem exigir conferência humana.

#### Página 1 — ficha 05ba93b0be94ff0a591c

O estudo propõe um modelo de classificação de resíduos baseado em IA que combina IoT e blockchain para coleta inteligente em cidades inteligentes, usando sensores ultrassônicos e CNNs para identificar e classificar resíduos em tempo real, otimizar rotas e reduzir emissões de CO₂.

- IoT-connected bins transmit data to a central server, which uses blockchain to ensure secure, transparent data storage. — citação conferida: IoT-connected bins transmit data to a central server, which uses blockchain to ensure secure, transparent data storage.

Interpretação: O trabalho combina três pilares (IoT, IA e blockchain) para criar um ciclo de coleta de resíduos mais eficiente e rastreável, alinhado aos objetivos de sustentabilidade de cidades inteligentes.

Dúvidas: Quais são os custos operacionais e de manutenção da infraestrutura blockchain proposta? Como a solução lida com falhas de conectividade dos sensores em áreas com cobertura de rede limitada?

#### Página 2 — ficha 9bc0da69557701dac1b1

O estudo propõe um sistema de gestão de resíduos sólidos que combina monitoramento em tempo real via sensores ultrassônicos IoT, classificação de resíduos por IA e armazenamento de dados em blockchain. A blockchain garante integridade e acesso rápido aos dados, enquanto algoritmos de IA otimizam rotas de coleta, reduzindo consumo de combustível e impactos ambientais. O modelo híbrido de IA aprende continuamente, melhorando a eficiência e a escalabilidade da solução.

- Algoritmos de IA otimizam rotas de coleta, reduzindo consumo de combustível e impacto ambiental. — citação conferida: Optimization of waste collection routes using AI algorithms, reducing fuel consumption, labor, and environmental impact.

Interpretação: A integração de IA, IoT e blockchain cria um ciclo virtuoso onde dados confiáveis alimentam modelos preditivos que, por sua vez, aprimoram a operação logística, resultando em menor desperdício energético e maior sustentabilidade urbana.

Dúvidas: Como a solução lida com a revogação de credenciais de dispositivos IoT comprometidos? Qual é o overhead de latência introduzido pela escrita em blockchain em ambientes de borda? Existem métricas de privacidade avaliadas para os dados compartilhados entre diferentes autoridades municipais?

#### Página 3 — ficha 023543cd48bdb399d7cf

O trecho descreve os desafios crescentes de volume de resíduos e a ineficiência da triagem manual, apresentando soluções baseadas em IA (software, contêineres e máquinas de classificação) e sensores IoT, além de evidenciar o alto desempenho de CNNs (até 90% de acurácia). Destaca ainda a falta de integração de IoT nos trabalhos de classificação existentes.

- AI-based waste classification software enhances the precision in identifying and categorizing different types of waste materials. — citação conferida: AI-based waste classification software enhances the precision in identifying and categorizing different types of waste materials.

Interpretação: O texto reforça que a IA, especialmente CNNs, oferece alta acurácia na classificação de resíduos, mas a maioria dos trabalhos ainda não combina essa capacidade com sensores IoT, criando uma oportunidade para soluções integradas que também abordem segurança e privacidade via blockchain e SSI.

Dúvidas: Quais são os requisitos de comunicação e energia para os sensores IoT em ambientes urbanos densos? Como garantir a integridade e a imutabilidade dos dados de classificação ao serem armazenados em blockchain em tempo real?

#### Página 4 — ficha 9c3688bcf713727246c4

O artigo apresenta um sistema de gestão de resíduos sólido que combina IoT (sensores ultrassônicos, de carga e câmeras) com blockchain para garantir integridade, segurança e transparência dos dados. Deep learning (CNNs) classifica o lixo, enquanto protocolos MQTT e CoAP viabilizam a comunicação. Estudos relacionados são citados, destacando robôs com 95% de acurácia e frameworks blockchain leves. O modelo inclui camadas de aplicação, consenso, rede e dados, e discute vulnerabilidades e contramedidas.

Interpretação: A integração de blockchain e IoT oferece uma base robusta para rastreamento e classificação de resíduos, mas a falta de exploração de designs profundos de aprendizado indica oportunidade de pesquisa.

Dúvidas: Como o consenso escolhido impacta a latência em ambientes de borda? Qual a viabilidade de aplicar SSI e ABE nos sensores de recursos limitados?

#### Página 5 — ficha b674a7f089b75dd49db5

O estudo propõe um framework de gestão de resíduos baseado em IA para cidades inteligentes, combinando classificação de lixo por rede neural convolucional (CNN) e lixeiras inteligentes equipadas com IoT. Os dados são registrados em blockchain para garantir integridade, transparência e responsabilidade, permitindo geração de rotas de coleta otimizadas e ações automatizadas. A metodologia inclui aprendizado por transferência para melhorar a acurácia da classificação com conjuntos de dados limitados.

Interpretação: O trabalho combina classificação visual de resíduos por CNN com lixeiras inteligentes conectadas via IoT, usando blockchain como camada de confiança para registrar dados de coleta e garantir transparência. Essa arquitetura visa melhorar a eficiência operacional das cidades inteligentes ao automatizar rotas e notificações, ao mesmo tempo em que protege a integridade dos dados.

Dúvidas: Qual mecanismo de consenso foi adotado na blockchain? Como são gerenciados os direitos de acesso aos dados dos sensores? Há uso de contratos inteligentes para incentivos ou pagamentos? De que forma a privacidade dos dados sensoriais é preservada além da imutabilidade da blockchain?

#### Página 6 — ficha b008bb4a9ba50d9639d2

O trecho descreve a arquitetura de lixeiras inteligentes que combinam sensores IoT (câmera, ultrassônico e de carga) com um microcontrolador que executa classificação CNN e aciona um servo para separar resíduos. Os dados de nível, peso e imagens são enviados a uma plataforma em nuvem e visualizados via aplicativo Blynk, permitindo monitoramento remoto em tempo real.

- Os lixos são equipados com sensores habilitados para IoT que facilitam o monitoramento em tempo real e a transmissão de dados. — citação conferida: These bins are equipped with IoT-enabled sensors that facilitate real-time waste monitoring and data transmission.

- Os dados coletados são enviados a uma plataforma baseada na nuvem e acessados via aplicativo Blynk. — citação conferida: The collected data is transmitted to a cloud-based platform and accessed via the Blynk application, enabling remote waste monitoring and management.

Interpretação: A proposta detalha uma solução prática de coleta inteligente, integrando IA para classificação de resíduos e IoT para monitoramento físico, o que reforça a viabilidade de sistemas distribuídos de gestão de resíduos em cidades inteligentes.

Dúvidas: Como garantir a privacidade dos dados de sensores ao transmiti‑los para a nuvem? Qual o impacto de latência da comunicação IoT na acurácia da classificação em tempo real? Há avaliação de consumo energético dos sensores e do microcontrolador?

#### Página 7 — ficha 36c91bf77e1f8addcdd8

O estudo apresenta um framework habilitado por IA para classificação, coleta e descarte de resíduos em cidades inteligentes, integrando sensores IoT e blockchain para rastreamento em tempo real, otimização de rotas e garantia de integridade dos dados, com latência de 1,2 s por imagem.

- The AI-driven system replaces traditional manual sorting, reducing human error. — citação conferida: replaces traditional manual sorting, reducing human error

- Blockchain framework was employed to store and track waste management data on a decentralized ledger. — citação conferida: store and track waste management data on a decentralized ledger

Interpretação: O trabalho demonstra que a combinação de IA para classificação de resíduos e blockchain para integridade dos registros pode melhorar a eficiência operacional e a transparência nas cidades inteligentes, embora ainda não apresente métricas de precisão ou análise de privacidade.

Dúvidas: Qual é a taxa de acurácia da classificação de resíduos obtida nos testes? Como a solução lida com a revogação de credenciais ou a atualização de políticas de acesso em ambientes distribuídos?

#### Página 8 — ficha deadb99c95c9fcbfd4b9

O trabalho apresenta um modelo de classificação de resíduos baseado em CNN com transfer learning, atingindo 95% de acurácia e latência de 1,2 s por imagem, graças a arquiteturas leves e computação de borda. A integração de blockchain garante integridade dos dados (98%) e rastreabilidade em tempo real, melhorando a eficiência de coleta para 92%. O sistema inclui sensores de nível e peso, e otimiza rotas de coleta via IA.

- O modelo atinge 95% de acurácia. — citação conferida: accuracy of 95%

- A latência do sistema é de 1,2 s por imagem. — citação conferida: lower latency (1.2 s per image)

Interpretação: A combinação de CNN otimizada para borda e blockchain oferece classificação rápida e confiável, reduzindo erros de separação e aumentando a transparência nas cadeias de gestão de resíduos urbanos.

Dúvidas: Como a solução lida com a heterogeneidade de sensores em diferentes cidades? Qual o impacto do uso de blockchain na latência total do sistema? Existem testes de robustez contra ataques de adulteração de dados em ambientes de borda?

#### Página 9 — ficha 5f458b2fdc28fc239d8d

O método proposto apresenta redução de emissões de CO₂ de 30%, superando abordagens de 2021 (15%) e 2022 (20%). Também alcança precisão de classificação de resíduos de 93%, acima das 85% e 89% das metodologias anteriores, indicando maior eficiência operacional e menor consumo de combustível.

- Precisão de 93% na classificação de resíduos. — citação conferida: Figure 8 showcases the precision performance of the proposed AI-driven waste classification system, achieving a high precision of 93%, surpassing the 2021 (85%) and 2022 (89%) methods.

Interpretação: Os resultados indicam que a combinação de blockchain com IA para classificação de resíduos melhora tanto a eficiência ambiental quanto a acurácia da separação, possivelmente devido a rotas otimizadas e melhor uso de recursos.

Dúvidas: Não há detalhes sobre a arquitetura de blockchain utilizada, custos computacionais, ou como a solução lida com privacidade e controle de acesso dos dados de sensores.

#### Página 10 — ficha 4efb298a3e3bcff0d81b

O estudo demonstra que o uso de Redes Neurais Convolucionais (CNNs) com transferência de aprendizado eleva a precisão da classificação de resíduos, reduzindo falsos positivos e melhorando a eficiência da triagem. Também apresenta métricas de recall comparando o modelo proposto com métodos de 2021 e 2022, destacando a capacidade de identificar corretamente todos os resíduos recicláveis.

- The improvement in precision can be attributed to the use of Convolutional Neural Networks (CNNs) with transfer learning — citação conferida: The improvement in precision can be attributed to the use of Convolutional Neural Networks (CNNs) with transfer learning

- Figure 9 illustrates the recall metric of the proposed AI-driven waste classification system — citação conferida: Figure 9 illustrates the recall metric of the proposed AI-driven waste classification system

Interpretação: A adoção de CNNs com transferência de aprendizado eleva significativamente a precisão e o recall da classificação de resíduos, indicando que abordagens de deep learning superam métodos tradicionais e podem ser fundamentais para sistemas de gestão de resíduos em cidades inteligentes.

Dúvidas: Como a solução se comporta em ambientes de borda com recursos computacionais limitados? Qual o impacto da integração de SSI e ABE na latência e no consumo de energia dos sensores IoT?

#### Página 11 — ficha e1fd058598bbf7f3dd4f

O método proposto usa transferência de aprendizado em CNNs leves integradas ao edge computing, alcançando recall de 91%, F1‑score de 0,94, precisão de 95% e latência de 1,2 s por imagem, embora apresente maior complexidade computacional.

- The proposed method achieves a recall of 91%, surpassing the 2021 method (78%) and the 2022 method (83%). — citação conferida: recall of 91%, surpassing the 2021 method (78%) and the 2022 method (83%)

- Latency is reduced to 1.2 s per image, compared to 2.5 s and 1.8 s for previous methods. — citação conferida: latency at 1.2 s per image, compared to 2.5 s for the 2021 model and 1.8 s for the 2022 model

Interpretação: A combinação de transfer learning e arquiteturas leves permite melhorar significativamente recall, precisão e velocidade, tornando o sistema viável para aplicações em tempo real em cidades inteligentes, embora a maior complexidade exija otimizações de hardware.

Dúvidas: Como a complexidade computacional impacta a energia consumida nos nós de borda? Qual seria o overhead de integrar blockchain e SSI ao fluxo de classificação em tempo real?

#### Página 12 — ficha a35089711df423ef93c4

O trabalho apresenta um sistema de classificação de resíduos baseado em CNNs com transfer learning, alcançando 95% de acurácia, e integra blockchain PoS para garantir integridade dos dados, embora aumente a complexidade computacional e exija latência de 1,2 s por imagem, sendo adequado para gestão de resíduos em cidades inteligentes.

- A acurácia de classificação alcançou 95% — citação conferida: we achieved a classification accuracy of 95%

- A latência de processamento por imagem foi de 1.2 s — citação conferida: maintain a low latency of 1.2 s per image

Interpretação: A combinação de CNN avançada e blockchain melhora a precisão e a integridade dos dados, mas impõe custos computacionais que precisam ser mitigados em ambientes de borda.

Dúvidas: Como a sobrecarga da blockchain afeta a energia consumida pelos nós de borda? Qual seria o impacto de substituir PoS por um consenso mais leve? Como garantir a privacidade das imagens ao usar aprendizado federado?

#### Página 13 — ficha a956bd705bc702b63c7e

O estudo apresenta um framework de gestão de resíduos baseado em IA que utiliza CNNs para classificação, sensores IoT para monitoramento em tempo real e blockchain para garantir integridade dos dados. A precisão de classificação atinge 95%, a latência é reduzida para 1,2 s por imagem, a integridade dos dados chega a 98% e a eficiência de coleta atinge 92%, reduzindo emissões de CO₂ em 30% e apoiando metas de sustentabilidade em cidades inteligentes.

- classification accuracy of 95% — citação conferida: classification accuracy of 95%

- data integrity score of 98% — citação conferida: data integrity score of 98%

Interpretação: A combinação de CNNs, IoT e blockchain eleva significativamente a precisão e a confiabilidade da gestão de resíduos, permitindo decisões de coleta mais rápidas e seguras, o que se traduz em maior eficiência operacional e redução de emissões de CO₂ nas cidades inteligentes.

Dúvidas: Como a complexidade computacional adicional impacta a viabilidade em dispositivos de borda com recursos limitados? Qual é o custo de implantação da infraestrutura blockchain em escala municipal? Como garantir a interoperabilidade das credenciais SSI entre diferentes provedores de serviços urbanos?

#### Página 14 — ficha 968ca4b8dce8047e9fb1

O texto destaca que a integração de IoT e blockchain ao sistema de classificação de resíduos aumenta a integridade e a segurança dos dados, mas reconhece vulnerabilidades a vazamentos e ataques cibernéticos em implantações em larga escala. Sugere ainda explorar análises preditivas para otimizar a geração e coleta de resíduos e aborda preocupações éticas como viés de IA, mitigadas por conjuntos de dados representativos.

Interpretação: O trecho reforça a proposta central do trabalho ao evidenciar benefícios de segurança trazidos pela blockchain, ao mesmo tempo em que aponta lacunas de proteção em ambientes IoT massivos e a necessidade de abordagens preditivas e éticas para melhorar a robustez e a justiça do sistema.

Dúvidas: Quais estratégias específicas de mitigação de riscos de IoT serão adotadas? Como os modelos preditivos de geração e coleta de resíduos serão integrados ao fluxo de classificação existente? Há planos para validar a eficácia das medidas de mitigação em cenários reais?

#### Página 15 — ficha c569904743a09654860d

O trecho apresenta referências a trabalhos que utilizam blockchain como serviço para IoT, arquiteturas de gerenciamento de acesso escaláveis, VANET habilitado por blockchain para gestão inteligente de resíduos sólidos e contratos inteligentes para sistemas de resíduos. Também inclui agradecimentos ao financiamento da King Abdulaziz University e informações de licenciamento aberto da publicação.

- Blockchain as a service for IoT. — citação conferida: 34. Samaniego, M., Jamsrandorj, U. & Deters, R. Blockchain as a service for IoT.

- Blockchain-enabled VANET for smart solid waste management. — citação conferida: 36. Saad, M. et al. Blockchain-enabled V ANET for smart solid waste management.

Interpretação: O material indica que o artigo se apoia em uma base crescente de literatura que combina blockchain e IoT para melhorar a gestão de resíduos sólidos, sugerindo que a solução proposta está alinhada a tendências de segurança, escalabilidade e automação no contexto de cidades inteligentes.

Dúvidas: Como a blockchain é integrada ao modelo de classificação AI descrito? Qual o impacto da camada blockchain na latência de coleta de dados dos sensores? Existem métricas de consumo energético da solução proposta? Como são tratadas questões de privacidade das imagens de resíduos?

<!-- agente:fim -->
