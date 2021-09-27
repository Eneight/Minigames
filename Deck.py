import random
from Cards import Card

class Deck:
    def __init__(self):
        self.cards = [Card(kind, suite)
                    for kind in ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King"]
                    for suite in ["Spades", "Hearts", "Diamonds", "Clubs"]]

    def shuffle(self):
        self.cards = random.shuffle(self.cards)
                    
    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return f"Deck({str(self.cards)})"