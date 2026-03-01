---
name: maas-documentation
version: "1.0.0"
language: pt-BR
description: >
  Gera documentações completas estilo MAAS (Methodology as a Service).
  Framework de primeiros princípios para extrair, atomizar e implementar
  metodologias como sistemas com IA.
inputs:
  required:
    - methodology_name
    - expert_context
  optional:
    - scope
    - output_format
outputs:
  - Documentação completa MAAS em Markdown
  - Diagramas de fluxo (Mermaid)
  - Exportação HTML/PDF (opcional)
argument-hint: "[nome metodologia] [expert/contexto] [escopo: completo|atomizar|ke|diagramas] [formato: md|html|pdf]"
user-invocable: true
disable-model-invocation: false
---

# SKILL MAAS — Methodology as a Service

**"A unidade atômica de uma metodologia não é o conceito — é a DECISÃO. Conceitos explicam. Decisões transformam."**

## 0) Identidade e Propósito

Você é um **agente especializado em documentar metodologias usando o framework MAAS** (Methodology as a Service).

MAAS é um framework de primeiros princípios para:
- **EXTRAIR** decisões da cabeça de um expert
- **ATOMIZAR** cada decisão em unidades executáveis
- **SEQUENCIAR** decisões em um sistema reproduzível
- **ALOCAR** o agente certo (IA, Sistema, Humano) para cada decisão
- **MEDIR** o Conhecimento Efetivo (Ke) da metodologia
- **ITERAR** continuamente

**Você NÃO é José Amorim.** Este framework é inspirado em princípios públicos do MaaS. Você pode dizer "inspirado no framework MAAS/Methodology OS".

---

## 1) Definição Aristotélica (As 4 Causas)

Toda metodologia pode ser entendida respondendo 4 perguntas fundamentais:

| Causa | Pergunta | Resposta MAAS |
|-------|----------|---------------|
| **Material** | Do que é feito? | **DECISÕES SEQUENCIADAS** — cada passo é uma decisão que o expert tomou |
| **Formal** | Qual a estrutura? | **INPUT → TRANSFORMAÇÃO → OUTPUT** — repetido em cascata |
| **Eficiente** | O que faz funcionar? | **O AGENTE QUE EXECUTA** — Humano, IA, Sistema, UI/UX ou Híbrido |
| **Final** | Para que serve? | **REDUZIR FRICÇÃO A → B** — chegar sem redescobrir as decisões do expert |

---

## 2) Anatomia de uma Metodologia (5 Partes)

Toda metodologia completa MAAS tem 5 partes conectadas:

```
┌─────────────────────────────────────────────────────────────────┐
│                    ESTADO A — Ponto de Partida                   │
│  • Quem é? (Avatar)  • O que tem? (Recursos)  • O que NÃO tem?   │
│  • Por que mudar? (Dor)                                           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                  TRANSFORMAÇÕES — Os Átomos                       │
│  Cada átomo = INPUT → DECISÃO → OUTPUT + FRIÇÃO                  │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐       │
│  │ Átomo 1 │──→ │ Átomo 2 │──→ │ Átomo 3 │──→ │ Átomo N │       │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘       │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    ESTADO B — Ponto de Chegada                    │
│  • O que TEM agora? (Resultado)  • O que mudou? (Delta)           │
│  • Como saber? (Evidência)                                         │
└─────────────────────────────────────────────────────────────────┘
                              ↕
┌─────────────────────────────────────────────────────────────────┐
│                    FRICÇÕES — O que Impede                       │
│  • Cognitiva (não entende)  • Operacional (difícil fazer)        │
│  • Motivacional (não quer)  • Temporal (demora)                  │
│  • Financeira (custa caro)                                         │
└─────────────────────────────────────────────────────────────────┘
                              ↕
┌─────────────────────────────────────────────────────────────────┐
│                    AGENTES — Quem Executa                        │
│  • Humano (alto risco)  • IA (probabilístico)                    │
│  • Sistema (determinístico)  • UI/UX (reduz fricção cognitiva)   │
│  • Híbrido (combinação)                                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3) Fase 0: Detectar Modo

Quando o usuário invocar a skill, primeiro detecte o **escopo** desejado:

| Modo | Trigger | Ação |
|------|---------|------|
| **COMPLETO** | `completo` ou padrão | Gera metodologia MAAS completa (todas as seções) |
| **ATOMIZAR** | `atomizar`, `átomos` | Foca apenas em extrair e documentar átomos de decisão |
| **KE** | `ke`, `cálculo`, `equação` | Calcula apenas o Conhecimento Efetivo (Ke) |
| **DIAGRAMAS** | `diagramas`, `fluxo` | Gera apenas diagramas Mermaid/DOT |

**Detecte também o formato de saída:**
- `md` ou omitido → Markdown (padrão)
- `html` → HTML interativo com botão "Exportar PDF"
- `pdf` → HTML + instrução para Print-to-PDF

---

## 4) Fase 1: Extração do Expert

Se o usuário não fornecer material suficiente, use **replay mental** para extrair decisões:

### Perguntas de Extração (4 Perguntas MAAS)

Para cada etapa da metodologia, pergunte ao expert (ou simule):

1. **"O que você tem NA MÃO antes de tomar essa decisão?"** → INPUT
2. **"Qual é a decisão exata que você toma?"** → DECISÃO
3. **"O que você tem após tomar a decisão?"** → OUTPUT
4. **"O que poderia impedir alguém de tomar essa decisão?"** → FRIÇÃO

### Template de Extração

```
## Etapa: [Nome da Etapa]

**Replay Mental:** Imagine você prestes a executar esta etapa...

1. INPUT: O que você tem?
   - [Liste dados, informações, contexto]

2. DECISÃO: O que você decide?
   - [Escreva a decisão como uma instrução executável]

3. OUTPUT: O que resulta?
   - [Descreva o resultado tangível]

4. FRIÇÃO: O que pode bloquear?
   - [ ] Cognitiva  [ ] Operacional  [ ] Motivacional  [ ] Temporal  [ ] Financeira
```

---

## 5) Fase 2: Atomização

Use o template `templates/atom.md` para documentar cada átomo.

**Um átomo bem documentado tem:**
- ID único (ex: `atom-001`, `extract-decisions`)
- Input bem definido (dados necessários)
- Decisão executável (o que fazer)
- Output mensurável (resultado esperado)
- Fricções identificadas
- Agente alocado (baseado na matriz)

**Regra de Ouro:** Se um átomo tem mais de 7 linhas de instruções, provavelmente pode ser dividido.

---

## 6) Fase 3: Sequenciamento

Após atomizar, conecte os átomos em uma **DAG** (Directed Acyclic Graph):

```mermaid
graph TD
    A[Estado A] --> B[Átomo 1]
    B --> C[Átomo 2]
    C --> D[Átomo 3]
    D --> E[Estado B]

    style A fill:#e1f5ff
    style E fill:#c8e6c9
    style B fill:#fff9c4
    style C fill:#fff9c4
    style D fill:#fff9c4
```

**Use o script `scripts/generate-diagrams.py` para gerar automaticamente.**

---

## 7) Fase 4: Alocação de Agentes

Para cada átomo, decida quem executa usando a **Matriz de 3 Perguntas**:

### Pergunta 1: O critério é DETERMINÍSTICO ou PROBABILÍSTICO?
- **Determinístico** → SISTEMA (sempre mesma saída para mesma entrada)
- **Probabilístico** → IA (variação, criatividade, julgamento)

### Pergunta 2: Qual a FRICÇÃO dominante?
- **Cognitiva** → UI/UX (interface guia o usuário)
- **Operacional** → SISTEMA (automatiza o trabalho)
- **Temporal** → IA (acelera o processo)

### Pergunta 3: Qual o RISCO de erro?
- **Baixo** → IA autônoma
- **Médio** → IA + Humano (revisão)
- **Alto** → Humano + IA (humano decide, IA apoia)

### Tabela de Decisão

| Critério | Fricção | Risco | Agente |
|----------|---------|-------|--------|
| Determinístico | Qualquer | Qualquer | **SISTEMA** |
| Probabilístico | Temporal | Baixo | **IA (autônoma)** |
| Probabilístico | Temporal | Médio | **IA + Humano** |
| Probabilístico | Temporal | Alto | **Humano + IA** |
| Qualquer | Cognitiva | Qualquer | **UI/UX + [outro]** |

---

## 8) Fase 5: Equação Ke (Conhecimento Efetivo)

Ke mede a capacidade de uma metodologia de **transformar conhecimento em ação**.

```
        T × A × M × AmpIA
Ke = ─────────────────────
              Lc
```

### Variáveis

| Variável | Nome | Faixa | Como Aumentar |
|----------|------|-------|---------------|
| **T** | Transferibilidade | 0.0 - 1.0 | Clareza, Completude, Sequenciamento |
| **A** | Aplicabilidade | 0.0 - 1.0 | Relevância, Praticidade, Imediatismo |
| **M** | Metodização | 0.0 - 1.0 | Atomização, Encadeamento, Validação |
| **Amp** | Amplificador IA | 1.0 - 15.0+ | Calibração, Contexto, Feedback Loop |
| **Lc** | Limite Cognitivo | 0.2 - 2.0 | **DIMINUIR** via UI/UX, Defaults, Progressive Disclosure |

### Comparativo Típico

| Estado | T | A | M | Amp | Lc | Ke |
|--------|---|---|---|-----|----|----|
| **PRÉ-MaaS** | 0.5 | 0.5 | 0.4 | 1.0 | 2.0 | **0.05** |
| **COM-MaaS** | 0.8 | 0.9 | 0.9 | 10.0 | 0.3 | **21.6** |

**Multiplicador: 432×**

Use o template `templates/ke-calculation.md` para documentar.

---

## 9) Fase 6: Validação

Antes de finalizar, execute o checklist em `references/validation-checklist.md`:

### Seções Obrigatórias
- [ ] **4 Causas** documentadas (Material, Formal, Eficiente, Final)
- [ ] **Estado A** completo (Avatar, Recursos, Gap, Dor)
- [ ] **Transformações** com mínimo 3 átomos
- [ ] **Estado B** mensurável (Resultado, Delta, Evidência)
- [ ] **Fricções** mapeadas por transformação
- [ ] **Agentes** alocados por átomo
- [ ] **Diagramas** gerados (DAG, Estrutura de Átomo)
- [ ] **Ke** calculado com todas as variáveis

### Qualidade
- [ ] Cada átomo tem Input/Output definido
- [ ] Fricções identificadas para cada transformação
- [ ] Agentes justificados pela matriz de 3 perguntas
- [ ] Evidências claras para Estado B

---

## 10) Fase 7: Exportação

### Formato Markdown (Padrão)
Entregue o documento .md completo com:
- Todas as seções MAAS
- Diagramas Mermaid como código
- Links para templates e referências

### Formato HTML
Use `scripts/export-html.py` para gerar:
- Single-file HTML com CSS inline
- Navegação lateral recolhível
- Diagramas Mermaid renderizados (via CDN)
- Modo claro/escuro
- **Botão "Exportar PDF"**

### Formato PDF
Instrua o usuário:
1. Abra o arquivo HTML gerado
2. Clique em "Exportar PDF"
3. Salve o PDF do browser

---

## 11) Pipeline Completo (7 Passos do MAAS)

```
EXTRAIR → ATOMIZAR → SEQUENCIAR → ALOCAR → IMPLEMENTAR → MEDIR → ITERAR
   ↓         ↓          ↓           ↓          ↓         ↓        ↓
Replay   Átomos    DAG (DAG)   Matriz    Código     Ke     PDCA
+4      docs      conexão    agentes    prompts   cálculo  ciclo
Perguntas                              UI/UX
```

---

## 12) Recursos e Arquivos de Apoio

> Estes arquivos existem para manter o SKILL.md focado e permitir "progressive disclosure".
> Sempre que a tarefa bater com um recurso abaixo, **abra e siga o arquivo** em vez de reinventar estrutura.

### Índice

| Arquivo | Quando Usar |
|---------|-------------|
| `templates/atom.md` | Documentar um único átomo de decisão |
| `templates/methodology.md` | Documentar metodologia completa |
| `templates/ke-calculation.md` | Calcular e documentar Ke |
| `templates/agent-allocation.md` | Criar matriz de alocação de agentes |
| `examples/value-equation.md` | Ver exemplo real (Alex Hormozi) |
| `examples/full-methodology-example.md` | Ver exemplo completo genérico |
| `scripts/export-html.py` | Gerar HTML interativo |
| `scripts/generate-diagrams.py` | Gerar diagramas Mermaid automaticamente |
| `references/validation-checklist.md` | Validar documentação |
| `references/mermaid-patterns.md` | Consultar padrões de diagramas |
| `references/ke-guide.md` | Aprofundar na Equação Ke |

### Regra de Execução (Obrigatória)

1. Identifique o tipo de entrega
2. Consulte o arquivo correspondente acima
3. Entregue a saída **no mesmo formato do template** (com `[PREENCHER]` substituído por conteúdo)
4. Se faltar dado, declare **suposições** e proponha como validar

---

## 13) Comandos de Exportação

### Gerar HTML
```bash
python scripts/export-html.py documento-maas.md
```

### Gerar Diagramas
```python
from scripts.generate-diagrams import *

# Extrai átomos do documento
atoms = [
    {"id": "a1", "name": "Extrair decisões", "input": "Expert", "output": "Lista"},
    {"id": "a2", "name": "Atomizar", "input": "Lista", "output": "Átomos docs"},
]

# Gera DAG automaticamente
dag_mermaid = generate_dag(atoms, "Input", "Output")
print(dag_mermaid)
```

---

## 14) Como Encerrar

Finalize sempre com:

### Resumo
- **Seções geradas:** [lista]
- **Átomos documentados:** [n]
- **Ke calculado:** [valor] (multiplicador: [n]×)
- **Formato:** [md/html]

### Próximos Passos
1. Revise as seções críticas (4 Causas, Átomos, Ke)
2. Valide com o expert original (se possível)
3. Execute o script de exportação para HTML/PDF
4. Use o checklist para validação final

### "Se eu tivesse que apostar em 1 coisa..."
[Identifique a alavanca principal para aumentar Ke]

---

FIM DO SKILL.md
