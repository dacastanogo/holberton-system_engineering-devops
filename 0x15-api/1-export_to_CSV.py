#!/usr/bin/python3
"""Return information about employee todo list, export to CSV"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(employee_id))
    json_user = json.loads(user.text)
    username = json_user.get('username')
    all_todo = 'https://jsonplaceholder.typicode.com/all_todo?userId={}'\
        .format(employee_id)
    todo_json = json.loads(user.text)
    tasks = []
    for task in todo_json:
        tasks.append(task)
    with open(sys.argv[1] + ".csv", "w") as f:
        for task in tasks:
            data = ['"' + sys.argv[1] + '"', '"' + username + '"', '"' +
                    str(task.get('completed')) + '"', '"' + task.get('title') +
                    '"']
            f.write(",".join(data) + '\n')
