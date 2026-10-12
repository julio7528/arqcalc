# Orquestrador de workflow

MVP Python para conduzir o fluxo existente em specs/workflow.yaml. A definição do fluxo permanece declarativa; estados de execução, respostas, aprovações, artefatos e eventos ficam no SQLite local configurado em orchestrator/config.json.

## Instalação e validação

Requer Python 3.11 ou superior.

Na raiz do projeto, instale as duas dependências usadas para ler e validar YAML:

    python -m pip install -r requirements.txt
    python -m unittest discover -s tests -v

O primeiro comando instala PyYAML e jsonschema. Nenhum pacote adicional ou serviço externo é usado.

## Comandos

Todos os comandos devem ser executados na raiz do projeto.

    python -m orchestrator status
    python -m orchestrator evaluate
    python -m orchestrator evaluate planning --json
    python -m orchestrator discover

discover inicia a etapa atual, reaproveita informações que já constem numa especificação e pergunta somente pelos campos obrigatórios ausentes. Para registrar uma resposta sem modo interativo:

    python -m orchestrator answer objective "Resultado que o usuário confirmou."
    python -m orchestrator answer scope "Escopo confirmado pelo usuário."
    python -m orchestrator answer functional_requirement "Comportamento observável confirmado."
    python -m orchestrator discover --no-interactive

Nenhum arquivo de especificação é criado até haver um objetivo, um escopo e ao menos um requisito funcional verificável confirmados. O próximo identificador disponível é calculado em toda a árvore specs/; specs/SPEC-001.md continua reservado e vazio. Um rascunho incompleto existente é atualizado no mesmo caminho.

O rascunho registra os IDs dos eventos SQLite que confirmaram objetivo, escopo e requisitos. Se houver mais de uma especificação válida, o workflow bloqueia até uma ser selecionada com spec select.

Revise e aprove explicitamente a versão apresentada:

    python -m orchestrator spec list
    python -m orchestrator spec show SPEC-002
    python -m orchestrator spec select SPEC-002
    python -m orchestrator spec review SPEC-002
    python -m orchestrator spec approve SPEC-002 --version 0.1.0 --hash HASH_MOSTRADO_NA_REVISAO --confirm --evidence "Aprovo SPEC-002 versão 0.1.0."
    python -m orchestrator complete --confirm
    python -m orchestrator advance --authorize --evidence "Autorizo iniciar o planejamento."
    python -m orchestrator start

spec review marca a versão como IN_REVIEW e aguarda o usuário. A aprovação grava ator, data/hora, decisão, evidência, ID DEC, versão e hash substantivo no SQLite e no arquivo. A aprovação não conclui a etapa nem avança o workflow. complete exige o gate da etapa; advance exige uma autorização explícita e registra um novo evento no decision log. Etapas seguintes ficam em PENDING até serem iniciadas por comando próprio.

Para solicitar ajustes, use:

    python -m orchestrator spec reject SPEC-002 --version 0.1.0 --hash HASH_MOSTRADO_NA_REVISAO --confirm --reason "Ajustar o requisito RF-001 conforme esta orientação."
    python -m orchestrator answer functional_requirement "Novo comportamento confirmado pelo usuário."
    python -m orchestrator discover

Para artefatos das etapas seguintes, registre o arquivo, a origem e os IDs relacionados antes de solicitar aprovação do gate:

    python -m orchestrator artifact register planning implementation-plan plans/implementation-plan.md --version 1 --spec-ref SPEC-002@0.1.0 --requirement RF-001
    python -m orchestrator artifact register planning work-items tasks/work-items.md --version 1 --spec-ref SPEC-002@0.1.0 --requirement RF-001 --task TASK-001
    python -m orchestrator gate review planning
    python -m orchestrator gate approve planning --hash HASH_MOSTRADO_NA_REVISAO --confirm --evidence "Aprovo os entregáveis de planejamento registrados."

Os arquivos precisam existir, corresponder aos entregáveis declarados e apontar para a versão aprovada da especificação. Requisitos precisam constar nessa especificação; IDs de tarefa precisam constar no arquivo ou em tasks/. Uma alteração posterior no arquivo invalida o gate e exige nova validação e aprovação.

## Contratos

Planning também exige `plans/contract-assessment.yaml`, inclusive quando a avaliação do Tech Lead conclui que não é necessário criar contratos de produto. O arquivo deve referenciar a versão/hash da especificação aprovada e as tarefas avaliadas. Consulte [`contracts/README.md`](../contracts/README.md) para schemas e o formato de tarefas.

```powershell
python -m orchestrator contract assess --justification "Nenhuma tarefa exige interface ou obrigação adicional."
python -m orchestrator contract assess --task-file tasks/TASK-001.yaml --contract-task TASK-001 --justification "A tarefa define uma interface compartilhada."
python -m orchestrator contract generate --task-file tasks/TASK-001.yaml
python -m orchestrator contract validate CONTRACT-004 --version 0.1.0 --check-inputs
python -m orchestrator contract review CONTRACT-004 --version 0.1.0
python -m orchestrator contract approve CONTRACT-004 --version 0.1.0 --hash HASH_MOSTRADO_NA_REVISAO --confirm --evidence "Aprovo esta versão exata."
python -m orchestrator contract evaluate --stage development --task TASK-001 --json
python -m orchestrator contract validate-output CONTRACT-004 docs/contract-output.json
python -m orchestrator contract validate-handoff tasks/TASK-001-handoff.json
```

Contratos de produto são derivados de especificações aprovadas e artefatos de planejamento. Campos técnicos ausentes ficam explícitos em `missing_fields`; rascunhos incompletos não podem ser aprovados. A aprovação é vinculada ao ID, versão, hash e evento de revisão no SQLite. Alterações na especificação ou no contrato invalidam a prontidão da tarefa dependente. Aprovar um contrato permanece independente de aprovar o gate da etapa ou autorizar a próxima etapa.

Se UX/UI confirmar uma obrigação de interface ausente, atualize a tarefa e repita `contract assess` durante `ux-ui-design`; gere, revise e aprove a nova versão. A avaliação atualizada invalida o gate de Planning, que precisa ser revisto e aprovado novamente antes de liberar tarefas dependentes.

Para a etapa de produção, além do gate da etapa 6, a etapa deployment exige uma autorização específica de escopo e versão antes de qualquer execução:

    python -m orchestrator deployment authorize --confirm --scope "produção: calculadora.example" --version "1.0.0" --evidence "Autorizo publicar esta versão em produção."

Esse comando só aceita quando deployment é a etapa atual e a revisão técnica e o aceite do Product Owner estão concluídos e aprovados.

## Execução controlada

run é dry-run por padrão; apenas exibe o comando e o contexto preparado:

    python -m orchestrator run
    python -m orchestrator run --task TASK-001
    python -m orchestrator resume

run exige que a etapa atual tenha sido iniciada. Na Etapa 1, discover inicia a etapa; nas demais etapas, use start depois do avanço explícito. Em Desenvolvimento, se a avaliação de Planning apontar tarefas que exigem contratos, informe `--task` para resolver apenas as obrigações daquela tarefa.

O padrão está em orchestrator/config.json: comando codex exec -, execução real desabilitada e timeout de 120 segundos. O processo real só pode ser iniciado com --execute --authorize, etapa atual em andamento, dependências atendidas, configuração habilitada e comando preenchido. Depois de revisar as permissões e o sandbox apropriados, o usuário pode habilitar allow_real_execution em orchestrator/config.json e então executar:

    python -m orchestrator run --execute --authorize
    python -m orchestrator resume --execute --authorize

O adaptador envia o prompt por stdin, não usa shell, limita o tempo e o tamanho de logs e registra códigos de saída. A sintaxe documentada do comando codex exec com - para ler o prompt de stdin aparece no [exemplo oficial de automação com Codex](https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex). Nenhum processo Codex foi iniciado para construir ou testar este MVP; testes do adaptador usam apenas um processo Python falso. A configuração real permanece desabilitada.

## Estados e aprovações

Resultados de resolução são distintos dos estados de execução:

- MISSING: ainda não existe uma especificação de produto preenchida.
- DRAFT: existe uma especificação com campos obrigatórios pendentes.
- AWAITING_APPROVAL: objetivo, escopo e requisito verificável estão completos, mas falta aprovação humana válida.
- READY: dependências atendidas e aprovação válida da versão/hash presente.
- BLOCKED: há dependência, artefato, gate ou restrição não atendidos.

Execuções usam PENDING, RUNNING, COMPLETED e FAILED numa tabela separada. Um status APPROVED escrito manualmente no Markdown não concede aprovação. Editar o conteúdo substantivo depois da aprovação invalida o hash. Gates de artefato também são vinculados aos hashes dos arquivos validados.

## Persistência e limites

- Workflow e aprovações declarativas: specs/workflow.yaml, validadas por orchestrator/workflow.schema.json.
- Respostas, execuções, gates, aprovações, artefatos e eventos: .codex/orchestrator-state.sqlite3 (ignorado pelo Git).
- Contratos, avaliações, validações, handoffs e hashes ligados à execução: `contracts/` e tabelas adicionadas ao mesmo SQLite por migrações aditivas.
- Especificações: specs/generated/, com o modelo specs/templates/SPEC-TEMPLATE.md.
- Perfis e Skills são lidos dos arquivos existentes em .codex/agents/ e .agents/skills/; o orquestrador não duplica suas instruções.
- A recuperação marca execuções deixadas em RUNNING como FAILED; resume reavalia e só tenta novamente com a autorização e configuração pedidas.

Este MVP executa um único executor. Agendamento distribuído, execução paralela, isolamento por Git Worktree e dashboard permanecem planejados. A criação de conteúdo para as etapas de planejamento até deploy depende de autorização da etapa e da tarefa Codex correspondente; nenhum deploy automático está habilitado.
