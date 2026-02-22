import pytest
import requests


@pytest.fixture(scope="session")
def http_client():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()


@pytest.fixture(scope="session")
def auth_token(dummyjson_base_url, http_client):
    response = http_client.post(
        f"{dummyjson_base_url}/auth/login",
        json={"username": "emilys", "password": "emilyspass"},
    )
    assert response.status_code == 200
    return response.json()["accessToken"]
