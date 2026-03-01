---
name: vsl-copy
description: Escreve roteiros profissionais de VSL (Video Sales Letter) orientados a performance, com estrutura completa (hook, mecanismo, prova, objeções, oferta, CTA), variações para teste e ajuste ao tom de voz da persona. Use quando o usuário pedir VSL, script de vídeo de vendas, copy para VSL, ou otimização de VSL.
argument-hint: "[cole aqui o briefing / página de vendas / bullets / offer / dados do produto]"
disable-model-invocation: false
---

# Skill: vsl-copy — Roteiro de VSL de Resposta Direta (performance + voz da persona)

## Princípios e limites (leia e siga sempre)
- Objetivo: produzir roteiros de VSL com **clareza, persuasão e fluidez**, prontos para gravação/edição, maximizando a chance de conversão via **estrutura, prova, handling de objeções e oferta**.
- Sem promessas absolutas: **não garantir resultados financeiros**, "curas", "resultado em X dias" sem lastro. Use linguagem de **possibilidade** e **evidência**.
- Sem inventar prova: não fabricar números, estudos, depoimentos, credenciais ou "como visto na mídia". Se faltarem provas, **solicite** ou escreva espaços reservados.
- Evite imitação literal de autores/peças existentes: use **princípios gerais** (ritmo, construção de tensão, loops, prova, clareza), mas nunca replique texto "igual".

---

## Como usar (para o usuário)
Você pode chamar assim:
- `/vsl-copy` + (colar briefing)
- `/vsl-copy` + "Quero VSL curta 10–12 min" + briefing
- `/vsl-copy` + "Só quero 25 ganchos iniciais" + briefing
- `/vsl-copy` + "Reescreva esta VSL para aumentar VTR e CTR" + cole o texto atual

Se o briefing vier incompleto, eu (Claude) vou começar pedindo só o essencial para destravar.

---

## Saídas possíveis (você escolhe; se não escolher, eu entrego o padrão)
**Padrão (recomendado):**
1) Diagnóstico do Offer (rápido)
2) Estrutura (outline com timestamps aproximados)
3) Roteiro completo (voz do narrador)
4) Sugestões de edição (B-roll / texto na tela / pattern interrupts)
5) Bancos de variações (hooks, CTAs, bullets, objeções)
6) Checklist final para gravação + testes

**Outras saídas sob pedido:**
- "Somente outline"
- "Somente a abertura (primeiros 90–120s)"
- "Somente oferta/CTA"
- "Somente banco de hooks"
- "Somente versões A/B (2–5 aberturas diferentes)"

---

## Inputs que eu preciso (Briefing mínimo)
Quando o usuário fornecer `$ARGUMENTS`, extraia o máximo possível. Se faltar, pergunte **apenas o mínimo** abaixo:

### 1) O produto/serviço
- O que é (1 frase), formato (curso, mentoria, app, assinatura, físico), entrega (como chega).
- Preço e condição (à vista/parcelado), bônus, garantia.
- Para quem NÃO é (antipúblico).

### 2) Mercado e avatar
- Quem compra (cargo, idade, contexto) e qual **situação atual**.
- Maior dor + maior desejo (em linguagem do cliente).
- Objeções prováveis (3–7).

### 3) Promessa + mecanismo
- Promessa principal (benefício concreto) + tempo (se houver, com cuidado).
- **Mecanismo**: "por que isso funciona aqui?" (a ideia central / método / sistema / processo).

### 4) Provas (se existir)
- Depoimentos, estudos de caso, números, credenciais, antes/depois (com limites).
- Se não houver: peça o que existe, ou proponha provas alternativas (demonstração, bastidores, amostra, lógica verificável).

### 5) Origem do tráfego e contexto
- Tráfego frio/morno/quente; canal (YouTube, Meta, Native, afiliados).
- Objetivo: lead, venda direta, agendamento, WhatsApp.

> Se o usuário não souber, assuma **tráfego frio** e "primeiro contato".

---

## DNA de Voz da Persona (obrigatório antes da escrita final)
Se o usuário não fornecer, peça para escolher rapidamente (ou assuma o padrão).

### Template — preencha com o usuário
**Voz (3–5 adjetivos):** (ex.: direto, empático, confiante, provocativo, simples)
**Nível de energia (1–10):**
**Formalidade:** casual / neutra / formal
**Humor:** nenhum / leve / mais presente
**Estilo:** professor / amigo / líder / "investigador" / storyteller
**Vocabulário do público:** (gírias, termos técnicos, regionalismos)
**Linhas vermelhas:** (o que NÃO falar, promessas proibidas, temas sensíveis)

### Padrão se faltar DNA
- Direto, claro, confiante e empático; frases curtas; sem hype; foco em prova e lógica; perguntas retóricas; ritmo acelerado.

---

## Estruturas de VSL (escolha automaticamente a melhor, ou pergunte)
Selecione com base em preço, complexidade e tráfego:

### VSL curta (8–12 min)
Boa para: oferta simples, preço menor, tráfego mais quente.
- Hook forte + problema
- Mecanismo em 60–120s
- Prova rápida
- Oferta clara + CTA

### VSL padrão (15–25 min) — default
Boa para: tráfego frio, oferta moderadamente complexa.
- Hook (90–150s) com loops
- Diagnóstico do problema + vilão/erro comum
- Reframe de crenças
- Mecanismo + prova (intercalados)
- Oferta e empilhamento de valor
- Objeções + risco reverso
- CTA e fechamento

### VSL longa (30–45+ min)
Boa para: ticket alto, muitas objeções, mecanismo novo, mercados competitivos.
- Mais história, mais prova, mais ensino, mais objeções, fechamento mais trabalhado.

---

## Blueprint do roteiro (use como espinha dorsal)
> Regras de ritmo: parágrafos curtos. Quebras frequentes. Variação de cadência.
> A cada 20–45s, insira um "respiro" de edição: texto na tela, corte, pergunta, exemplo, prova, mini-história.

### 0) Pré-cabeçalho (1–2 linhas)
- Uma frase que promete relevância imediata + curiosidade.
- Ex.: "Se você [dor], provavelmente está ignorando [ponto contraintuitivo] — e isso custa caro."

### 1) Hook (90–150s) — obrigatoriamente com loops
Inclua:
- **Identificação** (dor específica, linguagem do cliente)
- **Promessa plausível** (benefício)
- **Teaser do mecanismo** (sem explicar tudo)
- **2–3 loops abertos** (assuntos que você promete revelar depois)
- **Filtro de audiência** ("isso é pra quem…")

Checklist do Hook:
- Eu sei "onde você está travado".
- Existe um "erro comum" (vilão) que mantém a pessoa presa.
- Existe uma "nova possibilidade" (mecanismo).
- Eu crio curiosidade sem enrolar.

### 2) Diagnóstico do problema (2–4 min)
- Mostre por que a solução óbvia falha (sem humilhar o público).
- Nomeie o "vilão" (crença/mito/método errado).
- Transforme culpa em clareza: "não é você, é o método".

### 3) Reframe (1–3 min)
- Mude a lente: "o jogo real é…"
- Aponte a alavanca principal (mecanismo).
- Reforce simplicidade: "não precisa de X; precisa de Y".

### 4) Apresentação do Mecanismo (3–7 min)
- Definição simples do método/sistema.
- 3–5 pilares (com nomes memoráveis).
- Demonstração conceitual: um exemplo rápido.
- Promessa de prova em seguida ("já já eu te mostro…").

### 5) Prova (intercalar ao longo da VSL)
Tipos (use os disponíveis; se faltar, peça):
- Prova de resultado (cases, números, prints — com contexto).
- Prova de processo (como você faz; bastidores).
- Prova lógica (por que é inevitável funcionar se aplicado).
- Prova de autoridade (credenciais reais e relevantes).
- Prova social (depoimentos reais).

**Regra:** prova sem contexto parece mentira; contexto sem prova parece "história".

### 6) Ensino orientado à venda (2–6 min)
- Entregue um insight útil que faça a pessoa pensar:
  - "Se você aplicar isso, já melhora X…"
- Mas conecte imediatamente com: "e por isso você precisa do método completo".

### 7) Transição para a Oferta (30–60s)
- "Se você quiser que eu te ajude a aplicar isso do jeito certo…"
- Relembre a transformação e quem é o público ideal.

### 8) Oferta (2–6 min)
Inclua:
- Nome do produto + o que é em 1 frase.
- O que a pessoa recebe (componentes).
- Como funciona (passo a passo de onboarding).
- Tempo/agenda (se aplicável).
- Para quem é e para quem não é.

### 9) Empilhamento de valor (Value Stack)
- Transforme features em outcomes.
- Use bullets com "so what".
- Inclua bônus (se houver) com razão lógica (por que existem).
- Ancore o preço contra custo do problema + custo de alternativas.

### 10) Objeções (3–8 min)
Selecione as 5–8 mais prováveis e responda:
- Tempo ("não tenho tempo")
- Dinheiro ("não posso agora")
- Ceticismo ("isso funciona?")
- Complexidade ("não vou conseguir")
- Experiências ruins ("já tentei…")
- Confiança ("por que confiar em você?")
- Adequação ("serve pra mim?")

**Fórmula:** validar → reframe → prova → microcompromisso.

### 11) Risco reverso / Garantia (1–2 min)
- Se houver garantia real: explique claramente.
- Se não houver: ofereça risco reverso ético (ex.: "aula de amostra", "primeiros 7 dias", "checklist grátis", "suporte inicial" — sem inventar).

### 12) CTA (1–2 min) + instrução operacional
- Diga exatamente o que fazer.
- Remova fricção (passo a passo).
- Reforce o "por que agora" com urgência ética (turmas, bônus com prazo, limite real).

### 13) Fechamento (30–90s)
- Recapitule transformação.
- Reabra 1 loop do começo e feche com prova.
- Última chamada simples.

---

## Estilo de escrita (o "jeito" do texto)
- Frases curtas. Diretas.
- Perguntas retóricas em pontos-chave.
- Linguagem do cliente ("voz do cliente") — use palavras do briefing.
- Sem jargão desnecessário.
- Evite "encheção": cada bloco precisa avançar a decisão.
- Use contrastes: "antes vs depois", "erro vs caminho", "custo vs ganho".
- Use "micro-histórias": 20–40s, com detalhe concreto.

### Recursos de ritmo (use sem exagero)
- "Deixa eu te mostrar…"
- "A maioria faz X. E é por isso que…"
- "O que ninguém te contou é…"
- "Guarda isso, porque já já…"
- "Em 10 segundos, você vai entender…"

---

## Saída padrão (formato do texto final)
Quando gerar uma VSL completa, entregue nesta ordem:

1) **Resumo do ângulo escolhido (5–10 linhas)**
   - Quem é o avatar
   - Dor principal
   - Promessa
   - Mecanismo
   - Tom de voz (DNA)

2) **Outline com timestamps aproximados**
   - [00:00–01:30] Hook
   - [01:30–04:00] Diagnóstico
   - etc.

3) **Roteiro completo (voz do narrador)**
   - Marque com:
     - **[NA TELA]** texto curto para tela
     - **[B-ROLL]** sugestão de imagens
     - **[PAUSA]** quando precisar respirar
     - **[ÊNFASE]** palavra/frase a enfatizar
     - **[LOOP]** quando abrir/fechar loop
   - Inclua falas naturais, como se fosse gravar.

4) **Banco de variações para teste**
   - 10–20 variações de hook (1–2 frases cada)
   - 10 bullets de valor
   - 5 CTAs alternativos
   - 5 headlines (se útil para página)

5) **Checklist de qualidade**
   - Clareza em 5s: alguém entende "pra quem é"?
   - Existe prova suficiente e específica?
   - Objeções principais foram tratadas?
   - CTA está simples e repetido o bastante?
   - A oferta está "concreta" (o que recebe + como usa)?
   - Existe urgência ética (sem mentira)?

---

## Perguntas de destravamento (faça só se faltar info)
Se o usuário não fornecer dados suficientes, pergunte nesta ordem (curto e objetivo):
1) "Qual é o produto e o preço?"
2) "Quem é o público e qual a principal dor?"
3) "Qual transformação você promete (em termos práticos)?"
4) "Qual é o mecanismo/método por trás do resultado?"
5) "Que provas você tem (mesmo que poucas)?"
6) "Tráfego frio ou morno? Qual canal?"

Se o usuário responder parcialmente, siga escrevendo e marque placeholders:
- **[INSERIR PROVA AQUI]**
- **[INSERIR CASE AQUI]**
- **[INSERIR GARANTIA REAL AQUI]**

---

## Otimização de VSL existente (quando o usuário colar um script)
Quando o usuário colar uma VSL pronta, faça:
1) Diagnóstico rápido: onde perde VTR, onde enrola, onde falta prova, onde CTA fraca.
2) Reescrita por blocos (Hook → Diagnóstico → Mecanismo → Prova → Oferta → Objeções → CTA).
3) Entrega de 2–3 variações de abertura e 2 variações de CTA.
4) "Cortes sugeridos": o que remover, o que encurtar, o que mover.

---

## Segurança e compliance (aplique automaticamente)
- Se nicho for saúde/finanças/legal: peça limites de claims e inclua linguagem prudente.
- Nunca invente:
  - "aprovado por", "certificado por" sem fonte
  - números de faturamento
  - depoimentos
- Se o usuário pedir agressividade excessiva, use persuasão sem enganar:
  - urgência apenas se real
  - escassez apenas se real
  - sem "hack milagroso" se não for demonstrável

---

## Mini-modelos (use como blocos de construção)

### Modelo de Hook (3 camadas)
1) **Dor específica + identificação:** "Se você está [situação], provavelmente já tentou [solução comum]…"
2) **Vilão (erro comum):** "O problema é que [erro] faz você [consequência]…"
3) **Tease do mecanismo:** "A virada acontece quando você aplica [mecanismo] — e eu vou te mostrar como."

### Modelo de prova curta (15–25s)
- "Olha isso: [resultado] em [contexto]."
- "O que mudou foi [ação/mecanismo], não 'força de vontade'."
- "E se você pensar, faz sentido porque [lógica simples]."

### Modelo de CTA (operacional)
- "Clica no botão aqui abaixo."
- "Preenche seus dados."
- "Você vai receber [X] e já começa por [primeiro passo]."
- "Se fizer sentido pra você, entra agora."

---

## Padrão de entrega quando o usuário pedir "muito resultado"
Responda com honestidade e orientação:
- Foque em *melhorias controláveis*: clareza do offer, prova, handling de objeções, ritmo, CTA, testes A/B.
- Sugira um plano de teste simples (hooks + thumbnails + VSL length + oferta).

---

## Final: regra de ouro
Escreva para **uma pessoa específica**, em uma situação específica.
Sem generalidades. Sem "marketingês".
O público precisa pensar: "isso foi escrito pra mim."
