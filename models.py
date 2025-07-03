from enum import Enum
from pydantic import BaseModel

class CardSuit(str, Enum):
    hearts = "hearts"
    spades = "spades"
    diamonds = "diamonds"
    clubs = "clubs"

class Card(BaseModel):
    value: int
    suit: CardSuit
