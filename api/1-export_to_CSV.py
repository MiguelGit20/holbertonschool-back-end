#!/usr/bin/python3
"""
Script to export data in the CSV format.
"""
import requests
from sys import argv


def csv_format():
    """
    Data collection and organization
    """
    user_id = int(argv[1])

    data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            user_id)).json()

    id_name = argv[1]
    filename = id_name + '.csv'

    with open(filename, "w") as file:
        for t in user:
            file.write('"{}","{}","{}","{}"\n'.format(
                user_id, data['username'], t['completed'], t['title']))


if __name__ == "__main__":
    csv_format()
