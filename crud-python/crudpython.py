import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'bdcrud',
)

cursor = conexao.cursor()

#CREATE 
comando = 'INSERT INTO miniaturas (modelo, cor) VALUES ("70 Chevelle SS", "azul")'
cursor.execute(comando)
conexao.commit()

#READ
comando = f'SELECT * FROM bdcrud.miniaturas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

#UPDATE
variavel_modelo = "70 Chevelle SS"
varival_nova_cor = "vermelho"
comando = f'UPDATE miniaturas SET cor = "{varival_nova_cor}" WHERE modelo = "{variavel_modelo}" '
cursor.execute(comando)
conexao.commit()

#DELETE
variavel_modelo = "70 Chevelle SS"
varival_nova_cor = "vermelho"
comando = f'DELETE from miniaturas WHERE modelo = "{variavel_modelo}" '
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()