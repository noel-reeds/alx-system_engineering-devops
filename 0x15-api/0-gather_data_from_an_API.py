#!/usr/bin/python3
"""Retrieves data from an API"""

import requests
import sys
if __name__ == "__main__":
    userId = int(sys.argv[1])
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    done = 0
    pending = 0
    for todo in todos:
        if todo.get('userId') == userId:
            if todo.get('completed') is True:
                done += 1
            else:
                pending += 1
    tasks = pending + done
    print("Employee {} is done with tasks({}/{})".format(users[userId]['name'], done, tasks))
    for todo in todos:
        if todo.get('userId') == userId and todo.get('completed') is True:
            print("\t {}".format(todo.get('title')))
