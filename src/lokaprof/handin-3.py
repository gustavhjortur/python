def fixNames(string):
    if string == '.':
        return string
    if ('./' in string):
        string = string[2:].split('/')[-1]
    else:
        string = string.split('/')[-1] 
    return string
    
def process_du(inputText):
    inputLines = inputText.splitlines()
    listinn = dict()
    for x in inputLines:
        listinn[int(x.split()[0])] = x.split(maxsplit=1)[1] 
    listIndex =  sorted(listinn, reverse=True)
    returnList = []
    for x in listIndex:
        ( fixNames( listinn[x] ) )
        returnList.append( fixNames( listinn[x] ) )
    return returnList