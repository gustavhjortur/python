import yatzy

a = yatzy.gameTable()
b = yatzy.gameTable()
c = yatzy.gameTable()

print(yatzy.rolleDice(6))
print(yatzy.rolleDice(6))

#Add the simple one, two,...six to the score table
assert yatzy.addNumbToTable(a, [1,2,3,4,5,6], 1) == 0
assert yatzy.addNumbToTable(a, [1,2,3,4,5,6], 2) == 0
assert yatzy.addNumbToTable(a, [1,2,3,4,5,6], 3) == 0
assert yatzy.addNumbToTable(a, [1,2,3,4,5,6], 4) == 0
assert yatzy.addNumbToTable(a, [1,2,3,4,5,6], 5) == 0
assert yatzy.addNumbToTable(a, [1,2,3,4,5,6], 6) == 0
assert yatzy.addNumbToTable(a, [1,2,3,4,5,6], 1) == -1
assert yatzy.addNumbToTable(b, [1,2,3,4,5,6], 1) == 0
assert yatzy.addNumbToTable(b, [1,2,3,4,5,6], 4) == 0
assert yatzy.addNumbToTable(b, [1,2,3,4,5,6], 4) == -1
assert yatzy.addNumbToTable(b, [1,2,3,4,5,6], 4) == -1
assert yatzy.addNumbToTable(b, [6,6,6,6,6,6], 6) == 0
assert yatzy.addNumbToTable(b, [5,5,5,5,5,5], 5) == 0
assert yatzy.scoreCalc(a) == 21
assert yatzy.scoreCalc(b) == 121

#Add the 1 pair to the score table
assert yatzy.add1PairToTable(a, [3,4,5,5,4,3]) == 0
assert yatzy.add1PairToTable(a, [3,4,5,5,4,3]) == -1
assert yatzy.add1PairToTable(b, [3,4,6,6,1,1]) == 0
assert yatzy.scoreCalc(a) == 31
assert yatzy.scoreCalc(b) == 133

#Add the 2 pair to the score table
assert yatzy.add2PairToTable(a, [3,4,5,5,4,3]) == 0
assert yatzy.add2PairToTable(a, [3,4,5,5,4,3]) == -1
assert yatzy.add2PairToTable(b, [1,4,6,1,6,3]) == 0
assert yatzy.scoreCalc(a) == 49
assert yatzy.scoreCalc(b) == 147

#Add the 3 of a kind to the score table
assert yatzy.add3KindToTable(a, [3,4,5,4,4,3]) == 0
assert a['3kind'] == 12
assert yatzy.add3KindToTable(a, [3,4,5,4,4,3]) == -1
assert b['3kind'] == None
assert yatzy.add3KindToTable(b, [3,4,5,4,6,3]) == 0
assert yatzy.add3KindToTable(b, [3,4,5,4,4,3]) == -1
assert b['3kind'] == 0
assert yatzy.scoreCalc(a) == 61
assert yatzy.scoreCalc(b) == 147


#Add the 4 of a kind to the score table
assert yatzy.add4KindToTable(a, [3,4,5,4,4,4]) == 0
assert a['4kind'] == 16
assert yatzy.add4KindToTable(a, [3,4,5,4,4,3]) == -1
assert b['4kind'] == None
assert yatzy.add4KindToTable(b, [3,4,5,4,6,3]) == 0
assert yatzy.add4KindToTable(b, [3,4,5,4,4,3]) == -1
assert b['4kind'] == 0
assert yatzy.scoreCalc(a) == 77
assert yatzy.scoreCalc(b) == 147

#Add the smal straight to the score table
assert yatzy.addSStraightToTable(a, [3,4,5,1,4,2]) == 0
assert a['sstraight'] == 15
assert yatzy.addSStraightToTable(a, [3,4,5,4,4,3]) == -1
assert b['sstraight'] == None
assert yatzy.addSStraightToTable(b, [2,4,5,4,6,3]) == 0
assert yatzy.addSStraightToTable(b, [1,2,5,4,6,3]) == -1
assert b['sstraight'] == 0
assert yatzy.scoreCalc(a) == 92
assert yatzy.scoreCalc(b) == 147

#Add the large straight to the score table
##def addLStraightToTable(table, dice)

#Add the fullhouse to the score table
##def addFullHousePairToTable(table, dice)

#Add the chance to the score table
##def addChanceToTable(table, dice)

#Add the yatzy to the score table
assert yatzy.addYatzyToTable(a, [4,4,4,4,4,4]) == 0
assert yatzy.addYatzyToTable(a, [4,4,4,4,4,4]) == -1
assert yatzy.addYatzyToTable(b, [4,4,4,4,3,4]) == 0
assert yatzy.addYatzyToTable(b, [4,4,4,4,4,4]) == -1
assert yatzy.scoreCalc(a) == 142
assert yatzy.scoreCalc(b) == 147






