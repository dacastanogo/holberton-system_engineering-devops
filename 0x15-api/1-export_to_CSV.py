#!/usr/bin/pyton3
"""Return information about employee TODO list progress"""
import requests
import sys
import csv

requested_url = "https://jsonplaceholder.typicode.com/"


def api_request():
    """Request from an API"""
    if len(sys.argv) < 2:
        return print('USAGE:', __file__, '<employee id>')
    employee_id = sys.argv[1]
    try:
        _employee_id = int(sys.argv[1])
    except ValueError:
        return print("Employee id must be an integer")

    response = requests.get(requested_url + 'users/' + employee_id)
    if response.status_code == 404:
        return print('User id not found')
    elif response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    user = response.json()

    response = requests.get(requested_url + 'todos/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    todos = response.json()

    user_todos = [todo for todo in todos
                  if todo.get('userId') == user.get('id')]
    completed = [todo for todo in user_todos if todo.get('completed')]
    print('Employee', user.get('name'),
          'is done with tasks({}/{}):'.
          format(len(completed), len(user_todos)))
    [print('\t', todo.get('title')) for todo in completed]

    with open(employee_id + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n',
                            quoting=csv.QUOTE_ALL)
        [writer.writerow(['{}'.format(field) for field in
                          (todo.get('userId'), user.get('username'),
                           todo.get('completed'), todo.get('title'))])
         for todo in user_todos]

if __name__ == '__main__':
    api_request()
