from Cards import Card
from Deck import Deck
import random

round_cards = []

def main():
    setup()
    while len(player1) < 52 and len(player2) < 52:
        print(f"{player1.status()}\n{player2.status()}")
        random.shuffle(player1.cards)
        random.shuffle(player2.cards)
        play()
    print(f"{player1.status()}\n{player2.status()}")
    if not len(player1) < 52:
        print(f"{player1.name} wins!")
    else:
        print(f"{player2.name} wins!")


def setup():
    deck = Deck()
    random.shuffle(deck)
    global player1 
    player1 = Deck(deck.deal(26), input("Enter Name For Player 1: "))
    global player2
    player2 = Deck(deck.deal(26), input("Enter Name for Player 2: "))


#Being Implemented
def play():
    p1_card = player1.deal()[0]
    print(f"{player1.name} drew {p1_card}.")
    p2_card = player2.deal()[0]
    print(f"{player2.name} drew {p2_card}.")
    
    if p1_card.val > p2_card.val:
        print(f"{player1.name} wins the round and recieves all cards.")
        round_cards.extend([p1_card, p2_card])
        player1.cards.extend(round_cards)
        round_cards.clear()

    elif p1_card.val < p2_card.val:
        print(f"{player2.name} wins the round and recieves all cards.")
        round_cards.extend([p1_card, p2_card])
        player2.cards.extend(round_cards)
        round_cards.clear()
        
    else:
        print("Its a tie! Both players added an unknown card to the pot and will draw again.")
        round_cards.extend([p1_card, p2_card])
        try:
            round_cards.append(player1.deal()[0])
        except IndexError:
            print(f"{player1.name} is out of cards! {player2.name} wins the round and recieves all the cards.")
            player2.cards.extend(round_cards)
            round_cards.clear()
            
        try:
            round_cards.append(player2.deal()[0])
            play()
        except:
            print(f"{player2.name} is out of cards! {player1.name} wins the round and recieves all the cards.")
            player1.cards.extend(round_cards)
            round_cards.clear()
    
   
if __name__ == '__main__':
   main()