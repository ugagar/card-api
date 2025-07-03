from pydantic import BaseModel

class Card(BaseModel):
    value: int
    suit: str
