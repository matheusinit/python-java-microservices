import requests

BASE_URL = 'http://localhost:5001'


def novoLivro():
    nome = input('Digite o nome do livro: ')
    return nome


def main():
    print('### Biblioteca de Livros')
    while True:
        print('\nMENU:')
        print('1) Inserir Livro')
        print('2) Listar Livros')
        print('3) Atualiza Livro')
        print('0) Sair')
        op = input('> ')
        if op == '1':
            livro = novoLivro()
            requests.post(f"{BASE_URL}/book", json={'nome': livro})
        elif op == '2':
            livros = requests.get(f"{BASE_URL}/book").json()

            for livro in livros:
                print('Nome do livro:', livro['nome'])
        elif op == '3':
            livro_antigo = input('Nome do livro antigo: ')
            livro_novo = input('\nNome do livro novo: ')
            requests.put(
                f"{BASE_URL}/book", json={'to_update': livro_antigo,
                                          'update': livro_novo})
        elif op == '0':
            break
        else:
            print('Opcao invalida!')


if __name__ == '__main__':
    main()
