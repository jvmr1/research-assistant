# Metodologia e rastreabilidade da revisão

Atualizado: 2026-09-21T07:21:38

Orientação analisada: `ed7dd347db1679b96f2b`

## Objetivo e escopo

Identificar trabalhos recentes sobre o tema definido em INSTRUCOES.md, selecionar os que merecem aprofundamento, extrair evidências e formular hipóteses de lacuna com propostas de contribuição ainda não validadas.

## Consultas e fontes

As consultas são as registradas em INSTRUCOES.md e as consultas posteriores geradas para confrontar hipóteses. A descoberta usa OpenAlex, Semantic Scholar e Crossref; o sistema registra quais fontes responderam a cada busca. O texto completo é procurado em versões abertas indicadas pelas fontes, em PDF ou HTML/XML.

### Consultas registradas

- `André Luiz Almeida Cardoso limitations future work` — origem: proposta b979c89dcbc71adaf57a; página atual: 1

- `André Luiz Almeida Cardoso smart cities IoT blockchain access control` — origem: proposta b979c89dcbc71adaf57a; página atual: 1

- `Danilo_TCC_final limitations future work` — origem: proposta 12b50465b336547629f6; página atual: 1

- `Danilo_TCC_final smart cities IoT blockchain access control` — origem: proposta 12b50465b336547629f6; página atual: 1

- `dissertacao_wesleyFioreze_23_06_2026_anotada limitations future work` — origem: proposta 68f1e2c11e34b36725f0; página atual: 1

- `dissertacao_wesleyFioreze_23_06_2026_anotada smart cities IoT blockchain access control` — origem: proposta 68f1e2c11e34b36725f0; página atual: 1

## Seleção e análise

O fluxo reproduz uma revisão em funil: (1) definição de variáveis e consultas; (2) identificação por fontes acadêmicas; (3) deduplicação por DOI ou título; (4) triagem de título e resumo; (5) pré-leitura de introdução/conclusão ou resumo para confirmar alinhamento; (6) leitura integral dos aprovados; (7) extração de evidências; (8) comparação e síntese de lacunas; (9) propostas de contribuição como hipóteses a validar.

1. Resultados são deduplicados por DOI ou título normalizado.

2. A IA faz triagem de título e resumo em `priorizar`, `revisar`, `baixa` ou `sem_resumo`; a triagem não é decisão definitiva.

3. São tentados textos completos abertos dos trabalhos priorizados/revisados. Quando não há texto completo, o resumo é usado na pré-leitura como evidência limitada.

4. Antes da leitura integral, a IA avalia introdução e conclusão quando extraíveis para decidir `ler_integralmente`, `ler_com_resumo`, `manter_como_contexto`, `descartar` ou `precisa_texto_melhor`.

5. O texto aprovado é dividido em trechos. A IA produz fichas com resumo, interpretação, dúvidas e citações literais conferidas no trecho original. Propostas preliminares podem ser geradas a partir do fichamento de um único trabalho. Com novas leituras, elas podem ser reforçadas, contraditas, substituídas ou virar propostas comparativas do estado da arte.

6. A próxima busca só é liberada quando não há trabalho pendente no acervo. Cada trabalho é levado até um destino claro — descartado, sem texto integral, contexto ou lido/sintetizado — antes de o agente escolher outro. Assim o acervo cresce por trabalhos processados, não por coleta contínua sem síntese.

## Tags de busca

Tags derivadas das consultas: abe, blockchain, cidades-inteligentes, controle-de-acesso, credenciais-verificaveis, criptografia, criptografia-homomorfica, governanca-de-dados, identidade-digital, interoperabilidade, iot, privacidade, sistemas-distribuidos, ssi

## Contagem do fluxo

- Registros no acervo após deduplicação: 176.

- Trabalhos com triagem concluída: 18.

- Trabalhos selecionados para aprofundamento: até não informado.

- Trabalhos com pré-leitura concluída: 3.

- Leituras aprofundadas concluídas: 0.

- Propostas geradas: 7.

## Registros das buscas

- 2026-09-15T23:00:05 — fontes: OpenAlex; página: 1; consulta: **smart cities IoT blockchain access control**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:08 — fontes: OpenAlex; página: 1; consulta: **self sovereign identity smart cities interoperability**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:10 — fontes: OpenAlex; página: 1; consulta: **decentralized identity verifiable credentials public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:13 — fontes: OpenAlex; página: 1; consulta: **attribute based encryption IoT data sharing blockchain**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:20 — fontes: OpenAlex; página: 1; consulta: **blockchain enabled secure IIoT data sharing organizations**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:23 — fontes: OpenAlex; página: 1; consulta: **authentication access control blockchain smart cities**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:26 — fontes: OpenAlex; página: 1; consulta: **blockchain authentication public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:29 — fontes: OpenAlex; página: 1; consulta: **blockchain access control public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:31 — fontes: OpenAlex; página: 1; consulta: **blockchain interoperability public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:34 — fontes: OpenAlex; página: 1; consulta: **blockchain privacy public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:37 — fontes: OpenAlex; página: 1; consulta: **blockchain data sharing public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:40 — fontes: OpenAlex; página: 1; consulta: **blockchain revocation public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:42 — fontes: OpenAlex; página: 1; consulta: **blockchain cross-organization security public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:45 — fontes: OpenAlex; página: 1; consulta: **self-sovereign identity authentication public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:48 — fontes: OpenAlex; página: 1; consulta: **self-sovereign identity access control public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:51 — fontes: OpenAlex; página: 1; consulta: **self-sovereign identity interoperability public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:54 — fontes: OpenAlex; página: 1; consulta: **self-sovereign identity privacy public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:56 — fontes: OpenAlex; página: 1; consulta: **self-sovereign identity data sharing public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:00:59 — fontes: OpenAlex; página: 1; consulta: **self-sovereign identity revocation public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:01:02 — fontes: OpenAlex; página: 1; consulta: **self-sovereign identity cross-organization security public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:01:05 — fontes: OpenAlex; página: 1; consulta: **decentralized identity authentication public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:01:08 — fontes: OpenAlex; página: 1; consulta: **decentralized identity access control public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:01:11 — fontes: OpenAlex; página: 1; consulta: **decentralized identity interoperability public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:01:14 — fontes: OpenAlex; página: 1; consulta: **decentralized identity privacy public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:01:16 — fontes: OpenAlex; página: 1; consulta: **decentralized identity data sharing public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:01:19 — fontes: OpenAlex; página: 1; consulta: **decentralized identity revocation public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:01:22 — fontes: OpenAlex; página: 1; consulta: **decentralized identity cross-organization security public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:01:24 — fontes: OpenAlex; página: 1; consulta: **verifiable credentials authentication public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:01:27 — fontes: OpenAlex; página: 1; consulta: **verifiable credentials access control public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-15T23:01:30 — fontes: OpenAlex; página: 1; consulta: **verifiable credentials interoperability public sector**; origem: instruções do pesquisador; falhou. Nenhuma fonte acadêmica respondeu nesta consulta.

- 2026-09-16T10:56:26 — fontes: OpenAlex, Crossref; página: 1; consulta: **smart cities IoT blockchain access control**; origem: instruções do pesquisador; concluída. Miller_2025, Mansoor_2025, Almutairi_2025, Hudda_2025, Enaya_2025, Islam_2025, Yee_2025, Denis_2025, Ghadi_2025, Ababio_2025

- 2026-09-16T13:52:32 — fontes: OpenAlex, Crossref; página: 1; consulta: **smart cities IoT blockchain access control**; origem: instruções do pesquisador; concluída. Miller_2025, Mansoor_2025, Almutairi_2025, Hudda_2025, Enaya_2025, Islam_2025, Yee_2025, Denis_2025, Ghadi_2025, Ababio_2025

- 2026-09-16T13:52:41 — fontes: OpenAlex, Crossref; página: 1; consulta: **self sovereign identity smart cities interoperability**; origem: instruções do pesquisador; concluída. Denis_2025, Miron_2025, Papatheodorou_2025, Rejeb_2025, Prajapati_2025, Farhan_2025, Paredes-García_2025, Ramírez-Gordillo_2025, Nair_2025, Farina_2025

- 2026-09-16T14:14:20 — fontes: OpenAlex, Crossref; página: 1; consulta: **decentralized identity verifiable credentials public sector**; origem: instruções do pesquisador; concluída. Cordeiro_2025, Ramírez-Gordillo_2025, Babel_2025, Ding_2025, Gudipati_2025, Prajapati_2025, Moya_2025, Sofronie_2025, Calzada_2025, Ciriello_2025

- 2026-09-16T14:33:52 — fontes: OpenAlex, Crossref; página: 1; consulta: **attribute based encryption IoT data sharing blockchain**; origem: instruções do pesquisador; concluída. Tian_2025, Zhang_2025, Enaya_2025, Addula_2025, Mehla_2025, Li_2025, Nie_2025, Sathyabama_2025, Hudda_2025, Bagchi_2025

- 2026-09-16T17:38:10 — fontes: OpenAlex, Crossref; página: 2; consulta: **smart cities IoT blockchain access control**; origem: instruções do pesquisador; concluída. Sacoto-Cabrera_2025, Δρίτσας_2025, Addula_2025, Qiu_2025, Ragab_2025, Limbepe_2025, Kulothungan_2025, Pandey_2025, Miron_2025, Xiong_2025

- 2026-09-16T18:08:54 — fontes: OpenAlex, Crossref; página: 2; consulta: **self sovereign identity smart cities interoperability**; origem: instruções do pesquisador; concluída. Chaurasia_2026, Jôrgensen_2025, Karaduman_2025, Chowdhury_2025, Jamshed_2025, Maciá-Lillo_2025, Alar_2026, Karim_2025, Umoren_2025, Nie_2025

- 2026-09-16T18:52:40 — fontes: OpenAlex, Crossref; página: 3; consulta: **smart cities IoT blockchain access control**; origem: instruções do pesquisador; concluída. Sathyabama_2025, Alabdali_2025, Δρίτσας_2025_2, Alsubaei_2025, Erukala_2025, Ramírez-Gordillo_2025, Tawfik_2025, Singh_2025, Kotian_2025, Thanasi-Boçe_2025

- 2026-09-16T19:20:31 — fontes: OpenAlex, Crossref; página: 3; consulta: **self sovereign identity smart cities interoperability**; origem: instruções do pesquisador; concluída. Adeshina_2025, Khayer_2025, Enaya_2025, Fathalla_2025, Villafranca_2025, Anthony_2025, Liu_2025, Alatawi_2025, Naseef_2025, S_2026

- 2026-09-16T19:26:22 — fontes: OpenAlex, Crossref; página: 2; consulta: **decentralized identity verifiable credentials public sector**; origem: instruções do pesquisador; concluída. Buldini_2025, Papatheodorou_2025, Dordevic_2025, Karaduman_2025, Soy_2025, Alanzi_2025, Farhan_2025, Tommerdahl_2025, Buccafurri_2025, Siam_2025

- 2026-09-16T19:28:23 — fontes: OpenAlex, Crossref; página: 2; consulta: **attribute based encryption IoT data sharing blockchain**; origem: instruções do pesquisador; concluída. Wu_2025, Sobhan_2025, Alfahaid_2025, Mallick_2025, Ferrer-Rojas_2025, Ramírez-Gordillo_2025, Gao_2025, Limbepe_2025, Owusu-Berko_2025, Kumar_2025

- 2026-09-16T19:43:40 — fontes: OpenAlex, Crossref; página: 1; consulta: **blockchain enabled secure IIoT data sharing organizations**; origem: instruções do pesquisador; concluída. Ababio_2025, Shukla_2025, Asaithambi_2025, Munusamy_2025, Qiu_2025, Abdullahi_2025, Enaya_2025, Ghadi_2025, Zhukabayeva_2025, Hemdan_2025

- 2026-09-16T20:35:25 — fontes: OpenAlex, Crossref; página: 4; consulta: **smart cities IoT blockchain access control**; origem: instruções do pesquisador; concluída. Nie_2025, Rojek_2025, Reis_2025, Rehman_2025, Samuels_2025, O_2025, Ahsan_2025, Koulouras_2025, Alfahaid_2025, Waqar_2025

- 2026-09-16T20:38:05 — fontes: OpenAlex, Crossref; página: 4; consulta: **self sovereign identity smart cities interoperability**; origem: instruções do pesquisador; concluída. Saleh_2025, Alreshidi_2025, Vaziry_2025, Matta_2026, Aydeger_2025, Fendt_2026, Mazrae_2025, Pasupuleti_2025, Lopez_2026, Sebestyen_2025

- 2026-09-16T21:17:35 — fontes: OpenAlex, Crossref; página: 3; consulta: **decentralized identity verifiable credentials public sector**; origem: instruções do pesquisador; concluída. Babel_2025_2, Chowdhury_2025_2, Paredes-García_2025, Balan_2025, Ullah_2025, Pinyi_2026, Vindigni_2026, Zhang_2025_2, Mitrea_2025, Barros_2025

- 2026-09-20T23:30:20 — fontes: OpenAlex, Crossref, Semantic Scholar; página: 1; consulta: **smart city definition seminal survey urban computing**; origem: referencial conceitual obrigatório; concluída. Τρίγκα_2025, Assimakopoulos_2025, Al-Rimawi_2025, Zhou_2025, Coco_2025, Marjanović_2025, Alharthi_2026, Chen_2025, Kim_2025, Benedictis_2025

- 2026-09-20T23:34:18 — fontes: OpenAlex, Crossref; página: 1; consulta: **self-sovereign identity principles decentralized identity survey**; origem: referencial conceitual obrigatório; concluída. Chan_2025, Babel_2025, Schumm_2025, Ramírez-Gordillo_2025, Cordeiro_2025, Le_2025, Papatheodorou_2025, Prajapati_2025, Palavali_2025, Rjab_2026

- 2026-09-20T23:38:40 — fontes: OpenAlex, Crossref; página: 1; consulta: **W3C decentralized identifiers DID core verifiable credentials standard**; origem: referencial conceitual obrigatório; concluída. Garzon_2026, Cordeiro_2025, Ramírez-Gordillo_2025, Ding_2025_2, Buldini_2025_2, Ding_2025, Zhang_2025_2, Zhang_2025_3, Le_2025, Moya_2025

- 2026-09-20T23:38:45 — fontes: OpenAlex, Crossref; página: 1; consulta: **attribute-based encryption original paper survey ciphertext-policy ABE**; origem: referencial conceitual obrigatório; concluída. Kerl_2025, Abidin_2025, Wan_2025, Wu_2025_2, Ullah_2025, Tawfik_2025, Li_2025, Leilei_2025, Pióro_2026, Jiang_2025

- 2026-09-20T23:38:49 — fontes: OpenAlex, Crossref; página: 1; consulta: **homomorphic encryption original paper survey privacy preserving computation**; origem: referencial conceitual obrigatório; concluída. Tawfik_2025_2, Lee_2025, Kerl_2025, Haripriya_2025, Rahmati_2025, Jiao_2025, Zhan_2025, Shenoy_2025, Gilbert_2025, Δρίτσας_2025

- 2026-09-20T23:38:53 — fontes: OpenAlex, Crossref; página: 1; consulta: **verifiable credentials revocation status list survey**; origem: referencial conceitual obrigatório; concluída. Lee_2025_2, Zhang_2025_3, Δρίτσας_2025_2, Sofronie_2025, Buldini_2025_2, Enaya_2025, Rahdari_2025, Ramírez-Gordillo_2025, Hugenroth_2025, Moya_2025

- 2026-09-20T23:38:57 — fontes: OpenAlex, Crossref; página: 1; consulta: **self-sovereign identity smart cities verifiable credentials revocation blockchain**; origem: validação de proposta; concluída. Ramírez-Gordillo_2025, Papatheodorou_2025, Karaduman_2025, Enaya_2025, Rejeb_2025, Farhan_2025, Prajapati_2025, Paredes-García_2025, Khayer_2025, Chaurasia_2026

- 2026-09-20T23:40:57 — fontes: OpenAlex, Crossref; página: 1; consulta: **smart city definition seminal survey urban computing**; origem: referencial conceitual obrigatório; concluída. Τρίγκα_2025, Assimakopoulos_2025, Al-Rimawi_2025, Zhou_2025, Coco_2025, Marjanović_2025, Alharthi_2026, Chen_2025, Kim_2025, Benedictis_2025

- 2026-09-20T23:41:01 — fontes: OpenAlex, Crossref; página: 1; consulta: **Caragliu Del Bo Nijkamp smart cities definition**; origem: referencial conceitual obrigatório; concluída. Almulhim_2025, Karger_2025, Oyadeyi_2025, Bozkurt_2025, Aghdam_2025, Ntanda_2025, Zakka_2025, Russo_2025, Li_2025_2, Krúpová_2025

- 2026-09-20T23:41:47 — fontes: OpenAlex, Crossref; página: 1; consulta: **Caragliu Del Bo Nijkamp smart cities definition**; origem: referencial conceitual obrigatório; concluída. Caragliu_2025

- 2026-09-20T23:41:52 — fontes: OpenAlex, Crossref; página: 1; consulta: **Giffinger smart cities ranking definition**; origem: referencial conceitual obrigatório; concluída. Ostrowski_2025

- 2026-09-21T00:10:47 — fontes: OpenAlex, Crossref; página: 1; consulta: **smart city definition seminal survey urban computing**; origem: referencial conceitual obrigatório; concluída. Thiyagarajan_2025, Affif_2025, Kayode_2026, Sharma_2025

- 2026-09-21T00:48:32 — fontes: OpenAlex, Crossref; página: 1; consulta: **Caragliu Del Bo Nijkamp smart cities definition**; origem: referencial conceitual obrigatório; concluída. Caragliu_2025

- 2026-09-21T00:51:07 — fontes: OpenAlex, Crossref; página: 1; consulta: **Giffinger smart cities ranking definition**; origem: referencial conceitual obrigatório; concluída. Ostrowski_2025

## Limitações

A disponibilidade de texto completo depende de acesso aberto. A análise pode ser baseada apenas no resumo. PDFs sem texto extraível, figuras e tabelas podem exigir conferência humana. As propostas são hipóteses exploratórias: não comprovam novidade, ausência de trabalhos ou viabilidade.

## Pendências

PDF Erukala_2025: Texto HTML/XML sem conteúdo extraível.

PDF Khayer_2025: Texto HTML/XML sem conteúdo extraível.

PDF Fathalla_2025: Texto HTML/XML sem conteúdo extraível.

PDF Anthony_2025: Texto HTML/XML sem conteúdo extraível.

PDF Alatawi_2025: Texto HTML/XML sem conteúdo extraível.

PDF Alanzi_2025: Texto HTML/XML sem conteúdo extraível.

PDF Buccafurri_2025: Texto HTML/XML sem conteúdo extraível.

PDF Siam_2025: Texto HTML/XML sem conteúdo extraível.

PDF Wu_2025: Texto HTML/XML sem conteúdo extraível.

PDF Alfahaid_2025: Texto HTML/XML sem conteúdo extraível.

PDF Ferrer-Rojas_2025: Texto HTML/XML sem conteúdo extraível.

PDF Zhukabayeva_2025: Texto HTML/XML sem conteúdo extraível.

PDF Hemdan_2025: Texto HTML/XML sem conteúdo extraível.

PDF Rojek_2025: Texto HTML/XML sem conteúdo extraível.

PDF Reis_2025: Texto HTML/XML sem conteúdo extraível.

PDF Ahsan_2025: Texto HTML/XML sem conteúdo extraível.

PDF Koulouras_2025: Texto HTML/XML sem conteúdo extraível.

PDF Saleh_2025: Texto HTML/XML sem conteúdo extraível.

PDF Matta_2026: Texto HTML/XML sem conteúdo extraível.

PDF Sebestyen_2025: Texto HTML/XML sem conteúdo extraível.