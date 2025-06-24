

class RankService():
    def __init__(self,db):
        self.db = db

    def cadastra_pontuacao(self,nome,pontuacao):
        self.db.add_pontuacao(nome,pontuacao)    

    def retorna_pontuacoes(self):
        self.db.get_pontuacao()   
    
    def get_top_scores(self,n_top):
       return self.db.get_top_scores(n_top)