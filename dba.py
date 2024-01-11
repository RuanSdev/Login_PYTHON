import sqlite3 as lite
import datetime
# Classe do banco de dados de usuarios 
class Banco_Dados():
    def __init__(self):
        self.nome = 'dba.db'
        self.conexao = None
        self.cursor = None
        self.Conectar()
    # Conectar no banco 
    def Conectar(self):
        self.conexao = lite.connect(self.nome)
        self.cursor = self.conexao.cursor()
        self.cursor.execute('CREATE TABLE  IF NOT EXISTS USUARIOS(USER TEXT PRIMARY KEY NOT NULL,SENHA TEXT NOT NULL)')
        self.cursor.execute('CREATE TABLE  IF NOT EXISTS ACESSO (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,USER TEXT NOT NULL,DATA TEXT NOT NULL)')
    def Cadastrar(self, nome,senha):
        with self.conexao:
            self.cursor.execute('INSERT INTO USUARIOS (USER,SENHA) VALUES(?,?)',(nome,senha))
            self.conexao.commit()
    def Consultar(self,usuario):
        with self.conexao:
            return self.cursor.execute('SELECT * FROM  USUARIOS WHERE USER = ?',(usuario,)).fetchall()
    def Salvar_Ultimo(self,usuario):
        with self.conexao:
            self.cursor.execute('INSERT INTO ACESSO (USER,DATA) VALUES(?,?)',(usuario,datetime.date.today()))
            self.conexao.commit()
    def Pegar_Ultimo(self):
        return self.cursor.execute('SELECT MAX(ID), USER FROM ACESSO').fetchall()
    def Deletar(self,usuario):
        self.Conectar()
        self.cursor.execute('DELETE FROM USUARIOS WHERE USER = ?',(usuario,))
        self.conexao.commit()
        


