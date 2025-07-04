from fastapi import FastAPI

from constants import CARD_SUITS, CARD_VALUES
from models import Card


app = FastAPI()

@app.get("/cards/all")
async def read_all_cards():
    return [
        {"value": value, "suit": suit}
        for value in CARD_VALUES
        for suit in CARD_SUITS
    ]

@app.put("/cards/create")
async def create_card(card: Card):
    return card
