# UI Test Cases - TodoMVC

**Target URL:** https://demo.playwright.dev/todomvc

---

### TC-UI-001: Add a Single Todo
- **ID:** TC-UI-001
- **Title:** Add a new todo item
- **Mark:** smoke, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Click on the input field (placeholder: "What needs to be done?")
  3. Type "Buy groceries"
  4. Press Enter
- **Expected Result:**
  - Todo item "Buy groceries" appears in the list
  - Item count is 1
  - Input field is cleared

---

### TC-UI-002: Add Multiple Todos
- **ID:** TC-UI-002
- **Title:** Add multiple todo items
- **Mark:** smoke, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add "First task", "Second task", "Third task"
- **Expected Result:**
  - All 3 items visible in the list
  - Footer shows "3 items left"

---

### TC-UI-003: Complete a Todo
- **ID:** TC-UI-003
- **Title:** Mark a todo as completed
- **Mark:** smoke, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add "Complete this task"
  3. Click the checkbox next to the item
- **Expected Result:**
  - Item appears with strikethrough text
  - Item has "completed" CSS class
  - Items left counter decreases by 1

---

### TC-UI-004: Uncheck a Completed Todo
- **ID:** TC-UI-004
- **Title:** Toggle completed todo back to active
- **Mark:** regression, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add "Toggle task"
  3. Click checkbox to complete
  4. Click checkbox again to uncheck
- **Expected Result:**
  - Item no longer has "completed" class
  - Items left counter returns to original value

---

### TC-UI-005: Delete a Todo
- **ID:** TC-UI-005
- **Title:** Delete a todo item
- **Mark:** regression, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add "Task to delete"
  3. Hover over the item
  4. Click the "×" (destroy) button
- **Expected Result:**
  - Item removed from the list
  - List count is 0

---

### TC-UI-006: Delete One of Multiple Todos
- **ID:** TC-UI-006
- **Title:** Delete specific item from a list
- **Mark:** regression, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add "Keep this" and "Delete this"
  3. Hover over "Delete this"
  4. Click "×" button
- **Expected Result:**
  - Only "Keep this" remains
  - List count is 1

---

### TC-UI-007: Filter Active Todos
- **ID:** TC-UI-007
- **Title:** Filter to show only active todos
- **Mark:** regression, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add "Active task" and "Completed task"
  3. Complete "Completed task"
  4. Click "Active" filter link
- **Expected Result:**
  - Only "Active task" is visible
  - "Completed task" is hidden

---

### TC-UI-008: Filter Completed Todos
- **ID:** TC-UI-008
- **Title:** Filter to show only completed todos
- **Mark:** regression, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add "Active task" and "Completed task"
  3. Complete "Completed task"
  4. Click "Completed" filter link
- **Expected Result:**
  - Only "Completed task" is visible
  - "Active task" is hidden

---

### TC-UI-009: Filter All Todos
- **ID:** TC-UI-009
- **Title:** Show all todos after filtering
- **Mark:** regression, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add 2 tasks, complete one
  3. Switch to "Active" filter
  4. Click "All" filter link
- **Expected Result:**
  - Both items are visible

---

### TC-UI-010: Clear Completed Todos
- **ID:** TC-UI-010
- **Title:** Remove all completed todos at once
- **Mark:** regression, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add "Keep this" and "Remove this"
  3. Complete "Remove this"
  4. Click "Clear completed" button
- **Expected Result:**
  - Only "Keep this" remains
  - "Clear completed" button disappears

---

### TC-UI-011: Items Left Counter
- **ID:** TC-UI-011
- **Title:** Verify items left counter accuracy
- **Mark:** smoke, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add 3 tasks
  3. Complete 1 task
- **Expected Result:**
  - Counter shows "2 items left"
