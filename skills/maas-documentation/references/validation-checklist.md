# Checklist de Validação MAAS

> Use este checklist para garantir que a documentação MAAS está completa e correta.

---

## Seções Obrigatórias

### Definição Aristotélica (4 Causas)

- [ ] **Causa Material (Decisões)** — Lista de decisões sequenciadas está documentada
- [ ] **Causa Formal (Estrutura)** — Estrutura Input→Output está clara
- [ ] **Causa Eficiente (Agentes)** — Agentes de execução estão definidos
- [ ] **Causa Final (Propósito)** — Propósito de redução de fricção está claro

---

### Anatomia de Metodologia (5 Partes)

#### Estado A — Ponto de Partida
- [ ] **Avatar definido** — Quem é a pessoa (não "target" abstrato)
- [ ] **Recursos listados** — O que a pessoa TEM
- [ ] **Gap identificado** — O que a pessoa NÃO TEM
- [ ] **Dor clara** — Por que ela quer mudar

#### Transformações — Os Átomos
- [ ] **Mínimo 3 átomos** — Metodologia tem pelo menos 3 decisões sequenciadas
- [ ] **Input definido** — Cada átomo tem input claro
- [ ] **Decisão clara** — Cada átomo tem decisão executável
- [ ] **Output definido** — Cada átomo tem output mensurável
- [ ] **Sequência lógica** — Átomos se conectam em cascata (DAG)

#### Estado B — Ponto de Chegada
- [ ] **Resultado claro** — O que a pessoa TEM agora
- [ ] **Delta A→B** — O que mudou (antes vs depois)
- [ ] **Evidência** — Como saber que chegou (critérios mensuráveis)

#### Fricções — O que Impede
- [ ] **Mapeamento completo** — Cada transformação tem fricções identificadas
- [ ] **Tipos corretos** — Cognitiva, Operacional, Motivacional, Temporal ou Financeira
- [ ] **Mitigações propostas** — Como cada fricção será endereçada

#### Agentes — Quem Executa
- [ ] **Matriz aplicada** — Cada átomo tem agente alocado via 3 perguntas
- [ ] **Justificativa** — Alocação é justificada pela matriz de decisão

---

### Diagramas

- [ ] **Fluxo de decisões (DAG)** — Diagrama mostra Estado A → Átomos → Estado B
- [ ] **Matriz de agentes** — Distribuição visual de agentes (opcional para metodologias simples)
- [ ] **Equação Ke visual** — Diagrama da equação (se Ke calculado)

---

### Equação Ke

- [ ] **T (Transferibilidade)** calculada com 3 dimensões (Clareza, Completude, Sequenciamento)
- [ ] **A (Aplicabilidade)** calculada com 3 dimensões (Relevância, Praticidade, Imediatismo)
- [ ] **M (Metodização)** calculada com 3 dimensões (Atomização, Encadeamento, Validação)
- [ ] **Amp (Amplificador IA)** calculado com 3 dimensões (Calibração, Contexto, Feedback Loop)
- [ ] **Lc (Limite Cognitivo)** calculado com 3 dimensões (Decisões, Complexidade, Ambiguidade)
- [ ] **Comparativo Pré/Com-MaaS** — Multiplicador de Ke está documentado
- [ ] **Plano de iteração** — Variável prioritária identificada com ações

---

## Qualidade Adicional

### Átomos Bem Documentados

- [ ] Cada átomo tem **ID único**
- [ ] Cada átomo tem **nome curto e descritivo**
- [ ] Cada átomo tem **decisão executável** (não abstrata)
- [ ] Átomos muito grandes foram **divididos** (regra: < 7 linhas)

### Consistência

- [ ] **Terminologia consistente** — Mesmos termos usados em todo o documento
- [ ] **Números consistentes** — Contagens de átomos, distribuição de agentes conferem
- [ ] **Formato consistente** — Tabelas seguem mesmo padrão

### Clareza

- [ ] **Sem jargões não explicados** — Termos técnicos têm definição
- [ ] **Exemplos concretos** — Há exemplos para conceitos abstratos
- [ ] **Visualização** — Diagramas ajudam a entender (não apenas texto)

---

## Validação por Tipo de Documento

### Metodologia Completa

Todas as seções acima mais:
- [ ] Snapshot completo
- [ ] Pipeline de 7 passos documentado
- [ ] Apêndice com glossário

### Documento de Átomo Único

- [ ] 4 Causas do átomo documentadas
- [ ] Fricções específicas identificadas
- [ ] Agente justificado
- [ ] Critérios de sucesso definidos

### Documento de Cálculo Ke

- [ ] Todas as 5 variáveis calculadas
- [ ] Comparativo com estado PRÉ-MaaS
- [ ] Interpretação do resultado
- [ ] Plano de iteração com ações específicas

---

## Erros Comuns a Evitar

| Erro | Como Detectar | Como Corrigir |
|------|---------------|---------------|
| **Átomos muito grandes** | > 7 linhas de instrução | Dividir em múltiplos átomos |
| **Input vago** | "Informações", "Dados" | Especificar quais dados exatamente |
| **Decisão abstrata** | "Analisar", "Entender" | Escrever como ação executável |
| **Output não mensurável** | "Resultado melhor" | Definir métrica específica |
| **Fricção genérica** | "Difícil" | Identificar tipo específico (COG/OP/etc) |
| **Agente não justificado** | Alocado sem motivo | Aplicar matriz de 3 perguntas |
| **Ke sem comparação** | Apenas valor final | Calcular PRÉ vs COM-MaaS |
| **Diagrama ilegível** | Muitos nós, confuso | Dividir em múltiplos diagramas |

---

## Níveis de Qualidade

### Nível Bronze (Mínimo Viável)
- ✓ 4 Causas documentadas
- ✓ Mínimo 3 átomos
- ✓ Estado A e B definidos
- ✓ Agentes alocados
- ⚠️ Sem diagramas
- ⚠️ Ke não calculado

### Nível Prata (Funcional)
- ✓ Tudo do Bronze
- ✓ Diagrama de fluxo (DAG)
- ✓ Fricções mapeadas
- ✓ Ke calculado
- ⚠️ Sem exemplos
- ⚠️ Sem plano de iteração

### Nível Ouro (Completo)
- ✓ Tudo do Prata
- ✓ Todos os diagramas
- ✓ Exemplos concretos
- ✓ Plano de iteração detalhado
- ✓ Comparativo Pré/Com-MaaS
- ✓ Glossário e referências

---

## Metadados

- **Versão:** 1.0
- **Data:** Janeiro 2025
- **Skill:** MAAS Documentation

---

**FIM DO CHECKLIST DE VALIDAÇÃO**
