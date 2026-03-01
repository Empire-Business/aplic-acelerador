---
name: "sales-page-copy-longform"
version: "1.0.0"
language: "pt-BR"
type: "claude-code-skill"
description: >
  Skill para criar copy profissional de página de vendas em estilo clássico de direct response
  (long-form, com ritmo, curiosidade, prova e persuasão ética), inspirado em lendas do DR
  como Clayton Makepeace — sem copiar textos existentes.
inputs:
  required:
    - persona
    - oferta
    - mecanismo_unico
    - prova
    - precos_e_planos
    - objecoes
outputs:
  - "página de vendas completa (estrutura longa)"
  - "variações de headline e leads"
  - "bullets de curiosidade e prova"
  - "seções de prova, garantia, stack e FAQ"
---

# Skill: Copy de Página de Vendas (Long-form Direct Response) — Estilo Clássico de DR (inspirado em Clayton Makepeace)

> **Objetivo:** gerar uma **página de vendas longa, persuasiva e bem estruturada**, com voz alinhada à sua persona e foco em conversão (sem promessas falsas).
>
> **Importante (ética e compliance):**
> - Não invente resultados, estudos, depoimentos ou números.
> - Não prometa cura, renda garantida ou “resultado certo”.
> - Sempre diferencie **possibilidade** de **garantia** e inclua **disclaimers** quando necessário (saúde/finanças).
> - Esta skill maximiza qualidade persuasiva e clareza — **não garante** resultado financeiro.

---

## Quando usar

Use esta skill quando você precisar:
- Criar **sales page** completa (produto digital, serviço, mentoria, curso, assinatura, evento).
- Reescrever/otimizar uma página existente com foco em **CR, AOV, LTV**.
- Criar versões para testes A/B de headline, lead, bullets, CTAs e oferta.

---

## Resultado esperado (o que você vai receber)

1. **Blueprint** (mapa da página + “big idea” + promessa central + ângulos)
2. **Página completa** (long-form) pronta para publicar
3. **Assets extras**: 10 headlines, 2 leads alternativos, 30 bullets, 10 CTAs, FAQ + Objeções
4. **Checklist de conversão** e oportunidades de teste

---

## Como esta skill “pensa” (princípios do Direct Response long-form)

A página precisa manter o leitor em movimento com:
- **Curiosidade + especificidade** (sem “blá blá blá”)
- **Mecanismo único** (a explicação do “por que isso funciona”)
- **Prova** (credibilidade antes de pedir compra)
- **Empatia** (mostrar que você entende o mundo do prospect)
- **Risco reverso** (garantia, prova, transparência, clareza de entrega)
- **Oferta irresistível** (stack, bônus, escassez real, urgência real)
- **Objeções destruídas** (tempo, dinheiro, confiança, complexidade, “já tentei”)

---

# 1) Intake Obrigatório (preencha antes de gerar a copy)

> **Regra:** se algum campo estiver vazio, a skill deve **assumir** com base no que foi dado e marcar com `[[ASSUMIDO]]` para você validar depois.

## 1.1 Produto/Oferta
- Nome do produto:
- Tipo: (curso/mentoria/consultoria/software/serviço/outro)
- Formato de entrega:
- Duração/cronograma:
- O que o cliente recebe (entregáveis):
- Preço(s) e plano(s):
- Garantia (se houver):
- Prazo de implementação (tempo típico até ver resultado):
- Para quem **não** é:

## 1.2 Persona (o coração da página)
- Quem é (cargo/rotina/contexto):
- Nível (iniciante/intermediário/avançado):
- Desejo principal (transformação):
- Medos (o que eles evitam):
- Frustrações (o que já tentaram e falhou):
- Inimigo comum (o que “o mercado” faz errado):
- Crenças (o que eles acham que é verdade):
- Objeções (por que não comprariam):
- Linguagem (palavras que usam, gírias, termos técnicos):
- Tom de voz desejado: (ex.: direto, provocativo, acolhedor, premium, simples, técnico)

## 1.3 Mecanismo Único (o “porquê”)
- Qual é a “causa real” do problema?
- Qual é o método/estrutura que resolve?
- Por que isso é diferente do que já tentaram?
- Quais são os 3 pilares do método?
- Quais são os erros comuns que seu método evita?

## 1.4 Prova (sem isso, nada feito)
- Provas disponíveis (marque todas):
  - Estudos, dados internos, cases, depoimentos, prints, antes/depois, auditorias, números de performance.
- Detalhe de 3 melhores provas:
  - Prova 1:
  - Prova 2:
  - Prova 3:
- Autoridade:
  - Quem é você/marca?
  - Por que alguém deveria te ouvir?

## 1.5 Concorrência e Alternativas
- Alternativas que a persona usa hoje:
- O que elas fazem de errado:
- Por que elas falham para esse público:

---

# 2) Calibragem de Voz (Voice Model)

> A skill deve “travar” o tom antes de escrever qualquer linha.

## 2.1 Guia de voz (preencha)
- “Soar como”: (ex.: mentor exigente, amigo direto, especialista calmo, executiva premium)
- “Nunca soar como”: (ex.: coach vazio, hype sem prova, vendedor agressivo)
- Ritmo: (curto e socado / frases médias / mix)
- Nível de formalidade: (baixo/médio/alto)
- Emoção: (sereno/urgente/provocativo/esperançoso)
- Palavras proibidas:
- Palavras preferidas:

## 2.2 Regras de estilo (sempre)
- Escreva em **2ª pessoa** (você).
- Misture frases curtas com frases mais longas (ritmo).
- Evite “marketingês”: sinergia, disruptivo, transformação 360, etc.
- Use especificidade: números reais, prazos, etapas, nomes de frameworks.
- Sempre que fizer uma afirmação grande, sustente com:
  - um exemplo, ou
  - um raciocínio claro, ou
  - uma prova, ou
  - uma ressalva honesta.

---

# 3) Estrutura da Página (Long-form DR)

> A skill deve seguir esta ordem, mas pode ajustar conforme o produto.

## 3.1 Headline (3 níveis)
Gere:
- **Headline principal** (benefício + especificidade + “gancho”)
- **Subheadline** (mecanismo + prazo/condição + para quem)
- **Linha de qualificação** (quem deve/quem não deve continuar)

### Regras de headline
- Promessa clara (sem prometer o impossível)
- Um detalhe específico (prazo, método, “sem X”, “mesmo se Y”)
- Evite superlativos vazios (“o melhor do Brasil”) sem prova pública

---

## 3.2 Lead (abertura) — 3 opções
Crie 3 leads, com estilos diferentes:
1) **História curta** (um micro-episódio realista do prospect)
2) **Contraste/verdade incômoda** (o que ninguém fala)
3) **Mecanismo** (explicar a causa real do problema)

> O lead precisa: prender, criar identificação, elevar o custo da inação, e abrir loop de curiosidade.

---

## 3.3 Agitação do Problema (sem drama fake)
- Mostre consequências práticas.
- Mostre o “ciclo” de tentativas frustradas.
- Mostre o inimigo comum (má orientação, método errado, foco errado).

### Checklist de agitação
- [ ] A persona se reconhece em 3 frases?
- [ ] Há pelo menos 2 exemplos concretos do sofrimento?
- [ ] Você não culpou a persona — culpou o método errado?

---

## 3.4 A Virada (o “Aha”)
Aqui entra:
- “O problema não é X… é Y.”
- O **mecanismo único** (por que falha hoje e por que agora funciona)

---

## 3.5 O Mecanismo Único (explicação convincente)
Estrutura:
1) O que todo mundo tenta (e por que não funciona)
2) A causa raiz (o que realmente manda no resultado)
3) A solução (seu método)
4) Por que é mais simples do que parece (reduzir fricção)

> **Regra:** Sem jargão. Se precisar de termo técnico, explique como para alguém inteligente, mas ocupado.

---

## 3.6 Prova (em camadas)
Camada 1: credenciais e contexto  
Camada 2: casos e números (quando possível)  
Camada 3: demonstração lógica (por que faz sentido)

Inclua:
- mini-case(s)
- depoimentos (se existirem)
- prints (se existirem)
- comparações “antes/depois” **sem falsificar**

---

## 3.7 Oferta (o que exatamente você recebe)
Seção “o que vem dentro”:
- Módulos/etapas
- Entregáveis
- Acesso (prazo)
- Suporte (como funciona)
- Bônus (somente se aumentarem o “resultado”)

### Stack de valor (sem inflar)
- Nome do item
- Benefício
- Resultado que acelera
- Para quem serve
- Como usar

---

## 3.8 Preço e Ancoragem
- Ancorar com custo de alternativas (tempo, dinheiro, tentativa e erro)
- Mostrar custo da inação
- Mostrar que o investimento “compra”:
  - clareza, velocidade, redução de risco, execução guiada

---

## 3.9 Garantia (risco reverso)
Se houver garantia:
- Explique simples.
- Reforce ética e confiança.
- Remova medo de arrependimento.

Se não houver:
- Use substitutos:
  - prova forte, transparência, entrega clara, “primeiro passo rápido”, termos honestos

---

## 3.10 Objeções (derrubar uma por uma)
Objeções padrão:
- “Não tenho tempo”
- “Não tenho dinheiro”
- “Já tentei”
- “Não vai funcionar pra mim”
- “É complicado”
- “E se eu travar?”

Estratégias:
- Reenquadramento (tempo/dinheiro)
- Prova (casos)
- Especificidade (como funciona)
- Compromisso pequeno (primeiro passo simples)
- “Se você é X, isso funciona porque Y”

---

## 3.11 CTA (chamada para ação) — repetida com intenção
Tipos:
- CTA direto (comando claro)
- CTA de segurança (garantia + risco reverso)
- CTA de urgência real (prazo/limite real)
- CTA de clareza (o que acontece após clicar)

---

## 3.12 FAQ (10–15 perguntas)
- Perguntas reais, não enfeite.
- Inclua perguntas “difíceis” e responda com honestidade.

---

# 4) Gerador: Prompt Mestre (cole isso no Claude Code)

> Instrução: preencha os campos abaixo e rode o gerador.
> O modelo deve responder com **(A) Blueprint** e **(B) Página completa**.

## PROMPT MESTRE

Você é um copywriter sênior de direct response especializado em páginas longas (long-form).  
Escreva com persuasão **ética**, sem inventar prova, sem promessas garantidas.  
Estilo: clássico de DR (long-form) inspirado em lendas do DR como Clayton Makepeace — **sem copiar qualquer texto existente**.

### DADOS DO PROJETO
**Produto/Oferta:**  
{{OFERTA}}

**Persona:**  
{{PERSONA}}

**Mecanismo Único:**  
{{MECANISMO_UNICO}}

**Provas e autoridade (use somente o que está aqui):**  
{{PROVAS}}

**Preço(s) e condições:**  
{{PRECOS_E_PLANOS}}

**Garantia:**  
{{GARANTIA}}

**Objeções principais:**  
{{OBJECOES}}

**Tom de voz (obrigatório):**  
{{TOM_DE_VOZ}}

**Restrições e compliance:**  
{{RESTRICOES}}

### SAÍDA OBRIGATÓRIA
1) **Blueprint (antes de escrever a página):**
   - Big Idea (1 frase)
   - Promessa central (1 frase)
   - Mecanismo (2–5 bullets)
   - Ângulos (3 opções)
   - Avatares (quem é e quem não é)
   - Lista de provas (o que usar onde)
   - Objeções + respostas (mapa)
   - Oferta e stack (mapa)
   - CTAs (3 estilos)

2) **Página completa** com as seções:
   - Headline + subheadline + qualificação
   - Lead (escolha a melhor das 3 abordagens e inclua as outras 2 como alternativa)
   - Problema + agitação + consequências
   - Virada + mecanismo único
   - Prova em camadas
   - Apresentação do produto e como funciona
   - O que você recebe (stack)
   - Preço + ancoragem + condições
   - Garantia (ou substitutos)
   - Objeções (blocos claros)
   - CTA ao longo do texto (mín. 6)
   - FAQ (10–15)
   - Fechamento forte com urgência/escassez **somente se for real**

3) **Pacote extra no final:**
   - 10 headlines alternativas
   - 30 bullets (mix: curiosidade, prova, benefício)
   - 10 CTAs curtos
   - Checklist de testes A/B (headline, lead, prova, oferta, CTA)

### REGRAS
- Não use clichês genéricos.
- Não invente números, estudos ou depoimentos.
- Se faltar informação crítica, marque com `[[ASSUMIDO]]` e faça a melhor suposição realista.
- Escreva em pt-BR, com fluidez e ritmo.

---

# 5) Módulos Extras (para elevar conversão)

## 5.1 “Fascination Bullets” (bullets que puxam o olhar)
Crie bullets em 3 categorias:
- Curiosidade (abre loop)
- Prova (mostra que é real)
- Benefício (resultado prático)

**Modelo de bullet (use como guia, não como fórmula):**
- “Como {{PESSOA}} conseguiu {{RESULTADO}} sem {{DOR}} usando {{MECANISMO}}…”
- “O erro de {{ALTERNATIVA}} que faz você {{CONSEQUENCIA}} — e o ajuste simples que muda tudo…”
- “A pergunta de 15 segundos que revela se {{SOLUCAO}} serve pra você antes de gastar 1 real…”

> Regra: cada bullet deve sugerir algo específico que o leitor quer descobrir.

---

## 5.2 Matriz de Objeções (template)
Para cada objeção:
1) Concorde com empatia (sem se diminuir)
2) Reenquadre a causa
3) Mostre o “como” (passo 1 simples)
4) Prove com caso/dado (se houver)
5) Volte para o CTA

---

## 5.3 Seção “Por que agora?”
Boas razões (reais):
- abertura de turma
- bônus por prazo
- condição de preço
- agenda/limite de suporte
- mudança de cenário (mercado) **somente se você puder sustentar**

Evite:
- urgência falsa
- contagem regressiva fake
- “só hoje” eterno

---

# 6) Checklist Final (antes de publicar)

## Clareza
- [ ] Uma pessoa ocupada entende o que é em 10 segundos?
- [ ] Está claro para quem é / não é?
- [ ] O mecanismo único está explicando o “porquê”?

## Credibilidade
- [ ] Prova aparece antes do pitch pesado?
- [ ] Você não exagerou?
- [ ] Existe transparência sobre limites?

## Conversão
- [ ] Tem CTA suficiente e bem colocado?
- [ ] A oferta está “stacked” com lógica (não inflada)?
- [ ] Objeções principais foram respondidas?

## Tom de voz
- [ ] Soa como a persona espera ser falada?
- [ ] Sem “marketingês” e sem enrolação?

---

# 7) Modo Otimização (quando você já tem uma página)

Cole a página atual e peça:

**PROMPT DE OTIMIZAÇÃO**
- Diagnostique:
  1) Onde a atenção cai
  2) Onde falta prova
  3) Onde o mecanismo confunde
  4) Onde o CTA está fraco
- Reescreva:
  - Headline + lead + mecanismo + prova + oferta + CTAs
- Sugira testes A/B (mín. 12):
  - variações de headline
  - lead
  - bullets
  - oferta (bônus/garantia)
  - layout de CTA

---

# 8) Exemplo de “Campos Preenchidos” (modelo para você copiar)

{{OFERTA}}
- Mentoria “X”
- 6 semanas, 1 call/semana, templates, suporte no WhatsApp
- Preço: R$…
- Garantia: 7 dias…

{{PERSONA}}
- Dono de negócio, tráfego pago, ticket médio…
- Frustrações: …

{{MECANISMO_UNICO}}
- Pilar 1: …
- Pilar 2: …
- Pilar 3: …

{{PROVAS}}
- Case 1: …
- Depoimento 1: …
- Autoridade: …

{{OBJECOES}}
- tempo
- dinheiro
- já tentei
- não funciona pra mim

{{TOM_DE_VOZ}}
- Direto, inteligente, sem hype. Premium, mas humano.

---

## Nota final
Esta skill foi desenhada para produzir uma página **profissional, longa, com “pegada” clássica de direct response**, priorizando:
- **mensagem clara**
- **mecanismo convincente**
- **prova real**
- **oferta bem empilhada**
- **objeções destruídas**
- **CTAs fortes**

Para “resultado financeiro”, o que mais muda o jogo é: **oferta + prova + tráfego qualificado + testes**. Use o checklist de A/B sempre.
