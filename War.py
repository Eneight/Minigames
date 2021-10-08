from Cards import Card
from Deck import Deck
from Player import Player
import random

def main():
    setup()
    while len(player1) < 52 and len(player2) < 52:
        play()

def setup():
    deck = Deck()
    random.shuffle(deck)
    global player1 
    player1 = Player(input("Enter Name For Player 1: "), deck.deal(26))
    global player2
    player2 = Player(input("Enter Name for Player 2: "), deck.deal(26))

def play():
    pass
   
if __name__ == '__main__':
    main()