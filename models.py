from pydantic import BaseModel

from constants import CardSuit

class Card(BaseModel):
    value: int
    suit: CardSuit
