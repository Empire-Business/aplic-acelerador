# Acelerador de Audiência — Landing Page

Landing page premium para o programa Acelerador de Audiência da Empire.

## Deploy no Vercel

1. Faça push deste repositório para o GitHub
2. Conecte o repositório ao Vercel
3. O deploy será automático

## Estrutura

```
├── index.html          # Página principal
├── form.html           # Página de formulário
├── vercel.json         # Configuração do Vercel
├── images/
│   ├── hero-bg.png     # Background do hero
│   ├── founders/       # Fotos dos fundadores
│   ├── logos/          # Logos da Empire
│   └── marcas/         # Logos das marcas parceiras
└── copy-acelerador-audiencia.md  # Copy original
```

## Rotas Automáticas no Vercel

O projeto usa uma regra de rewrite curinga no `vercel.json` que **automaticamente** mapeia qualquer arquivo `.html` para uma URL limpa (sem a extensão).

### Como funciona:
- Basta criar um novo arquivo `.html` na raiz do projeto
- Ele será automaticamente acessível pela URL sem extensão

### Exemplos:
| Arquivo | URL de acesso |
|---------|---------------|
| `index.html` | `/` |
| `form.html` | `/form` |
| `nova-pagina.html` | `/nova-pagina` |
| `obrigado.html` | `/obrigado` |

**Importante:** Pastas como `images/`, `evento/` e `Marcas/` são excluídas da regra para não interferir com os arquivos de imagem.

## Tecnologias

- HTML5 semântico
- Tailwind CSS (CDN)
- JavaScript vanilla
- Fontes: Cormorant Garamond + DM Sans

## Performance

- Imagens otimizadas
- Lazy loading implementado
- CSS crítico inline
- Animações com GPU acceleration

## Design System

### Paleta de Cores

| Token | Hex | Uso |
|-------|-----|-----|
| `empire-bg` | `#0a0a0b` | Background principal |
| `empire-surface` | `#111113` | Superfícies secundárias |
| `empire-card` | `#18181b` | Cards e painéis |
| `empire-border` | `#27272a` | Bordas e divisores |
| `empire-muted` | `#71717a` | Texto secundário |
| `empire-text` | `#fafafa` | Texto principal |
| `empire-gold` | `#c9a962` | Cor de destaque / identidade |
| `empire-goldLight` | `#e4d4a5` | Gold claro (gradientes) |
| `empire-goldDark` | `#9a7b3c` | Gold escuro |

### Tipografia

- **Display / Títulos:** Cormorant Garamond (serif) — elegância e autoridade
- **Corpo / UI:** DM Sans (sans-serif) — legibilidade e modernidade

### Botões

#### `.btn-premium` — CTA Principal (verde)
Botão de alta conversão usado nas chamadas para ação principais da `index.html`.
- **Background:** gradiente verde `#16a34a → #22c55e → #16a34a`
- **Cor do texto:** `#ffffff`
- **Sombra:** `rgba(34, 197, 94, 0.35)`
- **Hover:** eleva 2px + sombra expandida `rgba(34, 197, 94, 0.5)`
- **Racional:** verde chamativo cria contraste máximo contra o fundo escuro, sinalizando ação imediata ao usuário

#### `.btn-secondary` — CTA Secundário (gold outline)
- **Background:** transparente
- **Borda:** `1px solid #c9a962`
- **Cor do texto:** `#c9a962`

### Identidade Visual

A identidade é **dark luxury** — fundo quase preto, tipografia serifada elegante, detalhes em dourado. O verde nos botões CTA é uma escolha deliberada de **contraste de conversão**: cria tensão visual positiva contra o fundo escuro, direcionando o olhar do usuário para a ação desejada sem quebrar a sofisticação geral da página.

> **Regra:** Verde apenas em `.btn-premium` (CTAs de ação). Dourado para todos os outros elementos de destaque (badges, ícones, bordas, textos de ênfase).
