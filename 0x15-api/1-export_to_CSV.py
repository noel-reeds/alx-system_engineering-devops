#!/usr/bin/python3
"""Exports API contents to CSV."""

import csv
import requests
import sys
if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    row = []
    for user in users:
        if user.get('id') == employee_id:
            username = user.get('username')
            break
    for todo in todos:
        if todo.get('userId') == employee_id:
            row.append([employee_id, username,
                        todo.get('completed'), todo.get('title')])
        filename = f"{employee_id}.csv"
        with open(filename, mode="w", encoding='utf-8') as file3:
            writer = csv.writer(file3, quoting=csv.QUOTE_ALL)
            writer.writerows(row)
