from playwright.sync_api import Page

from tests.ui.pages.base_page import BasePage


class TodoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._input = page.get_by_placeholder("What needs to be done?")
        self._todo_items = page.locator(".todo-list li")
        self._toggle_all = page.locator(".toggle-all")
        self._clear_completed_btn = page.get_by_role("button", name="Clear completed")

    def add_todo(self, text: str):
        self._input.fill(text)
        self._input.press("Enter")

    def complete_todo(self, index: int):
        self._todo_items.nth(index).locator(".toggle").click()

    def delete_todo(self, index: int):
        item = self._todo_items.nth(index)
        item.hover()
        item.locator(".destroy").click()

    def get_todo_count(self) -> int:
        return self._todo_items.count()

    def get_todo_text(self, index: int) -> str:
        return self._todo_items.nth(index).locator("label").inner_text()

    def is_todo_completed(self, index: int) -> bool:
        return "completed" in (self._todo_items.nth(index).get_attribute("class") or "")

    def filter_by(self, filter_name: str):
        self.page.get_by_role("link", name=filter_name).click()
        # Wait for the selected filter to reflect the route change
        self.page.locator(".filters .selected", has_text=filter_name).wait_for()

    def get_items_left_count(self) -> int:
        text = self.page.locator(".todo-count strong").inner_text()
        return int(text)

    def clear_completed(self):
        self._clear_completed_btn.click()

    def toggle_all(self):
        self._toggle_all.click()

    def edit_todo(self, index: int, new_text: str):
        item = self._todo_items.nth(index)
        item.locator("label").dblclick()
        edit_input = item.locator(".edit")
        edit_input.fill(new_text)
        edit_input.press("Enter")

    def cancel_edit_todo(self, index: int):
        item = self._todo_items.nth(index)
        item.locator("label").dblclick()
        item.locator(".edit").press("Escape")

    def get_items_left_text(self) -> str:
        return self.page.locator(".todo-count").inner_text().strip()

    def is_footer_visible(self) -> bool:
        return self.page.locator(".footer").is_visible()

    def is_clear_completed_visible(self) -> bool:
        return self._clear_completed_btn.is_visible()

    def is_input_empty(self) -> bool:
        return self._input.input_value() == ""
