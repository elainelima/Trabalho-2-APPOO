import sqlite3
import os

class Base_Dados:
    def __init__(self)-> None:
        self.db_name = os.path.join(os.path.dirname(__file__), 'protect_the_land.db')
        self.connection = None

    def connect(self) -> None:
        try:
            self.connection = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco: {e}")

    def execute_script(self)-> None:
        try:
            script_path = os.path.join(os.path.dirname(__file__), 'protect_the_land.sql')
            with open(script_path, 'r', encoding='utf-8') as file:
                script = file.read()
            cursor = self.connection.cursor()
            cursor.executescript(script)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro ao executar o script SQL: {e}")

    def add_pontuacao(self, nome, pontuacao)-> str:
        cursor =  self.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO jogadores (nome, pontuacao) 
                VALUES (?, ?)
            """, (nome, pontuacao))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro ao adicionar pontuacao: {e}")


    def get_pontuacao(self):
        cursor =  self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM jogadores ")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao recuperar pontuacoes: {e}")
            return []

    def get_top_scores(self, n_top):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM jogadores ORDER BY pontuacao DESC LIMIT ?", (n_top,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao recuperar pontuações: {e}")
            return []


    def close(self)-> None:
        if self.connection:
            self.connection.close()
            print("Conexão com o banco encerrada.")
         

    