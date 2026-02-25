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

---

### TC-UI-012: Edit Todo Text
- **ID:** TC-UI-012
- **Title:** Edit an existing todo item text
- **Mark:** regression, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add "Original text"
  3. Double-click the item label
  4. Clear the edit input and type "Updated text"
  5. Press Enter
- **Expected Result:**
  - Item text changes to "Updated text"

---

### TC-UI-013: Cancel Edit with Escape
- **ID:** TC-UI-013
- **Title:** Cancel todo edit by pressing Escape
- **Mark:** regression, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add "Original text"
  3. Double-click the item label to enter edit mode
  4. Press Escape
- **Expected Result:**
  - Item text remains "Original text"
  - Edit mode is cancelled

---

### TC-UI-014: Toggle All Completes All
- **ID:** TC-UI-014
- **Title:** Toggle all marks all todos as completed
- **Mark:** regression, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add "Task one" and "Task two"
  3. Click the toggle-all chevron
- **Expected Result:**
  - Both items have "completed" CSS class

---

### TC-UI-015: Toggle All Unmarks All
- **ID:** TC-UI-015
- **Title:** Second toggle all unmarks all completed todos
- **Mark:** regression, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add "Task one" and "Task two"
  3. Click toggle-all to complete all
  4. Click toggle-all again
- **Expected Result:**
  - Both items no longer have "completed" class

---

### TC-UI-016: Footer Hidden When No Todos
- **ID:** TC-UI-016
- **Title:** Footer is not visible on empty list
- **Mark:** smoke, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Do not add any todos
- **Expected Result:**
  - Footer element (.footer) is not visible

---

### TC-UI-017: Input Cleared After Adding Todo
- **ID:** TC-UI-017
- **Title:** Input field is empty after adding a todo
- **Mark:** smoke, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Type "Some task" and press Enter
- **Expected Result:**
  - Input field value is empty after submission

---

### TC-UI-018: Empty Todo Not Added
- **ID:** TC-UI-018
- **Title:** Pressing Enter on empty input does not add a todo
- **Mark:** regression, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Press Enter without typing anything
- **Expected Result:**
  - Todo list count remains 0

---

### TC-UI-019: Singular Items Left Counter
- **ID:** TC-UI-019
- **Title:** Items left counter uses singular form for one item
- **Mark:** regression, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add exactly one todo "Only task"
- **Expected Result:**
  - Footer shows "1 item left" (not "1 items left")

---

### TC-UI-020: Clear Completed Hidden When No Completed Items
- **ID:** TC-UI-020
- **Title:** Clear Completed button is hidden when no todos are completed
- **Mark:** regression, ui
- **Steps:**
  1. Navigate to TodoMVC
  2. Add "Active task" (do not complete it)
- **Expected Result:**
  - "Clear completed" button is not visible
