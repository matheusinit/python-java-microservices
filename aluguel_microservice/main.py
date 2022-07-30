from flask import Flask, jsonify, request
import requests

BASE_URL = "http://localhost:5001"

alugueis = []

app = Flask(__name__)


def create_aluguel(cliente: str, livro: str):
    return {'cliente': cliente, 'livro': livro}


def livro_was_rented(livro: str):
    filtered = list(filter(
        lambda aluguel: aluguel['livro'] == livro, alugueis))

    if len(filtered) > 0:
        return True

    return False


def livro_exists(livro: str):
    livros: list = requests.get(f"{BASE_URL}/book").json()

    try:
        livros.index({'nome': livro})
        return True
    except Exception:
        return False


def aluguel_size_existent(cliente: str):
    alugueis_existents = list(filter(
        lambda aluguel: aluguel['cliente'] == cliente, alugueis))

    return len(alugueis_existents)


@ app.get('/rent')
def get_aluguel_de_livros():
    return jsonify(alugueis)


@app.post('/rent')
def post_aluguel_de_livros():
    livro = request.json['livro']
    cliente = request.json['nome']

    if livro_was_rented(livro):
        return {'mensagem': 'Livro alugado'}

    if aluguel_size_existent(cliente) > 1:
        return {'mensagem': 'Número máximo de alugueis atingido'}

    if livro_exists(livro):
        aluguel = create_aluguel(cliente, livro)

        alugueis.append(aluguel)

        return aluguel

    return {'mensagem': 'Livro não existe'}


if __name__ == '__main__':
    app.run(port=5002)
