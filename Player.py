
class Player:
    def __init__(self, name = "Player", cards = []):
        self.name = name
        self.cards = cards

    def __str__(self):
        return f"Name: {self.name}\tCards: {str(self.cards)}"

    def __repr__(self):
        return f"Player(name={self.name}, cards={str(self.cards)})"
