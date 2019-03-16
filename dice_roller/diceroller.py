#!/user/bin/python3
 
import dice

print('')
print('')
print('Welcome to the D&D DMs Dice Roller!')
print('')

continue_executing = True

while continue_executing is True:
    
    dieType = input('What type of die would you like to roll? (enter q to quit)\n')
    dieNumber = 1

    if not dieType:
        print('empty input detected')
        continue

    parts = dieType.split(' ')

    
    if len(parts) > 1:
        dieType = parts[1]
        dieNumber = parts[0]
    else:
        dieType = parts[0]    
    
    if dieType == 'q' or dieType == 'Q':
        break
    else:        
        results = dice.roll_dice(dieType, int(dieNumber))
        total = 0
        

        print('')
        for x in results:

            if x == -1:
                print('Invalid die type supplied!')
                break
            else:
                total = total + int(x)
                print(dieType + ' rolled: ' + str(x))      
                
        if total > 0:
            print('')
            print('The total combined score is: ' + str(total))
            print('')
    