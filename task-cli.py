from sys import argv
import json
from datetime import datetime
from os import path

# Define status constants
STATUS_DONE = 'done'
STATUS_TODO = 'todo'
STATUS_IN_PROGRESS = 'in-progress'
TIMESTAMP_FORMAT = '%d-%m-%Y %H:%M'
timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)

def addTask(task_description: str):
    """Add a task to the task list."""

    with open('task.json', 'r+') as f:
        data = json.load(f)
        task_id = len(data['tasks']) + 1
        created_at = timestamp
        updated_at = timestamp
        task = {
            'id': task_id,
            'description': task_description,
            'status': STATUS_TODO,
            'createdAt': created_at,
            'updatedAt': updated_at
        }
        data['tasks'].append(task)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        print(f"Task added successfully (ID: {task_id})")


def findTaskByID(data, task_id: int):
    """Find a task by ID in the task list."""

    for task in data['tasks']:
        if task['id'] == task_id:
            return task


def updateTask(task_id: int, task_description: str):
    """Update a task in the task list."""

    with open('task.json', 'r+') as f:
        data = json.load(f)
        task = findTaskByID(data, task_id)
        if task is not None:
            task['description'] = task_description
            task['updatedAt'] = timestamp
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            print(f"Task updated successfully (ID: {task_id})")
        else:
            print(f"Task with ID {task_id} not found.")


def deleteTask(task_id: int):
    """Delete a task from the task list."""

    with open('task.json', 'r+') as f:
        data = json.load(f)
        task = findTaskByID(data, task_id)
        if task is not None:
            data['tasks'].remove(task)
            for t in data['tasks']:
                if t['id'] > task_id:
                    t['id'] -= 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            print(f"Task deleted successfully (ID: {task_id})")
        else:
            print(f"Task with ID {task_id} not found.")


def markInProgress(task_id: int):
    """Mark a task as in-progress in the task list."""

    with open('task.json', 'r+') as f:
        data = json.load(f)
        task = findTaskByID(data, task_id)
        if task is not None:
            task['status'] = STATUS_IN_PROGRESS
            task['updatedAt'] = timestamp
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            print(f"Task marked as in-progress (ID: {task_id})")
        else:
            print(f"Task with ID {task_id} not found.")


def markAsDone(task_id: int):
    """Mark a task as done in the task list."""

    with open('task.json', 'r+') as f:
        data = json.load(f)
        task = findTaskByID(data, task_id)
        if task is not None:
            task['status'] = STATUS_DONE
            task['updatedAt'] = timestamp
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            print(f"Task marked as done (ID: {task_id})")
        else:
            print(f"Task with ID {task_id} not found.")


def listTask(args = 'all'):
    """List tasks in the task list."""

    with open('task.json', 'r') as f:
        data = json.load(f)

    flag = False
    if args == 'todo':
        print('Tasks to do:')
        for task in data['tasks']:
            if task['status'] == 'todo':
                print(f"{task['id']}. {task['description']}")
                flag = True
        if not flag:
            print('No tasks to do. Add some tasks!')
    elif args == 'in-progress':
        print('Tasks in progress:')
        for task in data['tasks']:
            if task['status'] == 'in-progress':
                print(f"{task['id']}. {task['description']}")
                flag = True
        if not flag:
            print('No tasks in progress. Start working on your tasks!')
    elif args == 'done':
        print('Tasks done:')
        for task in data['tasks']:
            if task['status'] == 'done':
                print(f"{task['id']}. {task['description']}")
                flag = True
        if not flag:
            print('No tasks done. Finish your tasks!')
    else:
        print('All tasks:')
        for task in data['tasks']:
            print(f"{task['id']}. {task['description']} ({task['status']}) ")
            flag = True
        if not flag:
            print('No tasks found. Add some tasks!')


if not path.exists('task.json'):
    with open('task.json', 'w') as f:
        data = {
            'tasks': []
        }
        json.dump(data, f, indent=4)

if len(argv) < 2:
    print('Manage your tasks with this simple CLI tool.\n')
    print('USAGE:\n\tpython task-cli.py <command> <args>\n')
    print('COMMANDS')
    print('\tadd:\t\t\tAdd a new task')
    print('\tupdate:\t\t\tUpdate a task')
    print('\tdelete:\t\t\tDelete a task')
    print('\tmark-in-progress:\tMark a task as in-progress')
    print('\tmark-done:\t\tMark a task as done')
    print('\tlist:\t\t\tList tasks\n')
    print('EXAMPLES')
    print('\tpython task-cli.py add "Buy groceries"')
    print('\tpython task-cli.py update 1 "Buy milk"')
    print('\tpython task-cli.py delete 1')
    print('\tpython task-cli.py mark-in-progress 1\n')
    print('LEARN MORE')
    print('\tVisit https://github.com/rohit-373/task-tracker')
    quit()

command = argv[1]
command_args = argv[2:]
if command == 'add':
    if len(command_args) >= 1:
        addTask(command_args[0])
    else:
        print('Error: Missing task description for add command.')
elif command == 'update':
    if len(command_args) >= 2:
        updateTask(int(command_args[0]), command_args[1])
    else:
        print('Error: Missing arguments for update command.')
elif command == 'delete':
    if len(command_args) >= 1:
        deleteTask(int(command_args[0]))
    else:
        print('Error: Missing task ID for delete command.')
elif command == 'mark-in-progress':
    if len(command_args) >= 1:
        markInProgress(int(command_args[0]))
    else:
        print('Error: Missing task ID for mark-in-progress command.')
elif command == 'mark-done':
    if len(command_args) >= 1:
        markAsDone(int(command_args[0]))
    else:
        print('Error: Missing task ID for mark-done command.')
elif command == 'list':
    if len(command_args) == 1:
        listTask(command_args[0])
    else:
        listTask()
else:
    print('Invalid command')