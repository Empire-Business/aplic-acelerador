# Padrões Mermaid para MAAS

> Coleção de padrões de diagramas Mermaid usados em documentações MAAS.
> Copie e cole estes padrões nos seus documentos.

---

## 1. Fluxo de Átomos (DAG)

### Básico

```mermaid
graph TD
    A[ESTADO A] --> B[Átomo 1]
    B --> C[Átomo 2]
    C --> D[Átomo 3]
    D --> E[ESTADO B]

    style A fill:#e1f5ff
    style E fill:#c8e6c9
    style B fill:#fff9c4
    style C fill:#fff9c4
    style D fill:#fff9c4
```

### Com Feedback Loop

```mermaid
graph TD
    A[ESTADO A] --> B[Átomo 1]
    B --> C[Átomo 2]
    C --> D{Validação}
    D -->|Sucesso| E[ESTADO B]
    D -->|Falhar| B

    style A fill:#e1f5ff
    style E fill:#c8e6c9
    style B fill:#fff9c4
    style C fill:#fff9c4
    style D fill:#ffcc80
```

### Paralelo

```mermaid
graph TD
    A[ESTADO A] --> B[Átomo 1]
    B --> C[Átomo 2a]
    B --> D[Átomo 2b]
    C --> E[Átomo 3]
    D --> E
    E --> F[ESTADO B]

    style A fill:#e1f5ff
    style F fill:#c8e6c9
    style B fill:#fff9c4
    style C fill:#fff9c4
    style D fill:#fff9c4
    style E fill:#fff9c4
```

---

## 2. Estrutura de Átomo

### Simples

```mermaid
graph LR
    I[📥 INPUT] --> D{⚙️ DECISÃO}
    D --> O[📤 OUTPUT]
    F[⚠️ Fricção] -.bloqueia.-> D

    style I fill:#e3f2fd,stroke:#0288d1
    style D fill:#fff9c4,stroke:#fbc02d
    style O fill:#c8e6c9,stroke:#388e3c
    style F fill:#ffcdd2,stroke:#c62828
```

### Detalhado

```mermaid
graph TB
    subgraph INPUT["📥 CAUSA MATERIAL"]
    I1[Dado 1]
    I2[Dado 2]
    I3[Dado 3]
    end

    subgraph DECISAO["⚙️ CAUSA FORMAL"]
    D{Decisão}
    end

    subgraph OUTPUT["📤 CAUSA FINAL"]
    O1[Resultado 1]
    O2[Resultado 2]
    end

    subgraph FRICCAO["⚠️ FRICÇÕES"]
    F1[Cognitiva]
    F2[Operacional]
    end

    I1 --> D
    I2 --> D
    I3 --> D
    D --> O1
    D --> O2
    F1 -.bloqueia.-> D
    F2 -.bloqueia.-> D
```

---

## 3. Matriz de Agentes

### Por Tipo

```mermaid
graph TB
    subgraph SISTEMA["🔧 SISTEMA (n)"]
    S1[Átomo X]
    S2[Átomo Y]
    end

    subgraph IA["🤖 IA (n)"]
    I1[Átomo Z]
    I2[Átomo W]
    end

    subgraph HUMANO["👤 HUMANO + IA (n)"]
    H1[Átomo V]
    H2[Átomo U]
    end

    style SISTEMA fill:#e3f2fd
    style IA fill:#f3e5f5
    style HUMANO fill:#ffebee
```

### Fluxo com Agentes

```mermaid
graph LR
    A[Início] -->|Humano| B[Decisão]
    B -->|IA| C[Processamento]
    C -->|Sistema| D[Automação]
    D --> E[Fim]

    style B fill:#ffebee
    style C fill:#f3e5f5
    style D fill:#e3f2fd
```

---

## 4. Equação Ke

### Básica

```mermaid
graph LR
    T[T] --> M1((×))
    A[A] --> M1
    M1 --> M2((×))
    M[M] --> M2
    M2 --> M3((×))
    Amp[Amp] --> M3
    M3 --> M4((÷))
    Lc[Lc] --> M4
    M4 --> Ke[Ke]

    style T fill:#c8e6c9
    style A fill:#c8e6c9
    style M fill:#c8e6c9
    style Amp fill:#ce93d8
    style Lc fill:#ffcdd2
    style Ke fill:#fff9c4
```

### Com Valores

```mermaid
graph LR
    T["T=0.85"] --> M1((×))
    A["A=0.90"] --> M1
    M1 --> M2((×))
    M["M=0.85"] --> M2
    M2 --> M3((×))
    Amp["Amp=7×"] --> M3
    M3 --> M4((÷))
    Lc["Lc=0.5"] --> M4
    M4 --> Ke["Ke=9.12"]

    style T fill:#c8e6c9
    style A fill:#c8e6c9
    style M fill:#c8e6c9
    style Amp fill:#ce93d8
    style Lc fill:#ffcdd2
    style Ke fill:#fff9c4,stroke-width:3px
```

---

## 5. As 4 Causas

### Vertical

```mermaid
graph TD
    title[As 4 Causas de Metodologia]
    title --> M[Material<br/>📦 DECISÕES SEQUENCIADAS]
    title --> F[Formal<br/>🏗️ INPUT → TRANSFORMAÇÃO → OUTPUT]
    title --> E[Eficiente<br/>⚙️ O AGENTE QUE EXECUTA]
    title --> FI[Final<br/>🎯 REDUZIR FRICÇÃO A → B]

    style title fill:#e3f2fd,stroke-width:3px
    style M fill:#fff9c4
    style F fill:#fff9c4
    style E fill:#fff9c4
    style FI fill:#c8e6c9
```

### Circular

```mermaid
graph TD
    M((Material))
    F((Formal))
    E((Eficiente))
    FI((Final))

    M --> F
    F --> E
    E --> FI
    FI --> M

    style M fill:#fff9c4
    style F fill:#fff9c4
    style E fill:#fff9c4
    style FI fill:#c8e6c9
```

---

## 6. Anatomia de Metodologia (5 Partes)

```mermaid
graph TD
    A[ESTADO A<br/>Ponto de Partida]
    T[TRANSFORMAÇÕES<br/>Os Átomos de Decisão]
    B[ESTADO B<br/>Ponto de Chegada]
    F[FRIÇÕES<br/>O que Impede]
    AG[AGENTES<br/>Quem Executa]

    A --> T
    T --> B
    T -.bloqueia.-> F
    T -.executado por.-> AG

    style A fill:#e1f5ff
    style T fill:#fff9c4
    style B fill:#c8e6c9
    style F fill:#ffcdd2
    style AG fill:#e1bee7
```

---

## 7. Pipeline de 7 Passos

### Horizontal

```mermaid
graph LR
    A[1. EXTRAIR] --> B[2. ATOMIZAR]
    B --> C[3. SEQUENCIAR]
    C --> D[4. ALOCAR]
    D --> E[5. IMPLEMENTAR]
    E --> F[6. MEDIR Ke]
    F --> G[7. ITERAR]

    style A fill:#90caf9
    style B fill:#90caf9
    style C fill:#fff59d
    style D fill:#fff59d
    style E fill:#a5d6a7
    style F fill:#a5d6a7
    style G fill:#ef9a9a
```

### Com Loop

```mermaid
graph LR
    A[1. EXTRAIR] --> B[2. ATOMIZAR]
    B --> C[3. SEQUENCIAR]
    C --> D[4. ALOCAR]
    D --> E[5. IMPLEMENTAR]
    E --> F[6. MEDIR Ke]
    F --> G[7. ITERAR]
    G -.aprender.-> A

    style A fill:#90caf9
    style B fill:#90caf9
    style C fill:#fff59d
    style D fill:#fff59d
    style E fill:#a5d6a7
    style F fill:#a5d6a7
    style G fill:#ef9a9a
```

---

## 8. Comparativo Pré/Com-MAAS

```mermaid
graph LR
    subgraph PRE["PRÉ-MaaS"]
    T1[T=0.5]
    A1[A=0.5]
    M1[M=0.4]
    Amp1[Amp=1]
    Lc1[Lc=2.0]
    Ke1[Ke=0.05]
    end

    subgraph COM["COM-MaaS"]
    T2[T=0.85]
    A2[A=0.90]
    M2[M=0.85]
    Amp2[Amp=10]
    Lc2[Lc=0.3]
    Ke2[Ke=21.6]
    end

    PRE --> COM

    T1 --> T2
    A1 --> A2
    M1 --> M2
    Amp1 --> Amp2
    Lc1 --> Lc2
    Ke1 --> Ke2

    style Ke1 fill:#ffcdd2
    style Ke2 fill:#c8e6c9,stroke-width:3px
```

---

## 9. Matriz de Decisão (3 Perguntas)

```mermaid
graph TD
    Start[Átomo de Decisão]

    Start --> P1{Determinístico<br/>ou Probabilístico?}
    P1 -->|Determinístico| SISTEMA[SISTEMA]
    P1 -->|Probabilístico| P2{Qual Fricção?}

    P2 -->|Cognitiva| UI[UI/UX + Outro]
    P2 -->|Operacional/Temporal| P3{Qual Risco?}

    P3 -->|Baixo| IA[IA Autônoma]
    P3 -->|Médio| IAH[IA + Humano]
    P3 -->|Alto| HIA[Humano + IA]

    style SISTEMA fill:#90caf9
    style IA fill:#ce93d8
    style IAH fill:#b39ddb
    style HIA fill:#ef9a9a
    style UI fill:#ffcc80
```

---

## 10. Mapa de Fricções

```mermaid
mindmap
    root((Fricções))
        Cognitiva
            Não entende
            Confuso
            Complexo
        Operacional
            Difícil fazer
            Muitos passos
            Requer ferramenta
        Motivacional
            Não quer
            Sem benefício claro
            Esforço alto
        Temporal
            Demora muito
            Resultado distante
        Financeira
            Custa caro
            ROI incerto
```

---

## Paleta de Cores MAAS

| Uso | Cor | Hex |
|-----|-----|-----|
| Estado A | Azul claro | `#e1f5ff` |
| Estado B | Verde claro | `#c8e6c9` |
| Átomo | Amarelo | `#fff9c4` |
| Fricção | Vermelho claro | `#ffcdd2` |
| IA | Roxo claro | `#ce93d8` |
| Sistema | Azul | `#90caf9` |
| Humano | Rosa claro | `#ef9a9a` |
| UI/UX | Laranja claro | `#ffcc80` |
| Ke/Resultado | Amarelo destaque | `#fff9c4` |

---

## Metadados

- **Versão:** 1.0
- **Data:** Janeiro 2025
- **Skill:** MAAS Documentation

---

**FIM DOS PADRÕES MERMAID**
