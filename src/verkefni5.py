#!/usr/bin/env python3
import random, copy, itertools


def rolleDice(count):
    return [ random.randint(1,6) for x in range(count) ]

def gameTable():
    return {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1,
        'bonus': -1,
        '1pair': -1,
        '2pair': -1,
        '3kind': -1,
        '4kind': -1,
        'sstraight': -1,
        'lstraight': -1,
        'fullhouse': -1,
        'chance': -1,
        'yatzy': -1,
        'sum': -1,
        'spots': 15
        }
    

def player():
    myTable = copy.deepcopy(gameTable())
    print(myTable)
    while myTable['spots'] > 0:
        print( myTable['spots'] )
        print(rolleDice(6))
        for x in myTable:
            if ( x != 'spots' and x != 'bonus' ):
                addNumbToTable(myTable, rolleDice(6), x)
                #while myTable['spots'] < 0:
                myTable['spots'] -= 1
    print(myTable)
    return 0

def bonusCalc(table):
    sum = 0
    for x in range(1,7):
        if ( table[x] != -1 ):
            sum += table[x]
            if ( sum > 63 ):
                return 50
    return 0

def scoreCalc(table):
    sum = 0
    table['bonus'] = bonusCalc(table)
    for x in table:
        if ( ( table[x] != -1 ) and ( x != 'spots') and ( x != 'sum') ):
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
    if ( table[numb] != -1 ):
        return -1
    sum = 0
    for x in dice:
        if x == numb:
            sum += x
    updateTable(table, sum, numb)
    return 0

#Add the 1 pair to the score table
def add1PairToTable(table, dice):
    if ( table['1pair'] != -1 ):
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
    return 0

#Add the 2 pair to the score table
def add2PairToTable(table, dice):
    if ( table['2pair'] != -1 ):
        return -1
    sum1 = 0
    sum2 = 0
    last = 0
    dice.sort(reverse=True)
    for x in dice:
        if ( last == x and sum1 != 0 and sum2 == 0 and sum1/2 != x):
            sum2 = last + x
        if ( last == x and sum2 == 0 ):
            sum1 = last + x
        last = x
    if ( sum1 == 0 or sum2 == 0 ):
        sum1 = sum2 = 0
    updateTable(table, sum1 + sum2, '2pair')
    return 0

#Add the 3 of a kind to the score table
def add3KindToTable(table, dice):
    if ( table['3kind'] != -1 ):
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
    if ( table['4kind'] != -1 ):
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
    if ( table['sstraight'] != -1 ):
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
    if ( table['lstraight'] != -1 ):
        return -1
    dice.sort()
    last1 = 1
    sum = 0
    if ( (dice[0] != 2) and (dice[1] != 2) ):
        updateTable(table, 0, 'lstraight')
        return 0
    for x in dice:
        if ( (last1+1) == x ):
            sum += x
            last1 = x
    if ( sum == 20 ):
        updateTable(table, 20, 'lstraight')
        return 0
    updateTable(table, 0, 'lstraight')
    return 0

#Add the fullhouse to the score table
def addFullHouseToTable(table, dice):
    if ( table['fullhouse'] != -1 ):
        return -1
    sum1 = 0
    dice1Count = 1
    sum2 = 0
    dice2Count = 1
    last = 0
    i = 1
    dice.sort(reverse=True)
    print('\t',dice)
    for x in dice:
        # ef ( last == x AND ekkert bar fundid 
        if ( (last == x and dice1Count == 1) ):
            sum1 = last + x
            dice1Count += 1
            #print('\t fyrri, sum2: ', sum2)
        elif ( last == x and sum1/2 == x and dice1Count == 2 ):
            sum1 += x
            dice1Count += 1
        # ef ( last == x AND sum2 == 0 ) OR x == sum1/2
        elif ( last == x and dice2Count == 1 and x != sum1/3 ):
            sum2 = last + x
            dice2Count += 1
            #print('\t seinni, sum1: ', sum1)
        elif ( last == x and sum2/2 == x and dice2Count == 2 ):
            sum2 += x
            dice2Count += 1
        last = x
        #print('\t\t i: ', i, dice1Count, dice2Count)
        i += 1
    if ( (dice1Count + dice2Count) != 5 ):
        sum1 = sum2 = 0
    updateTable(table, sum1 + sum2, 'fullhouse')
    return 0






#Add the chance to the score table
def addChanceToTable(table, dice):
    if ( table['chance'] != -1 ):
        return -1
    sum = 0
    for x in dice:
        sum += x
    updateTable(table, sum, 'chance')
    return 0

#Add the yatzy to the score table
def addYatzyToTable(table, dice):
    if ( table['yatzy'] != -1 ):
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
#print('Test start')
#print(addChanceToTable(a, [3,3,5,5,5]))
#print(a['chance'], ' 21?' )
#print(addChanceToTable(b, [3,2,5,1,3,3,3]))
#print(b['chance'], ' 20?')

for x in a:
    #print(x)
    if (x == list(range(1,7))):
        print( list(range(1,6)), 'sdf', g[x])

