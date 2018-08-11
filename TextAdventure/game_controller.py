#!/user/bin/python3

import HelperFunctions
import dice
from pprint import pprint

def start_game():
    HelperFunctions.new_line(1)
    print('Welcome to the TAG (Text Adventure Game)')
    HelperFunctions.new_line(2)
    name = HelperFunctions.get_name()
    HelperFunctions.new_line(1)
    character = roll_character()
    pprint(vars(character))
    HelperFunctions.new_line(1)
    print(name + ' begins their descent into the Dungeon!')
    HelperFunctions.edit_config_key("playerName", name)
    HelperFunctions.new_line(4)
    print('Game Over! Goodbye ' + HelperFunctions.read_config_key("playerName"))
    HelperFunctions.new_line(1)

def roll_character():
    strength = dice.roll_dice("d20")
    dexterity = dice.roll_dice("d20")
    constitution = dice.roll_dice("d20")
    intelligence = dice.roll_dice("d20")
    while (strength + dexterity + constitution + intelligence) < 40:
        strength = dice.roll_dice("d20")
        dexterity = dice.roll_dice("d20")
        constitution = dice.roll_dice("d20")
        intelligence = dice.roll_dice("d20")
    return Player(strength, dexterity, constitution, intelligence)    

class Player:
    def __init__(self, strength, dexterity, constitution, intelligence):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
