"""Initializes a card and deck class for a go fish game."""

from random import shuffle

class Card:
    """This class represents the cards in a deck defined by the following attributes.
    
    Attributes:
        value(int): represents the number on a given card.
        suit(str): a categorical attribute that is used to further identify cards past their number.
    
    """

    def __init__(self, value, suit):
        """Initializes variables for the Card class and assigns a name for a card based on its value.

        Args:
            value(int): represents the number on a given card.
            suit(str): a categorical attribute that is used to further identify cards past their number.
        
        Side effects:
            If a cards value is over 10, it is assigned a name from a dictionary based on its value.

        """

        self.value = value
        self.suit = suit

        suit = {"Clubs", "Diamonds", "Hearts", "Spades"}

        name_dict = {11: "Jack" , 12: "Queen", 13: "King", 14: "Ace"}

        if value <= 10:
            self.name = str(value)
        
        else:
            self.name = name_dict[value]


    def __str__(self):
        """Lets the program create a string representation of the card based on variables from __init__.
        
        Returns:
            A string reading the cards name/value and its suit.
        
        """

        return f"{self.name} of {self.suit}"
    

class Deck:
    """Initializes a deck for the cards to get added and drawn from.
    
    Attributes:
        cards(list): an empty list that takes card values and suits to store in the Deck class.
    
    """

    def __init__(self):
        """Initializes variables for the Deck class. 

        Side effects:
            Adds cards to the cards list, and shuffles cards once the list is full.

        """

        self.cards = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

        for suit in suits:
            for value in range(2, 15):
                self.cards.append(Card(value, suit))
    
        if len(self.cards) == 52:
            shuffle(self.cards)
    
    def draw(self):
        """Removes cards from the cards list as long as the list isn't empty

        Returns:
            drawn_card: the card removed from the cards list
        
        Side effects:
            If the cards list is empty, a RuntimeError will occur.
            
        """
        if len(self.cards) > 0:
            drawn_card = self.cards.pop()
            return drawn_card
        
        else:
            raise RuntimeError("The deck is empty.")