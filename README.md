# QA Learning Project - Python / pytest / Playwright

Projekt edukacyjny dla testera średniozaawansowanego, który chce nauczyć się używać **Claude Code** do codziennej pracy QA.

## Cele edukacyjne

1. **pytest fixtures** - conftest.py, scope, parametrize
2. **API testing** - asercje na status code, body, headers
3. **Page Object Model** - separacja logiki UI od testów
4. **Playwright** - selektory, akcje, asercje
5. **Jak używać Claude Code** - generowanie test cases, debugowanie, refaktoryzacja

---

## Struktura projektu

```
├── requirements.txt         # Zależności Python
├── pytest.ini               # Konfiguracja pytest (markery, opcje)
├── conftest.py              # Globalne fixtures (base URLs)
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
│       │   ├── base_page.py # Page Object Model - klasa bazowa
│       │   └── todo_page.py # Page Object dla TodoMVC
│       └── test_todo.py     # Testy UI - TodoMVC
│
└── test_cases/
    ├── api_test_cases.md    # Manualne przypadki testowe dla API
    └── ui_test_cases.md     # Manualne przypadki testowe dla UI
```

---

## Instalacja

```bash
uv pip install -r requirements.txt
playwright install chromium
```

---

## Uruchamianie testów

```bash
# Wszystkie testy
pytest

# Tylko testy API
pytest tests/api/ -m api -v

# Tylko testy UI (headless)
pytest tests/ui/ -m ui -v

# Testy UI z widoczną przeglądarką
pytest tests/ui/ -m ui --headed -v

# Testy smoke
pytest -m smoke -v

# Testy regression
pytest -m regression -v

# Konkretny plik
pytest tests/api/test_posts.py -v

# Z raportem HTML (domyślnie włączony w pytest.ini)
pytest tests/api/ -v
# Raport: report.html
```

---

## Markery pytest

| Marker       | Opis                              |
|--------------|-----------------------------------|
| `api`        | Testy API (requests)              |
| `ui`         | Testy UI (Playwright)             |
| `smoke`      | Testy smoke - kluczowe funkcje    |
| `regression` | Testy regresyjne - pełne pokrycie |

---

## Serwisy testowe

| Serwis | URL | Opis |
|--------|-----|------|
| JSONPlaceholder | https://jsonplaceholder.typicode.com | Fake REST API (posty) |
| DummyJSON | https://dummyjson.com | REST API z auth (użytkownicy, JWT) |
| TodoMVC | https://demo.playwright.dev/todomvc | Aplikacja UI do testów |

---

## Jak używać Claude Code w pracy QA

### Generowanie test cases

```
Napisz test pytest dla endpointu GET /api/users/{id} na reqres.in.
Test powinien sprawdzać status 200 i strukturę odpowiedzi.
```

### Debugowanie testów

```
Ten test failuje z błędem AssertionError: assert 404 == 200.
Endpoint: GET /posts/0 na jsonplaceholder.typicode.com.
Jak naprawić?
```

### Refaktoryzacja

```
Mam 5 testów, które wszystkie tworzą sesję HTTP osobno.
Jak wyciągnąć to do fixtures w conftest.py?
```

### Analiza pokrycia

```
Przejrzyj tests/api/test_posts.py i powiedz jakich przypadków testowych brakuje.
```

### Tworzenie Page Objects

```
Napisz Page Object dla formularza logowania na stronie example.com/login.
Powinien mieć metody: fill_credentials(email, password), submit(), get_error_message().
```

---

## Struktura fixtures (conftest.py)

```
conftest.py (root)
├── api_base_url    → "https://jsonplaceholder.typicode.com"
├── reqres_base_url → "https://reqres.in"
└── ui_base_url     → "https://demo.playwright.dev/todomvc"

tests/api/conftest.py
├── http_client     → requests.Session (scope=session)
└── auth_token      → JWT accessToken z dummyjson.com /auth/login

tests/ui/conftest.py
└── todo_page       → TodoPage(page) z nawigacją do ui_base_url
```
