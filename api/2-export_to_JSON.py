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
    user_id = int(argv[1])

    data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            user_id)).json()
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            user_id)).json()

    id_name = argv[1]
    filename = id_name + '.json'

    with open(filename, "w") as file:
        tasks_list = []
        for t in user:
            tasks_dict = {}
            tasks_dict['task'] = t['title']
            tasks_dict['completed'] = t['completed']
            tasks_dict['username'] = data['username']
            tasks_list.append(tasks_dict)
        json_dict = json.dumps({'{}'.format(user_id): tasks_list})
        file.write(json_dict)


if __name__ == "__main__":
    export_to_json()
