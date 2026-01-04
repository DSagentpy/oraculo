# 📤 Instruções para Publicar no GitHub

O repositório Git local já está configurado e o commit inicial foi feito! 

Agora você precisa criar o repositório no GitHub e fazer o push. Siga os passos abaixo:

## Opção 1: Via Interface Web do GitHub (Recomendado)

1. **Crie o repositório no GitHub:**
   - Acesse https://github.com/new
   - Nome do repositório: `oraculo` (ou outro nome de sua preferência)
   - Deixe como **público** ou **privado** (sua escolha)
   - **NÃO** marque "Initialize this repository with a README" (já temos um)
   - Clique em "Create repository"

2. **Conecte o repositório local ao GitHub:**
   Execute os seguintes comandos no PowerShell (substitua `SEU_USUARIO` pelo seu username do GitHub):

```powershell
cd "C:\Users\W-10\OneDrive\PROJETO PYTHON\oraculo"
git remote add origin https://github.com/SEU_USUARIO/oraculo.git
git branch -M main
git push -u origin main
```

## Opção 2: Via GitHub CLI (se instalar depois)

Se você instalar o GitHub CLI (`gh`), pode executar:

```powershell
gh repo create oraculo --public --source=. --remote=origin --push
```

## Verificação

Após o push, você pode verificar se tudo funcionou acessando:
`https://github.com/SEU_USUARIO/oraculo`

---

**Nota:** Os arquivos `teste.py` e `opcao.py` foram ignorados conforme solicitado e não serão enviados ao GitHub.



