#!/user/bin/python3
 
import dice

print('Welcome to the D&D DMs Dice Roller!')

continue_executing = True

while continue_executing is True:
    
    dieType = input('What type of die would you like to roll? (enter q to quit)\n')
    dieNumber = 1

    if not dieType:
        print('empty input detected')
        continue

    dieTypeArray = list(dieType)

    # check whether the user has requested a specific number of dice
    if str.isdigit(dieTypeArray[0]):

        #is the next character a digit too?
        if str.isdigit(dieTypeArray[1]):
            dieNumber = dieTypeArray[0] + dieTypeArray[1]
            dieType = dieTypeArray[3] + dieTypeArray[4]  
        else: 
            dieNumber = dieTypeArray[0]
            dieType = dieTypeArray[2] + dieTypeArray[3]        


    #check the dietype input and process 
    if dieType == 'q' or dieType == 'Q':
        break
    else:        
        results = dice.roll_dice(dieType, int(dieNumber))
        total = 0
        
        for x in results:
            total = total + int(x)
            print(dieType + ' rolled: ' + str(x))      

        print('The total combined score is' + str(total))
    