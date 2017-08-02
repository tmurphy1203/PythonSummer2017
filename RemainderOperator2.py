class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        letters = {1:'A', 11:'J', 12:'Q', 13:'K'}
        letter = letters.get(self.rank, str(self.rank))
        return "<Card %s %s>" % (letter, self.suit)

hand = [Card(1, 'spade'), Card(10, 'club')]