# QA Learning Project - Python / pytest / Playwright

An educational project for intermediate-level QA engineers who want to learn how to use **Claude Code** in their daily QA work.

## Learning Objectives

1. **pytest fixtures** - conftest.py, scope, parametrize
2. **API testing** - assertions on status code, body, headers
3. **Page Object Model** - separation of UI logic from tests
4. **Playwright** - selectors, actions, assertions
5. **How to use Claude Code** - generating test cases, debugging, refactoring

---

## Project Structure

```
├── requirements.txt         # Python dependencies
├── pytest.ini               # pytest configuration (markers, options)
├── conftest.py              # Global fixtures (base URLs)
│
├── tests/
│   ├── api/
│   │   ├── conftest.py      # HTTP client, auth_token
│   │   ├── test_posts.py    # CRUD posts - jsonplaceholder.typicode.com
│   │   ├── test_users.py    # CRUD users - reqres.in
│   │   └── test_auth.py     # Login / Register - reqres.in
│   │
│   └── ui/
│       ├── conftest.py      # todo_page fixture
│       ├── pages/
│       │   ├── base_page.py # Page Object Model - base class
│       │   └── todo_page.py # Page Object for TodoMVC
│       └── test_todo.py     # UI tests - TodoMVC
│
└── test_cases/
    ├── api_test_cases.md    # Manual test cases for API
    └── ui_test_cases.md     # Manual test cases for UI
```

---

## Installation

```bash
uv pip install -r requirements.txt
playwright install chromium
```

---

## Running Tests

```bash
# All tests
pytest

# API tests only
pytest tests/api/ -m api -v

# UI tests only (headless)
pytest tests/ui/ -m ui -v

# UI tests with visible browser
pytest tests/ui/ -m ui --headed -v

# Smoke tests
pytest -m smoke -v

# Regression tests
pytest -m regression -v

# Specific file
pytest tests/api/test_posts.py -v

# With HTML report (enabled by default in pytest.ini)
pytest tests/api/ -v
# Report: report.html
```

---

## pytest Markers

| Marker       | Description                          |
|--------------|--------------------------------------|
| `api`        | API tests (requests)                 |
| `ui`         | UI tests (Playwright)                |
| `smoke`      | Smoke tests - critical functionality |
| `regression` | Regression tests - full coverage     |

---

## Test Services

| Service | URL | Description |
|--------|-----|------|
| JSONPlaceholder | https://jsonplaceholder.typicode.com | Fake REST API (posts) |
| DummyJSON | https://dummyjson.com | REST API with auth (users, JWT) |
| TodoMVC | https://demo.playwright.dev/todomvc | UI application for testing |

---

## Using Claude Code for QA Work

### Generating Test Cases

```
Write a pytest test for the GET /api/users/{id} endpoint on reqres.in.
The test should verify status 200 and the response structure.
```

### Debugging Tests

```
This test fails with AssertionError: assert 404 == 200.
Endpoint: GET /posts/0 on jsonplaceholder.typicode.com.
How do I fix it?
```

### Refactoring

```
I have 5 tests that each create an HTTP session separately.
How do I extract that into fixtures in conftest.py?
```

### Coverage Analysis

```
Review tests/api/test_posts.py and tell me which test cases are missing.
```

### Creating Page Objects

```
Write a Page Object for the login form at example.com/login.
It should have methods: fill_credentials(email, password), submit(), get_error_message().
```

---

## Fixture Structure (conftest.py)

```
conftest.py (root)
├── api_base_url    → "https://jsonplaceholder.typicode.com"
├── reqres_base_url → "https://reqres.in"
└── ui_base_url     → "https://demo.playwright.dev/todomvc"

tests/api/conftest.py
├── http_client     → requests.Session (scope=session)
└── auth_token      → JWT accessToken from dummyjson.com /auth/login

tests/ui/conftest.py
└── todo_page       → TodoPage(page) with navigation to ui_base_url
```
