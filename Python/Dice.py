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
    if varDiceType == "d4":
        varRoll = random.randint(1,4)
    elif varDiceType == "d6":
        varRoll = random.randint(1,6)
    elif varDiceType == "d8":
        varRoll = random.randint(1,8)
    elif varDiceType == "d12":
        varRoll = random.randint(1,12)
    elif varDiceType == "d20":
        varRoll = random.randint(1,20)
    elif varDiceType == "d100":
        varRoll = random.randint(1,100)
    else:
        varRoll = "Unrecognized type"

    #return value
    return varRoll
