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

    def buscarAutor(self, autor:str):
        return self.livrosDf[(self.livrosDf['autor'] == autor)]

    def modificarPreco(self, titulo: str, novo_preco: float):
        if titulo in self.livrosDf['titulo'].values:
            self.livrosDf.loc[self.livrosDf['titulo'] == titulo, 'preco'] = novo_preco
            print(f"Preço do livro '{titulo}' atualizado para R$ {novo_preco:.2f}.")
        else:
            print(f"Livro '{titulo}' não encontrado.")
    def mostrar(self):
        print(self.livrosDf)

