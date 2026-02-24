import pytest


@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regression
class TestRestfulApiObjects:
    def test_list_all_objects(self, http_client, restful_api_base_url):
        response = http_client.get(f"{restful_api_base_url}/objects")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        first = data[0]
        assert "id" in first
        assert "name" in first

    def test_get_single_object(self, http_client, restful_api_base_url):
        response = http_client.get(f"{restful_api_base_url}/objects/7")

        assert response.status_code == 200
        obj = response.json()
        assert obj["id"] == "7"
        assert "name" in obj
        assert "data" in obj

    def test_get_nonexistent_object(self, http_client, restful_api_base_url):
        response = http_client.get(f"{restful_api_base_url}/objects/nonexistent-id-999")

        assert response.status_code == 404


@pytest.mark.api
@pytest.mark.regression
class TestRestfulApiCrud:
    def test_create_object(self, http_client, restful_api_base_url):
        payload = {"name": "QA Test Device", "data": {"year": 2024, "price": 999.99}}

        response = http_client.post(f"{restful_api_base_url}/objects", json=payload)

        assert response.status_code == 200
        created = response.json()
        assert created["name"] == payload["name"]
        assert "id" in created
        assert "createdAt" in created

    def test_update_object(self, http_client, restful_api_base_url):
        created = http_client.post(
            f"{restful_api_base_url}/objects",
            json={"name": "Original", "data": {"price": 1.0}},
        ).json()
        obj_id = created["id"]

        response = http_client.put(
            f"{restful_api_base_url}/objects/{obj_id}",
            json={"name": "Updated", "data": {"price": 2.0}},
        )

        assert response.status_code == 200
        updated = response.json()
        assert updated["name"] == "Updated"
        assert "updatedAt" in updated

    def test_partial_update_object(self, http_client, restful_api_base_url):
        created = http_client.post(
            f"{restful_api_base_url}/objects",
            json={"name": "Original", "data": {"price": 1.0}},
        ).json()
        obj_id = created["id"]

        response = http_client.patch(
            f"{restful_api_base_url}/objects/{obj_id}",
            json={"name": "Patched Name"},
        )

        assert response.status_code == 200
        patched = response.json()
        assert patched["name"] == "Patched Name"
        assert "updatedAt" in patched

    def test_delete_object(self, http_client, restful_api_base_url):
        created = http_client.post(
            f"{restful_api_base_url}/objects",
            json={"name": "To Be Deleted", "data": {}},
        ).json()
        obj_id = created["id"]

        response = http_client.delete(f"{restful_api_base_url}/objects/{obj_id}")

        assert response.status_code == 200
        assert obj_id in response.json()["message"]

    def test_list_objects_by_ids(self, http_client, restful_api_base_url):
        response = http_client.get(
            f"{restful_api_base_url}/objects?id=3&id=5&id=7"
        )

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 3
        returned_ids = {obj["id"] for obj in data}
        assert returned_ids == {"3", "5", "7"}
