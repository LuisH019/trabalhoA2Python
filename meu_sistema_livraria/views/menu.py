import os
import time
from controller.gerenciadorLivros import GerenciadorLivros
from util.inputs import Inputs


class Menu:
    def __init__(self):
        self.gerLivros = GerenciadorLivros()
        self.inpt = Inputs()

    def exibirMenu(self):
        op = -1

        while op != 0:
            os.system('cls')
            print("===== MENU PRINCIPAL =====")

            # self.gerLivros.teste()
            
            print("Escolha uma opção: ")
            print("1. Adicionar Livro")
            print("2. Mostrar Todos os Livros")
            print("3. Buscar/Editar/Apagar Livro")
            print("4. Fazer Backup do Banco de Daddos")
            print("5. Exportar Dados para CSV")
            print("6. Importar Dados de CSV")
            print("0. Sair")

            op = self.inpt.input("Digite: ", 0, 6)

            os.system('cls')

            if op == 1:
                print("===== ADICIONAR LIVRO =====")

                titulo = input("Titulo: ")
                autor = input("Autor: ")
                anoPublicacao = int (self.inpt.input("Ano de Publicacao: ", 0, 3000))
                preco = self.inpt.input("Preço: ", 0, 99999999)

                self.gerLivros.criar(titulo.strip(), autor.strip(), anoPublicacao, preco)

            elif op == 2:
                print("===== LIVROS CADASTRADOS =====")
                self.gerLivros.mostrar()

            elif op == 3:
                print("=====  BUSCAR/EDITAR/APAGAR LIVRO =====")

                print("Deseja ver os livros cadastrados antes?")
                print("1. Sim")
                print("2. Não")
                
                op = self.inpt.input("Digite: ", 1, 2)
                os.system('cls')

                if op == 1:
                    print("===== LIVROS CADASTRADOS =====")
                    self.gerLivros.mostrar()
                    print("\n")

                print("Com qual atributo deseja pesquisar?")
                print("1. Titulo")
                print("2. Autor")

                op = self.inpt.input("Digite: ", 1, 2)

                texto = input ("Digite o texto que deseja pesquisar: ")
                os.system('cls')

                resultadoBusca = self.gerLivros.buscar(int(op) - 1, texto)

                if resultadoBusca != -1:
                    print("Escolha uma opção: ")
                    print("1. Editar o Preco do Livro")
                    print("2. Apagar Livro")
                    print("3. Voltar para o menu principal")

                    op2 = self.inpt.input("Digite: ", 1, 3)
                    os.system('cls')

                    if op2 == 1:
                        print("===== EDITAR PRECO DO LIVRO =====")

                        novo_preco = self.inpt.input("Preço: ", 0, 99999999)

                        self.gerLivros.editarPreco(resultadoBusca, novo_preco)

                    elif op2 == 2:
                        print("===== APAGAR LIVRO =====")
                        self.gerLivros.apagar(resultadoBusca)
            
            elif op == 4:
                self.gerLivros.backupSql()
            
            elif op == 5:
                self.gerLivros.exportarCsv()

            elif op == 6:
                self.gerLivros.importarCsv()

            elif op == 0:
                print("Saindo do programa...")
                break

            # else:
            #     print("ERRO: Valor inválido!")

            time.sleep(2)

