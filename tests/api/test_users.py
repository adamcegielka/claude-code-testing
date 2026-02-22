import pytest


@pytest.mark.api
@pytest.mark.smoke
class TestListUsers:
    def test_list_users(self, http_client, dummyjson_base_url):
        response = http_client.get(f"{dummyjson_base_url}/users")

        assert response.status_code == 200
        data = response.json()
        assert "users" in data
        assert isinstance(data["users"], list)
        assert len(data["users"]) > 0
        assert data["total"] > 0

    def test_list_users_with_limit(self, http_client, dummyjson_base_url):
        response = http_client.get(f"{dummyjson_base_url}/users?limit=5")

        assert response.status_code == 200
        data = response.json()
        assert len(data["users"]) == 5

    @pytest.mark.parametrize("page_skip", [0, 5, 10])
    def test_pagination_with_skip(self, http_client, dummyjson_base_url, page_skip):
        response = http_client.get(
            f"{dummyjson_base_url}/users?limit=5&skip={page_skip}"
        )

        assert response.status_code == 200
        data = response.json()
        assert data["skip"] == page_skip
        assert len(data["users"]) <= 5


@pytest.mark.api
@pytest.mark.smoke
class TestGetUser:
    def test_get_existing_user(self, http_client, dummyjson_base_url):
        response = http_client.get(f"{dummyjson_base_url}/users/1")

        assert response.status_code == 200
        user = response.json()
        assert user["id"] == 1
        assert "email" in user
        assert "firstName" in user
        assert "lastName" in user
        assert "username" in user

    def test_get_nonexistent_user(self, http_client, dummyjson_base_url):
        response = http_client.get(f"{dummyjson_base_url}/users/999")

        assert response.status_code == 404

    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_get_users_by_id(self, http_client, dummyjson_base_url, user_id):
        response = http_client.get(f"{dummyjson_base_url}/users/{user_id}")

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == user_id


@pytest.mark.api
@pytest.mark.regression
class TestCreateUser:
    def test_create_user(self, http_client, dummyjson_base_url):
        payload = {"firstName": "John", "lastName": "Doe", "age": 30}

        response = http_client.post(
            f"{dummyjson_base_url}/users/add", json=payload
        )

        assert response.status_code == 201
        created = response.json()
        assert created["firstName"] == payload["firstName"]
        assert created["lastName"] == payload["lastName"]
        assert "id" in created

    def test_update_user(self, http_client, dummyjson_base_url):
        payload = {"firstName": "Jane", "lastName": "Smith"}

        response = http_client.put(
            f"{dummyjson_base_url}/users/1", json=payload
        )

        assert response.status_code == 200
        updated = response.json()
        assert updated["firstName"] == payload["firstName"]
        assert updated["lastName"] == payload["lastName"]

    def test_delete_user(self, http_client, dummyjson_base_url):
        response = http_client.delete(f"{dummyjson_base_url}/users/1")

        assert response.status_code == 200
        data = response.json()
        assert data["isDeleted"] is True
