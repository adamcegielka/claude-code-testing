# CLAUDE.md

## Project Overview

Educational QA project using Python, pytest, and Playwright. GitHub: `adamcegielka/claude-code-testing`.

## Commands

```bash
# Install dependencies
uv pip install -r requirements.txt
playwright install chromium

# Run all tests
pytest

# API tests
pytest tests/api/ -m api -v

# UI tests (headless)
pytest tests/ui/ -m ui -v

# UI tests (headed)
pytest tests/ui/ -m ui --headed -v

# Smoke / regression
pytest -m smoke -v
pytest -m regression -v
```

HTML report is auto-generated as `report.html` (configured in `pytest.ini`).

## Project Structure

```
conftest.py              # Root fixtures: api_base_url, dummyjson_base_url, ui_base_url
pytest.ini               # Markers + --html=report.html
requirements.txt         # pytest, pytest-html, pytest-playwright, requests

tests/
  api/
    conftest.py          # http_client (requests.Session), auth_token (JWT)
    test_posts.py        # JSONPlaceholder CRUD
    test_users.py        # DummyJSON users
    test_auth.py         # DummyJSON login/register
  ui/
    conftest.py          # todo_page fixture
    pages/
      base_page.py       # BasePage (Playwright)
      todo_page.py       # TodoPage : BasePage
    test_todo.py         # TodoMVC UI tests

test_cases/
  api_test_cases.md
  ui_test_cases.md
```

## Test Services

| Service | URL |
|---------|-----|
| JSONPlaceholder | https://jsonplaceholder.typicode.com |
| DummyJSON | https://dummyjson.com |
| TodoMVC | https://demo.playwright.dev/todomvc |

## pytest Markers

| Marker | Scope |
|--------|-------|
| `api` | All API tests |
| `ui` | All UI tests |
| `smoke` | Critical path |
| `regression` | Full coverage |

## Conventions

- Fixtures live in `conftest.py` at the appropriate scope level (root or per-suite).
- UI tests use Page Object Model — page logic goes in `tests/ui/pages/`, not in test files.
- All test functions are marked with at least one pytest marker (`api`/`ui`) and one severity marker (`smoke`/`regression`).
- Keep API and UI tests strictly separated under `tests/api/` and `tests/ui/`.
