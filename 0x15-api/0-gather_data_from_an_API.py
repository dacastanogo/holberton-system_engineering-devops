#!/usr/bin/pyton3
"""Return information about employee TODO list progress"""
import requests
from sys import argv


def api_request():
    """Request from an API"""
    employee_id = argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    todo = requests.get(url_todo, params={'userId': employee_id})
    user = requests.get(url_user, params={'id': employee_id})

    todo_json_list = todo.json()
    user_json_list = user.json()

    done_tasks = []
    total_tasks = len(todo_json_list)
    employee = user_json_list[0].get('name')

    for task in todo_json_list:
        if task.get('completed') is True:
            done_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee, len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))

if __name__ == '__main__':
    api_request()
