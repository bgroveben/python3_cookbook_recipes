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


class Deck:
    """
    Each Deck object will contain a list of Card objects as an attribute.
    """
    def __init__(self):
        """
        Creates the cards attribute and generates a fifty-two card deck.
        The deck is a list and each card object is a (suit, rank) tuple.
        """
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def print_deck(self):
        """
        To print a Deck, we traverse the list and print each Card.
        """
        for card in self.cards:
            print(card)

    def __str__(self):
        """
        This is an alternative to the print_deck method above.
        Returns a string representation of a Deck.
        The cards are a single string printed in a cascade over 52 lines.
        """
        # s is an accumulator
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        """
        Use the shuffle method from the random number generator.
        """
        import random
        rng = random.Random()
        rng.shuffle(self.cards)

    def deal(self, hands, num_cards=999):
        """
        The two parameters are a list (or tuple) of hands and the total number
        of cards to deal.
        The second parameter is optional.
        If there aren't enogh cards, the method stops when all are dealt.
        """
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break  # if there are no more cards
            card = self.pop()  # take the next card
            hand = hands[i % num_hands]  # decide whose turn it is
            hand.add(card)  # add a card to that hand

    def remove(self, card):
        """
        Takes a card as a parameter and removes it.
        Returns True if the card was in the deck, False otherwise.
        """
        if card in self.cards:
            # the remove method checks for deep equality
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        """
        The pop method is used to deal the cards.
        The last card in the list is removed, like dealing from the bottom
        of the deck.
        """
        return self.cards.pop()

    def is_empty(self):
        """
        Returns True if the deck contains no cards.
        """
        return self.cards == []


class Hand(Deck):
    """
    Hand is a subclass of Deck, so it will inherit those methods as well.
    -->
    >> from cards import Card, Deck, Hand
    >> deck = Deck()
    >> deck.shuffle()
    >> hand = Hand("ben")
    >> deck.deal([hand], 5)
    >> print(hand)
    4 of Diamonds
     6 of Diamonds
      4 of Spades
       9 of Clubs
        7 of Clubs
    -->
    """
    def __init__(self, name =""):
        self.cards = []
        self.name = name

    def add(self, card):
        """
        The remove() method is inherited from Deck.
        """
        self.cards.append(card)

    def __str__(self):
        """
        Overrides the one in the Deck class so we can include more information.
        """
        s = "Hand for player " + self.name
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains: \n"
        return s + Deck.__str__(self)


class CardGame:
    """
    Creates the deck and shuffles it.
    """
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

######################  OLD MAID GAME #########################################
# The object of Old Maid is to get rid of cards in your hand.
# You do this by matching cards by rank and color.
# For example, the 4 of Clubs matches the 4 of Spades since both suits
# are black.
# The Jack of Hearts matches the Jack of Diamonds since both are red.
# To begin the game, the Queen of Clubs is removed from the deck so that the
# Queen of Spades has no match.
# The fifty-one remaining cards are dealt to the players in a round robin.
# After the deal, all players match and discard as many cards as possible.
# When no more matches can be made, play begins.
# In turn, each player picks a card (without looking) from the closest neighbor
# to the left who still has cards.
# If the chosen card matches a card in the player’s hand, the pair is removed.
# Otherwise, the card is added to the player’s hand.
# Eventually all possible matches are made, leaving only the Queen of Spades in
# the loser’s hand.
################################################################################

class OldMaidHand(Hand):
    """
    Inherits from Hand and provides an additional method called remove_matches()
    The __init__() method is inherited from CardGame, so we start with a new
    and shuffled deck ready.

    -->
    >> from cards import Card, Deck, Hand, CardGame, OldMaidHand
    >> game = CardGame()
    >> hand = OldMaidHand("ben")
    >> game.deck.deal([hand], 13)
    >> print(hand)
    Hand ben contains
    2 of Diamonds
     Queen of Spades
      9 of Diamonds
       King of Clubs
        7 of Spades
         6 of Spades
          4 of Clubs
           2 of Spades
            10 of Clubs
             Queen of Hearts
              8 of Clubs
               4 of Hearts
                7 of Diamonds

    >>
    -->
    """
    def remove_matches(self):
        """
        We start by making a copy of the list of cards, so that we can traverse the
        copy while removing cards from the original.
        Since self.cards is modified in the loop, we don’t want to use it to
        control the traversal.
        Python can get quite confused if it is traversing a list that is changing.
        For each card in the hand, we figure out what the matching card is and go
        looking for it.
        The match card has the same rank and the other suit of the same color.
        The expression:
        >> 3 - card.suit
        turns a Club (suit 0) into a Spade (suit 3) and a Diamond (suit 1) into a
        Heart (suit 2).
        You should satisfy yourself that the opposite operations also work.
        f the match card is also in the hand, both cards are removed.
        """
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Match for player {0}: {1} matches {2}"
                        .format(self.name, card, match))
                count += 1
        return count


class OldMaidGame(CardGame):
    """
    OldMaidGame is a subclass of CardGame with a new method called play that
    takes a list of players as a parameter.
    """
    def print_hands(self):
        for hand in self.hands:
            print(hand)

    def play(self, names):
        """
        This method implements the steps of the game with each player in turn.
        """
        # Remove Queen of Clubs:
        self.deck.remove(Card(0,12))

        # Make a hand for each player:
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))

        # Deal the cards:
        self.deck.deal(self.hands)
        print()
        print("------------ The cards have been dealt ------------")
        print()
        self.print_hands()

        # Remove initial matches:
        matches = self.remove_all_matches()
        print()
        print("---------------------------------------------------")
        print("----- Matches discarded ... Now play begins -------")
        print("---------------------------------------------------")
        print()
        self.print_hands()

        # Play until all 50 cards are matched:
        turn = 0
        # The variable turn keeps track of which player’s turn it is.
        # It starts at 0 and increases by one each time; when it reaches
        # num_hands, the modulus operator wraps it back around to 0.
        num_hands = len(self.hands)
        # When the total number of matches reaches twenty-five, fifty cards
        # have been removed from the hands, which means that only one card is
        # left and the game is over.
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print()
        print("------- Game Over --------")
        print()
        self.print_hands()

    def remove_all_matches(self):
        """
        Traverse the list of hands and invoke remove_matches on each.
        """
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def play_one_turn(self, i):
        """
        Takes a parameter that indicates whose turn it is.
        The return value is the number of matches made during this turn.
        """
        # If a player’s hand is empty, that player is out of the game, so he or
        # she does nothing and returns 0.
        if self.hands[i].is_empty():
            return 0
        # Otherwise, a turn consists of finding the first player on the left
        # that has cards, taking one card from the neighbor, and checking for
        # matches.
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Player", self.hands[i].name, "picked", picked_card)
        # Before returning, the cards in the hand are shuffled so that the next
        # player’s choice is random.
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbor(self, i):
        """
        Starts with the player to the immediate left and continues around the
        circle until it finds a player that still has cards remaining.
        """
        # If find_neighbor ever went all the way through the nested loops
        # without finding cards, it would return None and cause an error
        # elsewhere in the program.
        # That's why we need to make sure the game ending is specified.
        num_hands = len(self.hands)
        for next in range(1, num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor
