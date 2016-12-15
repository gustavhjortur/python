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
            #print(x, table[x] )
            sum += table[x]
    table['sum'] = sum
    return sum

def updateTable(table, sum, spot):
    table[spot] = sum
    table['spots'] -= table['spots']
    scoreCalc(table)
    return 0

#Add the simple one, two,...six to the score table
def addNumbToTable(table, dice, numb):
    if ( table[numb] != None ):
        return -1
    sum = 0
    for x in dice:
        if x == numb:
            sum += x
    updateTable(table, sum, numb)
    return 0

#Add the 1 pair to the score table
def add1PairToTable(table, dice):
    if ( table['1pair'] != None ):
        return -1
    sum = 0
    last = 0
    dice.sort(reverse=True)
    for x in dice:
        if x == last:
            sum = last + x
            updateTable(table, sum, '1pair')
            return 0
        last = x
    updateTable(table, sum, '1pair')
    print(dice)
    return 0

#Add the 2 pair to the score table
def add2PairToTable(table, dice):
    if ( table['2pair'] != None ):
        return -1
    sum1 = 0
    sum2 = 0
    last = 0
    dice.sort(reverse=True)
    #print(dice)
    for x in dice:
        if ( last == x and 0 != sum1 and sum2 == 0):
            #print('2', last, ' ', x)
            sum2 = last + x
        if ( last == x and sum2 == 0 ):
            #print('1', last, ' ', x)
            sum1 = last + x
        last = x
    updateTable(table, sum1 + sum2, '2pair')
    return 0

#Add the 3 of a kind to the score table
def add3KindToTable(table, dice):
    if ( table['3kind'] != None ):
        return -1
    dice.sort()
    last1 = 0
    last2 = 0
    for x in dice:
        if ( last1 == x ):
            if (last2 == x ):
                updateTable(table, last1 + last2 + x, '3kind')
                return 0
            last2 = last1
        last1 = x
    updateTable(table, 0, '3kind')
    return 0

#Add the 4 of a kind to the score table
def add4KindToTable(table, dice):
    if ( table['4kind'] != None ):
        return -1
    dice.sort()
    last1 = 0
    last2 = 0
    last3 = 0
    for x in dice:
        if ( last1 == x ):
            if (last2 == x ):
                if (last3 == x ):
                    updateTable(table, last1 + last2 + last3 + x, '4kind')
                    return 0
                last3 = last2
            last2 = last1
        last1 = x
    updateTable(table, 0, '4kind')
    return 0

#Add the smal straight to the score table
def addSStraightToTable(table, dice):
    if ( table['sstraight'] != None ):
        return -1
    dice.sort()
    last1 = 0
    sum = 0
    if ( dice[0] != 1 ):
         updateTable(table, 0, 'sstraight')
         return 0
    for x in dice:
        if ( (last1+1) == x ):
             sum += x
             last1 = x
    if ( sum == 15 ):
        updateTable(table, 15, 'sstraight')
        return 0
    updateTable(table, 0, 'sstraight')
    return 0
    

#Add the large straight to the score table
def addLStraightToTable(table, dice):
    if ( table['lstraight'] != None ):
        return -1

#Add the fullhouse to the score table
def addFullHousePairToTable(table, dice):
    if ( table['fullhous'] != None ):
        return -1

#Add the chance to the score table
def addChanceToTable(table, dice):
    if ( table['chance'] != None ):
        return -1

#Add the yatzy to the score table
def addYatzyToTable(table, dice):
    if ( table['yatzy'] != None ):
        return -1
    first = dice[0]
    for x in dice:
        if x != first:
            updateTable(table, 0, 'yatzy')
            return 0
    updateTable(table, 50, 'yatzy')
    return 0


a = gameTable()
b = gameTable()
print(addSStraightToTable(a, [3,2,5,1,4]))
print(a['sstraight'])
print(addSStraightToTable(b, [3,2,5,1,3,3,3]))
print(b['sstraight'])

for x in a:
    #print(x)
    if (x == list(range(1,7))):
        print( list(range(1,6)), 'sdf', g[x])

