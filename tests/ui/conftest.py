import pytest
from playwright.sync_api import Page

from tests.ui.pages.todo_page import TodoPage


@pytest.fixture
def todo_page(page: Page, ui_base_url: str) -> TodoPage:
    todo = TodoPage(page)
    todo.navigate(ui_base_url)
    return todo
