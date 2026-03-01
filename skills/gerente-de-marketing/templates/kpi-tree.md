# TEMPLATE — KPI TREE + PLANO DE MEDIÇÃO (Marketing “com prova”)
> Uso: este arquivo é o seu “sistema nervoso” de mensuração.
> Preencha tudo que estiver como **[PREENCHER]**.
> Regra: não rode campanha sem (1) baseline, (2) KPI primário e (3) regra de decisão.

---

## 0) Snapshot (60s)
- **Marca/Produto:** [PREENCHER]
- **Mercado/Idioma:** [PREENCHER]
- **Janela:** [PREENCHER] (datas)
- **Objetivo primário:** [PREENCHER] (ex.: penetração / receita / margem / retenção / equity)
- **North Star (1):** [PREENCHER]
- **Baseline da North Star:** [PREENCHER]
- **Meta (com prazo):** [PREENCHER]
- **Orçamento:** [PREENCHER]
- **Canais envolvidos:** [PREENCHER]
- **Restrições/Compliance:** [PREENCHER]

---

## 1) KPI Tree (estrutura obrigatória)
> Preencha de cima para baixo.
> Use NO MÁXIMO: 1 North Star + 3 Outcomes + 6–12 Drivers + 3–6 Guardrails.

### 1.1 North Star (1 métrica que decide sucesso)
**North Star:** [PREENCHER]  
**Por que é a North Star?** [PREENCHER]  
**Como mede (fonte de verdade):** [PREENCHER]  
**Cadência:** ( ) diária ( ) semanal ( ) quinzenal ( ) mensal  
**Owner:** [PREENCHER]

Exemplos (escolha 1 e adapte):
- Receita incremental (R$) / Lucro incremental (R$)
- Novos compradores (n) / Penetração (%)
- LTV (R$) / Retenção (%)
- Receita por ponto de venda / Share (%)
- Brand Equity Index (composto)

---

### 1.2 Outcomes (Lagging) — 1 a 3 métricas de resultado
Preencha:

**Outcome #1:** [PREENCHER]  
- Definição: [PREENCHER]  
- Baseline: [PREENCHER]  
- Meta: [PREENCHER]  
- Fonte: [PREENCHER]

**Outcome #2 (opcional):** [PREENCHER]  
**Outcome #3 (opcional):** [PREENCHER]

Exemplos comuns:
- Receita total / Receita incremental
- Share / Penetração / Frequência
- Conversão final (CVR) / CAC / LTV
- Retenção D30/D90 / Churn
- Preferência / Saliência / Diferenciação

---

### 1.3 Drivers (Leading) — o que move Outcomes
> Drivers devem ser “acionáveis” (dá para mexer neles na semana).

Organize por camadas (use as que fizerem sentido):

#### A) Distribuição / Disponibilidade (quando aplicável)
- **Distribuição numérica (%):** [PREENCHER]
- **Disponibilidade (ruptura %):** [PREENCHER]
- **Preço relativo / promo depth:** [PREENCHER]
- **Share of shelf / visibilidade no PDV:** [PREENCHER]

#### B) Mídia e alcance efetivo
- **Reach efetivo (pessoas únicas):** [PREENCHER]
- **Frequência efetiva:** [PREENCHER]
- **Qualidade de exposição (viewability, VTR, atenção qualificada):** [PREENCHER]
- **CPM / CPC / CPV:** [PREENCHER]

#### C) Criativo (a variável estratégica)
- **Hook rate (3s):** [PREENCHER]
- **Hold / retenção de vídeo (6s/15s):** [PREENCHER]
- **Branding early (marca até 3s):** [PREENCHER]
- **Scorecard de qualidade criativa (1–5):** [PREENCHER]

#### D) Funil / Jornada (digital/performance)
- **CTR qualificado:** [PREENCHER]
- **LP view → ATC:** [PREENCHER]
- **ATC → Checkout:** [PREENCHER]
- **Checkout → Compra:** [PREENCHER]
- **CAC:** [PREENCHER]
- **ROAS (não-incremental):** [PREENCHER]

#### E) CRM / Retenção (lifecycle)
- **Ativação (evento-chave):** [PREENCHER]
- **Recompra (D30/D60):** [PREENCHER]
- **Taxa de reativação:** [PREENCHER]
- **Open/Click/Response rate (por canal):** [PREENCHER]

#### F) Marca (para sustentar o longo prazo)
- **Saliência / lembrança:** [PREENCHER]
- **Preferência:** [PREENCHER]
- **Diferenciação:** [PREENCHER]
- **Consideração:** [PREENCHER]
- **Brand lift (se houver):** [PREENCHER]

---

### 1.4 Guardrails (o que NÃO pode piorar)
> Guardrails evitam “ganhar no dashboard e perder no negócio”.

- **Guardrail #1:** [PREENCHER] (ex.: margem, NPS, reclamações, devoluções)
- **Guardrail #2:** [PREENCHER]
- **Guardrail #3:** [PREENCHER]
- **Brand safety / compliance:** [PREENCHER] (regras de conteúdo, idade, claims etc.)

---

## 2) Dicionário de métricas (definição + fórmula)
> Sem dicionário, cada área mede “do seu jeito” e ninguém concorda.

Para cada métrica crítica (North Star + Outcomes + drivers-chave), preencha:

### Métrica: [PREENCHER]
- **Definição (1 frase):** [PREENCHER]
- **Fórmula:** [PREENCHER]
- **Fonte de verdade:** [PREENCHER] (ERP/CRM/GA/Ads/BI)
- **Janela / lookback:** [PREENCHER]
- **Segmentos obrigatórios:** [PREENCHER] (canal, público, região, SKU)
- **Cadência:** [PREENCHER]
- **Owner:** [PREENCHER]
- **Ação quando sobe:** [PREENCHER]
- **Ação quando cai:** [PREENCHER]

---

## 3) Plano de instrumentação (checklist “não quebra”)
- [ ] UTMs padronizadas (fonte / meio / campanha / conteúdo)
- [ ] Pixel/SDK instalado e validado
- [ ] Eventos de funil definidos (view → click → add_to_cart → checkout → purchase)
- [ ] Eventos com IDs (pedido, cliente, produto) e deduplicação
- [ ] Consentimento / LGPD ok (opt-in, política, armazenamento)
- [ ] Conversões offline (quando aplicável) integradas
- [ ] Painel no BI com fonte de verdade documentada
- [ ] Rotina de QA (amostras, discrepância ads vs BI)

---

## 4) Experimentos e prova de incrementalidade (anti-autoengano)
> Objetivo: separar impacto real de “correlação”.

### 4.1 Backlog de hipóteses (3–10)
**Hipótese #1:** Se fizermos [X], então [Y] porque [Z].  
- KPI primário: [PREENCHER]
- Público/contexto: [PREENCHER]
- Variável: ( ) criativo ( ) audiência ( ) oferta ( ) landing ( ) preço ( ) canal
- Risco: [PREENCHER]

Repita conforme necessário.

### 4.2 Desenho do teste (escolha 1)
( ) A/B clássico (randomizado)  
( ) Holdout de audiência (ex.: excluir % do público)  
( ) Geo-test (regiões/DMAs)  
( ) Pré/pós com controle (diferença-em-diferenças)  
( ) Teste criativo multivariado (com guarda-corpos)

### 4.3 Plano do experimento (template)
- **Nome do teste:** [PREENCHER]
- **Hipótese:** [PREENCHER]
- **Grupos (controle vs teste):** [PREENCHER]
- **Tamanho/amostra/duração:** [PREENCHER]
- **Métrica primária (incremental):** [PREENCHER]
- **Métricas secundárias:** [PREENCHER]
- **Guardrails:** [PREENCHER]
- **Regra de decisão (antes de rodar):**
  - Escalar se: [PREENCHER]
  - Iterar se: [PREENCHER]
  - Matar se: [PREENCHER]
- **Como ler resultado:** [PREENCHER]
- **Owner:** [PREENCHER]
- **Data de leitura D+7 / D+14:** [PREENCHER]

---

## 5) Rotina de leitura (operar como sistema)
> Recomendação: 1 “scoreboard” curto + 1 “narrativa” clara + 1 lista de decisões.

### 5.1 Scoreboard semanal (1 página)
- North Star: [PREENCHER]
- Outcomes: [PREENCHER]
- Drivers críticos: [PREENCHER]
- Guardrails: [PREENCHER]
- Decisões tomadas: [PREENCHER]
- Próximos testes: [PREENCHER]

### 5.2 Cadência sugerida
- **Diário (15 min):** saúde de gasto + guardrails + sinais de quebra
- **Semanal (45–60 min):** drivers, criativo, funil, decisões de budget
- **Mensal (60–90 min):** outcomes e efeitos de marca, revisão 70/20/10
- **Pós-mortem (30–60 min):** aprendizados e playbook atualizado

---

## 6) Matriz de decisões (o que fazer com os números)
> Preencha para evitar discussões eternas.

### 6.1 Se [Driver] cair
- Causas prováveis: [PREENCHER]
- Checagens: [PREENCHER]
- Ações imediatas (24–72h): [PREENCHER]
- Ações estruturais (2–6 semanas): [PREENCHER]

### 6.2 Se [Outcome] cair
- Causas prováveis (mídia vs oferta vs produto vs distribuição): [PREENCHER]
- Plano de diagnóstico: [PREENCHER]
- Ação: [PREENCHER]

---

## 7) Exemplo preenchido (mini) — para orientar
> **Cenário:** e-commerce de assinatura (exemplo didático)

- **North Star:** Receita incremental (R$) em 8 semanas  
- **Baseline:** R$ 500k / 8 semanas  
- **Meta:** R$ 650k / 8 semanas (+30%)

**Outcomes**
- Novos assinantes: baseline 2.000 → meta 2.700  
- Retenção D30: baseline 62% → meta 66%

**Drivers**
- Reach efetivo: 1,2M → 1,6M  
- Hook 3s: 28% → 35%  
- LP → ATC: 6,5% → 8,0%  
- ATC → Compra: 22% → 26%  
- CAC: ≤ R$ 120 (guardrail)

**Regra de decisão**
- Escalar criativo vencedor se CVR incremental ≥ +10% e CAC ≤ R$ 120  
- Matar rota se CVR ≤ -5% ou reclamações ↑ acima de [X]

---

## 8) Checklist final (antes de apertar “go”)
- [ ] North Star definida com baseline e fonte de verdade
- [ ] 1–3 Outcomes definidos
- [ ] Drivers acionáveis mapeados
- [ ] Guardrails definidos
- [ ] Instrumentação validada
- [ ] Regra de decisão pré-definida
- [ ] Rotina de leitura agendada (scoreboard + owners)

---
