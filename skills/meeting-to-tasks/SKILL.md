---
name: meeting-to-tasks
description: >
  Converte transcrições/atas de reunião em um plano de ação completo: tarefas detalhadas (com passos),
  responsáveis, prazos, prioridades, dependências, critérios de pronto, decisões, pendências e riscos.
  Use quando o usuário colar uma transcrição, pedir "action items", "tarefas", "follow-ups" ou "resumo em tarefas".
argument-hint: "[cole a transcrição] ou [/meeting-to-tasks caminho/do/arquivo.txt]"
allowed-tools: Read, Glob, Grep
---

# Meeting → Tasks (Tarefas didáticas a partir de transcrições)

## Objetivo
Transformar qualquer transcrição de reunião (com ou sem timestamps) em:
1) **Lista de tarefas acionáveis e didáticas** (com passos claros, critérios de pronto, dependências e próximos passos)
2) **Decisões tomadas**
3) **Pendências / perguntas em aberto**
4) **Riscos e bloqueios**
5) **Resumo de follow-up** (pronto para enviar no Slack/Email)

## Entrada (o que você recebe)
- **Transcrição colada no chat** (principal)
- OU **arquivo** passado em `$ARGUMENTS` (ex.: `/meeting-to-tasks notes/reuniao-2026-01-29.md`)
  - Se `$ARGUMENTS` parecer caminho/padrão: use `Glob` se necessário e `Read` para abrir.

### Se faltar contexto (não pergunte demais)
NÃO interrompa para perguntar. Faça suposições explícitas e use placeholders:
- Dono: `UNASSIGNED` (ou “Sugestão: <nome>”)
- Prazo: `TBD`
- Prioridade: `P2 (média)` por padrão
- Status: `Backlog`
- Se ninguém foi citado: “Necessário definir owner na próxima checkpoint”.

## Regras de ouro (não-negociáveis)
1) **Não invente tarefas**: toda tarefa deve estar ancorada em evidência do texto (frase, speaker, timestamp se houver).
2) **Prefira ações com entregável**: “Criar X”, “Enviar Y”, “Decidir Z”, “Atualizar W”.
3) **Tarefas didáticas**: cada tarefa deve ter passos “como fazer”, não só o título.
4) **Critério de pronto (DoD)** obrigatório: como saber que terminou.
5) **Separar**: decisões ≠ tarefas ≠ perguntas ≠ ideias soltas.
6) **Escreva em PT-BR** (salvo se a transcrição estiver em outro idioma; nesse caso, mantenha o idioma principal).

---

## Fluxo de trabalho (sempre siga)
### 1) Pré-processamento rápido
- Detecte estrutura: agenda, tópicos, timestamps, speakers, itens recorrentes (“vamos”, “precisa”, “ficou de”, “action item”, “follow up”, “decidimos”).
- Normalize nomes de pessoas/áreas (ex.: “João”, “JP”, “Joao P.” → “João (JP)”).

### 2) Extração (o que existe no texto)
Extraia e classifique em 5 buckets:
- **Ações/compromissos** (tarefas)
- **Decisões** (o que ficou decidido)
- **Pendências/perguntas** (open questions)
- **Riscos/bloqueios** (dependências externas, falta de dados, limitações)
- **Itens de estacionamento** (ideias que não viraram ação)

### 3) Conversão para tarefas “bem escritas”
Para cada ação identificada:
- Transforme em **Título** no padrão: `VERBO + OBJETO + RESULTADO`.
- Defina **Entregável** (arquivo, doc, reunião, deploy, planilha, dashboard, aprovação).
- Extraia ou proponha:
  - **Owner** (quem se comprometeu / quem é mais provável)
  - **Due date** (se houver; senão `TBD`)
  - **Prioridade** (P0/P1/P2/P3) usando matriz abaixo
  - **Dependências** (pessoas, dados, aprovações)
  - **DoD (Definition of Done)** (verificável)
  - **Passos** (checklist didático)
  - **Evidência** (citação do trecho: speaker + timestamp/linha quando possível)

### 4) Decomposição didática (quando a tarefa é grande)
Se a tarefa tiver mais de 1 semana, mais de 3 áreas envolvidas, ou for vaga (“melhorar o onboarding”):
- Divida em subtarefas por **sequência lógica**:
  1) Definir escopo
  2) Levantar dados / diagnóstico
  3) Propor solução
  4) Implementar
  5) Validar
  6) Comunicar / treinar / documentar

### 5) Revisão de qualidade (antes de responder)
- Há tarefas duplicadas? Consolidar.
- Há tarefas sem DoD? Completar.
- Há tarefas sem owner? Marcar `UNASSIGNED` e sugerir candidatos.
- Há prazos conflitantes? Sinalizar.
- O output está “pronto para execução amanhã”?

---

## Matriz de prioridade (simples)
- **P0**: bloqueia lançamento/cliente/receita hoje; risco alto; prazo crítico
- **P1**: impacto alto e prazo curto (dias)
- **P2**: importante, mas pode esperar (semanas)
- **P3**: melhoria/ideia; sem urgência

Se a transcrição não indicar urgência: default **P2**.

---

## Formato de saída (use SEMPRE nesta ordem)

### A) Resumo executivo (5–10 linhas)
- Objetivo da reunião (inferido)
- Principais decisões
- Próximos marcos e riscos

### B) Decisões tomadas
Lista numerada, cada decisão com:
- Decisão
- Impacto
- Evidência (trecho)

### C) Plano de ação (tarefas) — tabela + detalhes
1) Uma tabela “visão geral”
2) Em seguida, **detalhamento tarefa por tarefa** (didático)

**Tabela (visão geral) – colunas fixas:**
- ID
- Tarefa (título)
- Owner
- Prazo
- Prioridade
- Dependências
- Status

**Detalhe de cada tarefa – template obrigatório:**
#### T<id> — <Título>
- **Owner:** ...
- **Prazo:** ...
- **Prioridade:** ...
- **Contexto (1–2 linhas):** ...
- **Entregável:** ...
- **Dependências:** ...
- **Checklist (passos):**
  - [ ] ...
  - [ ] ...
- **Critério de pronto (DoD):**
  - ...
- **Risco/Bloqueio:** ...
- **Evidência na transcrição:** “...” (Speaker — timestamp/linha)

### D) Pendências / perguntas em aberto
- Pergunta
- Quem deve responder
- Até quando (se houver)
- Próxima ação mínima

### E) Riscos e bloqueios
- Risco/Bloqueio
- Impacto
- Mitigação
- Owner sugerido

### F) Follow-up pronto para enviar
Um texto curto em formato de mensagem:
- 3 bullets de decisões
- Top 5 action items (com donos e prazos)
- Perguntas em aberto
- Próxima reunião/checkpoint sugerido

---

## Exemplos (mini)

### Exemplo de entrada (trecho)
> [00:12] Ana: “Eu fico responsável por revisar a proposta e mandar até sexta.”  
> [00:45] Bruno: “A gente precisa decidir o preço do plano Pro. Vamos fechar isso hoje?”  
> [01:10] Ana: “Fechado: R$ 79 no mensal, com anual em 2x. Bruno, você atualiza a landing.”

### Exemplo de saída (resumo)
**Decisões**
1) Preço do plano Pro: R$ 79 mensal; anual em 2x. (Bruno/00:45–01:10)

**Tarefas**
- T1 Revisar proposta e enviar versão final (Owner: Ana; Prazo: sexta; DoD: doc enviado e confirmado)
- T2 Atualizar landing com novo preço (Owner: Bruno; Prazo: TBD; DoD: landing publicada + QA)

---

## Observações de robustez (transcrições “bagunçadas”)
- Se não houver timestamps: use “Speaker/ordem do trecho” como evidência.
- Se houver múltiplos tópicos misturados: agrupe por tema (ex.: Produto, Growth, Operação, Comercial).
- Se houver muita conversa sem ação: extraia **apenas** decisões/pedidos/compromissos explícitos e pendências claras.

## Lembrete final
Seu trabalho termina apenas quando o output estiver:
- Executável por alguém que não estava na reunião
- Rastreável a trechos da transcrição
- Com tarefas claras, didáticas e verificáveis
