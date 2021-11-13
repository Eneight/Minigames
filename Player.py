from deck import Deck

class Player():
    def __init__(self, name = "Player", chips = 0, deck = Deck()):
        self.name = name
        self.chips = chips
        self.deck = deck
    
    def status(self):
        return f"{self.name} has {len(self.deck.cards)} cards."

    def bet(self, amt):
        self.chips -= amt
        return amt

    def __str__(self):
        return f"Name: {self.name}\nMoney: {self.chips}\n{str(self.deck)}"

    def __repr__(self):
        return f"Player(name={self.name}, bank={self.chips}, deck={repr(self.deck)})"
