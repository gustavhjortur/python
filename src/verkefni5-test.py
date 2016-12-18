#!/usr/bin/env python3
import yatzy

a = yatzy.gameTable()
b = yatzy.gameTable()
c = yatzy.gameTable()

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
assert yatzy.add2PairToTable(b, [1,1,1,1,6,3]) == 0
assert yatzy.scoreCalc(a) == 49
assert yatzy.scoreCalc(b) == 133

#Add the 3 of a kind to the score table
assert yatzy.add3KindToTable(a, [3,4,5,4,4,3]) == 0
assert a['3kind'] == 12
assert yatzy.add3KindToTable(a, [3,4,5,4,4,3]) == -1
assert b['3kind'] == -1
assert yatzy.add3KindToTable(b, [3,4,5,4,6,3]) == 0
assert yatzy.add3KindToTable(b, [3,4,5,4,4,3]) == -1
assert b['3kind'] == 0
assert yatzy.scoreCalc(a) == 61
assert yatzy.scoreCalc(b) == 133


#Add the 4 of a kind to the score table
assert yatzy.add4KindToTable(a, [3,4,5,4,4,4]) == 0
assert a['4kind'] == 16
assert yatzy.add4KindToTable(a, [3,4,5,4,4,3]) == -1
assert b['4kind'] == -1
assert yatzy.add4KindToTable(b, [3,4,5,4,6,3]) == 0
assert yatzy.add4KindToTable(b, [3,4,5,4,4,3]) == -1
assert b['4kind'] == 0
assert yatzy.scoreCalc(a) == 77
assert yatzy.scoreCalc(b) == 133

#Add the smal straight to the score table
assert yatzy.addSStraightToTable(a, [3,4,5,1,4,2]) == 0
assert a['sstraight'] == 15
assert yatzy.addSStraightToTable(a, [3,4,5,4,4,3]) == -1
assert b['sstraight'] == -1
assert yatzy.addSStraightToTable(b, [2,4,5,4,6,3]) == 0
assert yatzy.addSStraightToTable(b, [1,2,5,4,6,3]) == -1
assert b['sstraight'] == 0
assert yatzy.scoreCalc(a) == 92
assert yatzy.scoreCalc(b) == 133

#Add the large straight to the score table
assert yatzy.addLStraightToTable(a, [3,4,5,1,6,2]) == 0
assert a['lstraight'] == 20
assert yatzy.addLStraightToTable(a, [3,4,5,4,4,3]) == -1
assert b['lstraight'] == -1
assert yatzy.addLStraightToTable(b, [2,4,4,4,6,3]) == 0
assert yatzy.addLStraightToTable(b, [1,2,5,4,6,3]) == -1
assert b['lstraight'] == 0
assert yatzy.addLStraightToTable(c, [2,4,5,4,5,5,3]) == 0
assert yatzy.addLStraightToTable(c, [1,2,5,4,6,3]) == -1
assert c['lstraight'] == 0
assert yatzy.scoreCalc(a) == 112
assert yatzy.scoreCalc(b) == 133
assert yatzy.scoreCalc(c) == 0

#Add the fullhouse to the score table
assert yatzy.addFullHouseToTable(a, [3,4,5,5,5,3]) == 0
assert a['fullhouse'] == 21
assert yatzy.addFullHouseToTable(a, [3,4,5,4,4,3]) == -1
assert b['fullhouse'] == -1
assert yatzy.addFullHouseToTable(b, [2,4,4,4,6,3]) == 0
assert yatzy.addFullHouseToTable(b, [1,2,5,4,6,3]) == -1
assert b['fullhouse'] == 0
assert yatzy.addFullHouseToTable(c, [2,4,4,4,5,5,3]) == 0
assert yatzy.addFullHouseToTable(c, [1,2,5,4,6,3]) == -1
assert c['fullhouse'] == 22
assert yatzy.scoreCalc(a) == 133
assert yatzy.scoreCalc(b) == 133
assert yatzy.scoreCalc(c) == 22

#Add the chance to the score table
##def addChanceToTable(table, dice)
assert yatzy.addChanceToTable(a, [3,4,5,5,5,3]) == 0
assert a['chance'] == 25
assert yatzy.addChanceToTable(a, [6,4,5,4,4,3]) == -1
assert b['chance'] == -1
assert yatzy.addChanceToTable(b, [6,6,4,4,6,6]) == 0
assert yatzy.addChanceToTable(b, [1,2,5,4,6,3]) == -1
assert b['chance'] == 32
assert yatzy.scoreCalc(a) == 158
assert yatzy.scoreCalc(b) == 165

#Add the yatzy to the score table
assert yatzy.addYatzyToTable(a, [4,4,4,4,4,4]) == 0
assert yatzy.addYatzyToTable(a, [4,4,4,4,4,4]) == -1
assert yatzy.addYatzyToTable(b, [4,4,4,4,3,4]) == 0
assert yatzy.addYatzyToTable(b, [4,4,4,4,4,4]) == -1
assert yatzy.scoreCalc(a) == 208
assert yatzy.scoreCalc(b) == 165
assert yatzy.scoreCalc(c) == 22





