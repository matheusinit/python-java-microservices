from flask import Flask, jsonify, request
import requests

BASE_URL = "http://localhost:5001"

alugueis = []

app = Flask(__name__)


def create_aluguel(cliente: str, livro: str):
    return {'cliente': cliente, 'livro': livro}


def livro_exists(livro: str):
    livros: list = requests.get(f"{BASE_URL}/book").json()
    print(livros)

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


@ app.post('/rent')
def post_aluguel_de_livros():
    livro = request.json['livro']
    cliente = request.json['nome']

    # If livro is rented

    if livro_exists(livro) and aluguel_size_existent(cliente) < 2:
        aluguel = create_aluguel(cliente, livro)

        alugueis.append(aluguel)

        alugueis_ordenados = sorted(alugueis)

        return alugueis_ordenados

    return {'mensagem': 'Livro não existe'}


if __name__ == '__main__':
    app.run(port=5002)
