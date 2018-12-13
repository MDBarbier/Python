#!/user/bin/python3
 
import random
import sys

print('loaded dice.py')

def roll_dice(varDiceType, numDice):
     
    random.seed()

    results = []

    for x in range(numDice):
        if varDiceType == "d6" or varDiceType == "D6":
            varRoll = random.randint(1,6)
        elif varDiceType == "D4" or varDiceType == "d4":
            varRoll = random.randint(1,4)
        elif varDiceType == "d8" or varDiceType == "D8":
            varRoll = random.randint(1,8)
        elif varDiceType == "d12" or varDiceType == "D12":
            varRoll = random.randint(1,12)
        elif varDiceType == "d20" or varDiceType == "D20":
            varRoll = random.randint(1,20)
        elif varDiceType == "d100" or varDiceType == "D100":
            varRoll = random.randint(1,100)    
        else:
            varRoll = -1
        
        results.append(varRoll)
            
    return results