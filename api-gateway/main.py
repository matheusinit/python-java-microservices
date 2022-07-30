from zeep import Client
from flask import Flask, jsonify, request


app = Flask(__name__)

client = Client('http://127.0.0.1:5000/biblioteca?wsdl')


@app.get('/book')
def get_all_biblioteca_service():
    livros: list = client.service.listarLivros()

    return jsonify(livros)


@app.post('/book')
def adicionar_biblioteca_service():
    livro_nome = request.json['nome']

    client.service.adicionarLivro(
        livro_nome
    )

    return request.data


@app.put('/book')
def atualizar_biblioteca_service():
    bookToUpdate = request.json['to_update']
    update = request.json['update']

    livro = client.service.atualizarLivro(bookToUpdate, update)

    return jsonify({'nome': livro})
