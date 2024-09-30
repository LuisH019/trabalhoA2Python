import pandas as pd
from livro import Livro

class GerenciarLivros:
    def __init__(self):
        self.livrosDf = pd.DataFrame({
            'titulo':[],
            'autor':[],
            'id':[],
            'anoPublicacao':[],
            'preco':[]
        })

        self.autoIncrement = 0

    def criar(self, titulo:str, autor:str, anoPublicacao:int, preco:float):
        novoLivro = {
            'titulo':titulo,
            'autor':autor,
            'id':self.autoIncrement,
            'anoPublicacao':anoPublicacao,
            'preco':preco
        }

        self.livrosDf = self.livrosDf._append(novoLivro, ignore_index = True)
        self.livrosDf = self.livrosDf.reset_index(drop=True)

        print("Livro criado com sucesso!")

        self.autoIncrement += 1

    def buscar(self, op: int, valor: str):
        variaveis = ['titulo', 'autor']

        if valor in self.livrosDf[variaveis[op]].values:
            resultado = self.livrosDf[(self.livrosDf[variaveis[op]] == valor)]
            
            print("Livro encontrado com sucesso!")
            print (resultado)

            return  resultado['id']
        else:
            print ("ERRO: Livro não encontrado!")

            return None
    
    # def buscarAutor(self, autor:str):
    #     return self.livrosDf[(self.livrosDf['autor'] == autor)]

    def apagar (self, idBusca: int):
        self.livrosDf.drop(idBusca)

        print("Livro apagado com sucesso!")

    def editarPreco(self, idBusca: int, novo_preco: float):
        self.livrosDf.loc[self.livrosDf['id'] == idBusca, 'preco'] = novo_preco
            
        print(f"Preço do livro atualizado para R$ {novo_preco:.2f}!")

    def mostrar(self):
        print(self.livrosDf)

