#!/usr/bin/pyton3
"""Return information about employee TODO list progress"""
import requests
from sys import argv


def api_request():
    """Request from an API"""
    employee_id = argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/todos/?userId='
    todo = requests.get(url_todo + employee_id).json()
    user = requests.get(url_user + employee_id).json()
    done_tasks = []
    done_count = 0
    total_tasks = len(todo)
    employee = user[0].get('name')

    for task in todo:
        if task.get('completed'):
            done_tasks.append(task)
            done_count += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee, done_count, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))

if __name__ == '__main__':
    api_request()
