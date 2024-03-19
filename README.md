## Como Rodar

Com o node instalado, rode o código:

```bash
npm run dev
```

Abra [http://localhost:3000](http://localhost:3000) no browser para ver o site

Modificamos as páginas que estão na pasta pages, como o  `pages/index.jsx`. A página se atualiza automático com as mudanças. Faça com que o VSCode salve automático o código, daí você pode deixar o o localhost aberto, fazer modificações e ele vai se atualizar

## O que é cada pasta:

- Pages: A pasta que o Next automaticamente interpreta como onde estão todas as páginas, fazendo com que o usuário possa acessá-las pela url
- Public: Onde ficam todos arquivos que ficam acessíveis ao longo do site, como imagens, ícones e dados, além das configurações para adição do site no Google no fim do projeto.
- Src: Onde fica a maior parte do código do site de fato, com os componentes, seus estilos, etc.
- api: aqui é onde toda a mágica dos acontece. Nessa pasta ficam todos os códigos python e o arquivo api.py será responsável por fazer a comunicação entre o back-end (parte que busca, limpa, trata e organiza os dados) e o front-end (parte que o usuário vê do site), através de um endpoint.

#### Dentro da pasta src
- Components: Onde colocaremos os componentes que utilizaremos nas páginas. Os componentes são a principal característica do React, eles permitem reutilizão de código por todo o site de forma fácil e eficiente
- Styles: Onde teremos os css's para os componentes em específico, para cada página e um css global.

##

This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.js`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.
