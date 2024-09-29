from gerenciarLivros import GerenciarLivros
def menu():
    gerLivros= GerenciarLivros()

    while True:
        print("\nMenu:")
        print("1. Adicionar Livro")
        print("2. Buscar Livro por Autor")
        print("3. Mostrar Todos os Livros")
        print("4. Modificar Preço de um Livro")
        print("5. Sair")

        op = input("Escolha uma opção: ")

        if op == '1':
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            anoPublicacao = int(input("Ano Publicacao: "))
            preco = float(input("Preço: "))
            gerLivros.criar(titulo, autor, anoPublicacao, preco)
            print("\nLivro adicionado com sucesso!")

        elif op == '2':
            autor = input("Autor: ")
            resposta = gerLivros.buscarAutor(autor)
            if not resposta.empty:
                print("\nResultado da busca por autor:")
                print(resposta)
            else:
                print("\nNenhum livro encontrado para este autor.")

        elif op == '3':
            print("Livros Cadastrados: ")
            gerLivros.mostrar()

        elif op == '4':
            titulo = input("Digite o título do livro para modificar o preço: ")
            novo_preco = float(input("Digite o novo preço: "))
            gerLivros.modificarPreco(titulo, novo_preco)

        elif op == '5':
            print("Saindo do programa...")
            break

