from Deck import Deck

class Player():
    def __init__(self, name = "Player", bank = 0, deck = Deck()):
        self.name = name
        self.bank = bank
        self.deck = deck
    
    def status(self):
        return f"{self.name} has {len(self.deck.cards)} cards."

    def bet(self, amt):
        self.bank -= amt
        return amt

    def __str__(self):
        return f"Name: {self.name}\nMoney: {self.bank}\n{str(self.deck)}"

    def __repr__(self):
        return f"Player(name={self.name}, bank={self.bank}, deck={repr(self.deck)})"
