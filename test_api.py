from fastapi.testclient import TestClient
from api import app

from models import Deck

client = TestClient(app)

def test_get_deck():
    response = client.get("/deck")
    assert response.status_code == 200

def test_shuffle_deck():
    response: Deck = client.post("/deck/shuffle")
    assert response.cards
    assert response.status_code in (200, 201, 202)
