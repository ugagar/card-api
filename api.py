from fastapi import FastAPI

from models import CardSuit, Card

suits = [CardSuit.clubs, CardSuit.diamonds, CardSuit.hearts, CardSuit.spades]
values = range(6, 14)

app = FastAPI()

@app.get("/cards/all")
async def read_all_cards():
    return [
        {"value": value, "suit": suit}
        for value in values
        for suit in suits
    ]

@app.put("/cards/create")
async def create_card(card: Card):
    return card
