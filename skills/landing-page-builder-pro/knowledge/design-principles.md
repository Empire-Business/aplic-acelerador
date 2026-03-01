# Knowledge: Princípios de Design de Alta Conversão

Compilação de princípios comprovados para landing pages que convertem.

---

## 1. HIERARQUIA VISUAL

### Princípio
O olho segue uma ordem natural. Use tamanho, cor e posição para guiar.

### Aplicação
```
ORDEM DE IMPORTÂNCIA:
1. Headline (maior, mais contrastante)
2. Subheadline (menor, menos contraste)
3. CTA (cor de destaque)
4. Conteúdo de suporte
5. Elementos secundários
```

### Checklist
- [ ] Headline é o elemento mais visível
- [ ] CTA se destaca do resto
- [ ] Cores secundárias não competem com CTA
- [ ] Tamanho segue hierarquia de importância

---

## 2. REGRA DO CONTRASTE

### Princípio
Elementos que se destacam são notados. Elementos iguais são ignorados.

### Aplicação
```css
/* CTA deve contrastar com fundo */
.cta {
  background: #ff6b35;  /* Cor vibrante */
  color: #ffffff;
}

/* Fundo mais neutro */
body {
  background: #0a0a0a;  /* Escuro neutro */
}
```

### Checklist
- [ ] CTA tem cor diferente do resto
- [ ] Headline contrasta com fundo
- [ ] Elementos importantes se destacam

---

## 3. LEI DE FITTS

### Princípio
O tempo para atingir um alvo depende do tamanho e distância.

### Aplicação
```
MAIORES botões = MAIS cliques
MENOS distância = MAIS cliques
```

### Tamanhos Recomendados
- Botão CTA desktop: mínimo 44x44px (ideal 200x60px)
- Botão CTA mobile: mínimo 48x48px
- Área clicável: expanda além do texto

### Checklist
- [ ] CTAs são grandes o suficiente
- [ ] CTAs estão próximos do conteúdo relevante
- [ ] Área clicável é generosa

---

## 4. EFEITO VON RESTORFF

### Princípio
Itens únicos são mais lembrados.

### Aplicação
```
Faça o CTA ser o ÚNICO elemento com aquela cor.
Faça a headline ser o ÚNICO texto naquele tamanho.
```

### Checklist
- [ ] Apenas CTAs usam a cor de destaque
- [ ] Apenas a headline é tão grande
- [ ] Elemento principal é único na página

---

## 5. GESTALT - PROXIMIDADE

### Princípio
Elementos próximos são percebidos como grupo.

### Aplicação
```
[Benefício] [Descrição do benefício]  ← Agrupados
                    ↑ Espaço maior
[Benefício] [Descrição do benefício]  ← Próximo grupo
```

### Checklist
- [ ] Títulos estão próximos de seus conteúdos
- [ ] CTAs estão próximos de elementos relevantes
- [ ] Grupos visuais são claros

---

## 6. GESTALT - SIMILARIDADE

### Princípio
Elementos similares são percebidos como relacionados.

### Aplicação
```css
/* Todos os botões com mesmo estilo */
.btn-primary { }
.btn-secondary { }

/* Todos os títulos com mesmo estilo */
h2 { }
```

### Checklist
- [ ] Todos os CTAs têm mesmo estilo
- [ ] Todos os títulos de seção têm mesmo estilo
- [ ] Consistência visual é mantida

---

## 7. CARGA COGNITIVA

### Princípio
Quanto mais informações, maior o esforço para processar.

### Aplicação
```
REDUZA:
- Quantidade de texto
- Opções de navegação
- Cores diferentes
- Fontes diferentes

MÁXIMO: 2-3 fontes, 3-4 cores, 1 caminho de ação
```

### Checklist
- [ ] Máximo 2 famílias de fonte
- [ ] Máximo 4 cores na paleta
- [ ] Texto é escaneável
- [ ] Um CTA principal por seção

---

## 8. HICK'S LAW

### Princípio
Mais opções = mais tempo para decidir = menos conversão.

### Aplicação
```
RUIM:
[Comprar] [Saiba mais] [Comparar] [Favoritar]

BOM:
[COMPRAR AGORA]
```

### Checklist
- [ ] Uma ação principal por vez
- [ ] Navegação mínima ou ausente
- [ ] Opções de escolha são limitadas

---

## 9. PADRÃO-Z / PADRÃO-F

### Princípio
O olho segue padrões previsíveis de leitura.

### Padrão-F (texto denso)
```
┌─────────────────────┐
│ ►─────────────      │  1. Topo esquerdo
│ ►─────────          │  2. Horizontal
│   │                 │  3. Vertical
│   │    ►──────      │  4. Segunda horizontal
│   │                 │
└─────────────────────┘
```

### Padrão-Z (páginas simples)
```
┌─────────────────────┐
│ ►───────────────►   │  1→2 Horizontal
│                     │
│         ▼           │  3 Diagonal
│                     │
│   ◄───────────────► │  4→5 Horizontal final
└─────────────────────┘
```

### Aplicação
- Coloque elementos mais importantes no caminho do olho
- CTA final da linha de visão

### Checklist
- [ ] Elementos importantes seguem o padrão
- [ ] CTA está no caminho natural do olho
- [ ] Hierarquia respeita o fluxo de leitura

---

## 10. ESCASSEZ VISUAL

### Princípio
Elementos raros chamam mais atenção.

### Aplicação
```
USE COM MODERAÇÃO:
- Cor vermelha/laranja (urgência)
- Animações
- Badges/etiquetas
- Contadores

EFEITO: Se usado demais, perde o poder.
```

### Checklist
- [ ] Cor de urgência usada apenas em urgência real
- [ ] Animações são poucas e com propósito
- [ ] Badges são usados estrategicamente

---

## 11. ANSIEDADE DO FORMULÁRIO

### Princípio
Cada campo adicional reduz conversão.

### Dados
- Cada campo adicional: -10% a -20% de conversão
- 3 campos é o ideal para lead magnets
- 5+ campos precisa de justificativa forte

### Aplicação
```
LEAD MAGNET: Nome + Email (2)
WEBINAR: Nome + Email + Telefone (3)
HIGH TICKET: Nome + Email + Telefone + Perguntas (5-7)
```

### Checklist
- [ ] Apenas campos necessários
- [ ] Labels claros
- [ ] Placeholder de exemplo

---

## 12. PROVA SOCIAL VISUAL

### Princípio
Pessoas confiam em outras pessoas.

### Formatos de alta conversão
1. **Depoimentos com foto** (+30% confiança)
2. **Depoimentos em vídeo** (+50% confiança)
3. **Logos de clientes** (+credibilidade)
4. **Números específicos** (+especificidade)

### Checklist
- [ ] Depoimentos têm foto/nome/cargo
- [ ] Resultados são específicos (não vagos)
- [ ] Prova aparece cedo na página

---

## 13. TESTE DOS 5 SEGUNDOS

### Princípio
Visitantes decidem em 5 segundos se continuam ou saem.

### Perguntas do Teste
1. O que esta página oferece?
2. Para quem é?
3. O que eu ganho?
4. O que eu preciso fazer?

### Checklist
- [ ] Headline responde "o que"
- [ ] Subheadline responde "para quem"
- [ ] Benefícios respondem "o que ganho"
- [ ] CTA responde "o que fazer"

---

## 14. VELOCIDADE DE CARREGAMENTO

### Princípio
Cada segundo adicional = -7% conversão.

### Metas
- First Contentful Paint: < 1.5s
- Largest Contentful Paint: < 2.5s
- Time to Interactive: < 3.5s

### Otimizações
- [ ] Imagens comprimidas (WebP)
- [ ] Fontes com display:swap
- [ ] JavaScript mínimo e defer
- [ ] CSS crítico inline

---

## 15. RESPONSIVIDADE

### Princípio
60%+ do tráfego é mobile.

### Mobile-First
```css
/* Base = Mobile */
.cta {
  width: 100%;
  padding: 1rem;
}

/* Desktop = Enhancement */
@media (min-width: 768px) {
  .cta {
    width: auto;
    padding: 1.25rem 2.5rem;
  }
}
```

### Checklist
- [ ] Testado em diferentes tamanhos
- [ ] CTAs são touch-friendly (48px+)
- [ ] Texto é legível sem zoom
- [ ] Formulários funcionam em mobile

---

## RESUMO DOS PRINCÍPIOS

| # | Princípio | Ação Principal |
|---|-----------|----------------|
| 1 | Hierarquia Visual | Guie o olhar |
| 2 | Contraste | Destaque o importante |
| 3 | Fitts | Facilite o clique |
| 4 | Von Restorff | Seja único |
| 5 | Proximidade | Agrupe relacionados |
| 6 | Similaridade | Seja consistente |
| 7 | Carga Cognitiva | Simplifique |
| 8 | Hick's Law | Menos opções |
| 9 | Padrões Z/F | Siga o fluxo |
| 10 | Escassez Visual | Use com moderação |
| 11 | Ansiedade do Form | Menos campos |
| 12 | Prova Social | Mostre pessoas |
| 13 | 5 Segundos | Seja claro |
| 14 | Velocidade | Seja rápido |
| 15 | Responsividade | Funcione em mobile |

---

*"Good design is obvious. Great design is transparent."* — Joe Sparano
