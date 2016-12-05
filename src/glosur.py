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
        lis.append( ( str(re.split(' ', x.strip(), maxsplit=8)[4:]) ) )
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

import 


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

import urllib.pars.urlencode
#resp = urlopen('http...')
data = { 'address': 'sdf%s', 'name': 'sdf'}
res = urlopen('http://apis.is...sdf %s', % urlencode(data) )
for comp in 

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
    





