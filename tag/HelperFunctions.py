#!/user/bin/python3

import json

def Exit():
    input('Press any key to exit')
    
def GetName():
    name = input('Please provide a character name:\n')

    return name

def NewLine(numOfLines):
    onetoten = range(0, numOfLines)
    for _ in onetoten:
        print('*')

def OpenConfigFileForRead():
    path = r'data\config.json'
    file = open(path, 'r')
    return file

def OpenConfigFileForAppend():
    path = r'data\config.json'
    file = open(path, 'a')
    return file

def OpenConfigFileForWrite():
    path = r'data\config.json'
    file = open(path, 'w')
    return file

def ReadConfigKey(keyName):
    file = OpenConfigFileForRead()    
    data = file.read()  
    jsondata = json.loads(data)  
    return jsondata[keyName]

def EditConfigKey(keyName, keyValue):
    flag = False
    existingFileData = OpenConfigFileForRead().readlines()
    newfileData = "" #to hold new version the data
    for line in existingFileData:
        print(line)
        
        line = line.replace(',', ' ')

        if (line.__contains__(keyName)): #in here need to check if the current line is the key we want
            line = '"' + keyName + '":"' + keyValue + '"' + '\n' #edit the line to put in the new value        
            #newfileData += line
            flag = True
        
        if line.__contains__("}") and flag is False:    
            newfileData +=  '\n' + '"' + keyName + '":"' + keyValue + '"' #add new line 
            newfileData += '\n' + line 
        elif line.__contains__("}") and flag is True:    
            newfileData +=  '\n' + '"' + keyName + '":"' + keyValue + '"' #add new line 
            newfileData += '\n' +line 
        elif line.__contains__("{"):
            newfileData += line
        else:
            newfileData += line + ","# write the line to the new file as-is     

    print('NewFileData:' + newfileData)
    file = OpenConfigFileForWrite()
    file.write(newfileData)
    file.close()    