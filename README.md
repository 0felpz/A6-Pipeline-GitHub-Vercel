# Atividade A6 - Pipeline completo com GitHub Actions e Vercel

Projeto simples em HTML. O workflow testa a página e, se estiver tudo certo, faz o deploy de produção na Vercel.

## Como entregar

1. Crie um repositório público ou privado no GitHub e coloque nele os arquivos desta pasta, inclusive `.github/workflows/pipeline.yml`.
2. Crie um projeto na Vercel vinculado a esse repositório ou importe o projeto usando a Vercel CLI. Confirme que a pasta publicada é `public`.
3. Obtenha o token da Vercel e os IDs da organização/equipe e do projeto (os IDs aparecem em `.vercel/project.json` depois de `vercel link`).
4. No GitHub, abra **Settings > Secrets and variables > Actions > New repository secret** e cadastre `VERCEL_TOKEN`, `VERCEL_ORG_ID` e `VERCEL_PROJECT_ID`.
5. No terminal dentro da pasta, rode:

   ```bash
   git init
   git branch -M main
   git add .
   git commit -m "Atividade A6 - pipeline GitHub Actions"
   git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   git push -u origin main
   ```

   Se o repositório remoto já contiver commits, clone-o antes e copie os arquivos para não provocar divergência de histórico.
6. Abra a aba **Actions** no GitHub, clique no workflow executado e confirme que **Validar projeto** e **Publicar na Vercel** concluíram com sucesso.
7. Tire uma captura de tela real da página com os jobs verdes. Esse print é a evidência solicitada pelo professor.

**Atenção:** apenas `git commit` local não aciona o GitHub Actions hospedado. É necessário enviar com `git push` ou disparar manualmente o workflow após o envio.

**Importante:** os segredos não devem ser colocados no código nem enviados para o GitHub. A pasta `.vercel/` também está ignorada.
