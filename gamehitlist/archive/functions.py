#!/user/bin/python3

import json
from pprint import pprint


def exit_program():
    input('Press any key to exit')


def add_game():
    name = input('Please enter the game name:\n')
    genre = input('Please enter the game genre:\n')

    return Game(name, genre)

def create_profile(name):
    create_profile = read_config_key("profile")
    if not create_profile:
        edit_config_key("profile", name)
    else:
        return create_profile

def create_list(listname, list):
    edit_config_key(listname, list)

def get_profile():
    get_profile = read_config_key("profile")
    return get_profile

def new_line(num_lines):
    one_to_ten = range(0, num_lines)
    for _ in one_to_ten:
        print('*')


def open_data_file_read():
    path = r'data/data.json'
    file = open(path, 'r')
    return file


def open_config_file_append():
    path = r'data/data.json'
    file = open(path, 'a')
    return file


def open_config_file_write():
    path = r'data/data.json'
    file = open(path, 'w')
    return file


def read_config_key(key_name):
    file = open_data_file_read()
    data = file.read()
    json_data = json.loads(data)
    return json_data[key_name]


def edit_config_key(key_name, key_value):

    with open('data/data.json') as data_file:
        data = json.load(data_file) #load the data file as json

    if data.get(key_name):
        if data[key_name] != key_value:  # update value if changed
            data[key_name] = key_value
    else:
        data[key_name] = key_value  # insert new key if the key does not exist

    file = open_config_file_write() # oper for writing
    json.dump(data, file) # dump the entire json file back 
    file.close()

class Game:
    def __init__(self, gamename, gamegenre):
        self.gamename = gamename
        self.gamegenre = gamegenre
