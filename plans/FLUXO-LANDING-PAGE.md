# Fluxo de trabalho — Landing page

## Objetivo

Executar a criação ou alteração de uma landing page em etapas sequenciais, com entregáveis verificáveis e pontos de decisão claros. O fluxo descreve como trabalhar; não autoriza por si só implementar ou publicar uma página.

## Acordos de execução

- Trabalhe em uma etapa por vez. Ao concluí-la, apresente o entregável ao usuário e aguarde sua orientação antes de iniciar a próxima.
- Preserve as decisões e os artefatos aprovados para que as etapas seguintes os usem como fonte de verdade.
- Se houver dúvida que afete escopo, conteúdo, comportamento ou aparência, pergunte ao usuário. Não preencha lacunas com requisitos inventados.
- Se testes ou revisão encontrarem problemas, retorne à etapa responsável, corrija e repita a validação pertinente.
- Registre decisões, alterações de escopo, resultados de testes e aprovações para manter a rastreabilidade.

## Etapas

| Etapa | Responsáveis | Entregável e condição para avançar |
| --- | --- | --- |
| 1. Levantamento de requisitos | Product Owner (PO) + Analista de Requisitos | Briefing e requisitos, construídos interativamente com o usuário e Codex. O usuário valida o levantamento antes do planejamento. |
| 2. Planejamento | Tech Lead + equipe necessária | Tarefas, prioridades, decisões técnicas, dependências, sequência e avaliação justificada de contratos por especificação/tarefa, mesmo quando nenhum contrato de produto adicional for necessário. Apresentar plano e avaliação e aguardar orientação. |
| 3. UX / UI Design | UX Designer + UI Designer | Organização e navegação (UX), wireframe e layout/identidade visual (UI, incluindo Figma quando aplicável). Identificar lacunas de interface; mudanças contratuais confirmadas exigem nova versão, revalidação e reapresentação do gate de Planning. Apresentar o design e aguardar orientação antes do desenvolvimento. |
| 4. Desenvolvimento | Desenvolvedor Frontend | Implementação conforme requisitos/design aprovados; verificar e cumprir contratos aplicáveis antes de cada tarefa dependente. Apresentar implementação e resultados das verificações locais. |
| 5. Testes e QA | QA Tester | Validar funcionamento, responsividade, acessibilidade e conformidade com contratos aplicáveis, separando validação estrutural de teste funcional. Problemas voltam para correção antes da revisão final. |
| 6. Revisão e aprovação | Tech Lead + Product Owner (PO) | Revisão técnica, conformance final dos contratos e validação contra requisitos. O PO aceita a entrega ou solicita ajustes; produção depende de aprovação explícita. |
| 7. Deploy | DevOps + Desenvolvedor Frontend | Publicação autorizada, verificação do site publicado e relato do endereço, versão e resultado da verificação. |

## Procedimento por etapa

### 1. Levantamento de requisitos — PO + Analista de Requisitos

1. O Codex conduz uma conversa interativa com o usuário para entender objetivo, público, conteúdo, funcionalidades, restrições e critérios de sucesso.
2. O Analista de Requisitos transforma as respostas em requisitos claros e verificáveis. Investiga, no mínimo, as necessidades para header, banner, catálogo, contato e rodapé quando fizerem parte do escopo.
3. O PO confere se o briefing representa o objetivo do usuário, identifica prioridades e aponta decisões de produto que ainda precisam ser tomadas.
4. O Codex apresenta um resumo, separa decisões confirmadas de perguntas em aberto e pede validação do usuário. Não avança ao planejamento até receber essa validação ou novas instruções.

**Entregável:** briefing, requisitos funcionais e não funcionais pertinentes, prioridades, restrições, critérios de aceitação e perguntas ainda abertas.

### 2. Planejamento — Tech Lead + equipe necessária

Dividir o escopo validado em tarefas, identificar dependências, riscos e sequência, e propor tecnologias considerando o projeto existente. Para cada tarefa/especificação, registrar se um contrato de produto é necessário e por quê. Quando necessário, definir os detalhes contratuais apenas a partir de requisitos e decisões técnicas confirmadas; se faltarem dados, registrar os campos pendentes e encaminhar perguntas ao responsável. Gerar rascunhos vinculados à especificação aprovada, validar e apresentar para revisão. Essa avaliação é entregável obrigatório do planejamento, inclusive quando conclui que nenhum contrato adicional é necessário. Apresentar plano e avaliação ao usuário antes de iniciar UX/UI ou desenvolvimento.

**Entregável:** plano de tarefas priorizadas, dependências e decisões técnicas registradas.

**Entregável adicional obrigatório:** `plans/contract-assessment.yaml`, referenciando a especificação aprovada, tarefas avaliadas, hash e justificativa. Contratos necessários ficam em `contracts/generated/`; rascunhos incompletos não liberam tarefas dependentes.

### 3. UX / UI Design — UX Designer + UI Designer

O UX Designer define a organização da informação e os caminhos de navegação. O UI Designer traduz isso em wireframe e layout visual, definindo identidade, cores, tipografia, componentes e estados responsivos. Se surgir uma obrigação de interface que não consta no plano, registre a lacuna e peça orientação. Após confirmação, o Tech Lead pode atualizar tarefa e avaliação em UX/UI, gerar outra versão do contrato e solicitar nova aprovação. A alteração também invalida o gate de Planning, que deve ser reapresentado e aprovado antes de qualquer tarefa dependente avançar. Apresentar o resultado para orientação do usuário antes de iniciar a implementação.

**Entregável:** estrutura de navegação, wireframe e layout visual aprovado para implementação, com referência ao arquivo Figma se utilizado.

### 4. Desenvolvimento — Desenvolvedor Frontend

Antes de cada tarefa, verificar contrato aplicável, versão/hash, aprovação, entradas, dependências e escopo. Implementar a estrutura semântica, estilos responsivos e interações previstas, seguindo requisitos, plano, design e contratos aprovados. Se a implementação descobrir uma obrigação nova, interromper a tarefa dependente e encaminhar para o Tech Lead e usuário; não alterar silenciosamente contrato ou requisito aprovado. Informar o que foi implementado e quais verificações locais foram executadas; não declarar testes que não foram realizados.

**Entregável:** versão implementada e resumo das verificações locais.

### 5. Testes e QA — QA Tester

Verificar critérios de aceitação, funcionamento, tamanhos de tela, acessibilidade pertinente e obrigações dos contratos aplicáveis. Registrar validação estrutural de schemas separadamente de testes funcionais; schema válido não prova que o requisito foi atendido. Classificar problemas, fornecer passos para reproduzir e evidências, e informar itens aprovados, reprovados e não verificados. Encaminhar problemas ao responsável pela implementação e repetir os testes afetados após correções.

**Entregável:** relatório de testes com resultado e evidências.

### 6. Revisão e aprovação — Tech Lead + PO

O Tech Lead revisa arquitetura, implementação, riscos, qualidade técnica e conformidade final com contratos, usando requisitos e relatório de QA. Confirma que versões e hashes aprovados continuam válidos e que mudanças de origem foram revalidadas. O PO decide se o resultado atende ao briefing e aos critérios de aceitação. Solicitações de ajuste retornam à etapa responsável e passam novamente por QA e revisão conforme o impacto.

**Entregável:** parecer técnico e decisão explícita do PO — aprovado ou ajustes solicitados.

### 7. Deploy — DevOps + Desenvolvedor Frontend

Iniciar somente após aprovação explícita do PO e orientação do usuário para publicação. Configurar o ambiente de produção conforme o plano aprovado, publicar a versão aprovada e verificar o site no endereço de produção. Relatar endereço publicado, versão e resultado das verificações pós-deploy.

**Entregável:** site publicado e verificado, com registro do resultado.
