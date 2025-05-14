from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_add_user():
    payload = {
        "name": "Jane Doe",
        "email": "jane@example.com"
    }
    response = client.post("/users", json=payload)
    data = response.json()
    assert data["message"] == "User added successfully"
    assert data["data"]["name"] == "Jane Doe"


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert "users" in response.json()


def test_get_user_by_id():
    payload = {
        "name": "John Smith",
        "email": "john@example.com"
    }
    response = client.post("/users", json=payload)
    add_user_data = response.json()
    user_id = add_user_data['data']['id']
    get_response = client.get(f"/users/{user_id}")
    get_user_data = get_response.json()
    assert get_response.status_code == 200
    assert get_user_data['id'] == user_id


def test_update_user():
    payload = {
        "name": "Old Name",
        "email": "old@example.com"
    }
    response = client.post("/users", json=payload)
    add_user_data = response.json()
    user_id = add_user_data['data']['id']
    update_response = client.put(f"/users/{user_id}", json={"name": "New Name", "email": "new@example.com"})
    update_data = update_response.json()
    assert update_response.status_code == 200
    assert update_data['data']['name'] == "New Name"


def test_delete_user():
    payload = {
        "name": "To Delete",
        "email": "delete@example.com"
    }
    response = client.post("/users", json=payload)
    add_user_data = response.json()
    user_id = add_user_data['data']['id']
    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "User deleted successfully"
    # Confirm deleted
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404
