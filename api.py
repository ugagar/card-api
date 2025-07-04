from fastapi import FastAPI
from random import shuffle as rand_shuffle

from constants import CARD_SUITS, CARD_VALUES
from models import Card, Deck


app = FastAPI()

@app.get("/cards/all")
async def read_all_cards(deck: Deck):
    return deck

@app.put("/cards/create")
async def create_card(card: Card):
    return card

@app.post("/deck/shuffle")
async def shuffle_deck(deck: Deck):
    rand_shuffle(deck.cards)
    return {
        "status": "Deck shuffled!",
        "deck": deck.cards
        }
