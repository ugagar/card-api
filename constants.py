from enum import Enum

class CardSuit(str, Enum):
    hearts = "hearts"
    spades = "spades"
    diamonds = "diamonds"
    clubs = "clubs"

CARD_SUITS = list(CardSuit)
CARD_VALUES = list(range(6, 15))
