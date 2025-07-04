from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_deck():
    response = client.get("/deck")
    assert response.status_code == 200

def test_shuffle_deck():
    response = client.post("/deck/shuffle")
    assert response.status_code == (200, 201, 202)
