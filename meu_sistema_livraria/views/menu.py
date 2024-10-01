import os
import time
from meu_sistema_livraria.controller.gerenciadorLivros import GerenciadorLivros


class Menu:
    def __init__(self):
        self.gerLivros = GerenciadorLivros()

    def exibirMenu(self):
        op = -1

        while op != 0:
            os.system('cls')
            print("===== MENU PRINCIPAL =====")

            self.gerLivros.teste()
            
            print("Escolha uma opção: ")
            print("1. Adicionar Livro")
            print("2. Mostrar Todos os Livros")
            print("3. Buscar/Editar/Apagar Livro")
            print("4. Fazer Backup do Banco de Daddos")
            print("5. Exportar Dados para CSV")
            print("6. Importar Dados de CSV")
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

                print("Deseja ver os livros cadastrados antes?")
                print("1. Sim")
                print("2. Não")
                
                op = input("Digite: ")
                os.system('cls')

                if op == '1':
                    print("===== LIVROS CADASTRADOS =====")
                    self.gerLivros.mostrar()
                    print("\n")
                elif op != '1' and op != '2':
                    print("ERRO: Valor inválido!")
                    continue

                print("Com qual atributo deseja pesquisar?")
                print("1. Titulo")
                print("2. Autor")

                op = input("Digite: ")

                if op == '1' or op == '2':
                    texto = input ("Digite o texto que deseja pesquisar: ")
                    os.system('cls')

                    resultadoBusca = self.gerLivros.buscar(int(op) - 1, texto)

                    if resultadoBusca != -1:
                        print("Escolha uma opção: ")
                        print("1. Editar o Preco do Livro")
                        print("2. Apagar Livro")
                        print("3. Voltar para o menu principal")

                        op2 = input("Digite: ")
                        os.system('cls')

                        if op2 == '1':
                            print("===== EDITAR PRECO DO LIVRO =====")

                            novo_preco = float(input("Digite o novo preço: "))

                            self.gerLivros.editarPreco(resultadoBusca, novo_preco)

                        elif op2 == '2':
                            print("===== APAGAR LIVRO =====")
                            self.gerLivros.apagar(resultadoBusca)

                        elif op2 == '3':
                            None

                        else:
                            print("ERRO: Valor inválido!")
                else:
                    print("ERRO: Valor inválido!")
            
            elif op == '4':
                self.gerLivros.backupSql()
            
            elif op == '5':
                self.gerLivros.exportarCsv()

            elif op == '6':
                self.gerLivros.importarCsv()

            elif op == '0':
                print("Saindo do programa...")
                break
            
            else:
                print("ERRO: Valor inválido!")

            time.sleep(2)

