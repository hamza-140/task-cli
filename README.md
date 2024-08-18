
---

<div align="center">
    
  # Task Tracker CLI
   
  [Overview](#🎯-overview) •
  [Features](#✨-features) •
  [Getting Started](#🚀-getting-started) •
  [Usage](#📘-usage) •
  [API](#📚-api)
  
</div>
  
---

## 🎯 Overview

Task Tracker is a command-line interface (CLI) application designed to help users manage and track their tasks efficiently. It allows you to add, update, delete, and list tasks, as well as mark them as in progress or completed. The main objective is to provide a simple and straightforward tool for tracking what needs to be done, what is currently being worked on, and what has been completed.

## ✨ Features

- **Task Management**: Add, update, and delete tasks using simple CLI commands.
- **Status Tracking**: Mark tasks as `todo`, `in-progress`, or `done`.
- **Task Listing**: List all tasks or filter them by their status (`todo`, `in-progress`, `done`).
- **Persistent Storage**: Tasks are stored in a JSON file, ensuring data is preserved between sessions.
- **Error Handling**: Gracefully handles errors and edge cases, such as attempting to delete a non-existent task.

## 🚀 Getting Started

To get a local copy up and running, follow these steps:

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Git

### 🔥 Installation

  Clone the repository:

   ```bash
   git clone https://github.com/hamza-140/task-cli.git
   cd task-tracker
   ```

## 📘 Usage

Below are examples of how to use the Task Tracker CLI:

- **Adding a new task**:

  ```bash
  python task-tracker.py add "Buy groceries"
  # Output: Task added successfully (ID: 1)
  ```

- **Updating a task**:

  ```bash
  python task-tracker.py update 1 "Buy groceries and cook dinner"
  # Output: Task #1's description updated successfully!
  ```

- **Marking a task as in progress**:

  ```bash
  python task-tracker.py mark-in-progress 1
  # Output: Task #1's status updated successfully!
  ```

- **Listing all tasks**:

  ```bash
  python task-tracker.py list
  ```

- **Listing tasks by status**:

  ```bash
  python task-tracker.py list done
  ```

- **Deleting a task**:

  ```bash
  python task-tracker.py delete 1
  # Output: Task #1 deleted successfully!
  ```

## 📚 API

This section documents the main functions of the CLI, detailing the parameters, return values, and examples.

### `add_task(description)`

Creates a new task with the specified description.

| Parameter    | Type   | Description                      |
|--------------|--------|----------------------------------|
| `description`| String | A short description of the task. |

**Returns**: Confirmation that the task was added, along with its unique ID.

**Example**:

```python
add_task("Buy groceries")
```

### `delete_task(id)`

Deletes the task with the specified ID.

| Parameter | Type   | Description                    |
|-----------|--------|--------------------------------|
| `id`      | String | The ID of the task to delete.  |

**Returns**: A boolean indicating whether the deletion was successful.

**Example**:

```python
delete_task("1")
```

### `update_task(id, description)`

Updates the description of the task with the specified ID.

| Parameter    | Type   | Description                           |
|--------------|--------|---------------------------------------|
| `id`         | String | The ID of the task to update.         |
| `description`| String | The new description of the task.      |

**Returns**: Confirmation that the task was updated.

**Example**:

```python
update_task("1", "Buy groceries and cook dinner")
```

### `mark_task(status, id)`

Updates the status of the task with the specified ID.

| Parameter | Type   | Description                                   |
|-----------|--------|-----------------------------------------------|
| `status`  | String | The new status of the task (`todo`, `in-progress`, `done`). |
| `id`      | String | The ID of the task to update.                 |

**Returns**: Confirmation that the task's status was updated.

**Example**:

```python
mark_task("done", "1")
```

### `display()`

Lists all tasks in the JSON file.

**Returns**: A list of all tasks.

**Example**:

```python
display()
```

### `display_status(status)`

Lists all tasks with the specified status.

| Parameter | Type   | Description                      |
|-----------|--------|----------------------------------|
| `status`  | String | The status of tasks to display.  |

**Returns**: A list of tasks with the specified status.

**Example**:

```python
display_status("done")
```

--- 

## CC
https://roadmap.sh/projects/task-tracker