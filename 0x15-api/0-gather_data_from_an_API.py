#!/usr/bin/pyton3
"""Return information about employee todo list progress"""
import requests
from sys import argv


if __name__ == '__main__':
    """Request from an API"""
    employee_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(employee_id))
    name = user.json()['name']
    all_todo = 'https://jsonplaceholder.typicode.com/all_todo?userId={}'\
        .format(employee_id)

    tasks = requests.get("{}".format(all_todo)).json()
    done_tasks = []
    for task in tasks:
        if task['completed'] is True:
            done_tasks.append(task)
    total_tasks = len(tasks)
    done_count = len(done_tasks)
    print("Employee {} is done with tasks({}/{}):".
          format(name, done_count, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task['title']))
