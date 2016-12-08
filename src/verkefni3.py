# 1.



# 2.
def count_names(start):
    from urllib.request import urlopen
    import json
    import re
    fjoldi1 = 0
    fjoldi2 = 0
    res = urlopen('https://mooshak.ru.is/~python/names.json')
    #d = dict(start)
    #d = (res.read().decode('utf-8') )
    read_data = res.read().decode('utf-8')
    data = json.loads(read_data)
    #leit = r'\'nafn\': \'' + start.lower()
    leit = '^' + start
    print(leit)
    for x in data:
        if re.search(leit, str(x.get('Nafn'))):
            print( x, data.index(x))
            #fjoldi2 += int(str(x[-1]))
            fjoldi1 += ( x.get('Fjoldi1') )
            fjoldi2 += ( x.get('Fjoldi2') )
            #tmpnum1 = ( list(map( str, re.split( ' ', str(x).strip(','), maxsplit=6)[3:4] )) )
            #print( tmpnum )
            #tmpnum2 = ( re.split( ' ', str(x).strip(')}'), maxsplit=6)[5:] )
            #print( *tmpnum1 )
            #print( *tmpnum2 )
    #print(json.loads(start).decode('utf-8'))
    for x in data:
        if re.search(r'\t', str(x.get('Nafn'))):
                     print('\t\t', x.get('Nafn'), data.index(x) )
    return (fjoldi1, fjoldi2)


#with open('names.json') as data_file:
#    data = json.loads(data_file)
#
#def count_names(s):
    
nafnalisti = [{"Nafn": "Linddís", "Fjoldi1": 1, "Fjoldi2": 1},
{ "Nafn": "Damjan", "Fjoldi1": 5, "Fjoldi2": 0},
{ "Nafn": "Bjarki", "Fjoldi1": 915, "Fjoldi2": 475},
{ "Nafn": "Þórhildur", "Fjoldi1": 374, "Fjoldi2": 38},]

# 3.
def release_days(cast, dates, actors):
    import csv, datetime, calendar
    #open('fil', encodinc) af f:
    #    read = csv.reader(f)
    #    csvdata = list(reader)
    #print(datetime.datetime.today().weekday())
    #print(datetime.date(2016,12,8).isoweekday())
    #print(calendar.day_name[datetime.date.today().weekday()])
    moviList = []
    with open(cast) as csvfile:
        reader = csv.DictReader(csvfile)
        #for name in actors:
        for row in reader:
            for name in actors:
                if row['name'] == name:
                    #print(row['title'], row['year'], row['name'])
                    moviList.append([row['title'], row['year']])
    #print()
    returnDict = dict()
    returnList = []
    read = []
    with open(dates) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['country'] == 'USA':
                #print('asd')
                read.append(row)
            else:
                pass
                #print('obbosiii')
                #next(row)
            #print(row)

        #print(*read)
        for f in read:
            #print(f['title'])
            for titill in moviList:
                #print(titill[1])
                #print( f['title'],  titill[0], f['country'], 'USA' )
                if ( f['title'] == titill[0] and f['country'] == 'USA'
                     and f['year'] == titill[1] ):
                    #print(f['title'], f['country'], f['date'])
                    WeekDayNumber = ( datetime.date(int((f['date']).split('-')[0]),
                           int((f['date']).split('-')[1]),
                           int((f['date']).split('-')[2])).isoweekday() )
                    returnList.append( [WeekDayNumber, f['title']] )
                    #returnDict = {WeekDayNumber : {row['title']} } 
                    #returnDict[WeekDayNumber] = row['title']
    #print(returnList)
    #print()
    #returnList.sort()
    for i in returnList:
        #print(i[0])
        if returnDict.get( i[0] ):
            tmp = returnDict[ i[0] ]
            tmp.add(i[1])
            #print(tmp)
            returnDict[i[0]] = tmp
            #returnDict[i[0]] = returnDict[ i[0] ].add(i[1])
        else:
            returnDict[i[0]] = { i[1] }
        #for d in i:
        #    print(d )
    print(returnDict)
    return returnDict
#DictReader
#Sniffer


#release_days('data/cast-small.csv', 'data/dates-small.csv', ['Meg Ryan', 'Tom Hanks'] )
release_days('data/cast.csv', 'data/dates.csv', ['Meg Ryan', 'Tom Hanks'] )

# 4.
def parse_submissions(directory):
    import os, shutil, glob, re
    #print( os.walk('.') )
    #print(os.getcwd())
    #print( glob.glob(directory + 'data.tcl') )
    fileList = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == ('data.tcl'):
                 fileList.append(os.path.join(root, file))
    #print(*fileList)
    data = []
    for x in fileList:
        file = open(str(x), 'r')
        content = file.read()
        file.close()
        if ( re.search('Classify Accepted', content) ):
            #print('\tAloop')
            tmpData = content.splitlines()
            #for x in tmpData:
            #    if ( 'Date' in x ):
            #        print( x.split(maxsplit=3)[-1] )
            tmp = []
            tmp.append( int(*[x.split(maxsplit=3)[-1] for x in tmpData if 'Date' in x]) )
            tmp.append( *[x.split(maxsplit=3)[-1] for x in tmpData if 'Team' in x] )
            tmp.append( *[x.split(maxsplit=3)[-1] for x in tmpData if 'Problem' in x] )

            #print( tmp )
            data.append( tmp )
    #print()
    print ( *sorted(data) )
    tuppluListi = []
    for x in sorted(data):
        tuppluListi.append( tuple( x[1:] ) )
        #print(tuppla)
    #print( x for x in sorted(data) if 'Team' in x )
    print()
    #print( content )
    print()
    return tuppluListi

#parse_submissions('tmp/submissions/28798882/')
#parse_submissions('tmp/submissions/31250938/')
#parse_submissions('tmp/submissions/')

import urllib
import urllib.request

from urllib.request import urlopen
from urllib.parse import urlencode
import json

def company_by_addr(addr):
    data = { 'address': addr}
    resp = urlopen('http://apis.is/company?%s' % urlencode(data) )
    res = json.loads(resp.read().decode('utf-8'))
    for comp in res['results']:
        print(comp['name'])
