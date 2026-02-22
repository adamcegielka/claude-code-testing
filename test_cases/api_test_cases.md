# API Test Cases

## JSONPlaceholder - Posts

### TC-API-001: Get All Posts
- **ID:** TC-API-001
- **Title:** Retrieve all posts
- **Mark:** smoke, api
- **Steps:**
  1. Send GET request to `/posts`
- **Expected Result:**
  - Status code: 200
  - Response is a JSON array
  - Array contains exactly 100 items
  - Each item has fields: `id`, `userId`, `title`, `body`

---

### TC-API-002: Get Single Post
- **ID:** TC-API-002
- **Title:** Retrieve a single post by ID
- **Mark:** smoke, api
- **Steps:**
  1. Send GET request to `/posts/1`
- **Expected Result:**
  - Status code: 200
  - Response contains `id: 1`
  - Response contains non-empty `title`, `body`, `userId`

---

### TC-API-003: Get Non-Existent Post
- **ID:** TC-API-003
- **Title:** Retrieve a post that does not exist
- **Mark:** regression, api
- **Steps:**
  1. Send GET request to `/posts/999`
- **Expected Result:**
  - Status code: 404

---

### TC-API-004: Create Post
- **ID:** TC-API-004
- **Title:** Create a new post
- **Mark:** regression, api
- **Steps:**
  1. Send POST request to `/posts` with body:
     ```json
     {"title": "Test Post", "body": "Test body", "userId": 1}
     ```
- **Expected Result:**
  - Status code: 201
  - Response echoes back `title`, `body`, `userId`
  - Response contains a new `id` field

---

### TC-API-005: Update Post
- **ID:** TC-API-005
- **Title:** Update an existing post
- **Mark:** regression, api
- **Steps:**
  1. Send PUT request to `/posts/1` with updated fields
- **Expected Result:**
  - Status code: 200
  - Response reflects updated `title` and `body`

---

### TC-API-006: Delete Post
- **ID:** TC-API-006
- **Title:** Delete an existing post
- **Mark:** regression, api
- **Steps:**
  1. Send DELETE request to `/posts/1`
- **Expected Result:**
  - Status code: 200

---

## Reqres.in - Users

### TC-API-007: List Users with Pagination
- **ID:** TC-API-007
- **Title:** List users on page 2
- **Mark:** smoke, api
- **Steps:**
  1. Send GET request to `/api/users?page=2`
- **Expected Result:**
  - Status code: 200
  - `page` field equals 2
  - `data` is a non-empty array
  - Response includes `total`, `total_pages`, `per_page`

---

### TC-API-008: Get Single User
- **ID:** TC-API-008
- **Title:** Retrieve user by ID
- **Mark:** smoke, api
- **Steps:**
  1. Send GET request to `/api/users/2`
- **Expected Result:**
  - Status code: 200
  - `data.id` equals 2
  - `data` has fields: `email`, `first_name`, `last_name`, `avatar`

---

### TC-API-009: Get Non-Existent User
- **ID:** TC-API-009
- **Title:** Retrieve user that does not exist
- **Mark:** regression, api
- **Steps:**
  1. Send GET request to `/api/users/999`
- **Expected Result:**
  - Status code: 404

---

### TC-API-010: Create User
- **ID:** TC-API-010
- **Title:** Create a new user
- **Mark:** regression, api
- **Steps:**
  1. Send POST request to `/api/users` with body:
     ```json
     {"name": "John Doe", "job": "QA Engineer"}
     ```
- **Expected Result:**
  - Status code: 201
  - Response contains `name`, `job`, `id`, `createdAt`

---

## Reqres.in - Authentication

### TC-API-011: Login Success
- **ID:** TC-API-011
- **Title:** Successful login returns token
- **Mark:** smoke, api
- **Steps:**
  1. Send POST request to `/api/login` with:
     ```json
     {"email": "eve.holt@reqres.in", "password": "cityslicka"}
     ```
- **Expected Result:**
  - Status code: 200
  - Response contains non-empty `token`

---

### TC-API-012: Login Missing Password
- **ID:** TC-API-012
- **Title:** Login fails when password is missing
- **Mark:** smoke, api
- **Steps:**
  1. Send POST request to `/api/login` with only `email`
- **Expected Result:**
  - Status code: 400
  - Response contains `error` field

---

### TC-API-013: Register Success
- **ID:** TC-API-013
- **Title:** Successful registration returns token
- **Mark:** regression, api
- **Steps:**
  1. Send POST request to `/api/register` with:
     ```json
     {"email": "eve.holt@reqres.in", "password": "pistol"}
     ```
- **Expected Result:**
  - Status code: 200
  - Response contains `id` and `token`

---

### TC-API-014: Register Missing Password
- **ID:** TC-API-014
- **Title:** Registration fails when password is missing
- **Mark:** regression, api
- **Steps:**
  1. Send POST request to `/api/register` with only `email`
- **Expected Result:**
  - Status code: 400
  - Response contains `error` field
