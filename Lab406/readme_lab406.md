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
Sendo assim, acesse a pasta que foi criado do ambiente `cd .venv`-> depois `cd Scripts` -> depois `_/.Activate.ps1_` e espere ele confirmar a troca de ambiente do powershell. 
Vai aparecer `(.venv)` no começo do path do seu terminal 
