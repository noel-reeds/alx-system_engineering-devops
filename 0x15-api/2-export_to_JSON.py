#!/usr/bin/python3
"""Exports API content into a JSON file"""

import csv
import json
import requests
import sys
if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    tasks = []
    task_d = {}
    for user in users:
        if user.get('id') == employee_id:
            for todo in todos:
                if todo.get('userId') == employee_id:
                    task_d = {}
                    task_d['title'] = todo.get('title')
                    task_d['completed'] = todo.get('completed')
                    task_d['username'] = user.get('username')
                    tasks.append(task_d)
    user = {employee_id: tasks}
    with open("USER_ID.json", mode="w", encoding="utf-8") as myFile:
        json.dump(user, myFile)
