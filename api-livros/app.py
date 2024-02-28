from flask import Flask, jsonify, request 

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Harry Potter',
        'autor': 'J. K. Rowling'
    },
    {
        'id': 2,
        'titulo': 'Hamlet',
        'autor': 'William Shakespeare'
    },
    {
        'id': 3,
        'titulo': 'Dom Casmurro',
        'autor': 'Machado de Assis'
    }
]

#consultar todos os livros
@app.route('/livros', methods=['GET'])

def obter_livros():
    return jsonify(livros)


#consulta livro por id
@app.route('/livros/<int:id>', methods=["GET"])

def obter_livros_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#editar livro por id
@app.route('/livros/<int:id>', methods=['PUT'])

def editar_livros_id(id):
    request.get_json() #pega a informaçao do usuario para a api
    livro_alterado = request.get_json()

    #pega o livro do indice e altera os parametros desse livro 
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
#criar um novo livro
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

#excluir um livro
@app.route('/livros/<int:id>', methods=['DELETE'])

def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
    return jsonify(livros)

app.run(port=5000, host='localhost') 