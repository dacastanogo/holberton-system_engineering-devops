#!/usr/bin/pyton3
"""Return information about employee todo list progress"""
import requests
from sys import argv
if __name__ == "__main__":

    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(argv[1]))

    name = response.json()['name']

    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
        .format(argv[1])

    tasks = requests.get("{}".format(url)).json()
    tasks_com = []
    task_im = []
    for task in tasks:
        if task['completed'] is True:
            tasks_com.append(task)
        else:
            task_im.append(task)

    num_total = len(tasks)
    num_complete = len(tasks_com)

    print("Employee {} is done with tasks({}/{}):".
          format(name, num_complete, num_total))
    for task in tasks_com:
        print("\t {}".format(task['title']))
