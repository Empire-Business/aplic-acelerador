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
