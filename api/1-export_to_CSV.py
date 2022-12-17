#!/usr/bin/python3
"""
Script to export data in the CSV format.
"""
import csv
import json
import requests
from sys import argv


def csv_format():
    """
    Data collection and organization
    """

    response_api_data = requests.get(
        'https://jsonplaceholder.typicode.com/todos')
    response_api_users = requests.get(
        'https://jsonplaceholder.typicode.com/users')

    data = response_api_data.text
    users = response_api_users.text
    id_name = argv[1]
    id = int(argv[1])
    filename = id_name + '.csv'

    parse_json_data = json.loads(data)
    parse_json_users = json.loads(users)

    with open(filename, 'w') as file:
        fieldnames = ['userId', 'name', 'completed', 'title', 'id']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        for i in range(len(parse_json_data)):
            d = dict(parse_json_data[i])
            if d['userId'] == id:
                writer.writerow(d)

    with open(filename, 'r') as file:
        reader = csv.reader(file, quotechar='"')
        for row in reader:
            for i in row:
                print('"{}", '.format(i), end="")
            print()


if __name__ == "__main__":
    csv_format()
