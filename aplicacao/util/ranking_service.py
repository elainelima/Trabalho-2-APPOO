from maps.graveyard_map import GraveyardMap
from maps.green_map import GreenMap

class RankService():
    def __init__(self, db):
        self.db = db

    def cadastra_pontuacao(self, nome, pontuacao, map):
        if isinstance(map, GreenMap):
            tabela ="green_map"
        else:
            tabela ="graveyard_map"
        self.db.add_pontuacao(tabela,nome, pontuacao)

    def retorna_pontuacoes(self, map):
        if isinstance(map, GreenMap):
            tabela ="green_map"
        else:
            tabela ="graveyard_map"
        return self.db.get_pontuacao(tabela)

    def get_top_scores(self, n_top, map):
        if isinstance(map, GreenMap):
            tabela ="green_map"
        else:
            tabela ="graveyard_map"
        return self.db.get_top_scores(tabela,n_top)
