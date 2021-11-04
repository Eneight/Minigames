from deck import Deck
from player import Player
import random

round_cards = []

def main():
    setup()
    while len(player1.deck) < 52 and len(player2.deck) < 52:
        print(f"{player1.status()}\n{player2.status()}")
        random.shuffle(player1.deck.cards)
        random.shuffle(player2.deck.cards)
        play()
    print(f"{player1.status()}\n{player2.status()}")
    if not len(player1.deck) < 52:
        print(f"{player1.name} wins!")
    else:
        print(f"{player2.name} wins!")


def setup():
    deck = Deck()
    random.shuffle(deck)
    global player1 
    player1 = Player(input("Enter Name For Player 1: "), int(input("Enter Number of Chips for Player 1: ")), Deck(deck.deal(26)))
    global player2
    player2 = Player(input("Enter Name For Player 2: "), int(input("Enter Number of Chips for Player 2: ")), Deck(deck.deal(26)))


def play():
    p1_card = player1.deck.deal()[0]
    print(f"{player1.name} drew {p1_card}.")
    p2_card = player2.deck.deal()[0]
    print(f"{player2.name} drew {p2_card}.")
    
    if p1_card.val > p2_card.val:
        print(f"{player1.name} wins the round and recieves all cards.")
        round_cards.extend([p1_card, p2_card])
        player1.deck.cards.extend(round_cards)
        round_cards.clear()

    elif p1_card.val < p2_card.val:
        print(f"{player2.name} wins the round and recieves all cards.")
        round_cards.extend([p1_card, p2_card])
        player2.deck.cards.extend(round_cards)
        round_cards.clear()
        
    else:
        print("Its a tie! Both players added an unknown card to the pot and will draw again.")
        round_cards.extend([p1_card, p2_card])
        try:
            round_cards.append(player1.deck.deal()[0])
        except IndexError:
            print(f"{player1.name} is out of cards! {player2.name} wins the round and recieves all the cards.")
            player2.deck.cards.extend(round_cards)
            round_cards.clear()
            
        try:
            round_cards.append(player2.deck.deal()[0])
            play()
        except:
            print(f"{player2.name} is out of cards! {player1.name} wins the round and recieves all the cards.")
            player1.deck.cards.extend(round_cards)
            round_cards.clear()
    
   
if __name__ == '__main__':
   main()