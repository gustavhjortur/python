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
#release_days('data/cast.csv', 'data/dates.csv', ['Meg Ryan', 'Tom Hanks'] )

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

# 5.
def jam(texti):
    #print(texti)
    firstList = []
    for x in texti.splitlines():
        #tmp = x.split(', ')[1:4]#.split('\" with \"')#.split(' and ')
        tmp = x.split(', ')[1:-1]#.split('\" with \"')#.split(' and ')
        print(tmp)
        first = (tmp[0]).split(' with ')
        tmp[0] = ''
        #firstList.append( lambda y: y in first )
        firstList.append(first[0])
        firstList.append(first[1])
        if ' and ' not in  tmp[1]:
            firstList.append(tmp[1])
            tmp[1] = ''
        try:
            if ' and ' in  tmp[2]:
                tmpList = (tmp[2]).split(' and ')
                for z in tmpList:
                    firstList.append(z)
                tmp[2] = ''
        except:
            pass
        i = 0
        isPlus = False
        for z in tmp:
            print('\t\t', i) ;i += 1
            if ' and ' in z and isPlus:
                break
            if isPlus:
                print('\t\t', z)
                firstList.append( z )
            if z.startswith('plus ') and isPlus == False:
                print('\t\t\t', z.strip( 'plus ') )
                isPlus = True
                firstList.append( z.strip( 'plus ' ) )
        if tmp[-1].startswith('plus ') == False:
            first = (tmp[-1]).split(' and ')
            print('\t', first)
            #firstList.append( str(lambda y: y in first) )
            for y in first:
                firstList.append( y )
        #firstList.append(first[0])
        #firstList.append(first[1])
        #print(first)
        #print(x)
    #print(firstList)
    secondList = []
    #for x in firstList:
        #print(x)
        #tmp = (x[0].split(' with '))#, x[1] )
        #print(tmp)
        #secondList.append(tmp[0])
        #secondList.append(tmp[1])
        #secondList.append(x[1])
        #print(secondList)
        #print(tmp[0])
    #print(secondList)
    returnDict = dict()
    print()
    #print(returnList)
    #print(*returnList.split(', '))
    for i in firstList:
        #ii = (i.split(','))
        #print(returnDict)
        #print(returnDict.get( i ))
        if i == '':
            #print('!!!!!!!!!!!!!!!!!!!!!!!!   ', i)
            pass
        elif returnDict.get( i ):
            tmp = returnDict[ i ]
            tmp += 1
            returnDict[i] = tmp
        else:
            returnDict[i] = int(1) 
    print(returnDict)
    for x in returnDict:
        print(x)
    return returnDict


##jam("""1/1/1 22 December 1967, Nicholas Parsons with Derek Nimmo, Clement Freud, Wilma Ewart, excuses for being late.
##2/1/2 29 December 1967, Nicholas Parsons with Derek Nimmo, Clement Freud, Sheila Hancock and Carol Binstead, bedrooms.
##3/1/3 5 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Betty Marsden and Elisabeth Beresford, ?
##4/1/4 12 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Isobel Barnett and Bettine Le Beau, ?
##5/1/5 20 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Prunella Scales, the brownies
##6/1/6 27 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Marjorie Proops and Millie Small, ?
##7/1/7 2 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Aimi Macdonald and Una Stubbs, my honeymoon.
##8/1/8 9 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Lucy Bartlett and Anona Winn, bloomer.
##9/1/9 17 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Charmian Innes, ?
##10/1/10 23 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Barbara Blake and Renee Houston, my first grown-up dress.
##213/10/19 27 January 1976, Nicholas Parsons with Clement Freud, Peter Jones, Sheila Hancock and Graeme Garden, puppets.
##23/3/1 31 December 1968, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Geraldine Jones, ?
##22/2/6 4 November 1968, Nicholas Parsons with Kenneth Williams, Clement Freud and Geraldine Jones, Pythagoras.
##683/52/1 31 December 2007, Nicholas Parsons with Paul Merton, Kenneth Williams, Clement Freud and Graham Norton, plus Derek Nimmo, Peter Jones, Tony Hawks, Sheila Hancock, Gyles Brandreth, Julian Clary, Linda Smith, Jenny Eclair, Ross Noble, Stephen Fry, Chris Neill, Alfred Marks, Barry Took, Tommy Trinder, Kenny Everett and Bob Monkhouse, 40th anniversary special.
##245/11/26 27 April 1977, Nicholas Parsons with Kenneth Williams, Derek Nimmo, Clement Freud and Peter Jones, plus Ian Messiter, my dignity.""")


#6. Leist af hjalta
import re
from fractions import Fraction

fraction_re = re.compile(r'[0-9]+ [0-9]+/[0-9]+|[0-9]+/[0-9]+|[0-9]+')


def pars_fraction(f):
    return sum([Fraction(x) for x in f.split()])

def fraction_to_str(f):
    ipart = int(f)
    fpart = f - ipart
    if ipart == 0 or fpart == 0:
        return str(f)
    else:
        return '%s %s' % (ipart, fpart)
    
def scale(recipe, scalar):
    scalar = Fraction(scalar)
    def fraction_scaler(match):
        amount = pars_fraction(match.group())
        amount = amount * scalar
        return fraction_to_str(amount)
    return fraction_re.sub(fraction_scaler, recipe)
    



tests = [ ('''Ingredients
    4 skinless, boneless chicken thighs
    1/2 cup/300g soy sauce
    12/2 cup ketchup
    1/33 cup honey
    3 1/4 cloves garlic, minced
    100 teaspoon dried basil''', '1/2') ]

for t in tests:
    print('--------------')
    print(t[0])
    print('--------------')
    print(scale(*t))










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
