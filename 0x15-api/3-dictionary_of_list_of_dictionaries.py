#!/usr/bin/python3
"""Displays tasks for each user."""

import json
import requests

if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    tasks = []
    userss = {}
    for user in users:
        for todo in todos:
            task_d = {}
            task_d['username'] = user.get('username')
            task_d['task'] = todo.get('title')
            task_d['completed'] = todo.get('completed')
            tasks.append(task_d)
        userId = user.get('id')
        userss[userId] = tasks
    filename = "todo_all_employees.json"
    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(userss, myFile)
