import os
import time
from gerenciarLivros import GerenciarLivros


class Menu:
    def __init__(self):
        self.gerLivros = GerenciarLivros()

    def exibirMenu(self):
        op = -1

        while op != 0:
            os.system('cls')

            print("===== MENU PRINCIPAL =====")

            print("Escolha uma opção: ")
            print("1. Adicionar Livro")
            print("2. Mostrar Todos os Livros")
            print("3. Buscar/Editar/Apagar Livro")
            print("0. Sair")

            op = input("Digite: ")
            
            os.system('cls')

            if op == '1':
                print("===== ADICIONAR LIVRO =====")

                titulo = input("Titulo: ")
                autor = input("Autor: ")
                anoPublicacao = int(input("Ano de Publicacao: "))
                preco = float(input("Preço: "))

                self.gerLivros.criar(titulo, autor, anoPublicacao, preco)

            elif op == '2':
                print("===== LIVROS CADASTRADOS =====")
                self.gerLivros.mostrar()

            elif op == '3':
                print("=====  BUSCAR/EDITAR/APAGAR LIVRO =====")

                print("Deseja ver a lista de livros antes?")
                print("1. Sim")
                print("2. Não")
                
                op = input("Digite: ")
                
                os.system('cls')

                if op == '1':
                    print("===== LIVROS CADASTRADOS =====")
                    self.gerLivros.mostrar()
                    print("\n")

                print("Com qual atributo deseja pesquisar?")
                print("1. Titulo")
                print("2. Autor")

                op = input("Digite: ")

                valor = input ("Digite o valor que deseja pesquisar: ")

                resultadoBusca = self.gerLivros.buscar(int(op) - 1, valor)

                if resultadoBusca:
                    print("Escolha uma opção: ")
                    print("1. Editar o Preco do Livro")
                    print("2. Apagar Livro")
                    print("3. Voltar para o menu principal")

                    op2 = input("Digite: ")

                    if op2 == '1':
                        print("===== EDITAR PRECO DO LIVRO =====")

                        novo_preco = float(input("Digite o novo preço: "))

                        self.gerLivros.editarPreco(resultadoBusca.index, novo_preco)

                    elif op2 == '2':
                        print("===== APAGAR LIVRO =====")
                        self.gerLivros.apagar(resultadoBusca.index)

                    elif op2 == '3':
                        None

                    else:
                        print("ERRO: Valor inválido!")


            elif op == '0':
                print("Saindo do programa...")
                break
            
            else:
                print("ERRO: Valor inválido!")

            time.sleep(1)

