import pandas as pd
from meu_sistema_livraria.util.arquivos import Arquivos

class GerenciadorLivros:
    def __init__(self):
        self.arq = Arquivos()

        self.autoIncrement = 0

        if self.arq.lerSql().empty:
            self.livrosDf = pd.DataFrame({
                'titulo':[],
                'autor':[],
                'id':[],
                'anoPublicacao':[],
                'preco':[]
            })

            
        else:
            self.livrosDf = self.arq.lerSql()

            self.autoIncrement = self.livrosDf.tail(1)['id'].tolist()[0] + 1

    # def teste(self):
    #     print (self.arq.teste())

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

        self.arq.escreverSql(self.livrosDf)
        
        self.autoIncrement += 1

        self.arq.backupSql()

    def mostrar(self):
        print(self.livrosDf)

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

    def apagar (self, idBusca: int):
        self.livrosDf = self.livrosDf.drop(idBusca)

        print("Livro apagado com sucesso!")

        self.arq.escreverSql(self.livrosDf)

        self.arq.backupSql()

    def editarPreco(self, idBusca: int, novo_preco: float):
        self.livrosDf.loc[idBusca, 'preco'] = novo_preco
            
        print(f"Preço do livro atualizado para R$ {novo_preco:.2f}!")

        self.arq.escreverSql(self.livrosDf)

        self.arq.backupSql()
    
    def backupSql(self):
        self.arq.backupSql()

        print("Backup feito com sucesso!")

    def exportarCsv(self):
        self.arq.exportarCsv(self.livrosDf)

        print("Exportacoes feita com sucesso!")

    def importarCsv(self):
        self.livrosDf = self.arq.importarCsv()

        self.arq.escreverSql(self.livrosDf)

        print("Importacao feita com sucesso!")