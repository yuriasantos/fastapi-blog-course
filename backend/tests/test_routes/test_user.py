from fastapi.testclient import TestClient
from conftest import SessionTesting

def test_create_user(client: TestClient, db_session: SessionTesting): # type: ignore
    user = {
        "email": "teste@teste.com",
        "password": "123456"
    }
    response = client.post("/users/", json=user)
    assert response.status_code == 201
    assert response.json()["email"] == user["email"]
