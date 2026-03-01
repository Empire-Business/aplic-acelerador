---
name: "whatsapp-conversion-copy"
version: "1.0.0"
language: "pt-BR"
type: "claude-code-skill"
description: >
  Skill para gerar copies profissionais para WhatsApp (mensagens e fluxos) com foco em resposta + conversão,
  variações A/B, CTAs em formato de pergunta, follow-ups e tom de voz alinhado à persona/marca.
inputs:
  required:
    - persona
    - oferta
    - publico
    - objetivo_conversa
    - origem_lead
  optional:
    - provas
    - objecoes
    - restricoes
    - tom_voz
outputs:
  - "3 variações de mensagem (A/B/C) em versão curta e média"
  - "2 follow-ups (24h e 72h)"
  - "CTAs em formato pergunta (microcompromisso)"
  - "checklist de conformidade"
  - "racional da copy + sugestão de teste A/B"
---

# Skill: Copy de WhatsApp de Alta Conversão (estilo *conversion copy* orientado a clareza, evidência e testes)

> **Nota importante (limite de estilo):** este skill **não tenta imitar exatamente** o estilo de uma pessoa específica. Em vez disso, ele aplica **princípios universais de conversion copywriting** (clareza, especificidade, prova, redução de fricção, linguagem de cliente, hipóteses e testes) que funcionam muito bem em WhatsApp.

---

## Objetivo do skill

Gerar **copies profissionais para WhatsApp** (mensagens e fluxos) com:
- tom de voz alinhado à **persona/marca** do usuário,
- foco em **resposta + conversão** (agendar, fechar, pagar, confirmar, comparecer),
- mensagens **curtas, humanas e acionáveis**,
- variações para **teste A/B**,
- estrutura que reduz objeções e aumenta **taxa de resposta**.

---

## Quando usar

- Captação e qualificação de leads (inbound e outbound com opt-in)
- Reativação de leads e clientes
- Follow-up pós-orçamento/proposta
- Confirmação de agendamento e redução de no-show
- Carrinho/checkout abandonado (quando aplicável)
- Nutrição curta (sequência de 3–7 dias)
- Pós-venda (review, upsell, renovação)

---

## Regras de ouro (WhatsApp)

1. **Respeite opt-in e contexto**
   Só envie primeira mensagem se houver consentimento/contato legítimo (lead pediu, clicou, preencheu, indicou, já é cliente etc.).

2. **Uma ideia por mensagem**
   WhatsApp é conversa. Se precisa explicar muito, quebre em partes.

3. **Pergunta > palestra**
   Mensagem que convida resposta converte mais do que textão.

4. **Fricção baixa**
   CTA simples: "posso te mandar?", "prefere A ou B?", "qual horário funciona?"

5. **Prova e especificidade**
   Use números e detalhes reais quando existirem. Sem promessas vagas.

6. **Sem hype/pressão desnecessária**
   Conversão sustentável = confiança. Pressão só quando faz sentido (prazo real, vagas reais).

---

## Inputs obrigatórios (briefing)

> **Antes de escrever copy, peça/valide estas informações.**
> Se o usuário não fornecer, faça suposições mínimas e peça *em 1 pergunta* o que faltou.

### 1) Persona & tom de voz
- Marca/empresa:
- Público-alvo (quem é a pessoa do outro lado?):
- Nível de consciência (não sabe que tem problema / sabe do problema / compara soluções / pronto pra comprar):
- Tom desejado (3–5 adjetivos): ex. direto, humano, confiante, simples, bem-humorado, premium…
- Coisas que **NÃO** posso usar: ex. emojis demais, gírias, palavrões, termos técnicos, promessas…

### 2) Oferta & contexto
- Produto/serviço e entrega (o que exatamente é):
- Ticket (R$) e condições:
- Principal transformação/benefício:
- Diferencial (o que torna você melhor/diferente):
- Provas (cases, números, depoimentos, tempo de mercado):
- Riscos/objeções típicas:
- Objetivo desta conversa (agendar call, fechar, pagamento, etc.):
- Canal de origem do lead (anúncio, indicação, site, evento, frio, etc.):

### 3) Restrições operacionais
- Horários para atendimento:
- Tempo médio de resposta:
- Link/forma de agendamento:
- Política de reembolso/garantia (se houver):
- Limites (vagas, datas, região, perfil mínimo):

---

## Output padrão (o que entregar)

Sempre entregue:

1) **3 variações** da mensagem (A/B/C)
   - A: mais direta
   - B: mais calorosa
   - C: mais curiosidade/diagnóstico

2) **Versões curta e média**
   - Curta: 1–2 linhas
   - Média: 4–7 linhas (com quebras)

3) **CTA em formato pergunta** (microcompromisso)
   Ex.: "Faz sentido pra você?", "Quer que eu te mostre como seria no seu caso?", "Prefere amanhã ou quinta?"

4) **2 follow-ups** (24h e 72h) sem soar desesperado.

5) **Checklist de conformidade**
   - opt-in?
   - contexto citado?
   - fricção baixa?
   - uma ação clara?
   - tom consistente?

---

## Playbook de estrutura (mensagem única)

Use esta fórmula (WhatsApp-friendly):

1) **Contexto + permissão**
   - "Oi, {Nome}! Vi que você {origem/ação}. Posso te fazer 2 perguntas rápidas pra entender se faz sentido?"

2) **Diagnóstico curto**
   - Pergunta 1 (situação atual)
   - Pergunta 2 (objetivo/urgência)

3) **Microvalor (1 insight)**
   - "Pelo que você descreveu, normalmente o que trava é {X}. Dá pra resolver com {Y} sem {dor}."

4) **Prova / credencial sem ego**
   - "A gente tem ajudado {perfil} a {resultado} em {prazo} usando {método}."

5) **CTA simples**
   - "Quer que eu te mande um exemplo aplicado ao seu caso?"
   - ou "Prefere {opção A} ou {opção B} pra eu te orientar?"

---

## Biblioteca de aberturas (escolha 1)

### Abertura direta
- "Oi, {Nome}! Aqui é {SeuNome} da {Marca}. Vi seu contato por {origem}. Ainda faz sentido falar sobre {assunto}?"

### Abertura com permissão (anti-spam)
- "Oi, {Nome}! Posso ser bem rápido? É sobre {assunto} — vi que você {ação/origem}."

### Abertura com contexto forte
- "Oi, {Nome}! Você pediu {material/orçamento} sobre {tema}. Pra eu não te mandar coisa genérica: qual é sua meta com {tema} hoje?"

### Abertura reativação elegante
- "Oi, {Nome}! Passando rápido: você ainda está com {objetivo} ou já resolveu isso?"

---

## CTAs que convertem (microcompromissos)

- "Posso te fazer 2 perguntas e já te dizer se consigo te ajudar?"
- "Você prefere resolver isso mais rápido (com ajuda) ou ir ajustando aos poucos?"
- "Se eu te mandar um exemplo aplicado ao seu caso, você me diz se faz sentido?"
- "Quer que eu te mostre as 2 rotas possíveis e você escolhe?"
- "Qual cenário te descreve melhor: A) ___ ou B) ___?"
- "O que é mais importante agora: {tempo}, {preço} ou {resultado}?"

---

## Templates prontos por situação

### 1) Primeiro contato (lead inbound)
**Estrutura:** contexto + pergunta + próximo passo

**Template**
- "Oi, {Nome}! Vi que você {origem}. Pra eu te ajudar direito: hoje você está tentando {objetivo} ou ainda está no começo?"
- "Se você me disser {1 variável-chave}, eu já te digo se {solução} faz sentido e qual seria o próximo passo."

**Follow-up 24h**
- "{Nome}, só pra eu não te deixar no vácuo: você quer que eu te mande um caminho rápido pra {objetivo} ou prefere que eu não te incomode?"

**Follow-up 72h**
- "Fechando por aqui 🙂 Se {objetivo} voltar a ser prioridade, me chama com a palavra 'VOLTEI' que eu te mando as opções."

---

### 2) Primeiro contato (outbound com opt-in/indicação)
**Estrutura:** referência + permissão + diagnóstico

**Template**
- "Oi, {Nome}! {Pessoa/Origem} comentou que você está com {dor}. Posso te fazer 1 pergunta pra ver se consigo te apontar um caminho?"
- "Hoje o que mais pesa pra você: {objeção 1} ou {objeção 2}?"

**Follow-up 24h**
- "Se não for prioridade agora, tudo bem. Quer que eu te mande um checklist rápido pra quando você retomar?"

---

### 3) Qualificação (descobrir fit sem interrogatório)
**Estrutura:** pergunta binária + pergunta aberta + confirmação

**Template**
- "Pra eu te orientar sem adivinhar: você está em {estágio A} ou {estágio B}?"
- "E o que te fez buscar isso agora?"
- "Perfeito. Se eu entendi: você quer {objetivo}, mas está travando em {dor}. Acertei?"

---

### 4) Envio de proposta/orçamento
**Estrutura:** alinhar valor + reduzir risco + próximo passo claro

**Template**
- "{Nome}, te enviei a proposta. Antes de você olhar: o ponto principal aqui é {benefício específico} e o que garante isso é {diferencial}."
- "Se fizer sentido, você prefere que eu te ajude a escolher a melhor opção (2 min aqui) ou você quer olhar sozinho e me dizer dúvidas?"

**Follow-up 24h**
- "Conseguiu ver? A dúvida mais comum nessa etapa é {objeção}. Quer que eu explique como isso funciona na prática?"

**Follow-up 72h**
- "Último toque, {Nome}: você quer seguir com isso agora ou prefere pausar e retomar mais pra frente?"

---

### 5) Objeção "tá caro"
**Estrutura:** validar + reancorar valor + oferecer rota menor

**Template**
- "Totalmente justo, {Nome}. Posso entender rápido: é caro comparado a quê — ao que você imaginava ou a outra opção?"
- "Se o objetivo é {resultado}, o custo maior normalmente vem de {custo invisível do problema}."
- "Se você quiser, eu te mostro 2 caminhos: um mais enxuto (menos investimento) e um mais completo. Qual faz mais sentido?"

---

### 6) Objeção "vou pensar"
**Estrutura:** tirar ambiguidade + microdecisão

**Template**
- "Claro. Só pra eu te ajudar do jeito certo: você vai pensar sobre {1} o investimento, {2} se é o momento, ou {3} se confia que funciona pra você?"
- "Dependendo do que for, eu te respondo em 30 segundos e você decide com mais clareza."

---

### 7) Agendamento (converter sem link jogado)
**Estrutura:** oferecer 2 horários + alternativa

**Template**
- "Bora fazer assim: tenho {dia} às {hora} ou {dia} às {hora}. Qual é melhor?"
- "Se preferir, me diga sua disponibilidade (manhã/tarde/noite) e eu encaixo aqui."

**Confirmação anti-no-show**
- "Fechado: {dia} {hora}. Pra eu reservar certinho: seu objetivo principal é {X}, certo?"
- "Se acontecer algo, me avisa por aqui que eu remanejo sem problema."

---

### 8) Pós-venda (review e upsell sem ser chato)
**Template review**
- "{Nome}, como foi {resultado/experiência} até aqui — de 0 a 10?"
- "Se você topar, 1 frase sua já ajuda muito: o que mudou depois de {solução}?"

**Template upsell**
- "Pelo que você comentou, o próximo passo natural seria {upsell}. Quer que eu te explique em 2 linhas como funciona?"

---

## Sequências prontas (3 dias)

> Use quando o lead sumiu, mas houve conversa inicial.

### Dia 1 — reabrir com contexto
- "{Nome}, fiquei pensando no que você disse sobre {dor}. Se eu te mandar 2 opções de caminho (rápido x completo), você me diz qual combina mais?"

### Dia 2 — microvalor
- "Um detalhe que costuma destravar: {insight prático}. Isso vale principalmente quando {condição}. Quer que eu aplique isso ao seu caso?"

### Dia 3 — saída elegante
- "Pra eu organizar aqui: você quer tocar isso agora, quer pausar, ou já resolveu por outro caminho?"

---

## Tom de voz: como calibrar automaticamente

Quando o usuário não fornece tom, use padrão:
- **humano, direto, respeitoso, confiante**, sem exagero
- 0–2 emojis por mensagem (máximo), só se combinar com o público
- sem termos "marketeiros" (ex.: "imperdível", "revolucionário") a menos que a persona seja agressiva

### Dicionário rápido (ajuste por persona)
- Persona premium: menos emojis, mais precisão, mais "processo"
- Persona jovem/descontraída: frases curtas, humor leve, mais energia
- B2B técnico: contexto, métricas, clareza de escopo, menos "marketingês"
- Saúde/jurídico/finanças: evite promessas; use orientações e limites

---

## Prova e credibilidade (sem parecer arrogante)

Use um destes formatos:
- "Temos ajudado {perfil} a {resultado} com {método}."
- "O padrão que a gente vê é: {padrão} → {solução}."
- "Nos últimos {período}, atendemos {n} casos parecidos com o seu."
- "Se fizer sentido, eu te mando 1 exemplo real (sem dados sensíveis)."

**Nunca invente números, cases ou depoimentos.**
Se não houver prova, use: "posso te explicar o processo e te dizer o que esperar".

---

## Checklist final (antes de entregar a copy)

- [ ] Tem **contexto** (de onde veio o contato)?
- [ ] Tem **permissão** ou mensagem respeitosa?
- [ ] É **curta** e com quebras de linha?
- [ ] Tem **1 CTA** claro em forma de pergunta?
- [ ] Não promete "garantia de resultado" se isso não for real.
- [ ] Não usa gatilhos falsos (urgência/vagas) sem ser verdade.
- [ ] Evita texto grande; se precisar, vira sequência.
- [ ] Inclui follow-ups que preservam dignidade.

---

## Como você (Claude Code) deve operar (passo a passo)

1) **Coletar briefing mínimo**
   Se faltar algo crítico (oferta/objetivo/público), faça 1 pergunta curta.
2) **Definir hipótese de conversão**
   Ex.: "Aumentar resposta com pergunta binária + prova curta."
3) **Gerar 3 variações (A/B/C)**
   Direta / calorosa / curiosidade-diagnóstico
4) **Gerar versão curta e média de cada**
5) **Adicionar 2 follow-ups**
6) **Explicar em 3 bullets o racional** (sem aula; só justificativa prática)
7) **Sugerir o que medir** (resposta, agendamento, conversão) e 1 ideia de teste

---

## Métricas e testes (para "resultado financeiro" sem chute)

Sugira sempre:
- **Taxa de resposta** (respondidos / enviados)
- **Taxa de avanço** (resposta → agendamento/proposta)
- **Taxa de fechamento** (agendamentos → vendas)
- **Tempo até resposta**

Testes A/B possíveis:
- Pergunta binária vs pergunta aberta
- Prova antes do CTA vs depois do CTA
- CTA "posso te mandar?" vs CTA "prefere A ou B?"
- Mensagem 1 linha vs 5 linhas

---

## Formato de entrega (padrão)

**Contexto assumido:** {resumo do briefing em 2 linhas}

### Mensagem 1 (A/B/C)
**A — Direta (curta):**
{mensagem}

**A — Direta (média):**
{mensagem}

**B — Calorosa (curta):**
{mensagem}

**B — Calorosa (média):**
{mensagem}

**C — Diagnóstico/curiosidade (curta):**
{mensagem}

**C — Diagnóstico/curiosidade (média):**
{mensagem}

### Follow-ups
**Follow-up 24h (leve):**
{mensagem}

**Follow-up 72h (saída elegante):**
{mensagem}

### Racional (3 bullets)
- {por que essa abertura}
- {por que esse CTA}
- {por que essa prova/estrutura}

### O que medir + 1 teste recomendado
- Medir: {métrica}
- Teste: {hipótese}

---

## Prompt pronto (para usar com este skill)

> Cole e preencha:

**Persona/tom:** {3–5 adjetivos} | **evitar:** {lista}
**Oferta:** {o que é} | **ticket:** {R$} | **diferencial:** {1–3 itens}
**Público:** {perfil} | **dor principal:** {dor} | **desejo:** {resultado}
**Provas:** {cases/números/depoimentos}
**Objetivo da conversa:** {agendar/fechar/pagar/confirmar}
**Origem do lead:** {anúncio/indicação/site/etc.}
**Objeções comuns:** {lista}
**Restrições:** {horários, vagas, etc.}

**Tarefa:** Escreva a primeira mensagem + 2 follow-ups e 3 variações (A/B/C), em versão curta e média.

---

## Exemplos de microajustes (edição profissional)

- Trocar "gostaria de" → "quer" (mais direto)
- Trocar "vamos marcar uma call" → "posso te ligar 10 min?" (mais específico)
- Trocar "aumentar suas vendas" → "aumentar agendamentos na semana" (mais concreto)
- Trocar "tenho uma solução" → "posso te mostrar 2 caminhos" (menos vendedor)

---

## Guardrails (segurança e reputação)

- Não criar mensagens que incentivem spam, assédio ou contato sem consentimento.
- Evitar promessas absolutas (ex.: "garantido", "100%", "vai funcionar").
- Para nichos sensíveis (saúde, finanças, jurídico): usar linguagem de orientação e limites.
- Sempre respeitar pedido de parar contato: "Sem problemas — paro por aqui."

---

## Fim do skill
