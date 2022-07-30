from zeep import Client
from flask import Flask, jsonify, request
import requests


ALUGUEL_MICROSERVICE = 'http://localhost:5002'

app = Flask(__name__)

client = Client('http://127.0.0.1:5000/biblioteca?wsdl')


@app.get('/book')
def get_all_biblioteca_service():
    list = []

    livros: list = client.service.listarLivros()

    for livro in livros:
        list.append({'nome': livro['nome']})

    return jsonify(list)


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


@app.get('/rent')
def get_rents():
    rents = requests.get(f'{ALUGUEL_MICROSERVICE}/rent').json()
    return jsonify(rents)


@app.post('/rent')
def post_rent():
    livro = request.json['nome']
    cliente = request.json['cliente']

    response = requests.post(f"{ALUGUEL_MICROSERVICE}/rent", json={
        'livro': livro,
        'nome': cliente}
    )

    return response.content


if __name__ == '__main__':
    app.run(port=5001)
