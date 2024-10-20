import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_items(client):
    response = client.post('/items')
    assert response.status_code == 200
