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

    def criar(self, titulo:str, autor:str, anoPublicacao:int, preco:float):
        novoLivro = {
            'titulo':titulo,
            'autor':autor,
            'id':int(len(self.livrosDf)),
            'anoPublicacao':anoPublicacao,
            'preco':preco
        }

        self.livrosDf = self.livrosDf._append(novoLivro, ignore_index = True)

        self.livrosDf = self.livrosDf.reset_index(drop=True)

    def buscar(self, titulo:str):
        return self.livrosDf[(self.livrosDf['titulo'] == titulo)]

    def mostrar(self):
        print(self.livrosDf)

