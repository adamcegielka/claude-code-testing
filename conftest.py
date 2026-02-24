import pytest


@pytest.fixture(scope="session")
def api_base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def dummyjson_base_url():
    return "https://dummyjson.com"


@pytest.fixture(scope="session")
def ui_base_url():
    return "https://demo.playwright.dev/todomvc"


@pytest.fixture(scope="session")
def restful_api_base_url():
    return "https://api.restful-api.dev"
