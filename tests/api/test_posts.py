import pytest


@pytest.mark.api
@pytest.mark.smoke
class TestGetPosts:
    def test_get_all_posts(self, http_client, api_base_url):
        response = http_client.get(f"{api_base_url}/posts")

        assert response.status_code == 200
        posts = response.json()
        assert isinstance(posts, list)
        assert len(posts) == 100

    def test_get_single_post(self, http_client, api_base_url):
        response = http_client.get(f"{api_base_url}/posts/1")

        assert response.status_code == 200
        post = response.json()
        assert post["id"] == 1
        assert "title" in post
        assert "body" in post
        assert "userId" in post

    @pytest.mark.parametrize("post_id", [1, 10, 50, 100])
    def test_get_post_by_id(self, http_client, api_base_url, post_id):
        response = http_client.get(f"{api_base_url}/posts/{post_id}")

        assert response.status_code == 200
        post = response.json()
        assert post["id"] == post_id

    def test_get_nonexistent_post(self, http_client, api_base_url):
        response = http_client.get(f"{api_base_url}/posts/999")

        assert response.status_code == 404


@pytest.mark.api
@pytest.mark.regression
class TestCreatePost:
    def test_create_post(self, http_client, api_base_url):
        payload = {
            "title": "Test Post Title",
            "body": "Test post body content",
            "userId": 1,
        }

        response = http_client.post(f"{api_base_url}/posts", json=payload)

        assert response.status_code == 201
        created = response.json()
        assert created["title"] == payload["title"]
        assert created["body"] == payload["body"]
        assert created["userId"] == payload["userId"]
        assert "id" in created

    @pytest.mark.parametrize(
        "payload",
        [
            {"title": "Post by user 1", "body": "Body 1", "userId": 1},
            {"title": "Post by user 2", "body": "Body 2", "userId": 2},
            {"title": "Post by user 3", "body": "Body 3", "userId": 3},
        ],
    )
    def test_create_post_multiple_users(self, http_client, api_base_url, payload):
        response = http_client.post(f"{api_base_url}/posts", json=payload)

        assert response.status_code == 201
        created = response.json()
        assert created["userId"] == payload["userId"]


@pytest.mark.api
@pytest.mark.regression
class TestUpdatePost:
    def test_update_post(self, http_client, api_base_url):
        payload = {
            "id": 1,
            "title": "Updated Title",
            "body": "Updated body content",
            "userId": 1,
        }

        response = http_client.put(f"{api_base_url}/posts/1", json=payload)

        assert response.status_code == 200
        updated = response.json()
        assert updated["title"] == payload["title"]
        assert updated["body"] == payload["body"]

    def test_patch_post(self, http_client, api_base_url):
        payload = {"title": "Patched Title"}

        response = http_client.patch(f"{api_base_url}/posts/1", json=payload)

        assert response.status_code == 200
        patched = response.json()
        assert patched["title"] == payload["title"]


@pytest.mark.api
@pytest.mark.regression
class TestDeletePost:
    def test_delete_post(self, http_client, api_base_url):
        response = http_client.delete(f"{api_base_url}/posts/1")

        assert response.status_code == 200

    @pytest.mark.parametrize("post_id", [1, 5, 10])
    def test_delete_multiple_posts(self, http_client, api_base_url, post_id):
        response = http_client.delete(f"{api_base_url}/posts/{post_id}")

        assert response.status_code == 200


@pytest.mark.api
@pytest.mark.smoke
class TestPostsFiltering:
    def test_get_posts_with_limit(self, http_client, api_base_url):
        response = http_client.get(f"{api_base_url}/posts?_limit=5")

        assert response.status_code == 200
        posts = response.json()
        assert len(posts) == 5

    @pytest.mark.parametrize("start", [0, 10, 20])
    def test_get_posts_with_pagination(self, http_client, api_base_url, start):
        response = http_client.get(f"{api_base_url}/posts?_limit=5&_start={start}")

        assert response.status_code == 200
        posts = response.json()
        assert len(posts) <= 5

    def test_filter_posts_by_user(self, http_client, api_base_url):
        response = http_client.get(f"{api_base_url}/posts?userId=1")

        assert response.status_code == 200
        posts = response.json()
        assert isinstance(posts, list)
        assert all(post["userId"] == 1 for post in posts)

    def test_get_comments_for_post(self, http_client, api_base_url):
        response = http_client.get(f"{api_base_url}/posts/1/comments")

        assert response.status_code == 200
        comments = response.json()
        assert isinstance(comments, list)
        assert all("email" in comment and "body" in comment for comment in comments)


@pytest.mark.api
@pytest.mark.regression
class TestPostStateVerification:
    def test_create_post_response_matches_payload(self, http_client, api_base_url):
        payload = {
            "title": "State Verification Title",
            "body": "State verification body content",
            "userId": 5,
        }

        response = http_client.post(f"{api_base_url}/posts", json=payload)

        assert response.status_code == 201
        created = response.json()
        assert created["title"] == payload["title"]
        assert created["body"] == payload["body"]
        assert created["userId"] == payload["userId"]
        assert isinstance(created["id"], int)

    def test_patch_preserves_untouched_fields(self, http_client, api_base_url):
        # First fetch the original post to get baseline values
        original = http_client.get(f"{api_base_url}/posts/1").json()

        patch_payload = {"title": "Patched Title Only"}
        response = http_client.patch(f"{api_base_url}/posts/1", json=patch_payload)

        assert response.status_code == 200
        patched = response.json()
        assert patched["title"] == patch_payload["title"]
        assert patched["body"] == original["body"]
        assert patched["userId"] == original["userId"]

    def test_delete_post_returns_empty_object(self, http_client, api_base_url):
        response = http_client.delete(f"{api_base_url}/posts/1")

        assert response.status_code == 200
        assert response.json() == {}

    def test_update_nonexistent_post_response(self, http_client, api_base_url):
        # JSONPlaceholder mock limitation: PUT on a non-existent resource
        # (id > 100) returns 500 instead of 404, as the mock does not support
        # creating resources via PUT for out-of-range IDs.
        payload = {
            "title": "Title for nonexistent post",
            "body": "Body for nonexistent post",
            "userId": 1,
        }

        response = http_client.put(f"{api_base_url}/posts/999", json=payload)

        assert response.status_code == 500
