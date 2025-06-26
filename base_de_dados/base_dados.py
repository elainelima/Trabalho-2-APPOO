import sqlite3
import os

class BaseDados:
    def __init__(self):
        self.db_name = os.path.join(os.path.dirname(__file__), 'protect_the_land.db')
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(f"[ERRO] Conexão: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexão com o banco encerrada.")

    def execute_script(self):
        try:
            script_path = os.path.join(os.path.dirname(__file__), 'protect_the_land.sql')
            with open(script_path, 'r', encoding='utf-8') as file:
                script = file.read()
            self.connection.executescript(script)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"[ERRO] Script SQL: {e}")


    
    def add_pontuacao(self, tabela: str, nome: str, pontuacao: int):
        try:
            self.connection.execute(
                f"INSERT INTO {tabela} (nome, pontuacao) VALUES (?, ?)", (nome, pontuacao)
            )
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"[ERRO] Inserção em {tabela}: {e}")

    def get_pontuacoes(self, tabela: str):
        try:
            cursor = self.connection.execute(f"SELECT * FROM {tabela}")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"[ERRO] Consulta em {tabela}: {e}")
            return []

    def get_top_scores(self, tabela: str, n_top: int):
        try:
            cursor = self.connection.execute(
                f"SELECT * FROM {tabela} ORDER BY pontuacao DESC LIMIT ?", (n_top,)
            )
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"[ERRO] Ranking em {tabela}: {e}")
            return []
