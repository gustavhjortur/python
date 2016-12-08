def jam(texti):
    firstList = []
    for x in texti.splitlines():
        tmp = x.split(', ')[1:4]#.split('\" with \"')#.split(' and ')
        first = (tmp[0]).split(' with ')
        firstList.append(first[0])
        firstList.append(first[1])
        firstList.append(tmp[1])
        first = (tmp[2]).split(' and ')
        for y in first:
            firstList.append( y )
    secondList = []
    returnDict = dict()
    for i in firstList:
        if returnDict.get( i ):
            tmp = returnDict[ i ]
            tmp += 1
            returnDict[i] = tmp
        else:
            returnDict[i] = int(1) 
    return returnDict


jam("""1/1/1 22 December 1967, Nicholas Parsons with Derek Nimmo, Clement Freud, Wilma Ewart and Beryl Reid, excuses for being late.
2/1/2 29 December 1967, Nicholas Parsons with Derek Nimmo, Clement Freud, Sheila Hancock and Carol Binstead, bedrooms.
3/1/3 5 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Betty Marsden and Elisabeth Beresford, ?
4/1/4 12 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Isobel Barnett and Bettine Le Beau, ?
5/1/5 20 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Prunella Scales, the brownies
6/1/6 27 January 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Marjorie Proops and Millie Small, ?
7/1/7 2 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Aimi Macdonald and Una Stubbs, my honeymoon.
8/1/8 9 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Lucy Bartlett and Anona Winn, bloomer.
9/1/9 17 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Andree Melly and Charmian Innes, ?
10/1/10 23 February 1968, Nicholas Parsons with Derek Nimmo, Clement Freud, Barbara Blake and Renee Houston, my first grown-up dress.""")















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
