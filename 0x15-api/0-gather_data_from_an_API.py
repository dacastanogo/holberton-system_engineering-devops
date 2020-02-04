#!/usr/bin/pyton3
"""Return information about employee todo list progress"""
import requests
from sys import argv


if __name__ == '__main__':

    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(argv[1]))
    name = response.json()['name']
    tasks_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
        .format(argv[1])

    tasks = requests.get("{}".format(tasks_url)).json()
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
