import requests
import sys

BASE_URL = 'http://localhost:5001'


def novoLivro():
    nome = input('Digite o nome do livro: ')
    return nome


def main():
    print('### Biblioteca de Livros')

    while True:
        print('\nINÍCIO:')
        print('0) Para sair')
        print('1) Para ver o estoque da biblioteca')
        print('2) Para alugar livros')
        escolha = input('Escolha: ')

        if escolha == '1':
            while True:
                print('\nMENU:')
                print('1) Inserir Livro')
                print('2) Listar Livros')
                print('3) Atualiza Livro')
                print('0) Voltar para o início')
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
        elif escolha == '2':
            print('1) Ver livros alugados')
            print('2) Alugar livro')

            aluguel_escolha = input('Escolha:')

            print('\n')
            if aluguel_escolha == '1':
                alugueis = requests.get(f"{BASE_URL}/rent").json()

                for aluguel in alugueis:
                    print(f"Cliente: {aluguel['cliente']}")
                    print(f"Livro: {aluguel['livro']}\n")
            elif aluguel_escolha == '2':
                cliente = input('Seu nome: ')
                livro = input('Livro para alugar: ')

                requests.post(f"{BASE_URL}/rent",
                              json={'nome': livro, 'cliente': cliente})
        elif escolha == '0':
            sys.exit(0)
        else:
            print('Opção inválida')


if __name__ == '__main__':
    main()
