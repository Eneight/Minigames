from Cards import Card
from Deck import Deck
import random

def main():
    setup()
    while len(player1) < 52 and len(player2) < 52:
        random.shuffle(player1.cards)
        random.shuffle(player2.cards)
        global round_cards 
        round_cards = []
        play()

def setup():
    deck = Deck()
    random.shuffle(deck)
    global player1 
    player1 = Deck(input("Enter Name For Player 1: "), deck.deal(26))
    global player2
    player2 = Deck(input("Enter Name for Player 2: "), deck.deal(26))


#Being Implemented
def play():
    p1_card = player1.deal()
    print(f"{player1.name} drew {p1_card}.")
    p2_card = player2.deal()
    print(f"{player2.name} drew {p2_card}.")
    round_cards.append([p1_card, p2_card])
    if p1_card.val > p2_card.val:
        print(f"{player1.name} wins the round and recieves all cards.")
        player1.cards.append([p1_card, p2_card])
    elif p1_card.val < p2_card.val:
        print(f"{player2.name} wins the round and recieves all cards.")
        player2.cards.append([p1_card, p2_card])
    else:
        
    
   
if __name__ == '__main__':
    main()