# PROTOCOLO DE ENTREGA - FASE 04: ACOMPANHAMENTO

> **Programa:** Acelerador de Audiência  
> **Fase:** 04 - Acompanhamento: Time faz junto, roteiros prontos  
> **Versão:** 1.0  
> **Última atualização:** Fevereiro/2026

---

## 📋 OBJETIVO DO PROTOCOLO

Este protocolo estabelece o processo operacional para execução da **Fase 4 - Acompanhamento** do programa Acelerador de Audiência, garantindo que o cliente aproveite o máximo do acompanhamento hands-on do time para colocar a estratégia em prática.

**Objetivo principal:** Acompanhar o cliente na execução prática do sistema de conteúdo, criando roteiros juntos, revisando entregas e garantindo que a transição para autonomia seja suave.

---

## ✅ CHECKLIST DE INSUMOS NECESSÁRIOS

### 🎥 Gravações de Aulas para Extração
- [ ] **Aula 11 - Conteúdo Bruto da Semana 1** (60-90 minutos)
  - Gravação livre sobre os temas da semana
  - Conversa natural, sem roteiro rígido
  - Conhecimento sendo compartilhado organicamente
- [ ] **Aula 12 - Conteúdo Bruto da Semana 2** (60-90 minutos)
  - Continuação do fluxo de conteúdo
- [ ] **Aula 13 - Conteúdo Bruto da Semana 3** (60-90 minutos)
  - Última aula do período de acompanhamento

### 📁 Documentação de Entrada
- [ ] Linha Editorial completa (Fase 03)
- [ ] Mapa de Produção (Fase 03)
- [ ] Mapa de Distribuição (Fase 03)
- [ ] Brand Book (Fase 02)
- [ ] Calendário editorial da semana (definido com cliente)

### 🔧 Acessos e Permissões
- [ ] Acesso à pasta de conteúdo em produção
- [ ] Acesso ao canal de comunicação direta
- [ ] Permissão para postar em nome do cliente (se aplicável)
- [ ] Acesso às métricas dos posts

### 📋 Materiais de Apoio
- [ ] Brief da semana (temas definidos)
- [ ] Briefing de produto/serviço (se houver lançamento)
- [ ] Referências visuais aprovadas
- [ ] Banco de imagens do cliente

---

## 🔄 PASSO A PASSO DA EXECUÇÃO

### SEMANA 1 - Integração e Primeira Produção

#### DIA 1: Kickoff e Briefing

```bash
# Comando de início da semana
EXECUTAR: iniciar_semana_acompanhamento \
  --semana=1 \
  --cliente=[NOME_CLIENTE] \
  --brief=[brief_semana.yaml] \
  --pasta=[CAMINHO_PASTA]
```

**Ações:**
1. Revisar brief da semana com cliente (call 30 min)
2. Confirmar temas e objetivos
3. Validar canais de prioridade
4. Alinhar expectativas de entrega
5. Criar estrutura de pastas:
   ```
   📁 [CLIENTE] - Fase 04/
   ├── 📁 Semana 01/
   │   ├── 📁 01 - Gravacao Bruta/
   │   ├── 📁 02 - Transcricoes/
   │   ├── 📁 03 - Extracao/
   │   ├── 📁 04 - Roteiros/
   │   ├── 📁 05 - Pecas Prontas/
   │   └── 📁 06 - Publicados/
   ├── 📁 Semana 02/
   └── 📁 Semana 03/
   ```

#### DIA 2: Recepção e Análise da Gravação

```bash
# Comando de análise de conteúdo bruto
EXECUTAR: analisar_gravacao \
  --video=[aula11.mp4] \
  --extrair=[ouro,narrativas,dados,quotes] \
  --saida=[analise_aula11.md]
```

**Ações:**
1. Receber gravação da aula
2. Assistir na íntegra (60-90 min)
3. Extrair e marcar momentos de "ouro":
   - 💎 Insights valiosos
   - 💎 Histórias envolventes
   - 💎 Dados e provas
   - 💎 Quotes memoráveis
   - 💎 Calls-to-action naturais
4. Criar índice de conteúdo por timestamp
5. Gerar transcrição completa (se possível)

#### DIA 3: Extração de Peças

```bash
# Comando de extração de conteúdo
EXECUTAR: extrair_pecas \
  --analise=[analise_aula11.md] \
  --quantidade=15 \
  --formatos=[reels,carrossel,stories,legenda] \
  --saida=[pecas_brutas.yaml]
```

**Estratégia de Extração:**
```
📦 EXTRAÇÃO SEMANA 1

Conteúdo Fonte: [X minutos de gravação]

PEÇAS LONGAS (5-10 min):
→ [ ] Vídeo YouTube: [Tema - usar bloco X ao Y]
→ [ ] Podcast: [Tema - usar bloco X ao Y]
→ [ ] IGTV/Vídeo longo: [Tema - usar bloco X ao Y]

PEÇAS MÉDIAS (1-3 min):
→ [ ] Reels 1: [Hook - timestamp X-Y]
→ [ ] Reels 2: [Hook - timestamp X-Y]
→ [ ] Reels 3: [Hook - timestamp X-Y]
→ [ ] Stories sequência: [Tema - timestamps]

PEÇAS CURTAS (15-60 seg):
→ [ ] Short 1: [Hook - timestamp X-Y]
→ [ ] Short 2: [Hook - timestamp X-Y]
→ [ ] Short 3: [Hook - timestamp X-Y]
→ [ ] Short 4: [Hook - timestamp X-Y]

TEXTO:
→ [ ] Carrossel 1: [Estrutura - usar parte X]
→ [ ] Carrossel 2: [Estrutura - usar parte Y]
→ [ ] Post texto: [Ângulo - usar citação Z]
→ [ ] Newsletter: [Resumo da aula]
```

#### DIA 4: Desenvolvimento de Roteiros

```bash
# Comando de criação de roteiros
EXECUTAR: criar_roteiros \
  --pecas=[pecas_brutas.yaml] \
  --brandbook=[brandbook.md] \
  --linha=[linha_editorial.md] \
  --saida=[roteiros_prontos/]
```

**Template de Roteiro:**
```markdown
# ROTEIRO: [Tipo] - [Tema]

📋 INFORMAÇÕES
- Tipo: [Reels/Carrossel/Stories/etc]
- Duração/Tamanho: [X segundos / X cards]
- Objetivo: [Engajamento/Venda/Autoridade]
- Canal: [Instagram/LinkedIn/etc]
- Timestamp origem: [XX:XX - XX:XX]

🎬 ESTRUTURA

[HOOK] (3 segundos)
"[Frase de atenção]"

[DESENVOLVIMENTO]
1. [Ponto 1 - timestamp XX:XX]
2. [Ponto 2 - timestamp XX:XX]
3. [Ponto 3 - timestamp XX:XX]

[CTA - Call to Action]
"[Ação que quer que o espectador tome]"

📝 LEGENDA COMPLETA
[Texto da legenda com tom da marca]

#️⃣ HASHTAGS
[Hashtags relevantes]

🎨 DIREÇÃO VISUAL
- [Descrição do que aparece em cada momento]
- [Referências de estilo]
- [Elementos gráficos necessários]
```

#### DIA 5: Produção e Entrega ao Cliente

```bash
# Comando de entrega semanal
EXECUTAR: entregar_semana \
  --semana=1 \
  --roteiros=[roteiros_prontos/] \
  --cliente=[EMAIL] \
  --template=[email_entrega_semana.md]
```

**Ações:**
1. Finalizar todos os roteiros
2. Criar pacote de entrega organizado
3. Enviar ao cliente com instruções claras
4. Agendar call de acompanhamento (30 min)

---

### SEMANA 2 - Consolidação

#### DIA 1-5: Repetir fluxo da Semana 1

```bash
EXECUTAR: ciclo_semana_acompanhamento --semana=2
```

**Foco adicional:**
- Identificar padrões do que funcionou na Semana 1
- Ajustar estratégia com base nos primeiros resultados
- Refinar processo de extração
- Aumentar complexidade gradualmente

---

### SEMANA 3 - Transição para Autonomia

#### DIA 1-4: Último Ciclo de Acompanhamento

```bash
EXECUTAR: ciclo_semana_acompanhamento --semana=3 --foco=transicao
```

**Ações adicionais de transição:**
1. Documentar aprendizados do cliente
2. Criar checklist de auto-extração
3. Treinar cliente no processo
4. Identificar pontos de dificuldade

#### DIA 5: Encerramento e Documentação

```bash
# Comando de fechamento da fase
EXECUTAR: encerrar_fase04 \
  --cliente=[NOME_CLIENTE] \
  --historico=[historico_3semanas.md] \
  --aprendizados=[aprendizados.yaml] \
  --saida=[relatorio_fase04.md]
```

**Entregáveis de encerramento:**
- Relatório de performance das 3 semanas
- Documento de aprendizados do cliente
- Checklist de extração para autonomia
- Template de roteiro personalizado

---

## ✅ CHECKLIST DE ENTREGÁVEIS SEMANAIS

### 📄 Por Semana (x3)
- [ ] **Análise da gravação** (documento)
- [ ] **Índice de conteúdo** (com timestamps)
- [ ] **Roteiros prontos** (15-20 peças)
- [ ] **Sugestões de legendas**
- [ ] **Direções visuais** (quando aplicável)

### 🎥 Peças Produzidas (exemplo por semana)
- [ ] 3-5 Reels/Vídeos curtos
- [ ] 2-3 Carrosséis
- [ ] 1-2 Posts de texto
- [ ] Sequência de Stories
- [ ] 1 Peça longa (YouTube/Podcast)

### 📊 Acompanhamento
- [ ] Call de briefing semanal
- [ ] Call de acompanhamento/feedback
- [ ] Registro de métricas (se disponível)
- [ ] Ajustes na estratégia

---

## ⚡ COMANDO DE EXECUÇÃO (TEMPLATE)

```bash
# EXECUÇÃO COMPLETA DA FASE 04 (3 semanas)
EXECUTAR: protocolo_fase04_completo \
  --cliente="[NOME_DO_CLIENTE]" \
  --pasta_projeto="[CAMINHO_DA_PASTA]" \
  --aulas="[URL_AULA11],[URL_AULA12],[URL_AULA13]" \
  --fase03="[CAMINHO_FASE03]" \
  --briefs="[BRIEF_S1,BRIEF_S2,BRIEF_S3]" \
  --saida="[CAMINHO_ENTREGA]"

# EXECUÇÃO SEMANAL INDIVIDUAL
EXECUTAR: semana_acompanhamento \
  --semana=[1|2|3] \
  --gravacao="[URL_VIDEO]" \
  --brief="[ARQUIVO_BRIEF]" \
  --config="[config.yaml]"

# EXTRAÇÃO DE PEÇAS ESPECÍFICA
EXECUTAR: extrair_pecas_fase04 \
  --video="[URL_VIDEO]" \
  --minutos=[90] \
  --meta_pecas=[15] \
  --canais="[instagram,linkedin,youtube]"
```

---

## 🎯 CRITÉRIOS DE QUALIDADE

### ✅ Qualidade das Extrações
- [ ] Peças extraídas mantêm a essência da fala do cliente
- [ ] Hooks são impactantes e alinhados com a Linha Editorial
- [ ] CTAs são claros e contextualizados
- [ ] Cada peça tem objetivo definido

### ✅ Alinhamento com Estratégia
- [ ] Conteúdo segue os pilares definidos na Linha Editorial
- [ ] Mix de formatos respeita o Mapa de Distribuição
- [ ] Tom de voz está consistente com Brand Book
- [ ] Peças cobrem diferentes etapas do funil

### ✅ Viabilidade de Produção
- [ ] Roteiros são claros para o cliente executar
- [ ] Timestamps de origem estão documentados
- [ ] Direções visuais são aplicáveis
- [ ] Peças respeitam capacidade de produção do cliente

### ✅ Resultados
- [ ] Cliente conseguiu publicar com consistência
- [ ] Engajamento foi satisfatório (vs. baseline)
- [ ] Cliente reporta confiança para continuar
- [ ] Processo de extração foi documentado para autonomia

---

## 💬 TEMPLATE DE COMUNICAÇÃO COM CLIENTE

### 📧 Email de Abertura - Início da Fase 4

```
Assunto: [Acelerador de Marca] Fase 4 - Agora é na prática! 🎬

Olá, [NOME_CLIENTE]!

Chegou a hora de colocar a mão na massa! 🙌

A Fase 4 é de ACOMPANHAMENTO PRÁTICO. Nosso time vai 
trabalhar junto com você nas próximas 3 semanas.

🎯 COMO FUNCIONA:

SEMANA 1:
→ Segunda: Call de briefing (30 min)
→ Terça a Quinta: Nós criamos os roteiros
→ Sexta: Você recebe tudo pronto + call de alinhamento

SEMANA 2:
→ Mesmo fluxo, refinando o processo

SEMANA 3:
→ Última semana de acompanhamento
→ Foco na transição para sua autonomia

📹 O QUE VOCÊ PRECISA FAZER:

GRAVAR 1 AULA POR SEMANA (60-90 min)
→ Fale livremente sobre os temas definidos
→ Sem roteiro rígido - seja natural
→ Compartilhe conhecimento, histórias, exemplos

Nós extraímos TUDO e transformamos em:
✓ Reels
✓ Carrosséis  
✓ Stories
✓ Posts
✓ Conteúdo para YouTube/Podcast

📅 PRIMEIRA CALL: [DATA/HORA]
Link: [LINK_ZOOM]

Bora produzir! 🚀

Abraço,
[SEU_NOME]
```

### 📧 Email de Entrega Semanal

```
Assunto: [Acelerador de Marca] Semana [X] - Seus roteiros 
estão prontos! ✍️

Olá, [NOME_CLIENTE]!

Sua produção da Semana [X] está pronta!

📊 RESUMO DA EXTRAÇÃO:

Da sua aula de [XX] minutos, extraímos:
→ [X] Reels
→ [X] Carrosséis
→ [X] Posts de texto
→ [X] Stories
→ [X] Peças longas

TOTAL: [XX] peças de conteúdo! 🎉

📎 ANEXOS:
✓ Roteiros completos
✓ Sugestões de legendas
✓ Direções visuais
✓ Índice de timestamps (se quiser regravar algo)

💡 DICAS DE PRODUÇÃO:
→ [Dica específica para essa semana]
→ [Observação sobre algum roteiro específico]

📅 CALL DE ACOMPANHAMENTO: [DATA/HORA]
Vamos conversar sobre:
1. Dúvidas nos roteiros
2. Ajustes necessários
3. Resultados da semana anterior (se houver)

Qualquer dúvida antes da call, é só chamar!

Abraço,
[SEU_NOME]
```

### 📧 Email de Encerramento da Fase 4

```
Assunto: [Acelerador de Marca] Fase 4 Concluída - Você está 
pronto! 🎓

Olá, [NOME_CLIENTE]!

3 semanas de acompanhamento prático finalizadas! 🎉

Você produziu conteúdo consistentemente e agora está 
pronto para voar solo!

📊 BALANÇO DA FASE 4:

Total de aulas gravadas: 3
Tempo total de gravação: [XX] minutos
Peças de conteúdo criadas: [XX]
Publicações realizadas: [XX]

🎯 APRENDIZADOS DO PERÍODO:

→ [Ponto forte identificado do cliente]
→ [Formato que mais funcionou]
→ [Tema que teve melhor engajamento]
→ [Área a desenvolver]

📎 MATERIAL DE TRANSIÇÃO:

Para sua autonomia, estamos entregando:
✓ Checklist de Extração (passo a passo)
✓ Template de Roteiro personalizado
✓ Relatório de Performance
✓ Recomendações para continuidade

📅 PRÓXIMA ETAPA:
A Fase 5 (Transição) começa em [DATA].
Você terá acesso à documentação completa e 
suporte pontual se necessário.

Você provou que consegue manter consistência!
Agora é continuar o ritmo. 💪

Parabéns por essa etapa!

Abraço,
[SEU_NOME]
Equipe Acelerador de Marca
```

---

## 📊 MÉTRICAS DE ACOMPANHAMENTO

| Métrica | Semana 1 | Semana 2 | Semana 3 | Meta |
|---------|----------|----------|----------|------|
| Peças produzidas | | | | 15-20 |
| Publicações realizadas | | | | 80%+ |
| Taxa de aprovação de roteiros | | | | 90%+ |
| Satisfação do cliente (1-5) | | | | 4+ |
| Aulas gravadas no prazo | | | | 100% |

---

**Protocolo desenvolvido para o Programa Acelerador de Audiência**
