class Player:
    def __init__(self):
        self.gold = 100  # Começa com 100 moedas

    def can_afford(self, cost: int):
        return self.gold >= cost

    def spend(self, cost: int):
        if self.can_afford(cost):
            self.gold -= cost
            return True
        return False
