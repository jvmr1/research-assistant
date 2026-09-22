---
nome_local: Ragab_2025
openalex_id: https://openalex.org/W4407230907
doi: https://doi.org/10.1038/s41598-025-88843-2
ano: 2025
status: triagem_pendente
acesso_aberto: true
pdf_local: obsidian/referencias/pdfs/Ragab_2025.pdf
tags: [blockchain, cidades-inteligentes, controle-de-acesso, iot, privacidade, seguranca]
---
# Ragab_2025

## Tags

#blockchain #cidades-inteligentes #controle-de-acesso #iot #privacidade #seguranca
<!-- agente:inicio -->

## Leitura e relações atualizadas pelo agente

Fonte: https://doi.org/10.1038/s41598-025-88843-2

Triagem: revisar. O trabalho aborda IoT em cidades inteligentes e trata de privacidade e segurança mediante aprendizado federado, temas alinhados ao interesse geral do grupo (segurança e privacidade em IoT/Smart Cities). Contudo, não envolve as tecnologias centrais de interesse – blockchain, identidade auto-soberana, credenciais verificáveis, criptografia baseada em atributos ou controle de acesso interoperável – nem propõe soluções para interoperabilidade ou gestão de identidade. Assim, embora relevante para a temática de segurança, não preenche diretamente as lacunas de pesquisa prioritárias, justificando uma revisão detalhada antes de decidir sua inclusão ou exclusão.

[PDF local](../pdfs/Ragab_2025.pdf)

### Relações bibliográficas verificadas nos metadados

Referencia: nenhum trabalho do acervo identificado.

É citado por: nenhum trabalho do acervo identificado.

### Como se correlaciona com os demais na análise

**Com  — Ragab_2025: Realizar experimentos com conjuntos de dados multi‑administrador que reflitam heterogeneid**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Realizar experimentos com conjuntos de dados multi‑administrador que reflitam heterogeneidade realista e avaliar estratégias de normalização ou personalização de modelos locais

[Proposta completa nas anotações](../ANOTACOES.md)

**Com  — Ragab_2025: Incorporar técnicas de agregação robusta (ex**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Incorporar técnicas de agregação robusta (ex.: medianas robustas, detecção de outliers) para mitigar ataques de envenenamento de modelo

[Proposta completa nas anotações](../ANOTACOES.md)

**Com  — Ragab_2025: Medir e otimizar o overhead de comunicação e latência em nós de borda, possivelmente usand**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Medir e otimizar o overhead de comunicação e latência em nós de borda, possivelmente usando compressão de modelo ou atualização esparsa

[Proposta completa nas anotações](../ANOTACOES.md)

### Fichamento

Base: pdf; 16/16 trechos. Páginas sem texto extraível: []. Figuras e tabelas podem exigir conferência humana.

#### Página 1 — ficha 3365ebacbbc86eb8ad7b

O artigo propõe o AAIFLF-PPCD, um framework que combina inteligência artificial avançada, aprendizado federado e otimizações meta-heurísticas para detectar ciberameaças em IoT de cidades inteligentes, preservando a privacidade dos usuários e alcançando 99,47% de acurácia em dataset de referência.

- Federated Learning offers a privacy-preserving solution for detecting cyberattacks in IoT systems — citação conferida: Federated Learning (FL) offers an encouraging solution to address these challenges by providing a privacy-preserving solution for investigating and detecting cyberattacks in IoT systems

- The AAIFLF-PPCD technique achieved 99.47% accuracy — citação conferida: The performance validation of the AAIFLF-PPCD technique exhibited a superior accuracy value of 99.47% over existing models

Interpretação: O trabalho demonstra que a combinação de aprendizado federado, seleção de atributos via Harris Hawk Optimization e classificação por autoencoders esparsos pode melhorar significativamente a detecção de ameaças em IoT de cidades sustentáveis, ao mesmo tempo em que preserva a privacidade dos dados locais.

Dúvidas: Como o modelo lida com dados heterogêneos provenientes de diferentes organizações? Qual é o overhead computacional e de comunicação nas bordas de rede? O framework foi testado contra ataques adversariais ao modelo federado? Como garantir a escalabilidade e a interoperabilidade em ambientes multi‑administradores?

#### Página 2 — ficha 4c147c115c45c215e76d

O trecho destaca a importância da segurança em cidades inteligentes, apontando vulnerabilidades de hardware e software que podem levar a dados falsos e falhas por ataques. Propõe investigar a impossibilidade do aprendizado federado (FL) para detecção de ciberameaças preservando a privacidade, reconhecendo ainda que FL pode ser vulnerável a ataques de envenenamento e enfrentar desafios de alta dimensionalidade e heterogeneidade dos dispositivos IoT.

- Ensuring security in smart cities means sustaining data and the lattice from any evil actions and threats. — citação conferida: Ensuring security in smart cities means sustaining data and the lattice from any evil actions and threats.

- This work investigates the impossibility of FL for privacy-preserving cyberthreat detection. — citação conferida: To address these problems, this work investigates the impossibility of FL for privacy-preserving cyberthreat detection

Interpretação: O texto enfatiza que a segurança dos dados é crítica nas cidades inteligentes e que os produtos atuais frequentemente ignoram essa necessidade, expondo o sistema a falsificações e interrupções. Embora o aprendizado federado seja apresentado como solução potencial, os autores sugerem que sua aplicação para detecção de ameaças pode ser inviável devido a vulnerabilidades como ataques de envenenamento e à complexidade dos dados IoT.

Dúvidas: Quais são os cenários específicos em que o FL seria inviável para detecção de ciberameaças? Como os autores propõem contornar os ataques de envenenamento em FL? Há métricas ou experimentos que quantifiquem o impacto da alta dimensionalidade nos modelos propostos? Como a integração de SSI ou blockchain poderia ser concretizada dentro do framework descrito?

#### Página 3 — ficha 0496bd8c9938d870579f

O artigo propõe o AAIFLF‑PPCD, um framework que combina aprendizado federado, seleção de atributos via Harris Hawk Optimization, classificação por stacked sparse auto‑encoder e ajuste de hiperparâmetros com Walrus Optimization para detectar ameaças cibernéticas em cidades inteligentes assistidas por IoT, preservando a privacidade dos usuários. O método visa melhorar a acurácia e reduzir o tempo de resposta, integrando técnicas avançadas de IA em ambientes distribuídos.

- The AAIFLF-PPCD model introduces a novel feature selection mechanism based on HHO to improve cyberthreat detection performance. — citação conferida: The AAIFLF-PPCD model introduces a novel feature selection mechanism based on HHO to improve cyberthreat detection performance.

- The AAIFLF-PPCD approach integrates the WOA model for hyperparameter tuning to enhance classifier performance. — citação conferida: The AAIFLF-PPCD approach integrates the WOA model for hyperparameter tuning to enhance classifier performance.

Interpretação: O trabalho combina três técnicas de otimização (HHO, SSAE, WOA) dentro de um esquema de aprendizado federado, buscando melhorar a detecção de ameaças sem expor dados sensíveis. A ênfase está na eficiência (dimensionalidade reduzida, ajuste fino) e na adaptabilidade a padrões dinâmicos de ataque, mas ainda carece de validação em ambientes reais e de análise de vulnerabilidades específicas ao aprendizado federado.

Dúvidas: Quais são os impactos de comunicação e latência entre os nós federados na prática? Como o modelo lida com dados não‑i.i.d. típicos de dispositivos IoT heterogêneos? Há avaliação de segurança contra ataques de model poisoning ou backdoor?

#### Página 4 — ficha 313b9e85272462586464

O artigo apresenta o método AAIFLF‑PPCD para cidades inteligentes sustentáveis assistidas por IoT, focado em detecção robusta e escalável de ciberameaças com preservação da privacidade dos usuários. O modelo opera em três estágios – seleção de características baseada em HHO, reconhecimento de ataques via SSAE e ajuste de hiperparâmetros com WOA – visando melhorar a acurácia e a eficiência computacional. O texto também destaca limitações de alto custo computacional e complexidade ao integrar blockchain, aprendizado federado e IA, especialmente em ambientes com recursos limitados, apontando lacunas de escalabilidade e explicabilidade.

- The primary focus of the AAIFLF-PPCD method is to ensure robust and scalable cyberthreat detection while preserving the privacy of IoT users in smart cities. — citação conferida: The primary focus of the AAIFLF-PPCD method is to ensure robust and scalable cyberthreat detection while preserving the privacy of IoT users in smart cities.

- The limitations of the existing studies in this domain include the high computational cost and complexity associated with integrating BC, FL, and AI, particularly in resource-constrained environments. — citação conferida: The limitations of the existing studies in this domain include the high computational cost and complexity associated with integrating BC, FL, and AI, particularly in resource-constrained environments.

Interpretação: O trabalho propõe uma arquitetura híbrida que combina otimização bioinspirada (HHO, WOA) e redes neurais (SSAE) dentro de um framework federado, buscando equilibrar precisão e eficiência em dispositivos IoT limitados. Contudo, a discussão sobre a viabilidade prática da integração com blockchain e a escalabilidade em larga escala permanece superficial.

Dúvidas: Como o modelo lida com a latência de comunicação em ambientes federados reais? Qual o impacto real da inclusão de blockchain na sobrecarga computacional dos nós de borda?

#### Página 5 — ficha 6dee8b8b99f01dbdf25f

O trecho descreve detalhes do algoritmo de otimização Hawk‑Hawk (HH) usado na fase de seleção de características do modelo AAIFLF‑PPCD, explicando como números aleatórios (q, r) definem estratégias de exploração e exploração, e como o parâmetro En controla a transição entre esses estágios, incluindo táticas de cerco duro e suave.

- The randomly formed number r characterizes the likelihood that the prey would escape — citação conferida: The randomly formed number r characterizes the likelihood that the prey would escape from the unsafe surroundings once the HH presents an unexpected attack.

Interpretação: O algoritmo HHO serve como mecanismo de busca meta‑heurística para selecionar características relevantes, alternando entre exploração e exploração guiada por parâmetros aleatórios e pela métrica En, o que pode influenciar a eficácia e o custo computacional da fase de pré‑processamento do modelo.

Dúvidas: Como a escolha dos limites UB e LB e dos parâmetros aleatórios (q, r) afeta a convergência e a robustez da seleção de características em cenários de IoT com recursos limitados?

#### Página 6 — ficha 3a2e70687d8f41fd4d8e

O trecho descreve o comportamento de fuga do algoritmo Harris Hawks Optimization (HHO) quando r ≥ 0.5 e |En| ≥ 0.5, apresentando as equações (4) e (5) que modelam a atualização da posição do predador em relação à presa, e indica que a instrução imita o modelo comportamental, conforme ilustrado na Figura 3.

- The prey's escaping feature is relatively large when r ≥ 0.5 and |En|≥ 0.5. — citação conferida: If r ≥ 0.5 and |En|≥ 0.5, the prey’ s escaping feature is relatively large; hence, it attempts to escape from unsafe surroundings by jumping arbitrarily.

- The instruction in Eq. (4) imitates the behavioural model. — citação conferida: The instruction in Eq. (4) imitates the behavioural model.

Interpretação: O texto detalha como o HHO modela a estratégia de fuga da presa, usando parâmetros que controlam a magnitude da atualização de posição, o que fundamenta a fase de seleção de características do modelo proposto.

Dúvidas: Não está claro o significado exato dos símbolos En e Ju nas equações, nem como esses parâmetros são ajustados na prática durante a otimização.

#### Página 7 — ficha 475a4f592ccd4a559149

O trecho descreve as táticas de otimização do algoritmo HHO (hard siege, soft besiege, etc.) e a formulação da função de fitness que combina erro do classificador e taxa de redução de atributos. Em seguida, apresenta o classificador SSAE, destacando sua capacidade de aprender representações hierárquicas esparsas, maior precisão e resistência a ruído, sendo indicado para detecção de ameaças cibernéticas em tempo real em cidades inteligentes.

- The SSAE classifier is employed for detecting cyberthreats — citação conferida: SSAE outperforms handling complex, unstructured data and is less prone to overfitting.

Interpretação: O trecho detalha as táticas de otimização HHO e a formulação da função de fitness, além de justificar a escolha do SSAE por sua capacidade de aprender representações hierárquicas esparsas, o que reforça a proposta de detecção de ameaças em tempo real.

Dúvidas: Como os parâmetros r e |En| são ajustados dinamicamente durante a execução do HHO? Qual o custo computacional adicional introduzido pelas táticas de hard/soft besiege em dispositivos de borda?

#### Página 8 — ficha 1304f09da4cf05306921

O trecho descreve a arquitetura de um auto‑codificador (AE) e sua variante esparsa (SAE). O encoder mapeia os dados de entrada X para uma representação oculta h usando pesos W1 e viés b1, enquanto o decoder reconstrói a saída z a partir de h com pesos W2 e viés b2. A função de perda J mede o erro de reconstrução. A SAE introduz uma penalidade de esparsidade Jsparse, baseada na divergência KL entre a taxa de ativação desejada ρ e a média observada ˆρ, incentivando que a maioria dos neurônios ocultos permaneça inativa.

- The SAE is an NN method that presents a sparsity limitation on the conventional AE. — citação conferida: The SAE is an NN method that presents a sparsity limitation on the conventional AE.

- Jsparse = β ∑_{j=1}^{s} KL (ρ || ˆρ_j) adiciona penalidade de esparsidade ao treinamento. — citação conferida: Jsparse = β
∑ s
j=1
KL (ρ |
⏐⏐ˆρ j
)

Interpretação: O texto detalha como a camada codificadora/decodificadora e a função de perda são estendidas por uma penalidade de esparsidade, tornando a representação latente mais compacta e potencialmente mais robusta contra overfitting, o que pode ser benéfico para a detecção de ameaças em ambientes IoT distribuídos.

Dúvidas: Como a escolha do parâmetro β influencia o trade‑off entre precisão da detecção e consumo de recursos nos nós de borda? Qual o impacto da penalidade de esparsidade na privacidade dos dados quando o modelo é treinado de forma federada?

#### Página 9 — ficha 5284d06e436fd6285a06

O trecho detalha a formulação da função de perda do SSAE, incluindo o termo de penalidade de esparsidade β e a divergência KL, e descreve o uso do algoritmo de otimização Walrus (WO/WOA) para ajuste de hiperparâmetros, destacando sua eficiência em convergência e menor custo computacional comparado a buscas convencionais.

- The last SSAE loss function is described as: JssAE = J (W, b)+ Jsparse = 1/m Σ ... + β Σ KL(ρ ∥ ˆρ_j). — citação conferida: JssAE = J (W, b)+ Jsparse = 1
m
∑ m
i=1
1
2 (∥ xi − zi∥ )2 + β
∑ s
j=1
KL(ρ ∥ ˆρ j
)

Interpretação: O uso do WO como otimizador de hiperparâmetros reforça a proposta de melhorar a eficiência computacional, alinhado ao objetivo de reduzir custos em ambientes de borda.

Dúvidas: Como a escolha de β impacta a convergência do SSAE em cenários de dados heterogêneos? Qual o overhead real de implementar WO em dispositivos com recursos limitados?

#### Página 10 — ficha 924c58a63d575f5c798a

O trecho descreve os mecanismos de migração e reprodução do algoritmo Whale Optimization (WO) usados para ajustar a posição dos vetores solução, incluindo sinais de perigo, coeficiente β, passos de migração, e comportamentos de roosting e juvenis baseados em sequências de Halton e voos de Lévy.

- If danger signals are incredibly high, more than a particular pre-defined level, the walrus group must migrate to other, suitable regions for survival. — citação conferida: If danger signals are incredibly high, more than a particular pre-defined level, the walrus group must migrate to other, suitable regions for survival.

Interpretação: Os detalhes do WO apresentados (sinais de perigo, coeficiente β, passos de migração e estratégias de roosting) sugerem um controle fino entre exploração global e exploração local, o que pode ser aproveitado para melhorar a busca de hiperparâmetros e a robustez do modelo federado em cenários de cidades inteligentes.

Dúvidas: Como o coeficiente β evolui ao longo das iterações em ambientes reais de IoT? Qual o impacto da migração baseada em danger_signal sobre o consumo energético dos nós de borda? Como integrar as estratégias de roosting (Halton, Lévy) ao processo de agregação federada sem comprometer a privacidade?

#### Página 11 — ficha 29d16f8d483e0cc2a02a

O trecho descreve o comportamento de forrageamento inspirado no algoritmo Whale Optimization (WOA), apresentando equações para atualização de posições, coeficientes de coleta e seleção de fitness baseada em precisão, além de detalhar o conjunto de dados usado (30.000 instâncias, 12 classes).

- The dataset comprises 30,000 instances across 12 attack classes. — citação conferida: Total Number of Instances 30,000

Interpretação: O texto detalha a formulação matemática do WOA e seu uso na seleção de soluções ótimas, bem como apresenta o conjunto de dados empregado para validar o modelo de detecção de ameaças em IoT.

Dúvidas: Como o algoritmo WOA se integra ao framework federado proposto? Qual o impacto dos parâmetros a e b na convergência em ambientes de borda? Há avaliação de consumo de energia durante a otimização?

#### Página 12 — ficha 5f1ba42b08864a2ef0ef

A análise dos resultados do modelo AAIFLF-PPCD, testado no conjunto de dados Kaggle com 30.000 instâncias e 12 classes, mostrou que apenas 32 das 65 características foram selecionadas. A matriz de correlação revelou relações variadas entre parâmetros de rede, destacando uma forte correlação positiva (0,93) entre File_activity e Process_activity e correlações fracas ou negativas entre outras variáveis, como Scr_port e Des_port (‑0,04).

- Only 32 out of 65 features were selected for the model. — citação conferida: but only 32 have been selected.

- File_activity and Process_activity share a robust positive correlation of 0.93. — citação conferida: File_activity and Process_activity share a robust positive correlation of 0.93

Interpretação: A correlação forte entre atividades de arquivos e processos indica que esses atributos são críticos para a detecção de ameaças, enquanto correlações fracas sugerem que alguns atributos podem ser descartados sem perda significativa de informação, potencialmente aliviando a carga computacional.

Dúvidas: Como a seleção de apenas 32 atributos impacta a capacidade de generalização do modelo em cenários reais de cidades inteligentes? Qual seria o efeito de incorporar a energia consumida pelos nós IoT na função de fitness do algoritmo WOA?

#### Página 13 — ficha 78d52304ff1e01680875

O trecho descreve a análise de correlações entre variáveis de rede e demonstra que o modelo AAIFLF‑PPCD alcança alta precisão (≈99,5%) e AUC (~98%) na detecção de múltiplas classes de ameaças em cenários com 80%/20% de treinamento/validação, confirmando sua eficácia preditiva.

Interpretação: Os resultados indicam que o modelo possui excelente desempenho de classificação, embora a presença de correlações fortes sugira oportunidade de reduzir dimensionalidade para melhorar eficiência.

Dúvidas: Qual é o impacto do custo computacional em dispositivos de borda limitados? Como o modelo se comporta em ambientes com recursos de rede variáveis? A avaliação cobre cenários de ataque emergentes ou apenas as classes listadas?

#### Página 14 — ficha d3a488507a89186bdd3c

O método AAIFLF‑PPCD demonstra alta eficácia na detecção de ameaças cibernéticas em ambientes IoT de cidades inteligentes, alcançando acurácia média de 99,18 % e AUC de 97,33 % sob divisão 70 %/30 % de treinamento e teste, com confusões nulas nas matrizes de classificação.

- AAIFLF-PPCD approach achieved average accuracy of 99.18% under 70% TRPH. — citação conferida: With 70%TRPH, the AAIFLF-PPCD approach presents average accuy , precn, recal, F 1score , and AU Cscore of 99.18%, 95.11%, 95.10%, 95.10%, and 97.33%, respectively.

- Confusion matrices show correct identification of all class labels. — citação conferida: Figure 11a and b displays the confusion matrices with correct identification and classification of all class labels.

Interpretação: Os resultados indicam que o método AAIFLF‑PPCD mantém alta acurácia e boas métricas de precisão/recall mesmo com divisão 70/30 de treinamento/teste, sugerindo boa capacidade de generalização.

Dúvidas: Não há detalhes sobre o custo computacional real nos nós de borda nem sobre a escalabilidade para grandes redes IoT; falta informação sobre a robustez frente a ataques adversariais.

#### Página 15 — ficha 2f159572abea5e5d0b80

O modelo AAIFLF‑PPCD apresenta aumento progressivo de acurácia e redução de perda ao longo de 0‑25 épocas, superando técnicas como SVM, KNN e CNN+GRU, com precisão de 97.20 % e F1‑score de 96.92 %. O tempo de processamento é de 4.51 s, consideravelmente menor que os demais métodos, indicando eficiência para detecção de ciberameaças em cidades inteligentes assistidas por IoT.

- AAIFLF-PPCD alcançou precisão de 97.20 % e F1‑score de 96.92 %. — citação conferida: AAIFLF-PPCD approach reported enhanced performance with superior precn, recal, accuy , and F 1score of 97.20%, 96.84%, 99.47%, and 96.92%

- Tempo de processamento de 4.51 s, inferior aos demais métodos. — citação conferida: AAIFLF-PPCD model presents lesser PT of 4.51s, demonstrating its superior efficiency in PT

Interpretação: Os resultados indicam que a combinação de seleção de atributos via HHO, classificação SSAE e ajuste WOA produz um modelo competitivo tanto em acurácia quanto em latência, adequado para ambientes de borda em cidades inteligentes.

Dúvidas: Como o modelo se comporta em cenários de recursos extremamente limitados ou com tráfego de ataque zero‑day não representado nos dados de treinamento?

#### Página 16 — ficha e2363b4cb3a823b08f57

O método AAIFLF-PPCD foi testado em um conjunto de dados de referência, apresentando acurácia superior de 99,47% em comparação com modelos existentes, sob diferentes medidas de desempenho.

- the AAIFLF-PPCD technique was evaluated using a benchmark dataset — citação conferida: the AAIFLF-PPCD technique was evaluated using a benchmark dataset.

- superior accuracy value of 99.47% over existing models — citação conferida: The performance validation of the AAIFLF-PPCD technique exhibited a superior accuracy value of 99.47% over existing models under diverse measures.

Interpretação: Os resultados indicam que o modelo atinge alta acurácia, porém o trecho não detalha outras métricas nem descreve o benchmark utilizado, limitando a avaliação comparativa.

Dúvidas: Qual a composição exata do benchmark dataset? Como foram definidos TRPH e TSPH? Qual o custo computacional observado nas fases de HHO, SSAE e WOA?

<!-- agente:fim -->
