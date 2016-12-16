from urllib.request import urlopen
from urllib.parse import urlencode
import json
def encodeDate(day, month, year):
    return ( str(day + 40) + str(month).zfill(2) + str(year)[-2:] )

def companies(day, month, year):
    
    data = { 'socialnumber': encodeDate(day, month, year) }
    resp = urlopen('http://apis.is/company?%s' % urlencode(data) )
    res = json.loads(resp.read().decode('utf-8'))
    returnList = []
    for comp in res['results']:
        if ( comp['active'] == 1 ):
            returnList.append(comp['name'])
    return returnList