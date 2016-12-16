import csv
def count_votes(fileName):
    returnDict = dict()
    dataList = []
    with open(fileName) as file:
        read = csv.DictReader(file)
        csvData = list(read)
        dataList.append(csvData)
    voteList = []
    for x in dataList:
        for y in x:
            for y in y['Hvaða verkefni fannst þér skemmtilegust?'].split(','):
                voteList.append(y.strip())
    for i in voteList:
        if i == '':
            pass
        elif returnDict.get( i ):
            tmp = returnDict[ i ]
            tmp += 1
            returnDict[i] = tmp
        else:
            returnDict[i] = int(1) 
    return returnDict