# Task Tracker

**Description:**

*This Python script is a command-line tool for managing tasks stored in a task.json file. It uses several functions: addTask to add new tasks, findTaskByID to locate tasks, updateTask to modify tasks, deleteTask to remove tasks, markInProgress to mark tasks as in-progress, and markAsDone to mark tasks as completed. The listTask function displays tasks based on their status. The script processes command-line arguments to execute these functions, enabling efficient task management through a dynamic JSON file.*

**How to Use:**

To use this script, follow these steps:

1. *Setup*: Ensure you have Python installed on your system. Save the script in a file, for example, task-cli.py.

2. *Initialize*: Run the script to create an initial task.json file:
```sh
python task-cli.py
```
3. *Add a Task*: Add a new task with the add command:
```sh
python task-cli.py add "Buy groceries"
```

4. *Update a Task*: Update an existing task by ID:
```sh
python task-cli.py update 1 "Buy milk"
```

5. *Delete a Task*: Delete a task by ID:
```sh
python task-cli.py delete 1
```

6. *Mark In Progress*: Mark a task as in-progress:
```sh
python task-cli.py mark-in-progress 1
```

7. *Mark as Done*: Mark a task as done:
```sh
python task-cli.py mark-done 1
```

8. *List Tasks*: List all tasks or filter by status (all, todo, in-progress, done):
```sh
python task-cli.py list
python task-cli.py list todo
```
Make sure to replace 1 with the actual task ID and the task description accordingly. Happy task managing!

**Features:**

* Add, Update, Delete Tasks: Manage your tasks efficiently.
* Change Task Status: Mark tasks as in-progress or done.
* List Tasks: View tasks by their status.
* Command-Line Interface: Simple commands for task management.
* Persistent Storage: Tasks are saved in a JSON file for future access.

**Requirement:**

* Python 3

**Link:**

*This is a project as part of*
[roadmap.sh](https://roadmap.sh/projects/task-tracker)