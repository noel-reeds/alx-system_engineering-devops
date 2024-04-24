#!/usr/bin/python3
"""Exports to CSV"""

import csv
import requests
import sys
if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    for todo in todos:
        if todo.get('userId') == employee_id:
            for user in users:
                if user.get('id') == employee_id:
                    output = f"{user.get('id')},\
{user.get('username')},{todo.get('completed')},\
{todo.get('title')}\n"
                    with open("output.txt", "a") as myFile:
                        myFile.write(output)
with open("output.txt", "r") as myFile:
    stripped = (line.strip() for line in myFile)
    splitted = (line.split(",") for line in myFile if line)
    with open("USER_ID.csv", "w") as file3:
        writer = csv.writer(file3)
        writer.writerows(splitted)
