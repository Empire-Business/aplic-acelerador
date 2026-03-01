# PROTOCOLO DE ENTREGA - FASE 02: BRAND BOOK

> **Programa:** Acelerador de Audiência  
> **Fase:** 02 - Brand Book: Documento de Identidade Narrativa  
> **Versão:** 1.0  
> **Última atualização:** Fevereiro/2026

---

## 📋 OBJETIVO DO PROTOCOLO

Este protocolo estabelece o processo operacional para execução da **Fase 2 - Brand Book** do programa Acelerador de Audiência, resultando na entrega do **Documento de Identidade Narrativa** ao cliente.

**Objetivo principal:** Construir uma identidade de marca clara, consistente e narrativa, estabelecendo as bases para toda a comunicação do cliente nos próximos 12 meses.

---

## ✅ CHECKLIST DE INSUMOS NECESSÁRIOS

Antes de iniciar a execução, certifique-se de que todos os insumos abaixo foram recebidos do cliente:

### 🎥 Gravações Obrigatórias (Aulas da Fase 2)
- [ ] **Aula 04 - Essência da Marca** (mínimo 15 minutos)
  - Por que a empresa existe? (Propósito)
  - Onde quer chegar? (Visão)
  - Como vai chegar lá? (Missão)
  - O que não abre mão? (Valores)
- [ ] **Aula 05 - Voz e Tom** (mínimo 15 minutos)
  - Se a marca fosse uma pessoa, quem seria?
  - Exemplos de como fala e como NÃO fala
  - Momentos de tom formal vs. informal
- [ ] **Aula 06 - Narrativas Fundamentais** (mínimo 20 minutos)
  - História de origem da empresa
  - Transformações vividas por clientes
  - Momentos de superação e aprendizado

### 📁 Materiais Complementares
- [ ] Resultado da Fase 01 (Mapa de Riscos e Oportunidades)
- [ ] Depoimentos de clientes (mínimo 5, preferencialmente em vídeo)
- [ ] Cases de sucesso detalhados (mínimo 3)
- [ ] Materiais de comunicação anteriores (posts, emails, etc.)
- [ ] Entrevistas com colaboradores (se empresa tem equipe)
- [ ] Pesquisas de satisfação do cliente (se houver)

### 📝 Documentos de Referência
- [ ] Respostas ao Questionário de Personalidade da Marca
- [ ] Exemplos de marcas que admira (e por quê)
- [ ] Exemplos de marmas que NÃO quer ser (e por quê)
- [ ] Glossário de termos do setor

---

## 🔄 PASSO A PASSO DA EXECUÇÃO

### ETAPA 1: Preparação e Contextualização (Dia 1)

```bash
# Comando de preparação
EXECUTAR: preparar_fase02 \
  --cliente=[NOME_CLIENTE] \
  --fase01=[caminho/mapa_fase01.md] \
  --pasta=[CAMINHO_PASTA]
```

**Ações:**
1. Revisar Mapa de Riscos e Oportunidades (Fase 01)
2. Criar estrutura de pastas:
   ```
   📁 [CLIENTE] - Fase 02/
   ├── 📁 01 - Gravações/
   ├── 📁 02 - Depoimentos/
   ├── 📁 03 - Análises/
   ├── 📁 04 - Rascunhos/
   └── 📁 05 - Entregáveis/
   ```
3. Consolidar todos os insumos recebidos
4. Criar documento de brief com insights da Fase 01

### ETAPA 2: Extração de Narrativas das Aulas (Dia 1-2)

```bash
# Comando de extração narrativa
EXECUTAR: extrair_narrativas \
  --aulas=[aula04.mp4,aula05.mp4,aula06.mp4] \
  --categorias=[proposito,valores,historias,transformacoes] \
  --saida=[banco_narrativas.md]
```

**Ações:**
1. Assistir e transcrever trechos-chave das aulas
2. Identificar e catalogar:
   - 🎯 **Histórias de origem** - Como tudo começou
   - 🎯 **Momentos de virada** - Desafios superados
   - 🎯 **Conexões emocionais** - Por que faz o que faz
   - 🎯 **Provas sociais** - Resultados concretos
   - 🎯 **Vocabulário próprio** - Termos e expressões recorrentes

3. Criar **Banco de Narrativas** estruturado

### ETAPA 3: Definição da Essência da Marca (Dia 2-3)

```bash
# Comando de construção da essência
EXECUTAR: definir_essencia_marca \
  --narrativas=[banco_narrativas.md] \
  --framework=[essencia_template.md] \
  --saida=[essencia_rascunho.md]
```

**Elementos a definir:**

| Elemento | Descrição | Formato |
|----------|-----------|---------|
| **Propósito** | Razão de existir além do lucro | "Existimos para..." |
| **Visão** | Futuro desejado em 5-10 anos | "Queremos ser/ver..." |
| **Missão** | Compromisso diário | "Nossa missão é..." |
| **Valores** | Princípios não negociáveis | 3-5 valores com definição |
| **Promessa** | Resultado garantido ao cliente | "Com a gente você..." |
| **Posicionamento** | Território único | "A única que... para..." |

### ETAPA 4: Construção da Personalidade (Dia 3)

```bash
# Comando de persona da marca
EXECUTAR: construir_personalidade \
  --aulas=[aula05.mp4] \
  --arquetipos=[arquetipos_base.json] \
  --saida=[personalidade_marca.md]
```

**Framework de Personalidade:**
```
🎭 PERSONALIDADE DA MARCA

Arquétipo Principal: [Ex: O Mago, O Herói, O Sábio...]

Dimensões de Tom:
┌─────────────────────────────────────────────────┐
│ Formal ○─────────────────────────────● Informal │
│ Técnico ●────────────────────────────○ Acessível │
│ Sério   ○────────────────────────────● Leve     │
│ Tradicional ○────────────────────────● Inovador │
└─────────────────────────────────────────────────┘

Voz da Marca:
✓ Fala assim: [ex: "Vamos juntos", "Você consegue"]
✗ NUNCA fala assim: [ex: "O cliente deve", "É obrigatório"]

Expressões Típicas:
→ [Lista de 5-10 expressões que refletem a voz]

Exemplos de Aplicação:
│ Situação           │ Exemplo de escrita      │
├────────────────────┼─────────────────────────┤
│ Boas-vindas        │                         │
│ Anúncio de produto │                         │
│ Resposta a crise   │                         │
│ Comemoração        │                         │
```

### ETAPA 5: Estruturação das Narrativas Fundamentais (Dia 4)

```bash
# Comando de estruturação de narrativas
EXECUTAR: estruturar_narrativas \
  --banco=[banco_narrativas.md] \
  --framework=[storytelling_base.md] \
  --saida=[narrativas_fundamentais.md]
```

**Narrativas a estruturar:**

1. **História de Origem** (formato: Jornada do Herói simplificada)
   - Personagem: Fundador
   - Problema: Dores que viu/experimentou
   - Busca: Como encontrou a solução
   - Transformação: Nascimento da empresa
   - Lição: Propósito consolidado

2. **História do Cliente Tipo** (formato: Antes/Depois)
   - Situação inicial: Cliente com problema X
   - Busca por soluções: Tentativas frustradas
   - Encontro: Como conheceu a empresa
   - Transformação: Resultados obtidos
   - Nova realidade: Vida depois da solução

3. **História de Valores em Ação** (formato: Prova real)
   - Situação: Momento de teste de valores
   - Dilema: Escolha difícil
   - Decisão: Como os valores guiaram
   - Resultado: Consequência positiva

### ETAPA 6: Construção do Brand Book (Dia 4-6)

```bash
# Comando de montagem do Brand Book
EXECUTAR: montar_brand_book \
  --essencia=[essencia_rascunho.md] \
  --personalidade=[personalidade_marca.md] \
  --narrativas=[narrativas_fundamentais.md] \
  --template=[brandbook_template.md] \
  --saida=[BRANDBOOK_[CLIENTE].md]
```

**Estrutura do Brand Book:**

```
📘 BRAND BOOK - [NOME DA EMPRESA]
Documento de Identidade Narrativa

═══════════════════════════════════════════════════════

📍 SEÇÃO 1: QUEM SOMOS

1.1 Propósito
    "[Frase do propósito]"
    
1.2 Visão
    "[Frase da visão]"
    
1.3 Missão
    "[Frase da missão]"
    
1.4 Valores
    → Valor 1: [Nome]
      Definição: [O que significa]
      Em ação: [Como se manifesta no dia a dia]
      
    → Valor 2: [Nome]
      ...

═══════════════════════════════════════════════════════

🎭 SEÇÃO 2: COMO SOMOS

2.1 Personalidade da Marca
    Arquétipo: [Nome]
    Descrição: [Resumo da personalidade]
    
2.2 Dimensões de Tom
    [Gráfico de posicionamento]
    
2.3 Voz da Marca
    Fala assim:
    → [Exemplo 1]
    → [Exemplo 2]
    → [Exemplo 3]
    
    NUNCA fala assim:
    → [Exemplo 1]
    → [Exemplo 2]
    → [Exemplo 3]

═══════════════════════════════════════════════════════

📖 SEÇÃO 3: NOSSAS HISTÓRIAS

3.1 Nossa Origem
    [História estruturada]
    → Versão completa: [2-3 parágrafos]
    → Versão resumida: [1 parágrafo]
    → Elevator pitch: [2-3 frases]
    
3.2 A Jornada do Nosso Cliente
    [História estruturada]
    
3.3 Nossos Valores em Ação
    [História estruturada]

═══════════════════════════════════════════════════════

🎯 SEÇÃO 4: POSICIONAMENTO

4.1 Promessa de Marca
    "[Frase da promessa]"
    
4.2 Proposta de Valor
    "[Frase da proposta]"
    
4.3 Diferencial Competitivo
    [Descrição do diferencial]
    
4.4 Território de Marca
    [Onde a marca atua e domina]

═══════════════════════════════════════════════════════

🛠️ SEÇÃO 5: APLICAÇÕES

5.1 Mensagens-Chave por Contexto
    │ Contexto           │ Mensagem Principal      │
    ├────────────────────┼─────────────────────────┤
    │ Instagram Bio      │                         │
    │ Pitch de vendas    │                         │
    │ Página Sobre       │                         │
    │ Email de boas-vindas│                        │
    │ Anúncio pago       │                         │

5.2 Glossário da Marca
    Termos que usamos:
    → [Termo]: [Significado]
    
    Termos que evitamos:
    → [Termo]: [Motivo]

5.3 Perguntas Frequentes da Marca
    → Como explicar o que fazemos em 30 segundos?
    → Como responder "por que vocês?"?
    → Como falar sobre preço?
    → Como pedir indicação?

═══════════════════════════════════════════════════════

📎 APÊNDICE

A. Referências Visuais
B. Exemplos de Aplicação em Conteúdo
C. Checklist de Uso do Brand Book
```

### ETAPA 7: Revisão e Refinamento (Dia 6)

```bash
# Comando de revisão
EXECUTAR: revisar_brand_book \
  --arquivo=[BRANDBOOK_[CLIENTE].md] \
  --checklist=[critérios_qualidade_brandbook.md]
```

**Checklist de revisão interna:**
- [ ] Essência está alinhada com o discurso do fundador
- [ ] Personalidade é distintiva e memorável
- [ ] Narrativas são autênticas e verificáveis
- [ ] Linguagem é consistente em toda a marca
- [ ] Documento é aplicável no dia a dia

### ETAPA 8: Entrega e Apresentação (Dia 7)

```bash
# Comando de entrega
EXECUTAR: entregar_fase02 \
  --brandbook=[BRANDBOOK_[CLIENTE].md] \
  --cliente=[EMAIL] \
  --reuniao=[AGENDAR_CALL]
```

---

## ✅ CHECKLIST DE ENTREGÁVEIS

### 📘 Documento Principal
- [ ] **Brand Book** completo (PDF e MD)
- [ ] **Resumo Executivo** (1 página)
- [ ] **One-pager da Marca** (página única resumo)

### 📦 Materiais de Suporte
- [ ] Gravações das aulas organizadas
- [ ] Banco de Narrativas documentado
- [ ] Análise de personalidade

### 📚 Guias Complementares
- [ ] **Guia de Tom de Voz** (cartilha rápida)
- [ ] **Templates de Mensagens** (exemplos prontos)
- [ ] **Checklist de Aplicação** (como usar o Brand Book)

### 🎯 Extras Opcionais
- [ ] Vídeo de apresentação do Brand Book
- [ ] WallPaper/PDF da Essência para impressão
- [ ] Apresentação em slides do conteúdo

---

## ⚡ COMANDO DE EXECUÇÃO (TEMPLATE)

```bash
# EXECUÇÃO COMPLETA DA FASE 02
EXECUTAR: protocolo_fase02_completo \
  --cliente="[NOME_DO_CLIENTE]" \
  --pasta_projeto="[CAMINHO_DA_PASTA]" \
  --aulas="[URL_AULA4],[URL_AULA5],[URL_AULA6]" \
  --fase01="[CAMINHO_FASE01]" \
  --depoimentos="[LINKS_DEPOIMENTOS]" \
  --saida="[CAMINHO_ENTREGA]"

# EXECUÇÃO POR ETAPAS
EXECUTAR: protocolo_fase02_etapa --etapa=[1-8] --config=[arquivo_config.yaml]

# ATUALIZAÇÃO DE SEÇÃO ESPECÍFICA
EXECUTAR: atualizar_brand_book \
  --secao=[essencia/personalidade/narrativas] \
  --dados=[novos_dados.md]
```

---

## 🎯 CRITÉRIOS DE QUALIDADE

O Brand Book será considerado completo quando:

### ✅ Autenticidade
- [ ] Reflete a voz REAL do fundador (não inventada)
- [ ] Narrativas são baseadas em fatos verificáveis
- [ ] Valores são demonstráveis na prática
- [ ] Diferencial é real e sustentável

### ✅ Clareza
- [ ] Essência pode ser explicada em 30 segundos
- [ ] Personalidade é diferenciada da concorrência
- [ ] Tom de voz tem exemplos claros de uso
- [ ] Narrativas têm versões de diferentes tamanhos

### ✅ Aplicabilidade
- [ ] Contém exemplos práticos para cada seção
- [ ] Inclui templates de mensagens prontas
- [ ] Tem versão resumida para referência rápida
- [ ] É útil para quem cria conteúdo (interno ou externo)

### ✅ Consistência
- [ ] Todos os elementos se reforçam mutuamente
- [ ] Não há contradições entre propósito e prática
- [ ] Tom de voz é coerente com personalidade
- [ ] Posicionamento é defendido pelas narrativas

---

## 💬 TEMPLATE DE COMUNICAÇÃO COM CLIENTE

### 📧 Email de Abertura - Solicitação de Aulas

```
Assunto: [Acelerador de Marca] Fase 2 - Vamos construir sua 
Identidade Narrativa 🎨

Olá, [NOME_CLIENTE]!

Parabéns pela conclusão da Fase 1! Agora vamos para a construção 
da sua identidade de marca.

A Fase 2 é sobre transformar suas histórias e valores em um 
BRAND BOOK completo - o documento que vai guiar toda a sua 
comunicação.

📹 AULAS PARA GRAVAR:

AULA 04 - ESSÊNCIA DA MARCA (15 min)
→ Por que sua empresa existe além do dinheiro?
→ Onde você quer estar em 5-10 anos?
→ Quais são seus valores NÃO NEGOCIÁVEIS?

AULA 05 - VOZ E TOM (15 min)
→ Se sua marca fosse uma pessoa, quem seria?
→ Como ela fala? Dê exemplos reais!
→ Como ela NUNCA falaria?

AULA 06 - NARRATIVAS FUNDAMENTAIS (20 min)
→ Conte a história de como tudo começou
→ Compartilhe uma transformação de cliente
→ Fale sobre um momento que testou seus valores

📎 MATERIAIS COMPLEMENTARES:
- Envie 5 depoimentos de clientes (vídeo é melhor!)
- Compartilhe 3 cases de sucesso detalhados
- Liste 3 marcas que você admira e por quê
- Liste 3 marcas que você NÃO quer ser e por quê

⏰ PRAZO: 72 horas

Qualquer dúvida, estamos aqui!

Abraço,
[SEU_NOME]
```

### 📧 Email de Entrega do Brand Book

```
Assunto: [Acelerador de Marca] Seu Brand Book está pronto! 📘

Olá, [NOME_CLIENTE]!

Chegou o grande momento! 🎉

Seu BRAND BOOK está finalizado - este documento vai transformar 
como você se comunica e se posiciona no mercado.

📎 ENTREGÁVEIS:
✓ Brand Book Completo (PDF + editável)
✓ One-pager da Marca (resumo visual)
✓ Guia de Tom de Voz (cartilha rápida)
✓ Templates de Mensagens (prontos para usar)

🎯 O QUE VOCÊ TEM AGORA:

→ Propósito claro: "[INSERIR PROPÓSITO]"

→ Personalidade definida: Sua marca tem personalidade de 
   [ARQUÉTIPO], com tom [CARACTERÍSTICAS]

→ Narrativas prontas: 3 histórias fundamentais estruturadas 
   para usar em conteúdo

→ Posicionamento único: "[INSERIR POSICIONAMENTO]"

→ Voz consistente: Você sabe EXATAMENTE como sua marca fala 
   (e como não fala)

📅 PRÓXIMA ETAPA:
A Fase 3 (Estratégia Operacional) começa em [DATA]. Vamos 
transformar esse Brand Book em um sistema de conteúdo completo!

🤝 REUNIÃO DE APRESENTAÇÃO:
Agende aqui: [LINK_CALENDLY]
Vamos apresentar o Brand Book e tirar todas as dúvidas.

Esse documento é seu norte. Use-o sempre!

Abraço,
[SEU_NOME]
Equipe Acelerador de Marca
```

---

## 📊 MÉTRICAS DE ACOMPANHAMENTO

| Métrica | Valor |
|---------|-------|
| Data de início | |
| Data de conclusão | |
| Total de horas investidas | |
| Narrativas extraídas | |
| Versões do Brand Book | |
| Satisfação do cliente (1-5) | |
| Marca de referência mais citada | |
| Observações | |

---

**Protocolo desenvolvido para o Programa Acelerador de Audiência**
