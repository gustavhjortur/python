import csv, datetime, calendar
def release_days(cast, dates, actors):
    moviList = []
    with open(cast) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for name in actors:
                if row['name'] == name:
                    moviList.append([row['title'], row['year']])
    returnDict = dict()
    returnList = []
    read = []
    with open(dates) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['country'] == 'USA': 
                read.append(row)
            else:
                pass
        for f in read:
            for titill in moviList:
                if ( f['title'] == titill[0] and f['year'] == titill[1] ):
                    WeekDayNumber = ( datetime.date(int((f['date']).split('-')[0]),
                               int((f['date']).split('-')[1]),
                               int((f['date']).split('-')[2])).isoweekday() )
                    returnList.append( [WeekDayNumber, f['title']] )
    for i in returnList:
        if returnDict.get( i[0] ):
            tmp = returnDict[ i[0] ]
            tmp.add(i[1])
            returnDict[i[0]] = tmp
        else:
            returnDict[i[0]] = { i[1] }
    return returnDict
