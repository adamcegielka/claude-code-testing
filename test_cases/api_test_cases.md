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

## restful-api.dev - Objects

### TC-API-007: List All Objects
- **ID:** TC-API-007
- **Title:** Retrieve all objects
- **Mark:** smoke, api
- **Steps:**
  1. Send GET request to `/objects`
- **Expected Result:**
  - Status code: 200
  - Response is a JSON array
  - Array contains at least one item
  - Each item has fields: `id`, `name`

---

### TC-API-008: Get Single Object
- **ID:** TC-API-008
- **Title:** Retrieve a single object by ID
- **Mark:** smoke, api
- **Steps:**
  1. Send GET request to `/objects/7`
- **Expected Result:**
  - Status code: 200
  - `id` equals `"7"`
  - Response contains `name` and `data`

---

### TC-API-009: Get Non-Existent Object
- **ID:** TC-API-009
- **Title:** Retrieve an object that does not exist
- **Mark:** regression, api
- **Steps:**
  1. Send GET request to `/objects/nonexistent-id-999`
- **Expected Result:**
  - Status code: 404

---

### TC-API-010: Create Object
- **ID:** TC-API-010
- **Title:** Create a new object
- **Mark:** regression, api
- **Steps:**
  1. Send POST request to `/objects` with body:
     ```json
     {"name": "QA Test Device", "data": {"year": 2024, "price": 999.99}}
     ```
- **Expected Result:**
  - Status code: 200
  - Response contains `name`, `id`, `createdAt`

---

### TC-API-011: Update Object (PUT)
- **ID:** TC-API-011
- **Title:** Fully replace an object
- **Mark:** regression, api
- **Steps:**
  1. Create a new object via POST
  2. Send PUT request to `/objects/{id}` with updated body
- **Expected Result:**
  - Status code: 200
  - Response reflects new `name`
  - Response contains `updatedAt`

---

### TC-API-012: Partial Update Object (PATCH)
- **ID:** TC-API-012
- **Title:** Partially update an object's name
- **Mark:** regression, api
- **Steps:**
  1. Create a new object via POST
  2. Send PATCH request to `/objects/{id}` with `{"name": "Patched Name"}`
- **Expected Result:**
  - Status code: 200
  - `name` equals `"Patched Name"`
  - Response contains `updatedAt`

---

### TC-API-013: Delete Object
- **ID:** TC-API-013
- **Title:** Delete an existing object
- **Mark:** regression, api
- **Steps:**
  1. Create a new object via POST
  2. Send DELETE request to `/objects/{id}`
- **Expected Result:**
  - Status code: 200
  - Response message contains the deleted object's `id`

---

### TC-API-014: List Objects by IDs
- **ID:** TC-API-014
- **Title:** Retrieve a filtered list of objects by multiple IDs
- **Mark:** regression, api
- **Steps:**
  1. Send GET request to `/objects?id=3&id=5&id=7`
- **Expected Result:**
  - Status code: 200
  - Response is a JSON array with exactly 3 items
  - Returned IDs are `"3"`, `"5"`, `"7"`
