#!/usr/bin/python3
"""Return information about employee todo list, export to CSV"""
import json
import requests
import sys


if __name__ == "__main__":

    user = requests.get("https://jsonplaceholder.typicode.com/users/" +
                        sys.argv[1])
    json_user = json.loads(user.text)
    username = json_user.get('username')
    all_todo = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                            "?userId=" + sys.argv[1])
    todo_json = json.loads(all_todo.text)
    tasks = []
    for task in todo_json:
        tasks.append(task)
    with open(sys.argv[1] + ".csv", "w") as f:
        for task in tasks:
            data = ['"' + sys.argv[1] + '"', '"' + username + '"', '"' +
                    str(task.get('completed')) + '"', '"' + task.get('title') +
                    '"']
            f.write(",".join(data) + '\n')
