# TEMPLATE — CÁLCULO KE (Conhecimento Efetivo)

> **Uso:** Preencha as seções marcadas com **[PREENCHER]**.
> **Objetivo:** Calcular e documentar o Conhecimento Efetivo (Ke) de uma metodologia.
> **Fórmula:** Ke = (T × A × M × AmpIA) ÷ Lc

---

# Cálculo Ke: [NOME DA METODOLOGIA]

## A Fórmula

```
        T × A × M × AmpIA
Ke = ─────────────────────
              Lc
```

**O que significa:**
> **Ke** é a capacidade de uma metodologia de transformar conhecimento em ação.
> Quanto maior o Ke, mais facilmente o conhecimento se transforma em resultado.

---

## As 5 Variáveis

### T — Transferibilidade (0.0 - 1.0)

**Quão bem o conhecimento pode ser passado de uma pessoa para outra.**

#### Avaliação

| Dimensão | Peso | Nota (0-10) | Ponderado |
|----------|------|-------------|-----------|
| **Clareza** | 33% | [PREENCHER] | [X.XX] |
| **Completude** | 33% | [PREENCHER] | [X.XX] |
| **Sequenciamento** | 34% | [PREENCHER] | [X.XX] |
| **TOTAL** | 100% | — | **[X.XX]** |

#### Dimensões Explicadas

- **Clareza:** Cada passo é executável sem interpretação?
- **Completude:** Nada está implícito, tudo está documentado?
- **Sequenciamento:** A ordem é clara ("faça A, DEPOIS B")?

#### Como Aumentar

| Ação | Impacto | Esforço |
|------|--------|---------|
| Adicionar exemplos concretos | Alto | Médio |
| Remover ambiguidades | Alto | Baixo |
| Criar checklist visual | Médio | Baixo |
| Adicionar screenshots/vídeo | Alto | Alto |

**Valor Atual:** **[X.XX]** / 1.0

---

### A — Aplicabilidade (0.0 - 1.0)

**Quão útil e imediato é o output da metodologia.**

#### Avaliação

| Dimensão | Peso | Nota (0-10) | Ponderado |
|----------|------|-------------|-----------|
| **Relevância** | 33% | [PREENCHER] | [X.XX] |
| **Praticidade** | 33% | [PREENCHER] | [X.XX] |
| **Imediatismo** | 34% | [PREENCHER] | [X.XX] |
| **TOTAL** | 100% | — | **[X.XX]** |

#### Dimensões Explicadas

- **Relevância:** Resolve um problema REAL do usuário?
- **Praticidade:** Output é USÁVEL imediatamente (não teórico)?
- **Imediatismo:** Contexto do usuário considerado (nicho, momento)?

#### Como Aumentar

| Ação | Impacto | Esforço |
|------|--------|---------|
| Tornar output pronto-para-uso | Alto | Médio |
| Adicionar contexto do usuário | Médio | Baixo |
| Tratar casos de borda | Médio | Médio |
| Remover passos teóricos | Alto | Baixo |

**Valor Atual:** **[X.XX]** / 1.0

---

### M — Metodização (0.0 - 1.0)

**Quão bem estruturado está o processo.**

#### Avaliação

| Dimensão | Peso | Nota (0-10) | Ponderado |
|----------|------|-------------|-----------|
| **Atomização** | 33% | [PREENCHER] | [X.XX] |
| **Encadeamento** | 33% | [PREENCHER] | [X.XX] |
| **Validação** | 34% | [PREENCHER] | [X.XX] |
| **TOTAL** | 100% | — | **[X.XX]** |

#### Dimensões Explicadas

- **Atomização:** Quebrado em menores unidades possíveis (átomos)?
- **Encadeamento:** Átomos se conectam em sequência lógica (DAG)?
- **Validação:** Cada passo tem critério de "feito" mensurável?

#### Como Aumentar

| Ação | Impacto | Esforço |
|------|--------|---------|
| Dividir passos grandes em átomos | Alto | Médio |
| Criar diagrama de fluxo (DAG) | Médio | Baixo |
| Adicionar critérios de conclusão | Alto | Baixo |
| Remover dependências circulares | Alto | Alto |

**Valor Atual:** **[X.XX]** / 1.0

---

### Amp — Amplificador IA (1.0 - 15.0+)

**Multiplicador de capacidade com IA.**

#### Avaliação

| Dimensão | Peso | Nota (0-10) | Multiplicador |
|----------|------|-------------|---------------|
| **Calibração** | 40% | [PREENCHER] | [X.XX] |
| **Contexto** | 30% | [PREENCHER] | [X.XX] |
| **Feedback Loop** | 30% | [PREENCHER] | [X.XX] |
| **TOTAL** | 100% | — | **[X.XX]×** |

#### Dimensões Explicadas

- **Calibração:** System prompt tem DNA Mental do expert?
- **Contexto:** RAG com knowledge base específica do domínio?
- **Feedback Loop:** Output → validação → ajuste?

#### Como Aumentar

| Ação | Impacto | Esforço |
|------|--------|---------|
| Criar system prompt especializado | Muito Alto | Alto |
| Adicionar RAG com KB do domínio | Alto | Médio |
| Incluir exemplos reais (few-shot) | Alto | Médio |
| Implementar feedback loop | Alto | Alto |

**Valor Atual:** **[X.XX]**× (1.0 = sem IA, 10× = clone cognitivo)

---

### Lc — Limite Cognitivo (0.2 - 2.0)

**Quanto esforço mental o usuário gasta.**

#### Avaliação

| Dimensão | Peso | Nota (0-10) | Ponderado |
|----------|------|-------------|-----------|
| **Decisões** | 33% | [PREENCHER] | [X.XX] |
| **Complexidade** | 33% | [PREENCHER] | [X.XX] |
| **Ambiguidade** | 34% | [PREENCHER] | [X.XX] |
| **TOTAL** | 100% | — | **[X.XX]** |

#### Dimensões Explicadas

- **Decisões:** Quantas decisões o usuário toma?
- **Complexidade:** Quão complexo é cada passo?
- **Ambiguidade:** O quê é ambíguo ou confuso?

> **IMPORTANTE:** Lc deve ser DIMINUÍDO, não aumentado!
> Menor Lc = menor esforço cognitivo = melhor.

#### Como DIMINUIR

| Ação | Impacto | Esforço |
|------|--------|---------|
| Criar UI/UX que guia | Alto | Alto |
| Usar defaults inteligentes | Alto | Baixo |
| Progressive disclosure | Médio | Médio |
| Feedback imediato | Alto | Médio |

**Valor Atual:** **[X.XX]** / 2.0 (menor é melhor)

---

## Resultado Final

### Cálculo

```
Ke = (T × A × M × AmpIA) ÷ Lc
Ke = ([X.XX] × [X.XX] × [X.XX] × [X.XX]) ÷ [X.XX]
Ke = [X.XX]
```

### Comparativo

| Estado | T | A | M | Amp | Lc | Ke |
|--------|---|---|---|-----|----|----|
| **PRÉ-MaaS** | 0.5 | 0.5 | 0.4 | 1.0 | 2.0 | **0.05** |
| **COM-MaaS** | [X.XX] | [X.XX] | [X.XX] | [X.XX] | [X.XX] | **[X.XX]** |

**Multiplicador:** **[X]×**

### Interpretação

| Faixa de Ke | Interpretação |
|-------------|---------------|
| < 1.0 | Conhecimento não se transforma em ação |
| 1.0 - 5.0 | Transformação parcial, muita fricção |
| 5.0 - 15.0 | Boa transformação, metodologia funcional |
| 15.0 - 50.0 | Excelente transformação, sistema escalável |
| > 50.0 | Conhecimento se torna impacto exponencial |

**Classificação:** [PREENCHER]

---

## Plano de Iteração

### Variável Prioritária

**Identifique a variável com menor pontuação relativa ao alvo:**

| Variável | Atual | Alvo | Gap | Prioridade |
|----------|-------|------|-----|------------|
| T | [X.XX] | 0.8 | [X.XX] | [ ] |
| A | [X.XX] | 0.8 | [X.XX] | [ ] |
| M | [X.XX] | 0.8 | [X.XX] | [ ] |
| Amp | [X.XX] | 5.0 | [X.XX] | [ ] |
| Lc | [X.XX] | <0.5 | [X.XX] | [ ] |

**Variável prioritária:** **[NOME]** (gap: [X.XX])

### Ações de Melhoria

Para **[VARIÁVEL PRIORITÁRIA]**:

| Ação | Responsável | Prazo | Effort | Impacto |
|------|-------------|-------|--------|---------|
| [AÇÃO 1] | [QUEM] | [QUANDO] | Alto/Médio/Baixo | Alto/Médio/Baixo |
| [AÇÃO 2] | [QUEM] | [QUANDO] | Alto/Médio/Baixo | Alto/Médio/Baixo |
| [AÇÃO 3] | [QUEM] | [QUANDO] | Alto/Médio/Baixo | Alto/Médio/Baixo |

### Projeção

Após implementar as ações acima, a nova projeção de Ke é:

```
Ke_novo = [X.XX]
Melhoria: +[X]%
```

---

## Histórico de Medições

| Data | Ke | T | A | M | Amp | Lc | Observações |
|------|----|---|---|---|-----|----|-------------|
| [DATA] | [X.XX] | [X.X] | [X.X] | [X.X] | [X.X] | [X.X] | [OBS] |
| [DATA] | [X.XX] | [X.X] | [X.X] | [X.X] | [X.X] | [X.X] | [OBS] |

---

## Metadados

- **Data do cálculo:** [PREENCHER]
- **Calculado por:** [PREENCHER]
- **Metodologia:** [NOME]
- **Versão:** 1.0

---

**FIM DO TEMPLATE DE CÁLCULO KE**
