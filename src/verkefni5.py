#!/usr/bin/env python3
import random, copy, itertools


def rolleDice(count):
    return [ random.randint(1,6) for x in range(count) ]

def gameTable():
    return {
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        'bonus': None,
        '1pair': None,
        '2pair': None,
        '3kind': None,
        '4kind': None,
        'sstraight': None,
        'lstraight': None,
        'fullhouse': None,
        'chance': None,
        'yatzy': None,
        'sum': None,
        'spots': 15
        }
    

def player():
    myTable = copy.deepcopy(gameTable())
    print(myTable)
    while myTable['spots'] > 0:
        print( myTable['spots'] )
        print(rolleDice(6))
        myTable['spots'] -= 1
    return 0



#print(gameTable())

#def playRound(table):

def bonusCalc(table):
    sum = 0
    for x in range(1,7):
        if ( table[x] != None ):
            sum += table[x]
            if ( sum > 63 ):
                return 50
    return 0

def scoreCalc(table):
    sum = 0
    table['bonus'] = bonusCalc(table)
    for x in table:
        if ( ( table[x] != None ) and ( x != 'spots') and ( x != 'sum') ):
            print(x, table[x] )
            sum += table[x]
    table['sum'] = sum
    return sum


g = gameTable()
for x in g:
    #print(x)
    if (x == list(range(1,7))):
        print( list(range(1,6)), 'sdf', g[x])

