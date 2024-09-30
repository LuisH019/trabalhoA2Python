import pandas as pd
import os
from arquivos import Arquivos

class GerenciadorLivros:
    def __init__(self):
        self.arq = Arquivos()

        # if not os.path.getsize('livros.csv'):
        #     self.livrosDf = pd.DataFrame({
        #         'titulo':[],
        #         'autor':[],
        #         # 'id':[],
        #         'anoPublicacao':[],
        #         'preco':[]
        #     })
        # else:
        #     self.livrosDf = pd.read_csv('livros.csv')
        
        self.livrosDf = self.arq.lerSql()

        # self.autoIncrement = 0

    def criar(self, titulo:str, autor:str, anoPublicacao:int, preco:float):
        novoLivro = {
            'titulo':titulo,
            'autor':autor,
            # 'id':self.autoIncrement,
            'anoPublicacao':anoPublicacao,
            'preco':preco
        }

        self.livrosDf = self.livrosDf._append(novoLivro, ignore_index = True)
        self.livrosDf = self.livrosDf.reset_index(drop=True)

        print("Livro criado com sucesso!")

        # self.livrosDf.to_csv('livros.csv', index=False)
        self.ar
        # self.autoIncrement += 1

    def buscar(self, op: int, texto: str):
        variaveis = ['titulo', 'autor']

        if texto in self.livrosDf[variaveis[op]].values:
            resultado = self.livrosDf[(self.livrosDf[variaveis[op]] == texto)]
            
            print("Livro encontrado com sucesso!")
            print (resultado)

            return resultado.index.to_list()[0]
        else:
            print ("ERRO: Livro não encontrado!")

            return -1
    
    # def buscarAutor(self, autor:str):
    #     return self.livrosDf[(self.livrosDf['autor'] == autor)]

    def apagar (self, idBusca: int):
        self.livrosDf = self.livrosDf.drop(idBusca)

        print("Livro apagado com sucesso!")

        self.livrosDf.to_csv('livros.csv', index=False)

    def editarPreco(self, idBusca: int, novo_preco: float):
        self.livrosDf.loc[idBusca, 'preco'] = novo_preco
            
        print(f"Preço do livro atualizado para R$ {novo_preco:.2f}!")

        self.livrosDf.to_csv('livros.csv', index=False)

    def mostrar(self):
        print(self.livrosDf)

