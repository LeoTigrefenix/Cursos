# LABORATÓRIO 406 LABBITS UFABC - PROFESSORA PATRÍCIA, JOEL , __
        Laboratório de simulação de energia elétrica, sistemas elétricos, altas potências, armazenamentos de energia e afins. 

## UFABC_404 - v01 Criando Enviroment 
* environment é importante, pois o python pode ter várias bibliotecas para baixar e uma pode não ser compatível com a outra. Isso, caso salvo na raiz do computador, vai causar problemas. Além disso, para versionamento de bibliotecas é bem mais útil termos ambientes separados. 
* COMO CRIAR: 
    ctrl + shift + p -> vai abrir a aba superior de busca do VSCode , ali procure pela opção de:
    Python: Select Interpreter 
    Create Virtual Environment 
    Selecione o tipo (Venv is perfect for straightforward, Python-only projects, while conda excels at managing complex dependencies across multiple languages.)
    Selecione o tipo de python que vai querer nesse ambiente 
    Enter e esperar para aparecer a pasta

* Como acessar. Precisamos fazer o nosso ambiente powershell (acessível via ctrl j), o famoso terminal, acessar esse ambiente e não o path raiz do computador. 
Sendo assim, acesse a pasta que foi criado do ambiente `cd .venv`-> depois `cd Scripts` -> depois `./Activate.ps1` e espere ele confirmar a troca de ambiente do powershell. 
Vai aparecer `(.venv)` no começo do path do seu terminal 

## Caso de problemas 

Permissões para execução de scripts no PowerShell:
Se você receber uma mensagem de erro relacionada à execução de scripts, como:

    Execution Policy Error: File C:\path\to\Activate.ps1 cannot be loaded because running scripts is disabled on this system.

Isso significa que a execução de scripts no PowerShell está desabilitada. Para resolver isso, você pode alterar a política de execução de scripts. 

* Passo 1: Verifique a política atual
No PowerShell, execute o seguinte comando para verificar a política de execução atual:

    `Get-ExecutionPolicy`

    Se o resultado for `Restricted`, significa que scripts estão bloqueados.

* Passo 2: Altere a política de execução para permitir scripts
Para permitir a execução de scripts locais, você pode alterar a política para RemoteSigned:

    `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` .

    O parâmetro -Scope CurrentUser altera a política apenas para o usuário atual, o que é uma prática recomendada.

* Passo 3: Confirme a alteração
Você será solicitado a confirmar. Digite Y (ou S, dependendo do idioma) e pressione Enter.

* Passo 4: Agora, tente ativar o ambiente novamente com: `.\Activate.ps1`

    Se tudo estiver correto, seu ambiente virtual deverá ser ativado!