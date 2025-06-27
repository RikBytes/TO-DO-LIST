
# 📝 To-Do List (Python CLI)

A simple command-line To-Do List app written in Python. You can add, view, remove, and mark tasks as completed. All tasks are saved in a local `todos.json` file.

## Features
- Add task with name, title, description, and duration.
- View task details by name.
- Remove tasks.
- Mark tasks as completed.
- Load and list all saved tasks.

## How to Run
Make sure Python is installed, then run:
```bash
python main.py
````

## File Structure

* `main.py` – Main menu and user interface.
* `tasks.py` – Task management functions.
* `inputs.py` – User input functions.
* `todos.json` – Task storage (JSON file).

## Sample JSON

```json
{
  "tasks": {
    "task1": {
      "title": "Study",
      "description": "Complete Python project",
      "duration": 60,
      "completed": false
    }
  }
}
```