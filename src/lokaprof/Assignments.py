# 1.
# Write a function split_n that takes one list, lis, and one integer, n, as parameters
# and returns a tuple containing two lists.
# The first list contains the first n elements of lis
# (in the same order as they appear in lis).
# The second list contains the remaining elements of lis
# (in the same order as they appear in lis).
# If n is greater than the number of elements in lis,
# the first element of the returned tuple should be lis and the second should be the empty list. 
def split_n(lis, n):
    if ( len(lis) <= n ):
        return ( lis, [] )
    i = 0
    lis1 = []
    lis2 = []
    while i < n:
        lis1.append(lis[i])
        i += 1
    while i < len(lis):
        lis2.append(lis[i])
        i += 1
    return ( lis1, lis2 )

##print( split_n([1, 9, 30, 12], 2) )
##print( ([1, 9], [30, 12]) )
##print()
##print( split_n([1, 9, 30, 12, 34, 12, 12], 5) )
##print( ([1, 9, 30, 12, 34], [12, 12]) )
##print()
##print( split_n([1, 9, 30, 12], 4) )
##print( ([1, 9, 30, 12], []) )


# 2.
from urllib.request import urlopen
from urllib.parse import urlencode
import json
def encodeDate(day, month, year):
    #print( str(day + 40) )
    #print( str(month).zfill(2) )
    #print( str(year)[-2:] )
    return ( str(day + 40) + str(month).zfill(2) + str(year)[-2:] )

def companies(day, month, year):
    
    data = { 'socialnumber': encodeDate(day, month, year) }
    #data = { 'address': 'Hl'}
    resp = urlopen('http://apis.is/company?%s' % urlencode(data) )
    res = json.loads(resp.read().decode('utf-8'))
    returnList = []
    for comp in res['results']:
        if ( comp['active'] == 1 ):
##            print(comp['name'])
            returnList.append(comp['name'])
    return returnList

##print( companies(2, 12, 1986) )
##print('''['Búnaðarfélag A-Eyjafjallahrepps',
## 'Jarðsýn,bókaforlag',
## 'Sæbólsbraut 30,húsfélag',
## 'Uns universal']''')
##print()
##print()
##print( companies(7, 1, 2008) )
##print('''['Gjafa- og minningarsjóður Sjúkrahússins og heilsugæslustöðvarinnar á '
## 'Akranesi',
## 'Húsfélagið Grensásvegi 12A',
## 'Knattspyrnudeild Þróttar',
## 'Landnám Ingimundar gamla',
## 'Langalína 10-14,húsfélag',
## 'Langholtsvegur 93,húsfélag',
## 'Norðurbakki 23,húsfélag',
## 'Sólheimar 42,húsfélag',
## 'Tannlæknastofa Jóns Ólafs slf.',
## 'Áhugamannafélagið Heilunarhofið',
## 'Þak og renna slf.']''')
##print()
##print()
##print ( companies(21, 5, 2014) )
##print( '''['Brekkugata 9,húsfélag',
## 'Eignarhaldsfélagið Dórulundur ehf.',
## 'Grámann slf.',
## 'Haust ljós ehf.',
## 'Hollvinasamtök Félagsheimilisins Skrúðs (H.F.S.)',
## 'Hólshraun ehf.',
## 'Kirkjulundur 12-14, húsfélag',
## 'Oxford ehf.',
## 'Radiant Games ehf.',
## 'Rekstrarfélagið Bæjarlind 1-3',
## 'Skátabúðin ehf.',
## 'Stuðningsfélag Ögmundar Þ. Jóhannessonar',
## 'Vír og lykkjur ehf.',
## 'Íþróttafélag Úlfljótsvatns']''')

# 3.
#For this I vould use sort and cut: "du -b | sort -nr | cut -f2"
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
    #print(inputLines)
    listinn = dict()
    for x in inputLines:
        #print(x.split(maxsplit=1)[0])
        listinn[int(x.split()[0])] = x.split(maxsplit=1)[1] 
        #print(x)
    listIndex =  sorted(listinn, reverse=True)
    returnList = []
    for x in listIndex:
        #print( listinn[x] )
        ( fixNames( listinn[x] ) )
        returnList.append( fixNames( listinn[x] ) )
    return returnList




##print(process_du("""228136 ./Example preim 312
##202099  ./Library
##561775  ./Submission-arXiv v1
##100294  ./B-inv-proposition
##799927  ./CodeSage/SageRuns
##826594  ./CodeSage
##569863  ./Submission-FPSAC2012/Final submission
##315957  ./Submission-FPSAC2012/Sample
##1210768 ./Submission-FPSAC2012/Galley
##6670    ./Submission-FPSAC2012/Original submission/auto
##572082  ./Submission-FPSAC2012/Original submission
##2737508 ./Submission-FPSAC2012
##1298628 ./CodeHaskell/s
##4513852 ./CodeHaskell
##9759720 ."""))
##print()
##print()
##print( ['.', 'CodeHaskell', 'Submission-FPSAC2012', 's', 'Galley', 'CodeSage', 'SageRuns',
## 'Original submission', 'Final submission', 'Submission-arXiv v1', 'Sample',
## 'Example preim 312', 'Library', 'B-inv-proposition', 'auto'] )
##print()
##print()
##print(process_du("""228136 Meshmachine/Example preim 312
##202099 Meshmachine/Library
##561775 Meshmachine/Submission-arXiv v1
##100294 Meshmachine/B-inv-proposition
##799927 Meshmachine/CodeSage/SageRuns
##826594 Meshmachine/CodeSage
##569863 Meshmachine/Submission-FPSAC2012/Final submission
##315957 Meshmachine/Submission-FPSAC2012/Sample
##1210768 Meshmachine/Submission-FPSAC2012/Galley
##6670 Meshmachine/Submission-FPSAC2012/Original submission/auto
##572082 Meshmachine/Submission-FPSAC2012/Original submission
##2737508 Meshmachine/Submission-FPSAC2012
##1298628 Meshmachine/CodeHaskell/s
##4513852 Meshmachine/CodeHaskell
##9759720 Meshmachine"""))

# 4.
import csv
def count_votes(fileName):
    returnDict = dict()
    dataList = []
    with open(fileName) as file:
        read = csv.DictReader(file)
        csvData = list(read)
        #print(csvData)
        dataList.append(csvData)
    voteList = []
    for x in dataList:
        #print(x)
        for y in x:
            #print()
            #print(y['Hvaða verkefni fannst þér skemmtilegust?'])
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






##print( count_votes('Kennslumat_small.csv') )
##print()
##print()
##print('''{'10. vika - rafrænt: Leit að mótífum í erfðamengjum': 2,
## '12. vika - rafrænt: Recursive Programming in SML': 2,
## '6. vika - rafrænt: Automata Programming': 1,
## '6. vika - skýrsla: Finite Automata': 1,
## '8. vika - rafrænt: Robots': 2,
## '9. vika - rafrænt: Sets': 1}''')

# 5.
def splitProp(list):
    if ':' not in list:
        return ''
    retValue = []
    #print( list)
    for x in list.strip().split(';'):
        if x == '':
            continue
        k = x.split(':')[0].strip()
        v = x.split(':')[1].strip()
        retValue.append((k,v))
        print( '\t', x.replace(' ', '').split(':') )
        #retValue.append(x.strip().split(':'))
    return retValue

def css_properties(css):
    rawList = (css.replace('\n', '').split('{'))
    propList = []
    for x in rawList:
        propList.append( x.split('}', maxsplit=1)[0] )
    retValue = []
    for x in propList:
        tmp = ( splitProp(x) )
        for x in tmp:
            retValue.append(tuple(x))
    return retValue









print( css_properties("""
#LasVegas .billboard { text-decoration: blink; }

.ninja, #Snowden { visibility: hidden; }


.oliveoil
{
  z-index: 1;
}
.water
{
  z-index: 0;
}

#poop {
  float  : none  ;
  color  : brown ;

  width  : 15cm  ;
  height : 120cm ;
}

.God { position: absolute; display: none; }
#blackhole { padding: -9999em; }

.word {  font-family:    "Comic Sans", "Times New Roman", sans-serif  ;  }
""") )
print()
print()
print('''[('text-decoration', 'blink'),
('visibility', 'hidden'),
('z-index', '1'),
('z-index', '0'),
('float', 'none'),
('color', 'brown'),
('width', '15cm'),
('height', '120cm'),
('position', 'absolute'),
('display', 'none'),
('padding', '-9999em'),
('font-family', '"Comic Sans", "Times New Roman", sans-serif')]''')

print()
print()
print( css_properties("""('a{color:pink;}',)"""))

print()
print()
print( css_properties("""('a { color : pink ; }',)"""))


