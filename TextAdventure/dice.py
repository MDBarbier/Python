#!/user/bin/python3

import random
import sys

def roll_dice(varDiceType):
	
	random.seed()
	
	if varDiceType == "d6":
		varRoll = random.randint(1,6)
	elif varDiceType == "D6":
		varRoll = random.randint(1,6)
	elif varDiceType == "D4":
		varRoll = random.randint(1,4)
	elif varDiceType == "d4":
		varRoll = random.randint(1,4)
	elif varDiceType == "d8":
		varRoll = random.randint(1,8)
	elif varDiceType == "D8":
		varRoll = random.randint(1,8)	
	elif varDiceType == "d12":
		varRoll = random.randint(1,12)
	elif varDiceType == "D12":
		varRoll = random.randint(1,12)	
	elif varDiceType == "d20":
		varRoll = random.randint(1,20)
	elif varDiceType == "D20":
		varRoll = random.randint(1,20)
	else:
		varRoll = "error"
		
	return varRoll

