# 1. Write a function process_ls(output) that takes as a parameter a single string, which contains output from running ls -l in a directory. The function should return a list of all the files in the directory, ordered by size in descending order. Files with equal size should be ordered by the file name in ascending order.
import re
def process_ls(output):
    #print(output.sort)
    #for x in output:
    #listi = list(output.split(sep='\n'))
    # All directorys thrown out and files added to list
#    listi = list( filter(lambda n: n[0:1] != 'd', (list(output.split(sep='\n',s))) ) )
    #listinn = []
    #for x in output:
    #    listinn.append
    listi = list( filter(lambda n: n[0:1] != 'd', (list( x for x in output.split('\n'))) ) )
#    lis = list( filter(lambda n: n[27:29], ( n for n in listi) ) )
    #print(output)
    #print(listi)
    lis = []
    numb = int
    for x in listi:
        x = " ".join(x.split())
        x = " ".join(x.split('\''))
        x = " ".join(x.split(']'))
        x = " ".join(x.split('['))
        numb = list(map(int, re.split(' ', x.strip())[4:5])) 
        #numb = 5
        lis.append( ( str(re.split(' ', x.strip(), maxsplit=8)[4:]:q) ) )
    #newList = [[l[i] for i in listi] for l in listi]
    print(lis)
    numbers = []
    for x in lis:
        x = " ".join(x.split())
        x = " ".join(x.split('\''))
        x = " ".join(x.split(']'))
        x = " ".join(x.split('['))
        x = ",".join(x.split(' , '))
        #t = str(re.split(', ', x.strip())[0:1] )
        numbers.append( list(map(int, re.split(', ', x.strip())[0:1])) )
        print('\t', x)
        #numbers.append( int( map(int, y) for y in t ) )
    lis.sort(reverse=True )
    numbers.sort()
    #print( sorted(lis, reverse=True, key=lambda x: x[0]) )
    #numb = list(int((y) for y in x for x in numbers ))
    for x in numbers:
        print(list(map(int, x)))
    print(numbers)
    l = []
    for x in lis:
        x = " ".join(x.split())
        x = " ".join(x.split('\''))
        x = " ".join(x.split(']'))
        x = " ".join(x.split('['))
        #print(x)
        l.append(str(re.split(',  ', x.strip(), maxsplit=4)[-1]))
    l.sort()
    #print (l)
    #return list( filter(lambda n: n[0:1] != 'd', listi ) )
    l2 = []
    for x in l:
            print(x)
            l2.append(str(re.split(',  ', x.strip(), maxsplit=4)[-1]))
    #for x in lis:
    #    print(re.sub('\ *\n', '*', x))
    print()
    return l

# 2. Sorting Icelandic Names
def sort_names(names):
    return []

# 3. Poker hands
def rank_hand(hand):
    return []

# Day 1
def test(*args, **kwargs):
    '''
    This is at test function

    Call it att will.
    '''
    print(args)
    print(kwargs)

# Day 2 - 1
s = set()
for i in range(30):
    s.add(str(i))
for i in sorted(s):
    print(i)

for i in enumerate(s):
    print(i)
for i, n in enumerate(s):
    print(i, n)

l1 = [1,3,5,7]
l2 = [2,4,6,8]
zip(l1,l2) #setur saman listana og skilar itterator. (single use)

# Day 2 - 1
l1 = [1,3,5,7]
2 in l2
True
'ab' in 'abcde'
True
'yay'.center(12)
'    yay    '
'yay'.center(12,'-')
'----yay----'
'yay'.rjust(12,'-')
'--------yay'
s = 'tetta er gaman'
s.capitalize()
'Tetta er gaman'
s.title()
'Tetta Er Gaman'
s.isdecimal()
False

ord('a')
97
ord('A')
65
chr(65)
'A'
cards = 'A23456789TGQK'
cards.index('K')  # kastar villu ef er ekki til
12
cards.find('K')   # skilar -1 ef er ekki til
12
cards[:cards.find('6')]
'A2345'
>>> long = '''
this
awsome string
has\tso
many linss'''
>>> long.splitlines()
['', 'this', 'awsome string', 'has\tso', 'many linss']
>>> long.splitlines(True)
['\n', 'this\n', 'awsome string\n', 'has\tso\n', 'many linss']
long.split() #splittar 'a 0llum whitespaceum og hendir non printable
>>> ' '.join(long.split())
'this awsome string has so many linss'
long.strip()
'this\nawsome string\nhas\tso\nmany linss'
>>> long.strip('\nt')
'his\nawsome string\nhas\tso\nmany linss'
lines = data.splitlines()[1:]
results[]
for line in lines:
    results.append(line.split('\t'))
# == results = [ line.split('\t') for line in lines ]
[ x**2 for x in range(10) if x % 2 == 1 ]


# Day 3
def my_filter():
    return [filter(lambda x: len(str(x)) == 2, map(lambda x: x**2, range(100))) ]

def my_sort1(strings):
    return sorted( strings, key=lambda x: x.lower() )

def my_sort2(strings):
    return sorted( strings, key=str.lower )

def my_sort3(strings):
    return sorted( strings, key=len )

def my_sort4(strings):
    return sorted(sorted( strings, key=lambda x: x.lower()), key=len )

def my_sort44(strings):
    return sorted( strings, key=lambda x: (len(x), x.lower(), x.lower() ) ) 

def my_sort444(strings):
    return sorted( strings, key=lambda x: (len(x), ( 'h' not in x.lower(), x.lower() ) ) )

def my_count(start, stop):
    curr = start
    while curr < stop:
        yield curr
        curr += 1

from itertools import cycle
def my_groops(users, groupcount):
    for s,g in zip(users, cycle(range(int(2)))):
        print(s,g)

from itertools import groupby
def my_grep1(listi):
    if list[-2].isdigit():
        return listi[-2]
    return None

def my_grep2(listi):
    for year, studs in groupby(sorted(listi, key=startyear), startyear):
        print(year, list(studs))
#{k:list(v) for k.v in groupbu(sorted(listi, key=startyear), startyear)

from itertools import combinations, product, permutations
def my_prod1():
    return list(product('abc', '123', '!@#'))

def my_prod2():
    return
#t = 7 * ('01')
#list(map(''.join,product(*t)))

def spilin():
    rank = 'A23456789TJQK'
    suit = 'HSCD'
    #return list( a+b for a,b in product(suit, rank) )
    return list( ''.join(x) for x in product(suit, rank) )
rank = 'A23456789TJQK'
suit = 'HSCD'
cards = list( ''.join(x) for x in product(suit, rank) )
c = combinations(cards, 5)
#next(c)
def comb1(hand):
    return all(map(lambda x: x == 'H', list(zip(*hand))[0]))

def comb2():
    i = 0
    for c in combinations(cards, 5):
        if(comb1(c)):
           i += 1
    return i
def check_flush(hand):
    return len(set(list(zip(*hand))[0])) == 1

def count_flush():
    i = 0
    for c in combinations(cards, 5):
        if check_flush(c):
            i += 1
    return i

# Day 4




# Day 5 - 1
#re.search('ab?', 'aadfgertberwerwerbwerwwe')
#re.search('a.*b', 'aadfgertberwerwerbwerwwe')
#re.search('a.*?b', 'aadfgertberwerwerbwerwwe') non gready
#re.search('ab{5}', 'aadfgertberwerwerbwerwwe') 5 * b
#re.search(r'\^a\.\*\?b', 'aadfgertberwerwerbwerwwe')
#re.search(r'\^a\.\*\?b', 'a^a.*?bgertberwerwerbwerwwe') r framanvi[ breitir 'i raw
#re.search(r'-?\b[0-9]+\b', 'x = 0.2343') \b wordborder
#re.search(r'(na|nan) * Battman', 'nanananan Battman') | er OR   ^ 'i mengi er compliment(not)
r = re.compile(r'^"([^"\\]|\\n|\\t|\\")*"$')
#re.search(r,'""')
#r.search('""')
#re.match eins og search nema fremst fremst
#re.fullmatch  finnur bara ef allur strengurinn matchar
conf = re.compile('\w+: .*')
#conf.findall(config)
#d = dict(conf.findall(config) b'yr til dictionary
#re.sub('aa*', '', 'afaaagggg')

#find og replace
def incr(m):   
    value = m.group(3)
    if vlaue.isdigit():
        value = str(int(value) + 1 )
    return ''.join([m.group(1), m.group(2), value])
#re.sub('(\w+)(: )(.*)', incr. config) incrementar allar tolur um 1

# Day 5 - 2

import os, shutil

import shutil
 copy, copy2, copytree, rmtree, move(rename), 


# Day 6 - 1
#apis.is
import jason
import pickle  #binari
dump, dumps
load, loads

import xml.etree.ElementTree as ET
ET.pars(filename) #tree object
xpath # .findall

sql db 'i einni skra og thread safe
import sqlite3


import csv
 open('fil', encodinc) af f:
     read = csv.reader(f)
     csvdata = list(reader)
DictReader
Sniffer

# Day 6 - 2

import urllib
urllit.request.urlopen
import urllib.request
urllib.request.urlopen('http://....?'Name-'sdf')
from urllib.request import urlopen
from urllib.parse import urlencode

import urllib.pars.urlencode
#resp = urlopen('http...')
def company_by_addr(addr):
    data = { 'address': addr}
    resp = urlopen('http://apis.is/company?%s' % urlencode(data) )
    res = json.loads(resp.read()).decode('utf-8'))
    for comp in res['results']:
        print(comp['name'])

print(json.loads(res.read()).decode('utf-8'))


import logging
logger = logging.getLogger('test')
logger.basicConfig(level=logging.DEBUG,
                   format='%(ascitime)s [%(levelname)s] %(message)s',
                   stream.stdout filename='my.log')

import tracepack
def fun():
    try:
        x = 1 / 0
    except:
        logger.exception('sdf', exc_info=True)
        return traceback.format.
    
# Day 7 - 1
# (verkefni 4)

#import sys #Alskonar system tools
# Fari[ yfir virkni og notkun a argparse
import argparse
import sys
import re
from collections import deque


def regex(string):
    try:
        return re.compile(string)
    except Exception as ex:
        raise argparse.ArgumentTypeError('Invalid regular expression\n%s' % ex.msg)

parser = argparse.ArgumentParser(description='Grep some stuff')
parser.add_argument('pattern', metavar='RE', type=regex, help='Regular expression')
parser.add_argument('input', metavar='N', type=argparse.FileType('r'), default=sys.stdin, nargs='?', help='Input')
parser.add_argument('-v', '--invert-match', default=False, action='store_true',  help='Select non-matching lines')
parser.add_argument('-c', '--count', default=False, action='store_true',  help='Count matching lines')
parser.add_argument('-o', '--only-matching', default=False, action='store_true',  help='Print only matched parts of matching lines')
parser.add_argument('-n', '--line-number', default=False, action='store_true',  help='Print each line of output with 1-based line number')
parser.add_argument('-C', '--context', type=int, metavar='NUM', default=0,  help='Print %(metavar)s lines of context (default: %(default)s)')

args = parser.parse_args()


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

for i, line in enumerate(args.input):
    m = re.search(args.pattern, line)
    if (m and not args.invert_match) or (args.invert_match and not m):
        flush_cache(cache)
        lines_after_match = args.context
        output_line(i + 1, line, m)
        counter += 1
    elif not lines_after_match:
        cache.append( (i + 1, line) )
    else:
        output_line(i + 1, line)
        lines_after_match -= 1

if args.count:
    print(counter)

# Day 7 - 2
import os
>>> os.system('ls')
0  # return value
import subprocess
subprocess.run()
subprocess.Popen()

import decimal #getur lagad flot errora 
import fraction
from fractions import Fraction
>>> Fraction(numerator=10, denominator=5)
Fraction(2, 1)
Fraction('10/5')
>>> from decimal import Decimal
>>> Decimal(0.3)
Decimal('0.299999999999999988897769753748434595763683319091796875')
>>> Fraction.from_decimal(Decimal(0.3))
Fraction(5404319552844595, 18014398509481984)
>>> Fraction.from_decimal(Decimal('0.3'))
Fraction(3, 10)

# Day 8 - 1

#Metaclass programming til a[ breita class
#min 31:00 talad um hvernig erfdir eru bunar til og constructors

class Cls:
    var = 12 # allir instancear fa somu breitu

    def __init__(self):
        selt.a = 12
        self.b = 'asd'
        self.g = a
        self._bla = 44 #_ meanes privete, __ python specific
        
    
    def fun(self):
        return 'yay'

    @property  # gerir thetta fall ad property geimslu
    def prop(self):
        return self.a

    @prop.setter
    def prop(self, s):
        if n % 2 = 1:
            self.a = n
        
    @prop.deleter
    def prop(self):
        pass        # kemur i veg fyrir delete
        del self.a

    @staticmethod
    def static():
        return 42

    @classmethod  #Bara notad 'i meta programming
    def clsmethod(self):
        return self

    def __repr(self:
        return 'Cls(a=%s, b=%s)' % (a,b)

    def __str__(self)
        return 'Cls(a=%s, b=%s)' % (a,b)

    def __getattribute__(self, name):
        if name == '__dict__' or name in self.__dict__:
            return super().__getattribute__(name)
        else:
            return 42

    def __len__(self):
        return 4

    def __getitem__(self, item):  #overload [] operatorinn
        return item * self.a

    def __setitem__(self, item, value):  #overload [] operatorinn
        print(item, value)
        return None

    def __call__(self, *args, **kwargs):   #Svona tekur fallid vid ollum parametrum
        print(args, kwargs)                #c(1,2,3,'asd', name-3)
getattr saekir oll object sem clasi a
setattr getur buid til ny setattr(c, 'asd', 12) byr til breituna asd i c og gefur gildid 12

from collections import UserList #inniheldur alskonar "listaverk"
#math vector daemi
class Vector:
    def __init__(self, vec=None)
        if vec in None:
            vec = []
        self.vec = list(vec)

    def __len__(self):
        return len(self._vec)

    def __repr__(self):
        return '<%s>' % (', '.join(map(str,self._vec)))

    def __add__(self, other):
        """
        self + other =>
        self.__add__(other)
        """
        if not isinstance(other, Vector):
            raise NotImplemented #ValueError("Don't be silly")
        if len(self) != len(other)
            raise ValueError('Lengd mismatch')
        return Vector( [ a + b for a,b in zip( self._vec, other._vec) ] )

    def __mul__(self, other):
        """
        self * other =>
        self.__mul__(other)
        """
        check = [int, float, complex]
        if not any(map(isinstance,[other]*3, check)):
            raise NotImplemented #ValueError("Don't be silly")
        return Vector( [ a * other for a in self._vec ] )

    der __rmul__(self, other):
        """
        other * self =>
        self.__rmul__(other)
        """
        return self * other
# Enum...
from enum import Enum #IntEnum for int only
class Suit(Enum):
    Harts = 1
    Dimonds = 2
# collections gott til ad flitja/geima gogn
from collections import namedtuple
Data = namedtuple('Data', ['name', 'year','age'])
# Use:
d = Data('asd', 123, 321)
d.name  returnar 'asd'


# Day 8 - 2
import traceback
               
try:
    a = 5
    b = 0
    res = a / b
except ZeroDivisionError as ex:  # 2. / 3, tekur bara thessa villu (as ex litid notad annad er betra)
    print('Oh no..%s', % ex)
    return traceback.format_exc()
except:  # 1. / 3, Basic tekur allt
    print('Oh no..')
    raise MyError   #notad td. til ad rename-a villu eda ef rid getum ekki hondlad "alla leid"
else:
    return res
finally:  #keyrir alltaf
    print('finaly')


raise ValueError('Nope')  # kastar villu
---------------
#with
---------------
PyPi

python3
yum install python3-pip
pip-python3 search cowpy
sudo pip-python3 install cowpy


#Day 9 - 1

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
               svar = request.get('thhp://apis.is/company', params=payload)
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
kt = requests.post('https://myschool.ru.is/myschool/?Page=Exe&ID=1.10', auth=('gustav13', password()), data=payload )

#Beautiful Soup for htmp parsing , hotar native en lxml er best
#sudo pip-python3 install beautifulsoup4
import bs4
from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')
#soup.table.td synir fyrstu toflu og tabledata, noexisting skilar None
#soup.find(attrs={'class': 'ruSep'}) == soup.find('td', class_='ruSep')
#td = soup.td geimir tableData en ekki texta eda strengi
#td.attrs synir attribute, strengir eda listar (eins og dict)
results =[ [td.text for td in tr('td')[:-1]] for tr in soup('center')[1].table('tr')[1:-1]]
#kann lika a xml: soup = BeautifulSoup(markup, 'xml') tharf lxml


session = requests.Session()
#res = session.post('https://deildu.net/login.php', data={'username': 'gustav', 'password': password()})
session.post('https://deildu.net/takelogin.php', data={'username': 'gustav', 'password': password()})
#if ('gustav' in res.text) == True successful login
res = session.get('https://deildu.net/index.php')
soup2 = BeautifulSoup(res.text, 'html.parser')

# Day 9 - 2

#Added i verkefni2.py

# Day 10 : No lecture
# Day 11 - 1
Tala[ um verkefni 5 og profid

# Day 11 - 2

#flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
@app.route("/<name>")
def hollo(name):
    return "Hola %s!" % name

if __name__ == "__main__":
    app.run()  #debug=True, port=8080 are options herna

#Til ad browsa files sja thedda
#url_for('static', filename='style.css')
#The file has to be stored on the filesystem as static/style.css.

from flask import render_template

#@app.route('/hello/')
#@app.route('/hello/<name>')
#def hello(name=None):
#    return render_template('hello.html', name=name)
#
#Flask will look for templates in the templates folder. 
#<!doctype html>
#<title>Hello from Flask</title>
#{% if name %}
#  <h1>Hello {{ name }}!</h1>
#{% else %}
#  <h1>Hello, World!</h1>
#{% endif %}


#tkinter  A GUI framework
#Lika til pyqt og pySide ss. python framework fyrir QT

import tkinter as tk
from tkinter import messagebox

def event_generator(widget):
    def event():
        print(widget.row, widget.col)
    return event

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def color_changer(self, event):
        #print(event.widget.row, event.widget.col)
        event.widget['bg'] = 'red'

    def clear_color(self, event):
        event.widget['bg'] = 'white'

    def toggle_color(self, event):
        print('yay')
        if event.widget.on:
            event.widget.create_rectangle(5,5,45,45, fill='#CCCCCC')
        else:
            event.widget.create_rectangle(5,5,45,45, fill='blue')
        event.widget.on = not event.widget.on
        self.lbl['text'] = '(%d, %d)' % ( event.widget.row, event.widget.col )
        messagebox.showinfo('WOW', '{%d, %d}' % ( event.widget.row, event.widget.col) )

    def create_widgets(self):
        self.lbl = tk.Label(self, text='Helllo, world!')
        self.lbl.grid(row=0, column=0, columnspan=10)
        
        for r in range(10):
            for c in range(10):
##                self.btn = tk.Button(self,
##                                     text="yay",
##                                     bg="white",
##                                     command=self.say_hi)
                can = tk.Canvas(self, width=50, height=50, bg='white')
                can.grid(row=r, column=c)
                can.create_rectangle(5,5,45,45, fill='#CCCCCC')
##                self.btn['command'] = event_generator(self.btn)
##                self.btn.grid(row=r, column=c)
##                self.btn.row = r
##                self.btn.col = c
                can.row = r
                can.col = c
                can.on = False
##                self.btn.grid(row=r, column=c)
##                self.btn.bind('<Enter>', self.color_changer)
##                self.btn.bind('<Leave>', self.clear_color)
                can.bind('<Enter>', self.color_changer)
                can.bind('<Leave>', self.clear_color)
                can.bind('<Button-1>', self.toggle_color)

####        self.hi_there = tk.Button(self)
####        self.hi_there["text"] = "Hello World\n(click me)"
####        self.hi_there["command"] = self.say_hi
####        self.hi_there.pack(side="top")
####        self.quit = tk.Button(self, text="QUIT", fg="red",
####                              command=root.destroy)
####        self.quit.pack(side="bottom")

    def say_hi(self, widget):
        print(widget.row, widget.col)

root = tk.Tk()
app = Application(master=root)
app.mainloop()


# Day 12 - 1

# Modular og pakkar,,, sidan hvernig vid b'uum til pip...


#plib / passwordlib fyrir module smidapaelingar
import random  #aetti ad nota secrets sem er secure random number generator
from random import choice, randint
from string import ascii_letters, digits, punctuation
from pathlib import Path

_non_punct = ascii_letters + digits
_with_punct = _non_punct + punctuation

_currdir = Path(__file__).parent #finnur parent dir (demo)
_words_path = str(_currdir / 'data/all_words.txt')

with open(_words_path, encoding='utf-8') as f:
    words = f.read().splitlines()

def random(minlen=5, maxlen=10, punct=False):
    letters = [_non_punct, _with_punct][punct]
    return ''.join( choice(letters) for _ in range(randint(minlen, maxlen)) )

def xkcd(nwords=4, sep=' '):
    return sep.join( choice(words) for _ in range(nwords) )

if __name__ == '__main__':  #prentar ekki ut ef importad
    print('welcom to shelllll')

# for further demo see: T-308-prla/fyrirlestrar/python-lectures/day_12/modules

##til ad importa fom place out of path ma gera
#    import sys
#    sys.path.insert(0,'..')  setur directoryid .. fremst i path
#    import mystuff

#Til ad sja dema um pakka sja T-308-prla/fyrirlestrar/python-lectures/day_12/plib

# Day 12 - 2

# Orstutt um pakka og virtual enviornment
# Ypthon packaging user guide

# Sja skrar i T-308-prla/fyrirlestrar/python-lectures/day_12/pip_test/plib/

#sudo pip-python3 install virtualenv
#virtualenv env
#run "source env/bin/activate til ad starta 
# thar er sidan pakkarnir
#deactivate til ad exita.
#
#install from git 2 flavors
#pip install https://github.com/hjalti/passwordlib/archive/master.zip
#pip install git+https://github.com/hjalti/passwordlib.git
#pip install git+https://github.com/hjalti/passwordlib.git@master velur master branch

















      
