import pytest


@pytest.mark.ui
@pytest.mark.smoke
class TestAddTodo:
    def test_add_single_todo(self, todo_page):
        todo_page.add_todo("Buy groceries")

        assert todo_page.get_todo_count() == 1
        assert todo_page.get_todo_text(0) == "Buy groceries"

    def test_add_multiple_todos(self, todo_page):
        todo_page.add_todo("First task")
        todo_page.add_todo("Second task")
        todo_page.add_todo("Third task")

        assert todo_page.get_todo_count() == 3

    def test_items_left_counter(self, todo_page):
        todo_page.add_todo("Task one")
        todo_page.add_todo("Task two")

        assert todo_page.get_items_left_count() == 2


@pytest.mark.ui
@pytest.mark.smoke
class TestCompleteTodo:
    def test_complete_todo(self, todo_page):
        todo_page.add_todo("Complete this task")
        todo_page.complete_todo(0)

        assert todo_page.is_todo_completed(0)

    def test_complete_reduces_items_left(self, todo_page):
        todo_page.add_todo("Task one")
        todo_page.add_todo("Task two")
        todo_page.complete_todo(0)

        assert todo_page.get_items_left_count() == 1

    def test_uncheck_completed_todo(self, todo_page):
        todo_page.add_todo("Toggle task")
        todo_page.complete_todo(0)
        assert todo_page.is_todo_completed(0)

        todo_page.complete_todo(0)
        assert not todo_page.is_todo_completed(0)


@pytest.mark.ui
@pytest.mark.regression
class TestDeleteTodo:
    def test_delete_todo(self, todo_page):
        todo_page.add_todo("Task to delete")
        todo_page.delete_todo(0)

        assert todo_page.get_todo_count() == 0

    def test_delete_one_of_multiple(self, todo_page):
        todo_page.add_todo("Keep this")
        todo_page.add_todo("Delete this")
        todo_page.delete_todo(1)

        assert todo_page.get_todo_count() == 1
        assert todo_page.get_todo_text(0) == "Keep this"


@pytest.mark.ui
@pytest.mark.regression
class TestFilters:
    def test_filter_active(self, todo_page):
        todo_page.add_todo("Active task")
        todo_page.add_todo("Completed task")
        todo_page.complete_todo(1)

        todo_page.filter_by("Active")

        assert todo_page.get_todo_count() == 1
        assert todo_page.get_todo_text(0) == "Active task"

    def test_filter_completed(self, todo_page):
        todo_page.add_todo("Active task")
        todo_page.add_todo("Completed task")
        todo_page.complete_todo(1)

        todo_page.filter_by("Completed")

        assert todo_page.get_todo_count() == 1
        assert todo_page.get_todo_text(0) == "Completed task"

    def test_filter_all(self, todo_page):
        todo_page.add_todo("Task one")
        todo_page.add_todo("Task two")
        todo_page.complete_todo(0)

        todo_page.filter_by("Active")
        todo_page.filter_by("All")

        assert todo_page.get_todo_count() == 2


@pytest.mark.ui
@pytest.mark.regression
class TestClearCompleted:
    def test_clear_completed(self, todo_page):
        todo_page.add_todo("Keep this")
        todo_page.add_todo("Remove this")
        todo_page.complete_todo(1)

        todo_page.clear_completed()

        assert todo_page.get_todo_count() == 1
        assert todo_page.get_todo_text(0) == "Keep this"

    def test_clear_all_completed(self, todo_page):
        todo_page.add_todo("Task one")
        todo_page.add_todo("Task two")
        todo_page.complete_todo(0)
        todo_page.complete_todo(1)

        todo_page.clear_completed()

        assert todo_page.get_todo_count() == 0


@pytest.mark.ui
@pytest.mark.regression
class TestEditTodo:
    def test_edit_todo_text(self, todo_page):
        todo_page.add_todo("Original text")
        todo_page.edit_todo(0, "Updated text")
        assert todo_page.get_todo_text(0) == "Updated text"

    def test_cancel_edit_with_escape(self, todo_page):
        todo_page.add_todo("Original text")
        todo_page.cancel_edit_todo(0)
        assert todo_page.get_todo_text(0) == "Original text"


@pytest.mark.ui
@pytest.mark.regression
class TestToggleAll:
    def test_toggle_all_completes_all(self, todo_page):
        todo_page.add_todo("Task one")
        todo_page.add_todo("Task two")
        todo_page.toggle_all()
        assert todo_page.is_todo_completed(0)
        assert todo_page.is_todo_completed(1)

    def test_toggle_all_unmarks_all(self, todo_page):
        todo_page.add_todo("Task one")
        todo_page.add_todo("Task two")
        todo_page.toggle_all()
        todo_page.toggle_all()
        assert not todo_page.is_todo_completed(0)
        assert not todo_page.is_todo_completed(1)


@pytest.mark.ui
@pytest.mark.smoke
class TestEmptyState:
    def test_footer_hidden_when_no_todos(self, todo_page):
        assert not todo_page.is_footer_visible()

    def test_input_cleared_after_add(self, todo_page):
        todo_page.add_todo("Some task")
        assert todo_page.is_input_empty()


@pytest.mark.ui
@pytest.mark.regression
class TestEdgeCases:
    def test_empty_todo_not_added(self, todo_page):
        todo_page._input.press("Enter")
        assert todo_page.get_todo_count() == 0

    def test_singular_items_left_counter(self, todo_page):
        todo_page.add_todo("Only task")
        assert "1 item left" in todo_page.get_items_left_text()

    def test_clear_completed_hidden_when_no_completed(self, todo_page):
        todo_page.add_todo("Active task")
        assert not todo_page.is_clear_completed_visible()
