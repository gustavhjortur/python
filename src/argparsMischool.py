#!/usr/bin/env python3
import argparse
import sys
import re
from collections import deque

def list():
    print('list was selected')
    return 0

def commandSelector(command):
    print('\t', command)
    

parser = argparse.ArgumentParser(description='Myshool SLI')
parser.add_argument('command', metavar='Basic command', nargs=1,
                    type = commandSelector,help='Command')
parser.add_argument('-f', metavar='N', type=argparse.FileType('r'),
                    nargs='?', help='File name for upload')
parser.add_argument('-v', '--invert-match', default=False, action='store_true',  help='Select non-matching lines')
parser.add_argument('-c', '--count', default=False, action='store_true',  help='Count matching lines')
parser.add_argument('-o', '--only-matching', default=False, action='store_true',  help='Print only matched parts of matching lines')
parser.add_argument('-n', '--line-number', default=False, action='store_true',  help='Print each line of output with 1-based line number')
parser.add_argument('-C', '--context', type=int, metavar='NUM', default=0,  help='Print %(metavar)s lines of context (default: %(default)s)')
#parser.add_argument('list', '--context', help='Print content from myschool')

args = parser.parse_args()

#print(args.command)
#print(args.input)

def flush_cache(cache):
    if cache:
        print('--')
    for line in cache:
        output_line(*line)
    cache.clear()

def output_line(i, line, match=None):
    if args.count:
        return
    if args.line_number:
        print('%03d:' % i, end=' ')
    if match and args.only_matching:
        print(match.group())
    else:
        print(line, end='')

cache = deque(maxlen=args.context)

counter = 0
lines_after_match = 0

##for i, line in enumerate(args.input):
##    m = re.search(args.pattern, line)
##    if (m and not args.invert_match) or (args.invert_match and not m):
##        flush_cache(cache)
##        lines_after_match = args.context
##        output_line(i + 1, line, m)
##        counter += 1
##    elif not lines_after_match:
##        cache.append( (i + 1, line) )
##    else:
##        output_line(i + 1, line)
##        lines_after_match -= 1

if args.count:
    print(counter)





#Request for http request ofl.
#python3 -m pip search request
#sudo python3 -m pip install request

import requests
svar = requests.get('http://dyraklam.is') #returnar status
svar.content.decode('utf-8')

svar = requests.get('http://apis.is/company?name=bifr')
svar.json() #returnar json 
def comps(name, address=''):
               payload = {'name': name, 'address': address}
               svar = requests.get('http://apis.is/company', params=payload)
               return svar.json()
#scraping....
from getpass import getpass

def store_pass():
    with open('supersecure', 'w') as f:
        f.write(getpass())
        
def password():
    return open('supersecure').read()

requests.get('https://myschool.ru.is/myschool', auth=('gustav13', password()))

payload = { 'kt': '6608922309' }
res = requests.post('https://myschool.ru.is/myschool/?Page=Exe&ID=1.10', auth=('gustav13', password()), data=payload )

#Beautiful Soup for htmp parsing , hotar native en lxml er best
#sudo pip-python3 install beautifulsoup4
import bs4
from bs4 import BeautifulSoup
#import lxml
##soup = BeautifulSoup(res.text, 'lxml')
thjodskraLeit = BeautifulSoup(res.text, 'html.parser')
#soup.table.td synir fyrstu toflu og tabledata, noexisting skilar None
#soup.find(attrs={'class': 'ruSep'}) == soup.find('td', class_='ruSep')
#td = soup.td geimir tableData en ekki texta eda strengi
#td.attrs synir attribute, strengir eda listar (eins og dict)
##results =[ [td.text for td in tr('td')[:-1]] for tr in soup('center')[1].table('tr')[1:-1]]
#kann lika a xml: soup = BeautifulSoup(markup, 'xml') tharf lxml


#session = requests.Session()
#res = session.post('https://deildu.net/login.php', data={'username': 'gustav', 'password': password()})
#session.post('https://deildu.net/takelogin.php', data={'username': 'gustav', 'password': password()})
#if ('gustav' in res.text) == True successful login
#res = session.get('https://deildu.net/index.php')
#soup2 = BeautifulSoup(res.text, 'html.parser')


#forsida = requests.get('https://myschool.ru.is/myschool', auth=('gustav13', password()))
#forsidaLeit = BeautifulSoup(forsida.text, 'html.parser')


forsidaLeit.table

