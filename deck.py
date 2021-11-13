from cards import Card

class Deck:
    def __init__(self, cards = [Card(kind, suite)
                    for kind in ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King"]
                    for suite in ["Spades", "Hearts", "Diamonds", "Clubs"]]):
        self.cards = cards
        self.len = len(self.cards)

    def deal(self, amount = 1):
        results = []
        for index in range(amount):
            results.append(self.cards.pop(0))
        return results
                  
    def __len__(self):
        return len(self.cards)
    
    def __setitem__(self, key, value):
        self.cards[key] = value
        
    def __getitem__(self, key):
        return self.cards[key]
    
    def __str__(self):
        message = ""
        for card in self.cards:
            message += f"{str(card)}, "
        message = message[:-2]
        return f"Cards: {message}"

    def __repr__(self):
        return f"Deck(cards={str(self.cards)})"
