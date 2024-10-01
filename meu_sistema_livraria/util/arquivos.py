import pandas as pd
import os
import sqlite3
from datetime import datetime
from pathlib import Path
import shutil
import time

class Arquivos:
    def __init__(self):
        root = Path('meu_sistema_livraria')
        self.dbDir = (root/'data'/'livraria.db')
        self.bkpsDir = (root/'backups')
        self.csvDir = (root/'exports'/'livros_exportados.csv')

        self.sqlConn = sqlite3.connect(f"{self.dbDir}")
        self.cur = self.sqlConn.cursor()

    def teste(self):
        # for filename in os.listdir(self.bkpsDir):
        #     print (os.path.getctime(filename))
        # return None
        # files = sorted(os.listdir(self.bkpsDir), key=os.path.getctime)

        # print (oldest = files[0])
        # print (newest = files[-1])

        for f in os.listdir(self.bkpsDir):
            print (time.ctime(os.path.getmtime(f)))
        return None

    def escreverSql (self, df):
        df.to_sql('tb_livros', self.sqlConn, if_exists='replace', index = False)

    def lerSql (self):
        df = pd.DataFrame()

        tabelas = self.cur.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='tb_livros';""").fetchall()
        
        if tabelas != []:
            df = pd.read_sql_query("SELECT * from tb_livros", self.sqlConn)
        
        return df
    
    def contadorBackups (self):
        count = 0

        for filename in os.listdir(self.bkpsDir):
            file = (os.path.join(self.bkpsDir, filename))

            if os.path.isfile(file):
                count += 1

            elif os.path.isdir(file):
                count += self.teste(file)

        return (count)

    # def backupMaisAntigo (self):

    def backupSql (self, df):
        date_str = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        nomeBkp = "backup_livraria_" + date_str + ".db"

        # if (self.contadorBackups >= 5):


        shutil.copyfile(self.dbDir, self.bkpsDir/nomeBkp)

    def exportarCsv(self, df):
        df.to_csv(self.csvDir, index=False)
    
    def importarCsv(self, df):
        df = pd.DataFrame()

        if os.path.getsize(self.csvDir):
            df = pd.read_csv(self.csvDir)
        
        return df
    
