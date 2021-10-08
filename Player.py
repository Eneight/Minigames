
class Player:
    def __init__(self, name = "Player", cards = []):
        self.name = name
        self.cards = cards

    def __len__(self):
        return len(self.cards)
    
    def __setitem__(self, key, value):
        self.cards[key] = value
        
    def __getitem__(self, key):
        return self.cards[key]

    def __str__(self):
        return f"Name: {self.name}\nCards: {str(self.cards)}"

    def __repr__(self):
        return f"Player(name={self.name}, cards={str(self.cards)})"
