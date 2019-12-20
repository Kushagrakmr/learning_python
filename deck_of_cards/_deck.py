from random import shuffle

class Card:
    possible_values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")

    def __init__(self, value, suit):
        if suit not in Card.suits:
            raise ValueError("You can't have {} as a suit.".format(self.suit))

        if value not in Card.possible_values:
            raise ValueError("You can't have {} as a value.".format(self.value))

        self.value = value
        self.suit = suit


    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        self.cards = [Card(value, suit) for suit in suits for value in values]

        # We can also do this by list comprehension (pythonic way)
        # for suit in self.suits:
        #     for value in self.values:
        #         self.cards.append(Card(value, suit))

    def __repr__(self):
        return "The Deck contains {} cards.".format(self.count())

    def __iter__(self):
        k = iter(self.cards)
        return k


    def count(self):
        return len(self.cards)

    def _deal(self, number):
        count = self.count()
        if count == 0:
            raise ValueError("All cards have been dealt.")
        else:
            count = min([count, number])
            cards = self.cards[-count:]
            self.cards = self.cards[:-count]
            return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self


d = Deck()
d._deal(5)
d.deal_card()

print()
print()

for card in d:
    print(card)