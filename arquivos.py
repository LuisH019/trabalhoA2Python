import pandas as pd
import sqlite3

class Arquivos:
    def __init__(self):
        self.sqlConn = sqlite3.connect("db.sqlite3")

    def escrever (self, df):
        df.to_sql('tb_livros', self.sqlConn, if_exists='replace')

    def lerSql (self):
        return pd.read_sql_query("SELECT * from tb_livros", self.sqlConn)