# Lista de afazeres
Meu primeiro projeto utilizando Framework Django com linguagem Python, realizado durante uma trilha de aprendizagem.

O projeto é uma lista de tarefas, onde o usuário pode cadastrar uma nova tarefa, alterá-la, excluí-la e concluí-la. As tarefas são organizadas de acordo com a data de vencimento mais próxima.

A aplicação é local, utiliza Django para desenvolvimento web, HTML e Bootstrp para criação do layout da página. Para o banco de dados foi utilizado Sqlite3 local.

Comandos Básicos:
```
cria o ambiente virtual: python -m venv .venv

altera a privacidade do código: Set-Executionpolicy -Scope Process -ExecutionPolicy ByPass

ativa o ambiente virtual: .\.venv\Scripts\activate

cria a estrutura básica do projeto: django-admin startproject setup .

executa o ambiente web Django: python manage.py runserver

crie o aplicativo: python manage.py startapp all

migração sqlite: migração python manager.py
```
