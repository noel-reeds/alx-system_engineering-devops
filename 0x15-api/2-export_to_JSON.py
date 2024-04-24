#!/usr/bin/python3
"""Exports API content into a JSON file."""

import json
import requests
import sys


def main():
    """main."""
    employee_id = int(sys.argv[1])
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    tasks = []
    task_d = {}
    user_dict = {user['id']: user['username'] for user in users}
    for todo in todos:
        if todo.get('userId') == employee_id:
            task_d = {}
            task_d['task'] = todo.get('title')
            task_d['completed'] = todo.get('completed')
            task_d['username'] = user_dict.get(todo.get('userId'))
            tasks.append(task_d)
    user = {employee_id: tasks}
    with open("USER_ID.json", mode="w", encoding="utf-8") as myFile:
        json.dump(user, myFile)


if __name__ == "__main__":
    main()
