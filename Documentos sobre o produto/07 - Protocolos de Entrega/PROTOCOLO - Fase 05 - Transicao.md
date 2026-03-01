# PROTOCOLO DE ENTREGA - FASE 05: TRANSIÇÃO

> **Programa:** Acelerador de Audiência  
> **Fase:** 05 - Transição: Cliente assume autonomia  
> **Versão:** 1.0  
> **Última atualização:** Fevereiro/2026

---

## 📋 OBJETIVO DO PROTOCOLO

Este protocolo estabelece o processo operacional para execução da **Fase 5 - Transição** do programa Acelerador de Audiência, garantindo que o cliente receba toda a documentação necessária para manter o sistema de conteúdo de forma autônoma e sustentável.

**Objetivo principal:** Empoderar o cliente com ferramentas, processos documentados e acesso a recursos para continuar executando a estratégia sem dependência do time do programa.

---

## ✅ CHECKLIST DE INSUMOS NECESSÁRIOS

### 📁 Documentação Acumulada (Todas as Fases Anteriores)
- [ ] **Fase 01:** Mapa de Riscos e Oportunidades
- [ ] **Fase 02:** Brand Book completo
- [ ] **Fase 03:** 
  - Linha Editorial
  - Mapa de Produção
  - Mapa de Distribuição
- [ ] **Fase 04:** 
  - Roteiros criados
  - Análises de performance
  - Aprendizados documentados

### 🎥 Material de Referência
- [ ] Gravações de todas as aulas do cliente
- [ ] Biblioteca de conteúdo produzido
- [ ] Templates e materiais editáveis
- [ ] Banco de ideias e referências

### 📊 Dados de Performance
- [ ] Métricas das primeiras publicações
- [ ] Análise do que funcionou melhor
- [ ] Insights de engajamento
- [ ] Padrões de melhor horário

### 🔧 Recursos e Acessos
- [ ] Lista de ferramentas utilizadas
- [ ] Acessos a contas criadas
- [ ] Fornecedores recomendados
- [ ] Links de recursos educativos

---

## 🔄 PASSO A PASSO DA EXECUÇÃO

### ETAPA 1: Consolidação da Documentação (Dia 1-2)

```bash
# Comando de consolidação
EXECUTAR: consolidar_documentacao \
  --cliente=[NOME_CLIENTE] \
  --fases="[F01,F02,F03,F04]" \
  --pasta=[CAMINHO_PASTA] \
  --saida=[DOCUMENTACAO_COMPLETA/]
```

**Ações:**
1. Reunir todos os documentos das fases anteriores
2. Criar estrutura de pasta final:
   ```
   📁 [CLIENTE] - Fase 05 - Entrega Final/
   ├── 📁 01 - Documentacao Estrategica/
   │   ├── 01 - Mapa Riscos e Oportunidades.pdf
   │   ├── 02 - Brand Book.pdf
   │   ├── 03 - Linha Editorial.pdf
   │   ├── 04 - Mapa de Producao.pdf
   │   └── 05 - Mapa de Distribuicao.pdf
   ├── 📁 02 - Ferramentas Operacionais/
   │   ├── Templates/
   │   ├── Checklists/
   │   └── Scripts/
   ├── 📁 03 - Biblioteca de Conteudo/
   │   ├── Roteiros/
   │   ├── Pecas Publicadas/
   │   └── Banco de Ideias/
   ├── 📁 04 - Guias e Tutoriais/
   │   ├── Guia de Autonomia.pdf
   │   ├── Tutoriais de Ferramentas/
   │   └── FAQ.pdf
   ├── 📁 05 - Recursos e Referencias/
   │   ├── Fornecedores Recomendados.pdf
   │   ├── Ferramentas Uteis.pdf
   │   └── Biblioteca de Conhecimento.pdf
   └── 📄 RESUMO EXECUTIVO - Plano de Continuidade.pdf
   ```
3. Verificar integridade de todos os arquivos
4. Organizar por ordem de uso/prioridade

### ETAPA 2: Criação do Guia de Autonomia (Dia 2-3)

```bash
# Comando de criação do guia
EXECUTAR: criar_guia_autonomia \
  --documentacao=[DOCUMENTACAO_COMPLETA/] \
  --fase04=[aprendizados_fase04.md] \
  --template=[guia_autonomia_template.md] \
  --saida=[GUIA_AUTONOMIA_[CLIENTE].md]
```

**Estrutura do Guia de Autonomia:**

```
📘 GUIA DE AUTONOMIA - [NOME DA EMPRESA]

Seu manual para manter o sistema de conteúdo funcionando

═══════════════════════════════════════════════════════════

🚀 CAPÍTULO 1: SEU SISTEMA EM RESUMO

1.1 O Que Você Construiu
    → [Resumo do que foi desenvolvido nas 4 fases]
    → [Principais conquistas]
    → [Ponto de partida atual]

1.2 Seu Ritmo Ideal (Baseado na Fase 4)
    → Dias/tempo de gravação: [Recomendação]
    → Dias de edição: [Recomendação]
    → Dias de publicação: [Recomendação]
    → Estoque mínimo a manter: [X peças]

1.3 Seus Pontos Fortes Identificados
    → [O que o cliente faz naturalmente bem]
    → [Formatos que mais funcionam para ele]
    → [Temas que ressoam mais]

1.4 Áreas de Atenção
    → [Onde precisa de mais cuidado]
    → [Gatilhos de procrastinação]
    → [Soluções predefinidas]

═══════════════════════════════════════════════════════════

⚙️ CAPÍTULO 2: SEU FLUXO DE TRABALHO

2.1 Ritual Semanal Recomendado
    
    SEGUNDA - Planning (30 min)
    → Revisar calendário
    → Definir temas da semana
    → Preparar ambiente de gravação
    
    TERÇA - Produção (60-90 min)
    → Gravar conteúdo bruto
    → Seguir checklist de gravação
    → Salvar e organizar arquivos
    
    QUARTA - Extração (60 min)
    → Revisar gravação
    → Marcar momentos de ouro
    → Definir peças a criar
    
    QUINTA - Criação (90-120 min)
    → Editar vídeos
    → Criar designs
    → Escrever legendas
    
    SEXTA - Agendamento (30 min)
    → Programar publicações
    → Revisar programação
    → Preparar stories diários

2.2 Checklist de Gravação
    → [ ] Ambiente preparado
    → [ ] Equipamento testado
    → [ ] Tema definido
    → [ ] Exemplos na ponta da língua
    → [ ] CTA mentalizado

2.3 Processo de Extração (Passo a Passo)
    
    PASSO 1: Assistir a gravação completa
    - Usar player com controles de velocidade
    - Anotar timestamps de momentos bons
    
    PASSO 2: Classificar conteúdo
    - Marcar: Insights / Histórias / Dados / Quotes
    - Avaliar: Potencial viral / Educativo / Venda
    
    PASSO 3: Definir peças
    - Selecionar 15-20 trechos
    - Definir formato de cada um
    - Priorizar por objetivo da semana
    
    PASSO 4: Criar roteiros
    - Hook: Primeiros 3 segundos
    - Corpo: Desenvolvimento
    - CTA: Chamada para ação

═══════════════════════════════════════════════════════════

🎯 CAPÍTULO 3: COMO CRIAR ROTEIROS

3.1 Estruturas Que Funcionam Para Você
    
    [Baseado no que funcionou na Fase 4]
    
    Estrutura 1: [Nome] - [Quando usar]
    1. [Elemento]
    2. [Elemento]
    3. [Elemento]
    
    Estrutura 2: [Nome] - [Quando usar]
    ...

3.2 Formulas de Hook Que Ressoam
    → "Você sabia que..."
    → "O erro que..."
    → "Em [ano] eu descobri..."
    → "Pare de fazer [X]..."
    → [Adicionar hooks que funcionaram bem]

3.3 CTAs Naturais Para Seu Negócio
    → "Comenta [X] se..."
    → "Salva para consultar depois"
    → "Link na bio para..."
    → "Me conta: [pergunta]"

3.4 Template de Roteiro Rápido
    ```
    TIPO: [Reels/Carrossel/etc]
    TEMA: [Do que é o conteúdo]
    OBJETIVO: [Engajamento/Venda/etc]
    
    HOOK:
    
    CORPO:
    1.
    2.
    3.
    
    CTA:
    
    LEGENDA:
    
    HASHTAGS:
    ```

═══════════════════════════════════════════════════════════

📅 CAPÍTULO 4: CALENDÁRIO E PLANEJAMENTO

4.1 Como Planejar Seu Mês
    
    SEMANA 1: [Tipo de conteúdo foco]
    - Objetivo:
    - Temas sugeridos:
    - Formato prioritário:
    
    SEMANA 2: [Tipo de conteúdo foco]
    ...

4.2 Sazonalidades Para Ficar de Olho
    → [Datas importantes do setor]
    → [Datas comemorativas relevantes]
    → [Momentos de venda programados]

4.3 Quando Postar (Baseado em Seus Dados)
    │ Canal      │ Melhores Dias  │ Melhores Horários  │
    ├────────────┼────────────────┼────────────────────┤
    │ Instagram  │                │                    │
    │ LinkedIn   │                │                    │
    │ YouTube    │                │                    │
    │ Email      │                │                    │

═══════════════════════════════════════════════════════════

🛠️ CAPÍTULO 5: FERRAMENTAS E RECURSOS

5.1 Sua Stack de Ferramentas
    
    GRAVAÇÃO:
    → Ferramenta: [Nome]
    → Como usar: [Link tutorial]
    → Dicas: [Específicas do cliente]
    
    EDIÇÃO DE VÍDEO:
    → Ferramenta: [Nome]
    → Como usar: [Link tutorial]
    → Dicas: [Específicas do cliente]
    
    DESIGN:
    → Ferramenta: [Nome]
    → Templates: [Onde estão salvos]
    → Dicas: [Específicas do cliente]
    
    AGENDAMENTO:
    → Ferramenta: [Nome]
    → Como usar: [Link tutorial]
    
    ANÁLISE:
    → Ferramenta: [Nome]
    → O que medir: [Métricas prioritárias]

5.2 Fornecedores Recomendados
    → Edição de vídeo: [Contato/Plataforma]
    → Design: [Contato/Plataforma]
    → Copy: [Contato/Plataforma]
    → Produção de imagem: [Contato/Plataforma]

5.3 Banco de Recursos
    → Imagens gratuitas: [Sites]
    → Músicas livres: [Sites]
    → Fontes: [Links]
    → Ícones: [Sites]

═══════════════════════════════════════════════════════════

📊 CAPÍTULO 6: COMO MEDIR SEU PROGRESSO

6.1 Métricas Principais (Mensurar Mensalmente)
    
    CRESCIMENTO:
    → Seguidores: [Meta]
    → Alcance: [Meta]
    → Impressões: [Meta]
    
    ENGAJAMENTO:
    → Taxa de engajamento: [Meta]
    → Salvamentos: [Meta]
    → Compartilhamentos: [Meta]
    
    CONVERSÃO:
    → Cliques no link: [Meta]
    → Leads gerados: [Meta]
    → Vendas atribuídas: [Meta]

6.2 Ritual de Análise
    → Diário: [O que verificar]
    → Semanal: [O que verificar]
    → Mensal: [O que verificar]

6.3 Quando Pedir Ajuda
    → Se publicação cair por 3 dias seguidos
    → Se engajamento cair 30% por 2 semanas
    → Se não conseguir manter ritmo
    → Se precisar de suporte técnico

═══════════════════════════════════════════════════════════

🆘 CAPÍTULO 7: RESOLUÇÃO DE PROBLEMAS

7.1 "Não sei o que gravar"
    → Consultar Banco de Ideias: [Link]
    → Usar prompts de emergência: [Lista]
    → Fazer Q&A com perguntas de seguidores

7.2 "Não tenho tempo"
    → Ativar modo "Mínimo viável": [Descrição]
    → Reduzir para 1 aula/semana
    → Focar em apenas 1 canal

7.3 "Engajamento caiu"
    → Checklist de diagnóstico: [Lista]
    → Ações de recuperação: [Lista]
    → Quando pivotar: [Critérios]

7.4 "Estou desmotivado"
    → Relembrar propósito: [Link Brand Book]
    → Ver resultados iniciais: [Prints conquistas]
    → Comunidade de apoio: [Links]

═══════════════════════════════════════════════════════════

📞 CAPÍTULO 8: CONTATOS E SUPORTE

8.1 Com Quem Falar
    → Suporte técnico: [Email/Contato]
    → Dúvidas estratégicas: [Email/Contato]
    → Comunidade de alunos: [Link]

8.2 Recursos Adicionais
    → Biblioteca de conhecimento: [Link]
    → Webinários mensais: [Link]
    → Material de atualização: [Link]
```

### ETAPA 3: Criação dos Templates e Checklists (Dia 3-4)

```bash
# Comando de criação de ferramentas
EXECUTAR: criar_ferramentas_autonomia \
  --templates="[lista_templates]" \
  --checklists="[lista_checklists]" \
  --saida=[FERRAMENTAS/]
```

**Ferramentas a criar:**

1. **Template de Roteiro Editável** (.docx ou Google Docs)
2. **Planilha de Calendário Editorial** (modelo mensal)
3. **Checklist de Pré-Gravação** (PDF/imprimível)
4. **Checklist de Pós-Produção** (PDF/imprimível)
5. **Planilha de Acompanhamento de Métricas** (mensal)
6. **Banco de Ideias** (planilha organizada)
7. **Template de Análise Mensal**

### ETAPA 4: Documentação de Recursos (Dia 4)

```bash
# Comando de documentação de recursos
EXECUTAR: documentar_recursos \
  --fornecedores=[lista_forncedores.yaml] \
  --ferramentas=[lista_ferramentas.yaml] \
  --tutoriais=[links_tutoriais.yaml] \
  --saida=[RECURSOS/]
```

**Documentos a criar:**
- [ ] **Fornecedores Recomendados** (com contatos e preços)
- [ ] **Ferramentas Úteis** (com guia de uso)
- [ ] **Biblioteca de Conhecimento** (links para aprofundamento)
- [ ] **FAQ do Programa** (dúvidas frequentes)

### ETAPA 5: Criação do Plano de Continuidade (Dia 4-5)

```bash
# Comando de criação do plano
EXECUTAR: criar_plano_continuidade \
  --documentacao=[DOCUMENTACAO_COMPLETA/] \
  --guia=[GUIA_AUTONOMIA.md] \
  --proximos_90dias=[plano_acao.yaml] \
  --saida=[PLANO_CONTINUIDADE_[CLIENTE].pdf]
```

**Estrutura do Plano de Continuidade:**
```
📋 PLANO DE CONTINUIDADE - [NOME DA EMPRESA]

Próximos 90 dias de execução autônoma

═══════════════════════════════════════════════════════════

🎯 OBJETIVOS DO TRIMESTRE

→ Objetivo 1: [Específico e mensurável]
→ Objetivo 2: [Específico e mensurável]
→ Objetivo 3: [Específico e mensurável]

Métricas a acompanhar:
│ Métrica      │ Atual │ Meta 30d │ Meta 60d │ Meta 90d │
├──────────────┼───────┼──────────┼──────────┼──────────┤
│              │       │          │          │          │
│              │       │          │          │          │

═══════════════════════════════════════════════════════════

📅 CRONOGRAMA DOS PRÓXIMOS 90 DIAS

MÊS 1 - Foco: [Consolidação/Expansão/etc]
Semana 1:
→ Tema: [Tema da semana]
→ Formato foco: [Formato]
→ Objetivo: [O que alcançar]

Semana 2:
...

MÊS 2 - Foco: [...]
...

MÊS 3 - Foco: [...]
...

═══════════════════════════════════════════════════════════

✅ CHECKPOINTS DE AVALIAÇÃO

Dia 30:
→ [O que avaliar]
→ [Ações se estiver abaixo da meta]
→ [Ações se estiver acima da meta]

Dia 60:
→ ...

Dia 90:
→ ...

═══════════════════════════════════════════════════════════

🎓 PRÓXIMOS PASSOS DE DESENVOLVIMENTO

Habilidades a desenvolver:
→ [Habilidade 1] - [Como desenvolver]
→ [Habilidade 2] - [Como desenvolver]

Expansão de canais:
→ [Canal atual] → [Canal novo] (quando: [critério])

Evolução do formato:
→ [Formato atual] → [Formato avançado] (quando: [critério])
```

### ETAPA 6: Call de Encerramento (Dia 5)

```bash
# Comando de encerramento
EXECUTAR: realizar_call_encerramento \
  --cliente=[NOME_CLIENTE] \
  --documentacao=[DOCUMENTACAO_COMPLETA/] \
  --plano=[PLANO_CONTINUIDADE.pdf] \
  --agenda=[agenda_call.md]
```

**Agenda da Call (60 min):**
1. **Apresentação da documentação** (20 min)
   - Tour pelos documentos
   - Explicação de como usar cada um
2. **Demonstração prática** (20 min)
   - Como usar o Guia de Autonomia
   - Como aplicar templates
3. **Dúvidas e ajustes** (15 min)
4. **Próximos passos** (5 min)

### ETAPA 7: Entrega Final (Dia 5-6)

```bash
# Comando de entrega final
EXECUTAR: entregar_fase05 \
  --pacote=[PACOTE_COMPLETO.zip] \
  --cliente=[EMAIL] \
  --acesso_permanente=[LINK_DRIVE] \
  --template=[email_entrega_final.md]
```

---

## ✅ CHECKLIST DE ENTREGÁVEIS

### 📘 Documentação Principal
- [ ] **Guia de Autonomia** completo (PDF e MD)
- [ ] **Plano de Continuidade** (PDF)
- [ ] **Resumo Executivo** (1 página)

### 🛠️ Ferramentas Operacionais
- [ ] **Template de Roteiro** (editável)
- [ ] **Planilha de Calendário Editorial** (modelo)
- [ ] **Checklist de Pré-Gravação** (PDF)
- [ ] **Checklist de Pós-Produção** (PDF)
- [ ] **Planilha de Métricas** (modelo)
- [ ] **Banco de Ideias** (planilha)

### 📦 Pacote de Documentação
- [ ] **Toda documentação das Fases 01-04** (organizada)
- [ ] **Templates de design** (arquivos editáveis)
- [ ] **Roteiros de referência** (exemplos do Fase 04)
- [ ] **Biblioteca de conteúdo** (produzido)

### 📚 Recursos e Referências
- [ ] **Fornecedores Recomendados** (lista)
- [ ] **Ferramentas Úteis** (guia)
- [ ] **Biblioteca de Conhecimento** (links)
- [ ] **FAQ** (documento)

### 🎯 Extras
- [ ] **Acesso permanente** (Google Drive/pasta compartilhada)
- [ ] **Gravação da call de encerramento**
- [ ] **Certificado de conclusão** (se aplicável)

---

## ⚡ COMANDO DE EXECUÇÃO (TEMPLATE)

```bash
# EXECUÇÃO COMPLETA DA FASE 05
EXECUTAR: protocolo_fase05_completo \
  --cliente="[NOME_DO_CLIENTE]" \
  --pasta_projeto="[CAMINHO_DA_PASTA]" \
  --fases_anteriores="[F01,F02,F03,F04]" \
  --plano_90dias="[plano_acao.yaml]" \
  --saida="[CAMINHO_ENTREGA]"

# EXECUÇÃO POR ETAPA
EXECUTAR: protocolo_fase05_etapa --etapa=[1-7] --config=[arquivo_config.yaml]

# CRIAÇÃO DE FERRAMENTA ESPECÍFICA
EXECUTAR: criar_ferramenta_autonomia \
  --tipo=[template/checklist/planilha] \
  --especificacao=[spec.md] \
  --saida=[arquivo_saida]
```

---

## 🎯 CRITÉRIOS DE QUALIDADE

### ✅ Completude
- [ ] Toda documentação das fases anteriores está incluída
- [ ] Guia de Autonomia cobre todas as necessidades operacionais
- [ ] Ferramentas estão prontas para uso imediato
- [ ] Cliente tem acesso a todos os recursos

### ✅ Clareza
- [ ] Documentos são autoexplicativos
- [ ] Processos estão descritos passo a passo
- [ ] Linguagem é acessível (nível do cliente)
- [ ] Templates são intuitivos

### ✅ Aplicabilidade
- [ ] Recomendações baseadas no perfil real do cliente
- [ ] Ritmos propostos são sustentáveis
- [ ] Ferramentas sugeridas são acessíveis
- [ ] Plano de 90 dias é realista

### ✅ Empoderamento
- [ ] Cliente demonstra confiança na call de encerramento
- [ ] Cliente sabe onde encontrar respostas
- [ ] Cliente tem plano para os próximos 90 dias
- [ ] Cliente sabe quando e como pedir ajuda

---

## 💬 TEMPLATE DE COMUNICAÇÃO COM CLIENTE

### 📧 Email de Abertura - Início da Fase 5

```
Assunto: [Acelerador de Marca] Fase 5 - Preparando sua 
autonomia! 🎓

Olá, [NOME_CLIENTE]!

Chegamos na Fase 5 - a última etapa do programa!

Nesta fase, vamos consolidar TUDO que construímos em 
um pacote completo para você voar solo.

🎯 O QUE VAMOS ENTREGAR:

→ Guia de Autonomia completo (seu manual de operação)
→ Todas as documentações organizadas
→ Templates e ferramentas para uso contínuo
→ Plano de Continuidade para os próximos 90 dias
→ Acesso permanente a toda documentação

📅 PROCESSO:

Dias 1-4: Nós preparamos toda a documentação
Dia 5: Call de encerramento (60 min)

Na call vamos:
✓ Apresentar todo o material
✓ Mostrar como usar cada ferramenta
✓ Tirar todas as dúvidas
✓ Definir seus próximos passos

📆 AGENDE SUA CALL DE ENCERRAMENTO:
Link: [LINK_CALENDLY]

Você está pronto para ser autônomo! 🚀

Abraço,
[SEU_NOME]
```

### 📧 Email de Entrega Final

```
Assunto: [Acelerador de Marca] Seu pacote de autonomia 
está pronto! 📦🎓

Olá, [NOME_CLIENTE]!

Parabéns! Você completou o Acelerador de Audiência! 🎉

Seu pacote completo de autonomia está pronto para download.

═══════════════════════════════════════════════════════════

📦 SEU PACOTE INCLUI:

📘 DOCUMENTAÇÃO ESTRATÉGICA
✓ Mapa de Riscos e Oportunidades
✓ Brand Book completo
✓ Linha Editorial
✓ Mapa de Produção
✓ Mapa de Distribuição

📕 GUIA DE AUTONOMIA
✓ Seu fluxo de trabalho personalizado
✓ Como criar roteiros sozinho
✓ Checklists de gravação e produção
✓ Como medir seus resultados
✓ Resolução de problemas comuns

🛠️ FERRAMENTAS OPERACIONAIS
✓ Template de Roteiro
✓ Planilha de Calendário Editorial
✓ Checklists (pré e pós-produção)
✓ Planilha de Métricas
✓ Banco de Ideias

📋 PLANO DE CONTINUIDADE
✓ Seus objetivos para os próximos 90 dias
✓ Cronograma sugerido
✓ Checkpoints de avaliação
✓ Próximos passos de desenvolvimento

📚 RECURSOS ADICIONAIS
✓ Fornecedores recomendados
✓ Ferramentas úteis
✓ Biblioteca de conhecimento
✓ FAQ completo

═══════════════════════════════════════════════════════════

📥 DOWNLOAD:
[PACOTE_COMPLETO.zip]

☁️ ACESSO PERMANENTE:
[LINK_DRIVE] (salve nos seus favoritos!)

📹 GRAVAÇÃO DA CALL:
[LINK_VIDEO] (disponível por 6 meses)

═══════════════════════════════════════════════════════════

🎯 PARA COMEÇAR:

1. Baixe e salve tudo em seu computador
2. Leia o Guia de Autonomia (prioridade #1)
3. Revise seu Plano de Continuidade
4. Comece a usar os templates já na próxima semana

═══════════════════════════════════════════════════════════

O QUE VOCÊ CONSTRUIU:

→ Uma marca com identidade clara e narrativa forte
→ Um sistema de conteúdo operacional e sustentável
→ Capacidade de transformar 1 hora em 50+ peças
→ Autonomia para manter consistência

Você está pronto! 🚀

Agora é manter o ritmo e escalar seus resultados.

═══════════════════════════════════════════════════════════

📞 SUPORTE PÓS-PROGRAMA:

→ Dúvidas técnicas: [EMAIL_SUPORTE]
→ Comunidade de alunos: [LINK_COMUNIDADE]
→ Webinários mensais: [LINK_WEBINAR]

═══════════════════════════════════════════════════════════

Foi um prazer fazer parte dessa jornada com você!

Sucesso sempre! 🌟

Abraço,
[SEU_NOME]
Equipe Acelerador de Marca
```

---

## 📊 MÉTRICAS DE ACOMPANHAMENTO

| Métrica | Resultado |
|---------|-----------|
| Data de início | |
| Data de conclusão | |
| Documentos entregues | |
| Ferramentas criadas | |
| Satisfação do cliente (1-5) | |
| Call de encerramento realizada | Sim / Não |
| Cliente reporta confiança para autonomia | Sim / Não |
| Observações | |

---

**Protocolo desenvolvido para o Programa Acelerador de Audiência**
