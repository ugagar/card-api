from fastapi import FastAPI
from random import shuffle as rand_shuffle

from constants import CARD_SUITS, CARD_VALUES
from models import Card


app = FastAPI()

deck = []

@app.get("/cards/all")
async def read_all_cards():
    global deck
    deck = [
        {"value": value, "suit": suit}
        for value in CARD_VALUES
        for suit in CARD_SUITS
    ]
    return deck

@app.put("/cards/create")
async def create_card(card: Card):
    return card

@app.post("/deck/shuffle")
async def shuffle_deck():
    rand_shuffle(deck)
    return {
        "status": "Deck shuffled!",
        "deck": deck
        }
