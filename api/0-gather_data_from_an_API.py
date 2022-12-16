#!/usr/bin/python3
import requests
from sys import argv
import json


def fetch_data_from_api():
    response_api_data = requests.get(
        'https://jsonplaceholder.typicode.com/todos')
    response_api_users = requests.get(
        'https://jsonplaceholder.typicode.com/users')

    data = response_api_data.text
    users = response_api_users.text

    parse_json_data = list(json.loads(data))
    parse_json_users = list(json.loads(users))
    id = int(argv[1])

    user_name = []
    for dic in parse_json_users:
        if dic['id'] == id:
            user_name.append(dic['name'])

    total_tasks_done, total_tasks = 0, 0
    title_task = []

    for dic in parse_json_data:
        if dic['userId'] == id:
            if dic['completed'] is True:
                total_tasks_done += 1
                title_task.append(dic['title'])
            total_tasks += 1

    print("Employee {} is done with tasks({}/{}):". format(
        user_name[0], total_tasks_done, total_tasks))
    for title in title_task:
        print("\t ", title)


if __name__ == "__main__":
    fetch_data_from_api()
