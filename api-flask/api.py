import pandas as pd
from flask import Flask, jsonify

#inicializando o app
app = Flask(__name__)


#constuçao da funcionalidade da api 

@app.route('/')

def quatidade_vendas():
    dados = pd.read_excel('Vendas.xlsx')
    total_vendas = dados['Quantidade'].sum()
    #retorno da resposta deve ser um dicionario
    resposta_api = {'total_vendas': int(total_vendas)}
    return jsonify(resposta_api)

#rodar a api
app.run()