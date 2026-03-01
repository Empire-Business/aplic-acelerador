# Guia da Equação Ke (Conhecimento Efetivo)

> **Ke** mede a capacidade de uma metodologia de transformar conhecimento em ação.
> Quanto maior o Ke, mais facilmente o conhecimento se torna resultado.

---

## A Fórmula

```
        T × A × M × AmpIA
Ke = ─────────────────────
              Lc
```

**Em palavras:** O Conhecimento Efetivo é o produto das capacidades de Transferência, Aplicabilidade e Metodização, amplificado pela IA, dividido pelo Limite Cognitivo.

---

## As 5 Variáveis

### T — Transferibilidade (0.0 - 1.0)

**O que é:** Quão bem o conhecimento pode ser passado de uma pessoa para outra.

**Dimensões:**

| Dimensão | Peso | O que medir |
|----------|------|-------------|
| **Clareza** | 33% | Cada passo é executável sem interpretação? |
| **Completude** | 33% | Nada está implícito, tudo está documentado? |
| **Sequenciamento** | 34% | A ordem é clara (faça A, DEPOIS B)? |

**Como AUMENTAR T:**

| Ação | Impacto | Exemplo |
|------|--------|---------|
| Adicionar exemplos concretos | Alto | De "analise o cliente" para "abra o CRM, clique em histórico..." |
| Remover ambiguidades | Alto | De "alguns dados" para "últimas 3 compras + ticket médio" |
| Criar checklist visual | Médio | Checklist com caixas de seleção para cada passo |
| Adicionar screenshots | Médio | Capturas de tela mostrando exatamente onde clicar |
| Especificar formatos | Baixo | "DD/MM/AAAA" em vez de "data" |

**Benchmark:**
- < 0.3: Conhecimento tácito (difícil de transferir)
- 0.3 - 0.5: Conhecimento parcialmente documentado
- 0.5 - 0.7: Conhecimento bem documentado
- > 0.7: Conhecimento altamente transferível

---

### A — Aplicabilidade (0.0 - 1.0)

**O que é:** Quão útil e imediato é o output da metodologia.

**Dimensões:**

| Dimensão | Peso | O que medir |
|----------|------|-------------|
| **Relevância** | 33% | Resolve um problema REAL do usuário? |
| **Praticidade** | 33% | Output é USÁVEL imediatamente? |
| **Imediatismo** | 34% | Contexto do usuário foi considerado? |

**Como AUMENTAR A:**

| Ação | Impacto | Exemplo |
|------|--------|---------|
| Tornar output pronto-para-usar | Alto | Template preenchido em vez de perguntas |
| Adicionar contexto do nicho | Alto | Exemplos específicos para o setor do usuário |
| Tratar casos de borda | Médio | "E se X acontecer?" |
| Remover passos teóricos | Alto | Cortar "por que isso funciona" — focar no "como" |
| Validar com usuários reais | Alto | Testar com 5 pessoas do público-alvo |

**Benchmark:**
- < 0.3: Conhecimento acadêmico (pouco aplicável)
- 0.3 - 0.5: Conhecimento teórico com alguma aplicação
- 0.5 - 0.7: Conhecimento prático
- > 0.7: Conhecimento imediatamente aplicável

---

### M — Metodização (0.0 - 1.0)

**O que é:** Quão bem estruturado está o processo.

**Dimensões:**

| Dimensão | Peso | O que medir |
|----------|------|-------------|
| **Atomização** | 33% | Quebrado em menores unidades possíveis? |
| **Encadeamento** | 33% | Átomos se conectam em sequência lógica (DAG)? |
| **Validação** | 34% | Cada passo tem critério de "feito" mensurável? |

**Como AUMENTAR M:**

| Ação | Impacto | Exemplo |
|------|--------|---------|
| Dividir passos grandes em átomos | Alto | 1 passo de 20 linhas → 5 átomos de 4 linhas |
| Criar diagrama de fluxo (DAG) | Médio | Visualizar Input→Output de cada átomo |
| Adicionar critérios de conclusão | Alto | "Feito quando: checklist concluído" |
| Remover dependências circulares | Alto | Se A depende de B e B de A, fundir ou refazer |
| Definir outputs mensuráveis | Alto | "Lista gerada" em vez de "Progresso feito" |

**Benchmark:**
- < 0.3: Processo ad-hoc (cada vez é diferente)
- 0.3 - 0.5: Processo parcialmente estruturado
- 0.5 - 0.7: Processo bem estruturado
- > 0.7: Sistema replicável

---

### Amp — Amplificador IA (1.0 - 15.0+)

**O que é:** Multiplicador de capacidade com IA.

**Dimensões:**

| Dimensão | Peso | O que medir |
|----------|------|-------------|
| **Calibração** | 40% | System prompt tem DNA Mental do expert? |
| **Contexto** | 30% | RAG com knowledge base específica? |
| **Feedback Loop** | 30% | Output → validação → ajuste? |

**Como AUMENTAR Amp:**

| Ação | Impacto | Exemplo |
|------|--------|---------|
| Criar system prompt especializado | Muito Alto | "Você são [EXPERT], especialista em [DOMÍNIO]..." |
| Adicionar RAG com KB do domínio | Alto | Base de conhecimento com materiais do expert |
| Incluir exemplos reais (few-shot) | Alto | "Aqui estão 3 exemplos de outputs bons..." |
| Implementar feedback loop | Alto | Usuário valida → IA aprende → próximos são melhores |
| Usar modelo mais capaz | Médio | GPT-4/Claude em vez de GPT-3.5 |

**Benchmark:**
- 1.0: Sem IA (processo manual)
- 2.0 - 3.0: IA genérica (ChatGPT padrão)
- 3.0 - 7.0: IA com prompt básico
- 7.0 - 12.0: IA com RAG + few-shot
- > 12.0: Clone cognitivo do expert

---

### Lc — Limite Cognitivo (0.2 - 2.0)

**O que é:** Quanto esforço mental o usuário gasta.

**IMPORTANTE:** Ao contrário das outras variáveis, Lc deve ser **DIMINUÍDO**, não aumentado.

**Dimensões:**

| Dimensão | Peso | O que medir |
|----------|------|-------------|
| **Decisões** | 33% | Quantas decisões o usuário toma? |
| **Complexidade** | 33% | Quão complexo é cada passo? |
| **Ambiguidade** | 34% | O quê é ambíguo ou confuso? |

**Como DIMINUIR Lc:**

| Ação | Impacto | Exemplo |
|------|--------|---------|
| Criar UI/UX que guia | Alto | Wizard com passos sequenciais |
| Usar defaults inteligentes | Alto | IA preenche, usuário só confirma |
| Progressive disclosure | Médio | Mostrar só o necessário no momento |
| Feedback imediato | Médio | Usuário sabe se está certo sem pensar |
| Remover opções desnecessárias | Alto | Menos escolhas = menos esforço |

**Benchmark:**
- > 1.5: Alto esforço cognitivo (usuário desiste)
- 1.0 - 1.5: Esforço médio
- 0.5 - 1.0: Baixo esforço
- < 0.5: Esforço mínimo (usuario flui)

---

## Interpretando Ke

### Faixas de Valor

| Faixa | Interpretação | O que significa |
|-------|---------------|-----------------|
| **< 1.0** | Conhecimento não vira ação | Método PDF que ninguém aplica |
| **1.0 - 5.0** | Transformação parcial | Algumas pessoas aplicam, com dificuldade |
| **5.0 - 15.0** | Transformação funcional | Metodologia que funciona para a maioria |
| **15.0 - 50.0** | Transformação excelente | Sistema escalável, alto impacto |
| **> 50.0** | Transformação exponencial | Conhecimento vira impacto massivo |

### Multiplicador

O **multiplicador** é quanto mais eficaz é a metodologia COM MAAS vs SEM MAAS:

```
Multiplicador = Ke_COM / Ke_PRÉ
```

| Multiplicador | Interpretação |
|---------------|---------------|
| < 10× | Melhoria marginal |
| 10× - 100× | Melhoria significativa |
| 100× - 500× | Transformação radical |
| > 500× | Revolucionário |

**Exemplo típico MAAS:** 300× - 500×

---

## Estudo de Caso: Value Equation

### PRÉ-MaaS (saber implícito)

| Variável | Valor | Justificativa |
|----------|-------|---------------|
| T | 0.4 | Expert sabe, mas não documentou |
| A | 0.6 | Funciona, mas não é claro para outros |
| M | 0.3 | Processo intuitivo, não estruturado |
| Amp | 1.0 | Sem uso de IA |
| Lc | 2.0 | Requer "talento" para entender |

**Ke = (0.4 × 0.6 × 0.3 × 1.0) ÷ 2.0 = 0.036**

---

### COM-MaaS (metodologia documentada)

| Variável | Valor | Como Aumentou |
|----------|-------|--------------|
| T | 0.85 | 4 decisões documentadas + exemplos |
| A | 0.95 | Aplicável a qualquer oferta |
| M | 0.90 | 4 átomos bem sequenciados |
| Amp | 10.0 | IA gera ofertas automaticamente |
| Lc | 0.4 | Template reduz esforço cognitivo |

**Ke = (0.85 × 0.95 × 0.90 × 10.0) ÷ 0.4 = 18.2**

---

### Resultado

**Multiplicador = 18.2 ÷ 0.036 = 505×**

A metodologia se torna **505 vezes mais eficaz** quando documentada com MAAS.

---

## Como Calcular Ke para sua Metodologia

### Passo 1: Avalie cada variável

Use `templates/ke-calculation.md` para documentar.

### Passo 2: Some as dimensões

Cada variável tem 3 dimensões ponderadas:
- T = Clareza × 0.33 + Completude × 0.33 + Sequenciamento × 0.34
- (e assim por diante)

### Passo 3: Aplique a fórmula

```
Ke = (T × A × M × Amp) ÷ Lc
```

### Passo 4: Compare com estado PRÉ

Estime Ke antes de documentar (tipicamente 0.01 - 0.1).

### Passo 5: Identifique a variável prioritária

Qual variável tem maior gap em relação ao alvo?
- Foque nela primeiro para maior impacto.

---

## Metadados

- **Versão:** 1.0
- **Data:** Janeiro 2025
- **Skill:** MAAS Documentation
- **Inspiração:** Framework MAAS/Methodology OS

---

**FIM DO GUIA DA EQUAÇÃO KE**
