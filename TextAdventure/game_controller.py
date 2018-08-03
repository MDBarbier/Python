#!/user/bin/python3

import HelperFunctions


def start_game():
    HelperFunctions.new_line(1)
    print('Welcome to the TAG (Text Adventure Game)')
    HelperFunctions.new_line(2)
    name = HelperFunctions.get_name()
    HelperFunctions.new_line(1)
    print(name + ' begins their descent into the Dungeon!')
    HelperFunctions.edit_config_key("playerName", name)
    HelperFunctions.new_line(4)
    print('Game Over! Goodbye ' + HelperFunctions.read_config_key("playerName"))
    HelperFunctions.new_line(1)
