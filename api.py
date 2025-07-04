from fastapi import FastAPI
from random import shuffle as rand_shuffle

from models import Card, Deck, DEFOULT_DECK


app = FastAPI()

@app.get("/deck")
async def read_all_cards(deck: Deck = DEFOULT_DECK):
    return deck

@app.put("/cards/create")
async def create_card(card: Card):
    return card

@app.post("/deck/shuffle")
async def shuffle_deck(deck: Deck = DEFOULT_DECK):
    rand_shuffle(deck.cards)
    return {
        "status": "Deck shuffled!",
        "deck": deck.cards
        }
