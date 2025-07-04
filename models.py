from pydantic import BaseModel

from constants import CardSuit, CARD_SUITS, CARD_VALUES

class Card(BaseModel):
    value: int
    suit: CardSuit

class Deck(BaseModel):
    cards: list[Card] = [
        {"value": value, "suit": suit}
        for value in CARD_VALUES
        for suit in CARD_SUITS
    ]

DEFOULT_DECK = Deck()
