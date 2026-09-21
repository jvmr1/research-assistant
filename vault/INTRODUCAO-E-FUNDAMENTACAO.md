# Introdução e fundamentação teórica

Atualizado: 2026-09-21T07:35:00

> Rascunho produzido pela IA a partir das fontes lidas. As citações usam links para os resumos no vault, permitindo abrir cada trabalho citado no Obsidian. A redação ainda exige revisão humana e conferência das referências.

Status: `rascunho_em_revisao`.

## Introdução

Cidades inteligentes representam uma transformação significativa na forma como serviços públicos são oferecidos e gerenciados, integrando Internet das Coisas (IoT), blockchain, sistemas distribuídos e plataformas urbanas para ampliar a eficiência da gestão e a qualidade dos serviços ao cidadão [[trabalhos/Cardoso_2024|Cardoso (2024)]]. Essa infraestrutura digital depende de mecanismos de identidade, autenticação e controle de acesso capazes de operar entre cidadãos, entidades administrativas, sensores, aplicações e organizações parceiras [[trabalhos/Maia_2025|Maia (2025)]]. Nesse cenário, a identidade autossoberana (SSI) surge como alternativa para reduzir a dependência de provedores centrais e ampliar o controle do titular sobre credenciais digitais, ainda que sua adoção em cidades inteligentes demande soluções maduras para interoperabilidade, revogação e recuperação de acesso [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]].

A SSI parte da premissa de que o indivíduo deve controlar sua identidade digital e apresentar credenciais verificáveis conforme a necessidade do serviço, sem entregar a um único provedor central todo o poder de autenticação e autorização [[trabalhos/Vaziry_2025|Vaziry et al. (2025)]]. Essa abordagem é especialmente relevante em cidades inteligentes, nas quais cidadãos, governo, sensores urbanos e plataformas de middleware interagem em fluxos que exigem autenticação, autorização, auditabilidade e preservação de privacidade [[trabalhos/Maia_2025|Maia (2025)]]. Contudo, os trabalhos analisados indicam que ainda há desafios técnicos e operacionais importantes, como interoperabilidade entre carteiras e padrões, custo de registro em blockchain, revogação de credenciais e escalabilidade sob grande volume de solicitações [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]].

O objetivo deste estudo é revisar como a identidade autossoberana pode ser utilizada em cidades inteligentes, mapeando as ações do cidadão e das entidades administrativas em cada fase do ciclo de vida da credencial e do dado. O recorte considera emissão, apresentação, verificação, transmissão, processamento, armazenamento, revogação e recuperação após perda de acesso, pois trabalhos recentes tratam partes desses fluxos, mas ainda deixam lacunas quando o ciclo completo é observado de modo integrado [[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Fioreze_2026|Fioreze (2026)]]. Para cada fase, serão registrados o estado da arte, os riscos de segurança e privacidade, os requisitos de interoperabilidade e as lacunas identificadas, sempre vinculando afirmações a trabalhos lidos e evitando apresentar hipóteses exploratórias como consenso.

A motivação para esta pesquisa surge da necessidade de estabelecer um modelo de gestão de identidade que responda às demandas das cidades inteligentes sem retirar do cidadão o controle sobre seus dados e credenciais. Segurança, privacidade e interoperabilidade aparecem como fatores críticos em arquiteturas que combinam blockchain, IoT e identidade digital [[trabalhos/Cardoso_2024|Cardoso (2024)]], [[trabalhos/Addula_2025|Addula et al. (2025)]]. Além disso, os trabalhos de base indicam espaço para aprofundar a interação entre cidadãos e entidades governamentais em fluxos SSI completos, especialmente quando se consideram revogação, recuperação de credenciais e controle seletivo de atributos [[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Fioreze_2026|Fioreze (2026)]].

A justificativa para esta pesquisa está na importância de criar um sistema de identidade que garanta segurança e privacidade, mas também promova interoperabilidade entre organizações e sistemas. A literatura recente sugere que SSI, DID, credenciais verificáveis e contratos inteligentes podem apoiar controle de acesso auditável e descentralizado, mas também mostra trade-offs de desempenho, governança, padronização e custo operacional que precisam ser avaliados empiricamente [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]], [[trabalhos/Vaziry_2025|Vaziry et al. (2025)]]. Técnicas como criptografia baseada em atributos e criptografia homomórfica aparecem como caminhos para reduzir exposição de dados em cenários de compartilhamento entre organizações, mas sua integração com SSI em cidades inteligentes ainda exige desenho arquitetural e avaliação experimental [[trabalhos/Fioreze_2026|Fioreze (2026)]], [[trabalhos/Addula_2025|Addula et al. (2025)]].

O objetivo geral deste estudo é mapear a aplicação da identidade autossoberana em cidades inteligentes, avaliando implicações de segurança, privacidade e interoperabilidade para as ações do cidadão e das entidades administrativas em cada fase do ciclo de vida da credencial. Os objetivos específicos são: identificar abordagens relacionadas a SSI em cidades inteligentes; analisar riscos de segurança e privacidade associados ao uso de credenciais verificáveis; investigar requisitos de interoperabilidade para integração de sistemas de identidade; identificar lacunas que precisam ser investigadas; e propor possibilidades de pesquisa envolvendo revogação, recuperação de acesso e uso de criptografia avançada quando houver justificativa técnica [[trabalhos/Cardoso_2024|Cardoso (2024)]], [[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Fioreze_2026|Fioreze (2026)]].

## Fundamentação teórica

### Cidades inteligentes e atores

Cidades inteligentes são sistemas sociotécnicos que integram IoT, plataformas digitais, serviços públicos, infraestrutura de comunicação e mecanismos de governança para melhorar a gestão urbana e a oferta de serviços ao cidadão [[trabalhos/Cardoso_2024|Cardoso (2024)]]. Esses ambientes envolvem cidadãos, entidades administrativas, organizações privadas, provedores de infraestrutura e dispositivos conectados; por isso, a identidade digital não pode ser tratada apenas como login de usuário, mas como elemento de coordenação entre atores, permissões, responsabilidades e fluxos de dados [[trabalhos/Maia_2025|Maia (2025)]]. A SSI se encaixa nesse contexto por propor maior controle do titular sobre credenciais e atributos, mas sua adoção depende de interoperabilidade técnica e governança entre múltiplas organizações [[trabalhos/Vaziry_2025|Vaziry et al. (2025)]].

### Identidade digital e SSI

A identidade digital refere-se à representação de sujeitos, dispositivos ou organizações em sistemas computacionais, permitindo autenticação, autorização e associação entre atributos e permissões [[trabalhos/Vaziry_2025|Vaziry et al. (2025)]]. A identidade autossoberana desloca parte desse controle para o titular da identidade, permitindo que credenciais sejam emitidas por uma entidade, armazenadas pelo usuário e apresentadas seletivamente a verificadores [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]]. Em cidades inteligentes, esse modelo é promissor porque aproxima autenticação, controle de acesso e privacidade do cidadão, mas ainda exige mecanismos seguros de revogação, recuperação e interoperabilidade entre plataformas heterogêneas [[trabalhos/Maia_2025|Maia (2025)]].

### DID e credenciais verificáveis

Os Decentralized Identifiers (DID) são componentes centrais em arquiteturas SSI porque permitem identificar sujeitos e resolver documentos de identidade sem exigir que todo o controle fique em um provedor central [[trabalhos/Vaziry_2025|Vaziry et al. (2025)]]. As credenciais verificáveis (VC) permitem que atributos emitidos por uma entidade sejam apresentados e verificados por outra, preservando a possibilidade de checagem criptográfica da origem e da integridade [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]]. Contudo, a implementação de DID e VC em cidades inteligentes exige planejamento de interoperabilidade, pois diferentes serviços urbanos podem usar blockchains, carteiras, middlewares e formatos de credenciais distintos [[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Fioreze_2026|Fioreze (2026)]].

### Autenticação e controle de acesso

A autenticação e o controle de acesso são elementos críticos para a segurança de sistemas de identidade em cidades inteligentes, pois definem quem pode acessar serviços, sensores, dados e operações administrativas [[trabalhos/Cardoso_2024|Cardoso (2024)]]. Modelos com SSI podem usar credenciais verificáveis, DIDComm, contratos inteligentes e assinaturas digitais para reduzir dependências centrais e registrar decisões de acesso de modo auditável [[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]]. Ainda assim, trabalhos recentes indicam que políticas mais granulares, como as baseadas em atributos, podem ser necessárias quando o objetivo é liberar apenas o dado ou recurso compatível com o papel, contexto ou atributo do solicitante [[trabalhos/Fioreze_2026|Fioreze (2026)]].

### Segurança e privacidade no ciclo de dados

Segurança e privacidade são fatores essenciais para sistemas de identidade em cidades inteligentes, pois credenciais e dados urbanos podem revelar informações sensíveis sobre localização, acesso a serviços, perfil do cidadão e comportamento de dispositivos [[trabalhos/Maia_2025|Maia (2025)]]. O ciclo de vida dos dados, desde emissão e apresentação até revogação e recuperação, deve ser protegido contra acessos não autorizados, fraudes, vazamentos e inconsistências de autorização [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]]. A criptografia baseada em atributos e a criptografia homomórfica aparecem como mecanismos complementares para reduzir exposição de conteúdo e permitir controle de acesso ou processamento sobre dados protegidos, mas sua aplicação integrada com SSI e IoT urbano ainda demanda validação experimental [[trabalhos/Fioreze_2026|Fioreze (2026)]], [[trabalhos/Addula_2025|Addula et al. (2025)]].

### Interoperabilidade e governança

A interoperabilidade é um desafio crítico para a implementação de sistemas de identidade em cidades inteligentes, especialmente quando diferentes entidades precisam compartilhar e validar informações sem pertencer à mesma infraestrutura institucional [[trabalhos/Vaziry_2025|Vaziry et al. (2025)]]. A SSI oferece uma abordagem promissora porque credenciais verificáveis podem circular entre emissores, titulares e verificadores, desde que padrões de DID, VC, carteiras, registros e protocolos de comunicação sejam compatíveis [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]]. A governança descentralizada, entretanto, ainda exige definição de responsabilidades, políticas de revogação, confiança entre organizações e aderência regulatória, especialmente em aplicações urbanas envolvendo dados pessoais [[trabalhos/Fioreze_2026|Fioreze (2026)]].

### Revogação e recuperação de acesso

Revogação e recuperação de acesso são elementos essenciais para a gestão de identidade em sistemas de cidades inteligentes, porque credenciais podem expirar, ser comprometidas ou ficar inacessíveis quando o cidadão perde o dispositivo ou a chave associada [[trabalhos/Maia_2025|Maia (2025)]]. Sistemas como YouGovern mostram que contratos inteligentes e registros em blockchain podem apoiar revogação e controle de acesso, mas também deixam questões sobre escalabilidade, latência e integração com serviços heterogêneos [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]]. A recuperação de credenciais perdidas permanece particularmente sensível, pois precisa restabelecer acesso sem recriar dependência centralizada nem expor atributos pessoais durante o processo [[trabalhos/Fioreze_2026|Fioreze (2026)]].

## Mapa do ciclo de vida e pontos de atenção

### Emissão

**Ações do cidadão**

O cidadão recebe ou solicita credenciais digitais em uma carteira SSI, mantendo controle sobre quais credenciais serão armazenadas e posteriormente apresentadas [[trabalhos/Maia_2025|Maia (2025)]]. Em cenários urbanos, essa etapa pode envolver serviços públicos, sensores ou cadastros municipais associados a atributos do cidadão.

**Ações das entidades administrativas**

As entidades administrativas atuam como emissoras de credenciais verificáveis, definindo esquemas, atributos e regras de validade [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]]. Em arquiteturas baseadas em blockchain, essas entidades também podem registrar identificadores, chaves públicas ou estados de credenciais em ledgers distribuídos.

**Riscos de segurança e privacidade**

A emissão pode ser afetada por fraude de identidade, emissão indevida de atributos, falhas de autenticação inicial e exposição excessiva de dados cadastrais [[trabalhos/Maia_2025|Maia (2025)]]. O risco aumenta quando múltiplos órgãos e plataformas precisam emitir credenciais compatíveis sem governança comum.

**Estado da arte**

Sistemas como YouGovern usam blockchain, DID, contratos inteligentes e armazenamento descentralizado para registrar e gerenciar identidades, incluindo métricas de latência média de registro de DID de 0,94 s e pico de 12,5 transações por segundo [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]]. Trabalhos nacionais de base também exploram blockchain e SSI em middleware de cidades inteligentes [[trabalhos/Cardoso_2024|Cardoso (2024)]], [[trabalhos/Maia_2025|Maia (2025)]].

**Lacunas ou melhorias a investigar**

Ainda falta detalhar requisitos funcionais e não funcionais para emissão de credenciais em escala urbana, incluindo desempenho, governança entre órgãos e interoperabilidade entre padrões [[trabalhos/Cardoso_2024|Cardoso (2024)]], [[trabalhos/Vaziry_2025|Vaziry et al. (2025)]].

**Fontes da fase**

[[trabalhos/Cardoso_2024|Cardoso (2024)]], [[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]], [[trabalhos/Vaziry_2025|Vaziry et al. (2025)]]

### Apresentação/Verificação

**Ações do cidadão**

O cidadão apresenta credenciais verificáveis a serviços públicos ou privados para provar atributos específicos, buscando reduzir a exposição de dados desnecessários [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]]. Esse fluxo é central em aplicações de acesso a serviços urbanos e autenticação em middleware de cidade inteligente [[trabalhos/Maia_2025|Maia (2025)]].

**Ações das entidades administrativas**

As entidades administrativas verificam assinatura, validade, emissor e estado da credencial antes de liberar acesso ao serviço ou recurso. Em modelos com contratos inteligentes, parte dessa verificação pode ser automatizada e registrada de forma auditável [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]].

**Riscos de segurança e privacidade**

Os principais riscos incluem replay de apresentações, aceitação de credenciais revogadas, exposição de atributos além do necessário e falhas de interoperabilidade entre carteiras e verificadores [[trabalhos/Maia_2025|Maia (2025)]]. Quando políticas de acesso são pouco granulares, o usuário pode revelar mais informação do que o serviço realmente precisa.

**Estado da arte**

Maia (2025) implementa autenticação e controle de acesso com SSI em ambiente de cidade inteligente e relata latência inferior a 500 ms nas fases avaliadas [[trabalhos/Maia_2025|Maia (2025)]]. YouGovern demonstra controle de acesso e gerenciamento de identidade baseado em blockchain, com suporte a registros e revogação [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]].

**Lacunas ou melhorias a investigar**

Faltam avaliações comparativas sobre apresentação seletiva de atributos, interoperabilidade entre implementações SSI e integração de controle de acesso baseado em atributos com credenciais verificáveis [[trabalhos/Fioreze_2026|Fioreze (2026)]], [[trabalhos/Vaziry_2025|Vaziry et al. (2025)]].

**Fontes da fase**

[[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]], [[trabalhos/Fioreze_2026|Fioreze (2026)]], [[trabalhos/Vaziry_2025|Vaziry et al. (2025)]]

### Transmissão

**Ações do cidadão**

O cidadão transmite apresentações de credenciais ou mensagens de autenticação por meio de carteiras, agentes SSI ou protocolos de comunicação entre pares [[trabalhos/Maia_2025|Maia (2025)]]. A transmissão precisa preservar integridade, confidencialidade e minimização de dados.

**Ações das entidades administrativas**

As entidades administrativas recebem, encaminham ou validam mensagens de credenciais entre serviços, middlewares e registros distribuídos. Quando a arquitetura envolve múltiplas organizações, a transmissão também precisa respeitar acordos de interoperabilidade e governança [[trabalhos/Fioreze_2026|Fioreze (2026)]].

**Riscos de segurança e privacidade**

Interceptação, correlação de transações, vazamento de metadados e falhas de configuração criptográfica podem comprometer a privacidade mesmo quando o conteúdo principal está protegido [[trabalhos/Addula_2025|Addula et al. (2025)]]. Em cenários urbanos, esses metadados podem revelar hábitos de mobilidade ou uso de serviços.

**Estado da arte**

As arquiteturas analisadas usam blockchain, agentes SSI, DIDComm, contratos inteligentes e mecanismos criptográficos para apoiar comunicação e validação em fluxos distribuídos [[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]]. Fioreze (2026) amplia essa discussão ao tratar compartilhamento seguro entre organizações sem relação prévia de confiança [[trabalhos/Fioreze_2026|Fioreze (2026)]].

**Lacunas ou melhorias a investigar**

Ainda é necessário avaliar como proteger metadados de transmissão, como integrar canais SSI a middlewares urbanos e como aplicar criptografia avançada sem inviabilizar desempenho [[trabalhos/Fioreze_2026|Fioreze (2026)]], [[trabalhos/Addula_2025|Addula et al. (2025)]].

**Fontes da fase**

[[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]], [[trabalhos/Fioreze_2026|Fioreze (2026)]], [[trabalhos/Addula_2025|Addula et al. (2025)]]

### Processamento

**Ações do cidadão**

O cidadão autoriza que determinados atributos ou dados associados à credencial sejam processados por serviços urbanos, idealmente com divulgação mínima. Essa autorização precisa ser compreensível e tecnicamente verificável para que o controle não seja apenas formal [[trabalhos/Maia_2025|Maia (2025)]].

**Ações das entidades administrativas**

As entidades administrativas processam credenciais, atributos e registros de acesso para decidir permissões, prestar serviços ou produzir análises agregadas. Quando os dados envolvem organizações distintas, a política de processamento precisa ser compatível com confiança distribuída e controle granular [[trabalhos/Fioreze_2026|Fioreze (2026)]].

**Riscos de segurança e privacidade**

O processamento pode revelar atributos sensíveis, permitir inferências indevidas ou manter dados além do necessário. Técnicas como criptografia homomórfica e ABE podem reduzir exposição, mas trazem custos computacionais e complexidade de integração [[trabalhos/Addula_2025|Addula et al. (2025)]], [[trabalhos/Fioreze_2026|Fioreze (2026)]].

**Estado da arte**

Os trabalhos de SSI em cidades inteligentes concentram-se mais em autenticação, verificação e controle de acesso do que em processamento privativo de dados após a apresentação da credencial [[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]]. Fioreze (2026) oferece uma base técnica para pensar controle baseado em atributos e compartilhamento seguro entre organizações [[trabalhos/Fioreze_2026|Fioreze (2026)]].

**Lacunas ou melhorias a investigar**

Há lacuna na integração entre SSI, ABE e criptografia homomórfica para permitir processamento urbano com menor exposição de atributos e avaliação quantitativa de desempenho, privacidade e escalabilidade [[trabalhos/Fioreze_2026|Fioreze (2026)]], [[trabalhos/Addula_2025|Addula et al. (2025)]].

**Fontes da fase**

[[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]], [[trabalhos/Fioreze_2026|Fioreze (2026)]], [[trabalhos/Addula_2025|Addula et al. (2025)]]

### Armazenamento

**Ações do cidadão**

O cidadão armazena credenciais em carteira digital ou agente SSI, mantendo controle sobre apresentação, atualização e eventual recuperação. A segurança da carteira é crítica porque perda de chave ou dispositivo pode afetar o acesso a serviços [[trabalhos/Maia_2025|Maia (2025)]].

**Ações das entidades administrativas**

As entidades administrativas podem armazenar esquemas, registros de status, chaves públicas, políticas ou evidências de auditoria em blockchains, bancos de dados ou sistemas descentralizados. O conteúdo armazenado precisa equilibrar auditabilidade, custo, privacidade e direito à atualização ou revogação [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]].

**Riscos de segurança e privacidade**

O armazenamento pode expor dados se atributos forem colocados indevidamente em ledger público, se backups forem mal protegidos ou se identificadores permitirem correlação de atividades. Armazenamento descentralizado também exige governança sobre disponibilidade, persistência e remoção lógica de dados [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]].

**Estado da arte**

YouGovern combina blockchain com IPFS/Web3.Storage para armazenamento descentralizado de dados de identidade, buscando privacidade, auditabilidade e controle de acesso [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]]. Cardoso (2024) e Maia (2025) exploram uso de blockchain e Hyperledger em cenários de cidades inteligentes [[trabalhos/Cardoso_2024|Cardoso (2024)]], [[trabalhos/Maia_2025|Maia (2025)]].

**Lacunas ou melhorias a investigar**

Faltam comparações entre alternativas de armazenamento descentralizado, análise de custo e latência, e estratégias de recuperação sem comprometer soberania ou privacidade do cidadão [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]], [[trabalhos/Fioreze_2026|Fioreze (2026)]].

**Fontes da fase**

[[trabalhos/Cardoso_2024|Cardoso (2024)]], [[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]], [[trabalhos/Fioreze_2026|Fioreze (2026)]]

### Revogação

**Ações do cidadão**

O cidadão pode precisar revogar credenciais por perda de controle, mudança de condição, expiração ou suspeita de comprometimento. Em SSI, essa revogação precisa ser verificável pelos serviços sem exigir que o cidadão exponha mais dados do que o necessário [[trabalhos/Maia_2025|Maia (2025)]].

**Ações das entidades administrativas**

As entidades administrativas mantêm ou consultam registros de status para impedir aceitação de credenciais inválidas. Contratos inteligentes e registradores de revogação podem automatizar parte desse controle, desde que não introduzam latência excessiva [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]].

**Riscos de segurança e privacidade**

Falhas de revogação podem permitir uso de credenciais comprometidas; por outro lado, mecanismos de consulta mal projetados podem revelar padrões de uso do cidadão. A revogação também pode ser alvo de negação de serviço ou inconsistências entre registros [[trabalhos/Fioreze_2026|Fioreze (2026)]].

**Estado da arte**

Papatheodorou et al. (2025) apresentam suporte a revogação em sistema SSI baseado em blockchain, enquanto Maia (2025) demonstra um fluxo de autenticação e controle de acesso que ainda deixa espaço para mecanismos concretos de revogação em larga escala [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]], [[trabalhos/Maia_2025|Maia (2025)]].

**Lacunas ou melhorias a investigar**

Há lacuna em revogação distribuída de baixa latência, validação de status em múltiplos serviços urbanos e análise de privacidade das consultas a registradores de revogação [[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Fioreze_2026|Fioreze (2026)]].

**Fontes da fase**

[[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]], [[trabalhos/Fioreze_2026|Fioreze (2026)]]

### Recuperação de acesso

**Ações do cidadão**

O cidadão precisa recuperar acesso quando perde a carteira, dispositivo, chave ou credencial necessária para usar serviços urbanos. Esse processo deve preservar a soberania da identidade, evitando recriar um modelo totalmente centralizado de recuperação por provedor [[trabalhos/Fioreze_2026|Fioreze (2026)]].

**Ações das entidades administrativas**

Entidades administrativas podem atuar como emissoras de nova credencial, verificadoras de prova de posse ou participantes de mecanismos distribuídos de recuperação. O desafio é ajudar na recuperação sem concentrar poder excessivo ou expor atributos sensíveis [[trabalhos/Maia_2025|Maia (2025)]].

**Riscos de segurança e privacidade**

Recuperação mal projetada pode permitir sequestro de identidade, engenharia social ou exposição de dados pessoais. Ao mesmo tempo, recuperação muito rígida pode gerar perda permanente de acesso a serviços essenciais [[trabalhos/Fioreze_2026|Fioreze (2026)]].

**Estado da arte**

Os trabalhos analisados tratam autenticação, controle de acesso, revogação e compartilhamento seguro, mas a recuperação pós-perda aparece menos consolidada do que emissão e verificação [[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]]. Fioreze (2026) aponta lacunas relacionadas a revogação de atributos, recuperação de credenciais e interoperabilidade em ambientes distribuídos [[trabalhos/Fioreze_2026|Fioreze (2026)]].

**Lacunas ou melhorias a investigar**

Uma linha promissora é investigar recuperação distribuída com limiares criptográficos, agentes de confiança ou mecanismos de prova que permitam restabelecer acesso sem revelar atributos além do necessário. Essa proposta precisa ser comparada com abordagens centralizadas e avaliada quanto a latência, usabilidade, segurança e privacidade [[trabalhos/Fioreze_2026|Fioreze (2026)]], [[trabalhos/Maia_2025|Maia (2025)]].

**Fontes da fase**

[[trabalhos/Maia_2025|Maia (2025)]], [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]], [[trabalhos/Fioreze_2026|Fioreze (2026)]]

## Fontes usadas

- [[trabalhos/Cardoso_2024|Cardoso (2024)]]
- [[trabalhos/Maia_2025|Maia (2025)]]
- [[trabalhos/Fioreze_2026|Fioreze (2026)]]
- [[trabalhos/Papatheodorou_2025|Papatheodorou et al. (2025)]]
- [[trabalhos/Vaziry_2025|Vaziry et al. (2025)]]
- [[trabalhos/Addula_2025|Addula et al. (2025)]]
