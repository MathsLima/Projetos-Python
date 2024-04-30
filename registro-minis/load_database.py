import pandas as pd
import mysql.connector

data = pd.read_excel('dados-minis.xlsx')
data

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'miniaturas',
)
cursor = conexao.cursor()

for index, row in data.iterrows():
    comando = f'INSERT INTO miniaturas (modelo, cor, marca, colecao) VALUES ("{row["modelo"]}", "{row["cor"]}", "{row["marca"]}", "{row["colecao"]}")' 
    cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()