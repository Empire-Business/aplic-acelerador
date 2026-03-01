# PROTOCOLO DE ENTREGA - FASE 01: DIAGNÓSTICO

> **Programa:** Acelerador de Audiência  
> **Fase:** 01 - Diagnóstico: Mapa de Riscos e Oportunidades  
> **Versão:** 1.0  
> **Última atualização:** Fevereiro/2026

---

## 📋 OBJETIVO DO PROTOCOLO

Este protocolo estabelece o processo operacional para execução da **Fase 1 - Diagnóstico** do programa Acelerador de Audiência, resultando na entrega do **Mapa de Riscos e Oportunidades** ao cliente.

**Objetivo principal:** Mapear a realidade atual do cliente, identificar gaps estratégicos, oportunidades de posicionamento e riscos que precisam ser mitigados antes da construção do Brand Book.

---

## ✅ CHECKLIST DE INSUMOS NECESSÁRIOS

Antes de iniciar a execução, certifique-se de que todos os insumos abaixo foram recebidos do cliente:

### 🎥 Gravações Obrigatórias
- [ ] **Aula 01 - Contexto do Negócio** (mínimo 15 minutos)
  - História da empresa
  - Produtos/serviços principais
  - Diferenciais competitivos
- [ ] **Aula 02 - Público-Alvo** (mínimo 15 minutos)
  - Quem é o cliente ideal
  - Dores e desejos do público
  - Objeções mais comuns
- [ ] **Aula 03 - Concorrência e Mercado** (mínimo 10 minutos)
  - Principais concorrentes
  - Posicionamento atual
  - Oportunidades identificadas

### 📁 Materiais Complementares
- [ ] Site atual do cliente (URL)
- [ ] Redes sociais ativas (links de acesso)
- [ ] Materiais de vendas existentes (PDFs, apresentações)
- [ ] Depoimentos de clientes (mínimo 3)
- [ ] Cases de sucesso documentados
- [ ] Pesquisas anteriores com clientes (se houver)

### 🔐 Acessos Necessários
- [ ] Acesso ao Google Analytics (se aplicável)
- [ ] Acesso ao Instagram Insights (screenshots ou acesso)
- [ ] Acesso ao LinkedIn Analytics (se aplicável)
- [ ] Acesso à pasta compartilhada do projeto

---

## 🔄 PASSO A PASSO DA EXECUÇÃO

### ETAPA 1: Coleta e Organização de Insumos (Dia 1)

```bash
# Comando de organização
EXECUTAR: organizar_insumos_fase01 --cliente=[NOME_CLIENTE] --pasta=[CAMINHO_PASTA]
```

**Ações:**
1. Criar estrutura de pastas na área de trabalho do projeto:
   ```
   📁 [CLIENTE] - Fase 01/
   ├── 📁 01 - Gravações/
   ├── 📁 02 - Materiais Existentes/
   ├── 📁 03 - Análises/
   └── 📁 04 - Entregáveis/
   ```
2. Baixar e salvar todas as gravações das aulas
3. Catalogar materiais recebidos
4. Solicitar insumos pendentes ao cliente (com prazo de 24h)

### ETAPA 2: Análise das Gravações (Dia 2-3)

```bash
# Comando de análise de conteúdo
EXECUTAR: analisar_gravacoes --fase=01 --extrair=[insights,narrativas,dados] --saida=[arquivo_analise.md]
```

**Ações:**
1. Assistir todas as aulas gravadas (total: ~40 minutos)
2. Extrair informações-chave por tópico:
   - ✏️ Tom de voz do empreendedor
   - ✏️ Termos repetidos (vocabulário próprio)
   - ✏️ Crenças e valores declarados
   - ✏️ Dores mencionadas
   - ✏️ Sonhos e aspirações
3. Criar resumo estruturado no arquivo `analise_aulas_fase01.md`

### ETAPA 3: Análise de Canais Existentes (Dia 3)

```bash
# Comando de análise digital
EXECUTAR: analisar_presenca_digital --urls=[SITE,INSTAGRAM,LINKEDIN] --saida=[analise_canais.md]
```

**Ações:**
1. **Site:**
   - Identificar proposta de valor atual
   - Mapear jornada do usuário
   - Listar pontos de atrito
   - Verificar SEO básico

2. **Instagram:**
   - Analisar últimos 30 posts
   - Mapear tipos de conteúdo (educativo/venda/engajamento)
   - Calcular taxa de engajamento média
   - Identificar posts com melhor performance

3. **LinkedIn (se aplicável):**
   - Analisar perfil da empresa
   - Mapear frequência de posts
   - Verificar consistência de mensagem

### ETAPA 4: Análise Competitiva (Dia 4)

```bash
# Comando de benchmark
EXECUTAR: analisar_concorrencia --concorrentes=[CONC_1,CONC_2,CONC_3] --dimensoes=[posicionamento,conteudo,engajamento]
```

**Ações:**
1. Selecionar 3 principais concorrentes mencionados
2. Analisar posicionamento de cada um
3. Mapear estratégia de conteúdo
4. Identificar gaps de mercado (oportunidades)
5. Documentar aprendizados aplicáveis

### ETAPA 5: Construção do Mapa (Dia 4-5)

```bash
# Comando de construção do entregável
EXECUTAR: gerar_mapa_riscos_oportunidades --analise=[arquivo_analise.md] --template=[mapa_fase01.md]
```

**Estrutura do Mapa:**
```
📊 MAPA DE RISCOS E OPORTUNIDADES
├── 🎯 RESUMO EXECUTIVO (1 página)
├── ⚠️ RISCOS IDENTIFICADOS
│   ├── Risco 1: [Descrição] | Severidade: [Alta/Média/Baixa] | Mitigação: [Ação]
│   ├── Risco 2: [Descrição] | Severidade: [Alta/Média/Baixa] | Mitigação: [Ação]
│   └── ...
├── 💎 OPORTUNIDADES MAPEADAS
│   ├── Oportunidade 1: [Descrição] | Potencial: [Alto/Médio/Baixo] | Aproveitamento: [Ação]
│   ├── Oportunidade 2: [Descrição] | Potencial: [Alto/Médio/Baixo] | Aproveitamento: [Ação]
│   └── ...
├── 📍 POSICIONAMENTO RECOMENDADO
│   ├── Posição atual vs. desejada
│   ├── Território de marca sugerido
│   └── Diferencial competitivo a explorar
└── 🚀 PRÓXIMOS PASSOS (para Fase 2)
```

### ETAPA 6: Revisão e Aprovação Interna (Dia 5)

```bash
# Comando de revisão
EXECUTAR: revisar_entregavel --arquivo=[mapa_fase01.md] --checklist=[critérios_qualidade.md]
```

**Ações:**
1. Revisar contra critérios de qualidade
2. Verificar consistência das informações
3. Validar recomendações estratégicas
4. Ajustar formatação e design

### ETAPA 7: Entrega ao Cliente (Dia 6)

```bash
# Comando de entrega
EXECUTAR: entregar_ao_cliente --arquivo=[mapa_fase01.md] --cliente=[EMAIL] --template=[email_entrega_fase01.md]
```

---

## ✅ CHECKLIST DE ENTREGÁVEIS

Ao final da execução, os seguintes entregáveis devem estar prontos:

### 📄 Documentos Principais
- [ ] **Mapa de Riscos e Oportunidades** (PDF e MD)
- [ ] **Resumo Executivo** (1 página)
- [ ] **Análise de Canais Digitais** (documento anexo)
- [ ] **Benchmark Competitivo** (tabela comparativa)

### 🎥 Materiais de Suporte
- [ ] Gravações das aulas organizadas
- [ ] Transcrições das aulas (se aplicável)
- [ ] Screenshots das análises

### 📋 Documentação Interna
- [ ] Análise completa das aulas
- [ ] Notas de estratégia para Fase 2
- [ ] Registro de decisões importantes

---

## ⚡ COMANDO DE EXECUÇÃO (TEMPLATE)

```bash
# EXECUÇÃO COMPLETA DA FASE 01
EXECUTAR: protocolo_fase01_completo \
  --cliente="[NOME_DO_CLIENTE]" \
  --pasta_projeto="[CAMINHO_DA_PASTA]" \
  --aulas="[URL_AULA1],[URL_AULA2],[URL_AULA3]" \
  --site="[URL_SITE]" \
  --instagram="[@HANDLE]" \
  --linkedin="[URL_LINKEDIN]" \
  --concorrentes="[@CONC1,@CONC2,@CONC3]" \
  --saida="[CAMINHO_ENTREGA]"

# OU EXECUÇÃO POR ETAPAS
EXECUTAR: protocolo_fase01_etapa --etapa=[1-7] --config=[arquivo_config.yaml]
```

---

## 🎯 CRITÉRIOS DE QUALIDADE

O Mapa de Riscos e Oportunidades será considerado completo quando:

### ✅ Cobertura de Conteúdo
- [ ] Mínimo 5 riscos identificados e categorizados por severidade
- [ ] Mínimo 5 oportunidades mapeadas com potencial avaliado
- [ ] Todas as aulas gravadas foram analisadas e referenciadas
- [ ] Análise de pelo menos 3 canais/concorrentes

### ✅ Clareza e Aplicabilidade
- [ ] Linguagem acessível (sem jargões desnecessários)
- [ ] Cada risco possui ação de mitigação sugerida
- [ ] Cada oportunidade possui plano de aproveitamento
- [ ] Recomendações são acionáveis e mensuráveis

### ✅ Profundidade Estratégica
- [ ] Identificação de padrões nas narrativas do cliente
- [ ] Análise cruzada entre discurso e prática observada
- [ ] Conexão clara entre diagnóstico e próximas fases
- [ ] Insights que só seriam possíveis com a análise profunda

### ✅ Formato e Apresentação
- [ ] Documento visualmente organizado
- [ ] Uso de elementos visuais (gráficos, tabelas, ícones)
- [ ] Versão PDF otimizada para apresentação
- [ ] Nomenclatura de arquivos padronizada

---

## 💬 TEMPLATE DE COMUNICAÇÃO COM CLIENTE

### 📧 Email de Abertura - Solicitação de Insumos

```
Assunto: [Acelerador de Marca] Fase 1 - Precisamos dos seus insumos 🎯

Olá, [NOME_CLIENTE]!

Tudo bem? Estamos animados para iniciar a Fase 1 do Acelerador de Marca 
e Conteúdo com você!

Para construirmos seu Mapa de Riscos e Oportunidades com qualidade, 
precisamos que você grave 3 aulas curtas:

📹 AULA 01 - CONTEXTO DO NEGÓCIO (15 min)
   → Conte a história da empresa, seus produtos/serviços e diferenciais

📹 AULA 02 - PÚBLICO-ALVO (15 min)
   → Quem é seu cliente ideal? Quais suas dores e desejos?

📹 AULA 03 - CONCORRÊNCIA E MERCADO (10 min)
   → Quem são seus principais concorrentes? Onde você vê oportunidades?

📎 MATERIAIS COMPLEMENTARES (enviar por email):
- Link do seu site
- Links das redes sociais ativas
- Materiais de vendas que já usa
- 3 depoimentos de clientes

⏰ PRAZO: 48 horas

Qualquer dúvida, estamos à disposição!

Abraço,
[SEU_NOME]
Equipe Acelerador de Marca
```

### 📧 Email de Entrega do Mapa

```
Assunto: [Acelerador de Marca] Fase 1 Concluída! 🎉

Olá, [NOME_CLIENTE]!

A Fase 1 do Acelerador de Audiência está pronta!

Analisamos todo o material enviado e construímos seu MAPA DE RISCOS E 
OPORTUNIDADES completo.

📎 ANEXOS:
✓ Mapa de Riscos e Oportunidades (PDF)
✓ Análise de Canais Digitais
✓ Benchmark Competitivo

🎯 PRINCIPAIS ACHADOS:
→ [INSIGHT 1 - ex: Identificamos uma oportunidade de posicionamento no 
   nicho X que seus concorrentes ainda não exploraram]

→ [INSIGHT 2 - ex: Seu Instagram tem potencial de crescimento X ao 
   explorar o formato Y]

→ [INSIGHT 3 - ex: O risco maior atual é Z, e recomendamos a mitigação 
   através de A, B e C]

📅 PRÓXIMA ETAPA:
A Fase 2 (Brand Book) começará em [DATA]. Você receberá as instruções 
em breve.

💬 FEEDBACK:
Após ler o material, me responda com:
1. O que fez mais sentido para você?
2. Alguma dúvida ou discordância?
3. O que te deixou mais animado?

Parabéns por essa primeira etapa concluída! 🚀

Abraço,
[SEU_NOME]
Equipe Acelerador de Marca
```

---

## 📊 MÉTRICAS DE ACOMPANHAMENTO

Registre os seguintes dados para cada execução:

| Métrica | Valor |
|---------|-------|
| Data de início | |
| Data de conclusão | |
| Total de horas investidas | |
| Insumos recebidos no prazo | Sim / Não |
| Revisões solicitadas | |
| Satisfação do cliente (1-5) | |
| Observações | |

---

**Protocolo desenvolvido para o Programa Acelerador de Audiência**
