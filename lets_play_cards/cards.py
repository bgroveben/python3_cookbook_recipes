class Card:
    """
    Use integers to encode the ranks and suits used in a deck of cards.
    In order to print Card objects in a way that people can easily read,
    we want to map the integer codes onto words.

    -->
    In [1]: from cards import Card
    In [2]: card1 = Card(1, 11)
    In [3]: print(card1)
    Jack of Diamonds

    In [4]: card2 = Card(1, 3)
    In [5]: print(card2)
    3 of Diamonds

    In [6]: print(card2.suits[1])
    Diamonds
    -->

    TODO:
    Error handling for invalid inputs in suits and ranks.
    Write a method or methods to compare the cards.
    http://openbookproject.net/thinkcs/python/english3e/collections.html#comparing-cards
    """
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    # "narf" is a placekeeper for the zeroth element, which we don't need.
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
             "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        Returns a string representation of the corresponding card.
        """
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def cmp_(self, other):
        """
        Start with a single method named cmp_ that houses the logic of ordering.
        The comparison method takes two parameters, self and other, and returns 1 if the first object is greater, -1 if the second object is greater, and 0 if they are equal to each other.
        suit will have precedence over rank.
        Aces appear lower than Deuces(2s).

        > from cards import Card
        > card1 = Card(1, 11)
        > card2 = Card(1, 3)
        > card3 = Card(1, 11)
        > card1 < card2
        False
        > card1 == card3
        True
        >
        """
        # Check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # Suits are compared, now check the ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # Ranks are compared, ties result in 0
        return 0

    # Define the six special methods that overload each the relational operators
    def __eq__(self, other):
        return self.cmp_(other) == 0

    def __le__(self, other):
        return self.cmp_(other) <= 0

    def __ge__(self, other):
        return self.cmp_(other) >= 0

    def __gt__(self, other):
        return self.cmp_(other) > 0

    def __lt__(self, other):
        return self.cmp_(other) < 0

    def __ne__(self, other):
        return self.cmp_(other) != 0
