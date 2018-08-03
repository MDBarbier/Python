#!/user/bin/python3

import json
from pprint import pprint


def exit_program():
    input('Press any key to exit')


def get_name():
    name = input('Please provide a character name:\n')

    return name


def new_line(num_lines):
    one_to_ten = range(0, num_lines)
    for _ in one_to_ten:
        print('*')


def open_data_file_read():
    path = r'data\data.json'
    file = open(path, 'r')
    return file


def open_config_file_append():
    path = r'data\data.json'
    file = open(path, 'a')
    return file


def open_config_file_write():
    path = r'data\data.json'
    file = open(path, 'w')
    return file


def read_config_key(key_name):
    file = open_data_file_read()
    data = file.read()
    json_data = json.loads(data)
    return json_data[key_name]


def edit_config_key(key_name, key_value):

    with open('data/data.json') as data_file:
        data = json.load(data_file)

    if data.get(key_name):
        if data[key_name] != key_value:  # update value if changed
            data[key_name] = key_value
    else:
        data[key_name] = key_value  # insert new key

    file = open_config_file_write()
    json.dump(data, file)
    file.close()
