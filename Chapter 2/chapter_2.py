import sqlite3
import argparse
from datetime import date


class Task:
    def __init__(self, name, deadline, description):
        self.name = name
        self.deadline = deadline
        self.description = description


conn = sqlite3.connect('task.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS tasks (
            name text,
            deadline text,
            description text,
            task_hash text

            )""")


def add_task(task):
    task_hash = hash(task)
    with conn:
        c.execute("INSERT INTO tasks VALUES (:name, :deadline, :description, :task_hash)", {
                  'name': task.name, 'deadline': task.deadline, 'description': task.description, 'task_hash': task_hash})
    print(f"Task {task.name} created! The hashcode is {task_hash}")


def remove_task(task_hash):
    with conn:
        c.execute("DELETE from tasks WHERE task_hash = :task_hash",
                  {'task_hash': task_hash, })
    after_remove = c.rowcount
    if after_remove == 1:
        print(f"Task with hash {task_hash} deleted")
    else:
        print("Please input correct hash number")


def get_all_tasks():
    c.execute("SELECT * FROM tasks")
    print("Your tasks: ")
    return c.fetchall()


def get_today_tasks(current_date):
    c.execute("SELECT * FROM tasks WHERE deadline = :deadline",
              {'deadline': current_date})
    print("Your today tasks: ")
    return c.fetchall()


def update_task_name(task_hash, name):
    with conn:
        c.execute("UPDATE tasks SET name = :name WHERE task_hash = :task_hash",
                  {'task_hash': task_hash, 'name': name})
    print(f"Task with the hash {task_hash} updated!")


def update_task_deadline(task_hash, deadline):
    with conn:
        c.execute("""UPDATE tasks SET deadline = :deadline
                    WHERE task_hash = :task_hash""",
                  {'task_hash': task_hash, 'deadline': deadline})
    print(f"Task with the hash {task_hash} updated!")


def update_task_description(task_hash, description):
    with conn:
        c.execute("""UPDATE tasks SET description = :description
                    WHERE task_hash = :task_hash""",
                  {'task_hash': task_hash, 'description': description})
    print(f"Task with the hash {task_hash} updated!")


parser = argparse.ArgumentParser()

parser.add_argument('operation',
                    help='Which operation do you want? There is "add", "update", "remove" and "list"',
                    )

parser.add_argument('-n', '--name',
                    help='name of your task'
                    )
parser.add_argument('-dead', '--deadline',
                    help='Deadline of your task. Date should be looks like: YYYY-MM-DD'
                    )

parser.add_argument('-desc', '--description',
                    help='Description of your task'
                    )
parser.add_argument('--hash',
                    help='Input your task hash to update or delete'
                    )
list_group = parser.add_mutually_exclusive_group()
list_group.add_argument('--all',
                        action='store_true',
                        help='Used with list operation. It display all tasks'
                        )
list_group.add_argument('--today',
                        action='store_true',
                        help='Used with list operation. It display task for today'
                        )


args = parser.parse_args()

if args.operation == "add":
    if args.name != None and args.deadline != None and args.description != None:
        task = Task(args.name, args.deadline, args.description)
        add_task(task)
    else:
        print("Missing arguments. Please write name, deadline and description")

elif args.operation == "list":
    if args.all:
        all_tasks = get_all_tasks()
        for task in all_tasks:
            print(task)
    elif args.today:
        current_date = date.today()
        today_task = get_today_tasks(current_date)
        for task in today_task:
            print(task)
    else:
        print("Missing argument. After 'list' please write --all or --today")

elif args.operation == "remove":
    remove_task(args.hash)

elif args.operation == "update":
    if args.name:
        update_task_name(args.hash, args.name)
    if args.deadline:
        update_task_deadline(args.hash, args.deadline)
    if args.description:
        update_task_description(args.hash, args.description)

else:
    print("Wrong command. Please type --help for more information")

conn.commit()
conn.close()
