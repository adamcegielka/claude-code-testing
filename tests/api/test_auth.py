import pytest


@pytest.mark.api
@pytest.mark.smoke
class TestLogin:
    def test_login_success(self, http_client, dummyjson_base_url):
        payload = {"username": "emilys", "password": "emilyspass"}

        response = http_client.post(
            f"{dummyjson_base_url}/auth/login", json=payload
        )

        assert response.status_code == 200
        data = response.json()
        assert "accessToken" in data
        assert len(data["accessToken"]) > 0
        assert "refreshToken" in data

    def test_login_missing_password(self, http_client, dummyjson_base_url):
        payload = {"username": "emilys"}

        response = http_client.post(
            f"{dummyjson_base_url}/auth/login", json=payload
        )

        assert response.status_code == 400
        data = response.json()
        assert "message" in data

    def test_login_missing_username(self, http_client, dummyjson_base_url):
        payload = {"password": "emilyspass"}

        response = http_client.post(
            f"{dummyjson_base_url}/auth/login", json=payload
        )

        assert response.status_code == 400
        data = response.json()
        assert "message" in data

    def test_login_wrong_credentials(self, http_client, dummyjson_base_url):
        payload = {"username": "wronguser", "password": "wrongpass"}

        response = http_client.post(
            f"{dummyjson_base_url}/auth/login", json=payload
        )

        assert response.status_code == 400
        data = response.json()
        assert "message" in data


@pytest.mark.api
@pytest.mark.regression
class TestAuthToken:
    def test_token_received_on_login(self, auth_token):
        assert auth_token is not None
        assert isinstance(auth_token, str)
        assert len(auth_token) > 0

    def test_authenticated_request(self, http_client, dummyjson_base_url, auth_token):
        headers = {"Authorization": f"Bearer {auth_token}"}
        response = http_client.get(
            f"{dummyjson_base_url}/auth/me", headers=headers
        )

        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert "username" in data

    def test_invalid_token_rejected(self, http_client, dummyjson_base_url):
        headers = {"Authorization": "Bearer invalidtoken"}
        response = http_client.get(
            f"{dummyjson_base_url}/auth/me", headers=headers
        )

        assert response.status_code == 401
        data = response.json()
        assert "message" in data
