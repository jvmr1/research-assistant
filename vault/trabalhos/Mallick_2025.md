---
nome_local: Mallick_2025
openalex_id: https://openalex.org/W4413317900
doi: https://doi.org/10.1007/s43926-025-00195-5
ano: 2025
status: triagem_pendente
acesso_aberto: true
pdf_local: pdfs/Mallick_2025.pdf
tags: [abe, blockchain, contratos-inteligentes, criptografia, governanca-de-dados, interoperabilidade, iot, privacidade]
---
# Mallick_2025

## Tags

#abe #blockchain #contratos-inteligentes #criptografia #governanca-de-dados #interoperabilidade #iot #privacidade

Secure and trusted data sharing in smart healthcare using blockchain and IoT integration

<!-- agente:inicio -->

## Leitura e relações atualizadas pelo agente

Fonte: https://doi.org/10.1007/s43926-025-00195-5

Triagem: revisar. O trabalho aborda IoT, blockchain, controle de acesso e privacidade de dados, temas centrais do grupo de pesquisa. Contudo, o foco está em saúde inteligente (smart healthcare) e não em cidades inteligentes ou serviços públicos urbanos, que são o domínio prioritário. Ainda assim, a proposta de arquitetura descentralizada com smart contracts, IPFS e monitoramento de dispositivos vulneráveis pode oferecer insights úteis para soluções de segurança, interoperabilidade e privacidade em ambientes de cidades inteligentes, especialmente em contextos de edge computing e sistemas distribuídos. Por isso, recomenda‑se revisar o artigo para avaliar possíveis adaptações ou extensões ao contexto de smart cities.

[PDF local](../../pdfs/Mallick_2025.pdf)

### Relações bibliográficas verificadas nos metadados

Referencia: nenhum trabalho do acervo identificado.

É citado por: nenhum trabalho do acervo identificado.

### Como se correlaciona com os demais na análise

**Com  — Mallick_2025: Desenvolver um esquema descentralizado de revogação baseado em SSI ou criptografia baseada**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Desenvolver um esquema descentralizado de revogação baseado em SSI ou criptografia baseada em atributos

[Proposta completa no relatório](../RELATORIO.md)

**Com  — Mallick_2025: Realizar experimentos de latência e throughput em ambientes de edge computing e redes 5G t**

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Realizar experimentos de latência e throughput em ambientes de edge computing e redes 5G típicas de cidades inteligentes

[Proposta completa no relatório](../RELATORIO.md)

**Com  — Mallick_2025: Projetar e testar um proxy escalável com balanceamento de carga para suportar milhares de **

Interpretação da IA: Hipótese preliminar gerada a partir do fichamento de um trabalho. Deve ser confrontada com as próximas leituras.

Possível alteração a investigar: Projetar e testar um proxy escalável com balanceamento de carga para suportar milhares de dispositivos IoT simultâneos

[Proposta completa no relatório](../RELATORIO.md)

### Fichamento

Base: pdf; 16/16 trechos. Páginas sem texto extraível: []. Figuras e tabelas podem exigir conferência humana.

#### Página 1 — ficha 8e89232501c48173131d

O artigo apresenta uma arquitetura de saúde inteligente que combina blockchain, contratos inteligentes e IPFS para armazenar registros médicos de forma segura e descentralizada. Um dispositivo proxy protege sensores IoT vulneráveis usando criptografia. Avaliações experimentais medem tempos de upload, download, acesso e mineração, indicando ganhos de eficiência e desempenho ao integrar IPFS. O objetivo é superar falhas de sistemas centralizados, melhorar privacidade, interoperabilidade e escalabilidade em ambientes de saúde conectados.

- Centralized storage architecture ... can lead to a single point of failure and easy manipulation. — citação conferida: Centralized storage architecture in most IoT healthcare systems can lead to a single point of failure and easy manipulation.

- Public blockchain‑based healthcare systems improve efficiency and performance when IPFS is integrated. — citação conferida: The results show that public healthcare systems based on the Blockchain considerably boost efficiency and performance by integrating IPFS.

Interpretação: O trabalho demonstra que combinar blockchain com IPFS pode mitigar vulnerabilidades de armazenamento centralizado em sistemas de saúde IoT, oferecendo maior privacidade e interoperabilidade, embora ainda não explore controle de identidade descentralizado ou criptografia fina.

Dúvidas: Como a solução lida com a revogação de credenciais de dispositivos comprometidos? Qual o impacto do uso de IPFS em termos de latência para consultas em tempo real? O modelo de proxy criptográfico escala para milhares de sensores simultâneos?

#### Página 2 — ficha 8652c5d9de08bd86ecf6

O trecho destaca que a privacidade e a segurança das informações de saúde em sistemas IoT são pouco protegidas, que dispositivos baratos são alvos fáceis e que a arquitetura centralizada gera gargalos de rede. Propõe blockchain integrado ao IoT e ao IPFS para eliminar ponto único de falha, melhorar escalabilidade e garantir integridade dos dados, mas reconhece limitações de desempenho e escalabilidade da própria rede blockchain.

- Blockchain with IoT integration can help healthcare systems overcome centralized communication architecture — citação conferida: Blockchain with IoT integration can help healthcare systems overcome centralized communication architecture

Interpretação: O texto reforça que as vulnerabilidades atuais dos sistemas de saúde IoT são principalmente de natureza de privacidade, segurança e dependência de infraestruturas centralizadas, e que a combinação de blockchain e IPFS é vista como caminho para descentralizar, garantir integridade e melhorar a escalabilidade, embora a própria blockchain ainda enfrente desafios de desempenho em grande escala.

Dúvidas: Quais métricas específicas de desempenho (latência, throughput) foram observadas ao integrar IPFS? Como a solução lida com a revogação de credenciais ou dispositivos comprometidos em tempo real?

#### Página 3 — ficha 44492b3f922b7e3bdd1b

O artigo propõe uma arquitetura que combina blockchain e IPFS para superar limitações de privacidade, escalabilidade, segurança e eficiência em sistemas de saúde IoT. Os dados são fragmentados, armazenados com identificadores criptográficos (CID) e distribuídos via rede P2P, evitando ponto único de falha. A integração reduz a sobrecarga da blockchain, melhora a capacidade de armazenamento e permite acesso rápido a arquivos frequentes, enquanto um proxy de dispositivos e autenticação criptográfica protegem a confidencialidade dos dados.

- once a file is uploaded, its hash is shared among all peer nodes in the network for instant access and to prevent data from having a single point of failure. — citação conferida: once a file is uploaded, its hash is shared among all peer nodes in the network for instant access and to prevent data from having a single point of failure.

- Integrates an Interplanetary File System (IPFS) with the Blockchain network to reduce blockchain network overload and enhance healthcare systems’ scalability and storage capacity. — citação conferida: Integrates an Interplanetary File System (IPFS) with the Blockchain network to reduce blockchain network overload and enhance healthcare systems’ scalability and storage capacity.

Interpretação: O texto descreve como a combinação de blockchain e IPFS pode eliminar o ponto único de falha ao distribuir dados de saúde, melhorar a escalabilidade ao armazenar apenas endereços na blockchain e acelerar o acesso via cache local, ao mesmo tempo que introduz mecanismos de autenticação para proteger a confidencialidade.

Dúvidas: Não há detalhes sobre métricas de desempenho, custos de implementação ou avaliação prática em larga escala; também falta informação sobre como a solução lida com a revogação de credenciais ou a interoperabilidade entre diferentes provedores de saúde.

#### Página 4 — ficha 071465af0b89fdcdb181

O trecho descreve a seção de avaliação e resultados do trabalho, apresenta um panorama de trabalhos relacionados que utilizam IPFS, blockchain e técnicas de criptografia para melhorar a escalabilidade, confidencialidade e segurança em sistemas de saúde inteligentes. São citados diversos estudos que combinam armazenamento off‑chain, contratos inteligentes, edge‑IoT e criptografia baseada em atributos para superar limitações de desempenho e privacidade.

- Zheng et al. proposed an IPFS-based Blockchain system to reduce the data storage in Blockchain networks and increase processing speed. — citação conferida: Zheng et al. [17] proposed an IPFS-based Blockchain system to reduce the data storage in Blockchain networks and increase processing speed.

Interpretação: O trabalho se alinha a uma tendência de combinar IPFS com blockchain para mitigar problemas de escalabilidade e ponto único de falha, reforçando a segurança e a eficiência na troca de dados de saúde, e posiciona-se dentro de um cenário de múltiplas propostas semelhantes que exploram off‑chain storage e criptografia avançada.

Dúvidas: Quais métricas específicas de desempenho foram usadas na avaliação? Como o framework lida com a revogação de credenciais em ambientes multi‑organizacionais? Há detalhes sobre a implementação prática em edge devices de cidades inteligentes?

#### Página 5 — ficha f56295978fa01c1e4014

Trecho pulado por falha técnica repetida na extração da ficha. O texto original existe, mas a IA não retornou uma ficha utilizável.

Interpretação: Falha técnica de leitura deste trecho; seguir para os demais para não travar o trabalho.

Dúvidas: Conferir manualmente este trecho se ele for importante.

#### Página 6 — ficha b3226e8203a93209580e

O estudo propõe armazenar registros de saúde em IPFS, mantendo apenas o hash na blockchain, para reduzir latência, custos de armazenamento e eliminar ponto único de falha; descreve um processo de criptografia de duas etapas e apresenta análise quantitativa que indica menor tempo de transação e tamanho reduzido da cadeia.

- IPFS elimina ponto único de falha. — citação conferida: no single point of failure

- IPFS reduz tempo de processamento de transações e tamanho da blockchain. — citação conferida: quantitative analysis to demonstrate how IPFS facilitates faster transaction processing and smaller Blockchain data sizes.

Interpretação: A proposta combina IPFS e blockchain para melhorar a resiliência e eficiência do compartilhamento de dados de saúde, usando criptografia de duas etapas para garantir integridade e confidencialidade.

Dúvidas: Quais são os custos operacionais de manter nós IPFS em larga escala? Como a solução lida com a revogação de credenciais em tempo real? Há avaliação de desempenho em redes 5G/edge típicas de cidades inteligentes?

#### Página 7 — ficha e624275cd4958fcfa0fb

O trecho apresenta equações que demonstram a redução do tamanho dos blocos da blockchain ao armazenar arquivos no IPFS, comparando o tamanho sem IPFS e com IPFS, evidenciando ganhos de eficiência para o compartilhamento de dados de saúde.

- Equações 2 e 3 quantificam, respectivamente, o número total de transações por bloco e o tempo de execução de cada transação. — citação conferida: Eq. 2 shows the total number of transactions per block, and Eq. 3 provides the execution time of each transaction.

Interpretação: Ao mover os arquivos para o IPFS, apenas seus hashes são armazenados na blockchain, o que diminui significativamente o tamanho dos blocos e pode acelerar o processamento de transações e reduzir o consumo de armazenamento.

Dúvidas: Como a redução do tamanho dos blocos impacta a segurança e a resistência a ataques de negação de serviço? Qual é o efeito da latência de rede ao recuperar dados do IPFS em ambientes de edge computing? Como garantir a integridade e a disponibilidade dos dados armazenados no IPFS em longo prazo?

#### Página 8 — ficha 2c4f4eadfdfb43e81ad0

O trecho da página 8 do artigo de Mallick et al. (2025) apresenta duas figuras: a Fig. 4 ilustra o processo de criptografia e descriptografia, e a Fig. 3 demonstra como os dados de saúde são acessados a partir da estrutura proposta, indicando a presença de mecanismos de segurança e acesso no framework de compartilhamento de dados.

- O artigo apresenta um processo de criptografia e descriptografia. — citação conferida: Fig. 4 Encryption and decryption process

- O artigo demonstra o acesso a dados de saúde a partir da estrutura proposta. — citação conferida: Fig. 3 Accessing healthcare data from the framework

Interpretação: As figuras sugerem que o framework inclui etapas de criptografia para proteger os dados e um mecanismo de acesso que permite a recuperação segura das informações de saúde, embora o texto não detalhe os algoritmos ou políticas de controle de acesso.

Dúvidas: Quais algoritmos de criptografia são utilizados no processo da Fig. 4? Como o controle de acesso é gerenciado na Fig. 3? O artigo descreve políticas de revogação ou auditoria para o acesso aos dados de saúde?

#### Página 9 — ficha 1998c0db98989cb1c243

O trabalho apresenta um sistema de compartilhamento seguro de dados de saúde baseado em IoT e blockchain, implementado em laboratório com hardware Intel i7 e SSD, usando IPFS para armazenamento e contratos inteligentes para autenticação de dispositivos. Avaliam o desempenho variando o tamanho dos arquivos (20 MB a 140 MB) e analisam métricas como número total de transações por bloco e tempo de execução de cada transação.

- Três algoritmos são apresentados, incluindo o de registro e upload de arquivos. — citação conferida: Algorithm 1 shows the registration and uploading of the file into the proposed framework.

Interpretação: O estudo foca na viabilidade prática de integrar IPFS e blockchain para garantir integridade e autenticidade dos dados de saúde, usando métricas de desempenho que relacionam tamanho dos arquivos e carga de transações.

Dúvidas: Não está claro como o modelo se comportaria em redes públicas ou com maior número de dispositivos simultâneos, nem quais estratégias de revogação de credenciais seriam adotadas.

#### Página 10 — ficha 5a836f5e481b480f4ae8

O trabalho propõe um framework onde um device proxy registra dispositivos mediante prova de identidade, e uma dApp baseada em smart contracts conecta usuários e pacientes ao sistema de saúde. Dados são armazenados no IPFS e seu hash criptográfico é gravado na blockchain; a recuperação ocorre mediante verificação do hash. O processo de criptografia/decriptação é descrito no Algoritmo 3.

- A device proxy is used to identify and register these devices. — citação conferida: A device proxy is used to identify and register these devices.

- The encryption and decryption process of proposed healthcare system is presented in Algorithm 3. — citação conferida: The encryption and decryption process of proposed healthcare system is presented in Algorithm 3.

Interpretação: O trecho descreve um fluxo completo de registro, armazenamento e recuperação de dados de saúde, combinando um proxy de dispositivos para autenticação, uma dApp para interação e IPFS + blockchain para integridade e disponibilidade dos arquivos.

Dúvidas: Qual o mecanismo exato de prova de identidade exigido pelo device proxy? Como são gerenciados os direitos de acesso ao arquivo após a verificação do hash?

#### Página 11 — ficha b255a12ec010211237e6

A página 11 apresenta a referência a Mallick et al. (2025) e indica a presença do Algoritmo 1, que trata do registro e upload de dados de saúde em um cenário de IoT e blockchain.

- O documento inclui um Algoritmo 1 para registro e upload de dados de saúde. — citação conferida: Algorithm 1 Registration and Healthcare Data Upload

- A referência citada é Mallick et al., Discover Internet of Things (2025). — citação conferida: Mallick et al. Discover Internet of Things (2025) 5:90

Interpretação: A presença do Algoritmo 1 sugere que o trabalho propõe um procedimento específico para registrar dispositivos e enviar dados de saúde, possivelmente usando blockchain como camada de confiança.

Dúvidas: Não há detalhes sobre como o algoritmo garante a identidade dos dispositivos, nem sobre métricas de desempenho ou segurança avaliadas.

#### Página 12 — ficha c80b2990a1b00f6caee6

O trecho apresenta dois algoritmos: o Algoritmo 2, que descreve como acessar dados de saúde armazenados no IPFS, e o Algoritmo 3, que trata da criptografia e descriptografia desses dados, indicando a integração de blockchain e IoT para compartilhamento seguro em ambientes de saúde inteligente.

- O trabalho inclui um algoritmo para acessar dados de saúde a partir do IPFS. — citação conferida: Algorithm 2 Accessing Healthcare Data From IPFS

- O trabalho inclui um algoritmo para criptografar e descriptografar dados de saúde. — citação conferida: Algorithm 3 Algorithm for Encrypting and Decrypting Healthcare Data

Interpretação: Os algoritmos sugerem que o estudo foca na utilização do IPFS como camada de armazenamento distribuído e na proteção dos dados por meio de criptografia, reforçando a proposta de compartilhamento seguro em smart healthcare.

Dúvidas: Não há detalhes sobre métricas de desempenho, protocolos de consenso blockchain empregados ou mecanismos de controle de acesso associados aos algoritmos apresentados.

#### Página 13 — ficha 97954b01beb4abfa3eb7

O estudo apresenta um framework que integra blockchain e IPFS para armazenamento, acesso e compartilhamento seguro de dados de saúde em cidades inteligentes, usando tokens de identidade não transferíveis e smart contracts para controle de acesso, e avalia desempenho (tempo de upload, download, acesso e mineração) em diferentes tamanhos de arquivos.

Interpretação: O trabalho demonstra que a combinação de blockchain e IPFS permite controle de acesso seguro e integridade dos dados de saúde, porém o desempenho de upload e download varia conforme o tamanho dos arquivos e a infraestrutura de rede, destacando a vantagem do IPFS para arquivos maiores.

Dúvidas: Como o modelo se comporta em redes de borda heterogêneas? Qual o impacto da dificuldade de mineração sobre a latência de acesso ao dado? Há avaliação dos riscos de privacidade associados aos metadados armazenados no IPFS?

#### Página 14 — ficha dddb3bea88f0e334c761

Os experimentos mostraram que, ao compartilhar dados de saúde em uma rede híbrida, o IPFS apresenta tempos de upload, download e acesso significativamente menores que a blockchain, independentemente do tamanho dos arquivos ou da estação de trabalho utilizada.

- O IPFS é mais rápido que a blockchain para acesso a arquivos. — citação conferida: accessing a file using the IPFS network is significantly faster than using the Blockchain network

- O IPFS requer muito menos tempo para upload, download e acesso de dados de saúde. — citação conferida: the IPFS network requires much less time for uploading, downloading, and accessing

Interpretação: Os resultados indicam que, para compartilhamento de dados de saúde em cidades inteligentes, o uso do IPFS pode reduzir significativamente a latência e melhorar a eficiência operacional em comparação com soluções baseadas exclusivamente em blockchain.

Dúvidas: Como o desempenho do IPFS se comporta em redes com alta perda de pacotes ou conectividade intermitente? Qual o impacto da integração de SSI sobre esses tempos de acesso?

#### Página 15 — ficha 0a41348519e164325c6b

O estudo compara desempenho de upload, download e acesso de arquivos entre IPFS e blockchain em um cenário de saúde inteligente, mostrando que IPFS oferece velocidades significativamente maiores, embora o tempo de mineração seja maior no blockchain.

- O tempo de upload aumenta com o número de pares e o tamanho do arquivo, mas estabiliza após certo ponto. — citação conferida: upload time increased with both the number of peers and the size of the file being uploaded, but that at a certain point, the upload time varies very little

- IPFS apresenta velocidades de upload e download muito superiores às da rede blockchain. — citação conferida: IPFS network has much faster upload and download speeds than the Blockchain network

Interpretação: Os resultados indicam que, para compartilhamento de dados de saúde em cidades inteligentes, utilizar IPFS pode reduzir significativamente a latência de transferência, embora a camada de blockchain ainda seja necessária para garantir integridade e consenso, refletindo um trade‑off entre desempenho e segurança.

Dúvidas: Como a latência de mineração impacta aplicações que exigem respostas em tempo real? Qual seria o efeito de integrar SSI ao fluxo de dados entre IPFS e blockchain?

#### Página 16 — ficha 88e47d80dfcf6fec0377

O estudo compara desempenho de Blockchain e IPFS para compartilhamento de dados em saúde IoT. Observa que o tempo de mineração da Blockchain cresce com o tamanho dos arquivos, enquanto o IPFS mantém tempos de upload/download menores. Dados experimentais mostram que o armazenamento IPFS aumenta proporcionalmente ao volume de arquivos, ao passo que o ledger da Blockchain cresce de forma constante, independentemente do tamanho.

Interpretação: Os resultados indicam que, para grandes volumes de dados de saúde, IPFS oferece melhor eficiência de armazenamento e tempos de transferência, enquanto a sobrecarga de mineração da Blockchain pode limitar sua escalabilidade em cenários de arquivos volumosos.

Dúvidas: Como a latência de mineração afeta a consistência dos registros em tempo real? Qual seria o impacto de combinar IPFS com mecanismos de consenso mais leves ou híbridos?

<!-- agente:fim -->
