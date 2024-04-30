# Sistema de Registro de Miniaturas
Este projeto é um sistema de resgistro de miniaturas em Python e MySQL.

# Tecnologias utilizadas
- Python
- MySQL

# Bibliotecas utilizadas
- Tkinter
- MySQL Connector
- Pandas

# Como executar este projeto
- Clone o repositório
```
git clone git@github.com:mathslima/registro-minis.git
```
  
- Crie uma base de dados no MySQL chamada miniaturas com uma tabela chamada minis, conforme arquivo 
```
miniaturas.mini.sql
```

- Instale as dependências
```
pip install -r requirements.txt
```
  
- Altere os dados de usuário e senha na conexão do banco de dados na main.py
```
user = 'seu_usuario'
password = 'sua_senha'
```

#### -Extra
- Para carregar uma lista com diversos dados no banco, execute o script no arquivo 
```
load_database.py
```
                      
