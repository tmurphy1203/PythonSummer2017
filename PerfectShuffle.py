# Perfect Shuffle
# A program that allows the user to shuffle a deck of cards
# By Tim Murphy 29/7/17

import Epic

rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

# Forming deck of cards
def buildDeck(rank, suit):
    deck = ["%s of %s" % (r, s) for r in rank for s in suit]
    return deck

def shuffle(deck):
# Evenly shuffling into 2 piles
    half1 = deck[:26]
    half2 = deck[26:]
    

    for i in range(0,26):
        deck[2*i] = half1[i]
        deck[2*i+1] = half2[i]
    return deck

# Deal first 5 cards of the newly shuffled deck
def deal(deck):
    dealDeck = deck[:5]
    return dealDeck
# User inputs how many times to shuffle
def main():
    deck = buildDeck(rank, suit)
    number = Epic.userInt("How many times do you want to shuffle? ")
    
    for i in range(0, number):
        deck = shuffle(deck)
        
    deck = deal(deck)
    
    print deck

main()