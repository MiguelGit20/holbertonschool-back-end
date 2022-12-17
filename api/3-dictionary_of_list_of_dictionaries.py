#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


def export_to_json():
    """
    Data collection and organization
    """
    filename = 'todo_all_employees.json'
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    dict_data = {}

    for u in user:
        user_task = requests.get(
            'https://jsonplaceholder.typicode.com/user/{}/todos'.format(
                u['id']
            )).json()

        user_t = []
        for t in user_task:
            data_tasks = {}
            data_tasks['username'] = u['username']
            data_tasks['task'] = t['title']
            data_tasks['completed'] = t['completed']
            user_t.append(data_tasks)

        dict_data['{}'.format(u['id'])] = user_t

    with open(filename, "w") as file:
        json_data = json.dumps(dict_data)
        file.write(json_data)


if __name__ == "__main__":
    export_to_json()
