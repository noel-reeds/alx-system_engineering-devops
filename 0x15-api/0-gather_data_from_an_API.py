#!/usr/bin/python3
"""Retrieves data from an API"""

import requests
import sys
if __name__ == "__main__":
    Id = int(sys.argv[1])
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    re = requests.get('https://jsonplaceholder.typicode.com/users').json()
    d = 0
    p = 0
    for todo in todos:
        if todo.get('userId') == Id:
            if todo.get('completed') is True:
                d += 1
            else:
                p += 1
    t = p + d
    for r in re:
        if r.get('id') == Id:
            print("Employee {} is done with tasks({}/{})".format(r.get('name'), d, t))
    for todo in todos:
        if todo.get('userId') == Id and todo.get('completed') is True:
            print("\t {}".format(todo.get('title')))
