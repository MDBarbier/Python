#!/user/bin/python3

import random
import sys

#method takes a string argument, if none supplied uses d6 as default
def rolldie(varDiceType = "d6"):

    #convert supplied argument to lower case
    requestedDice = varDiceType.lower()

    #seed the random
    random.seed()

    #conditional based on supplied argument
    if requestedDice == "d4":
        varRoll = random.randint(1,4)
    elif requestedDice == "d6":
        varRoll = random.randint(1,6)
    elif requestedDice == "d8":
        varRoll = random.randint(1,8)
    elif requestedDice == "d12":
        varRoll = random.randint(1,12)
    elif requestedDice == "d20":
        varRoll = random.randint(1,20)
    elif requestedDice == "d100":
        varRoll = random.randint(1,100)
    else:
        varRoll = "Unrecognized type"

    #return value
    return varRoll
