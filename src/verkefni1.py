def sum_two(a,b):
    return a + b

# 1. Write a function mod_sum(n) that takes an integer as parameters and returns the sum of all multiples of 3 or 5 below n. 
def mod_sum(n):
    if n < 3:
        return 0
    count = 3
    summa = 0
    while ( count < n ):
        if ( count % 3 == 0 ) or ( count % 5 == 0 ):
            summa += count
        count = count + 1
    return summa

# 2. Write a function remove_empty that takes a list of strings and returns the same list, where empty strings have been removed.
def remove_empty( strings ):
    print(strings)
    listi = []
    for x in strings:
        if ( x != '' ):
            listi.append(x)
    #return list
    return list( filter(bool, strings) )

# 3. Write a function reverse_words(s) that takes a string as a parameter. The string contains a single line (i.e. the string contains no \n). The function returns the string s, where the order of the words in the string have been reversed. The words are separated by single space. 
def reverse_words(s):
    if s == '' or s == ' ':
        return ''
    listi = s.split()
    st = ' '.join(str(e) for e in listi[::-1] )
    return st

# 4. Write a function duplicates(s) that takes a list of numbers or strings and returns a list containing all the elements that appear more than once in the list (duplicates).
def duplicates(s):
    listi = []
    while ( len(s) > 0 ):
        if ( s.count(s[-1]) != 1 ):
            if ( listi.count(s[-1]) == 0 ):
                listi.append(s.pop())
            else:
                s.pop()
        else:
            s.pop()
    return listi
import itertools
# 5. A list of integers of length n is called flat if it contains all the integers from 0 to n - 1. Given a list L of unique integers, we define the flattened list, written fl(L), as the list containing the integers from 0 to n - 1 with the same relative order as L. For example if L = [8,4,1,3] then fl(L) = [3,2,0,1].
# Write a function flatten that takes a list of unique integers and returns the flattened list.
def flatten(aList):
    #if ( len(aList) == 0 ):
    #    return []
    #if ( len(aList) == 1 ):
    #    return [0]
    #print(aList)
    #print(len(aList))
    #i = 0
    new = []
    for x in aList:
        new.append(int(x))
    res = list(range(len(aList)))
    #while ( i < len(aList)-1 ):
    #    if ( aList[i]<aList[i+1] ):
    #        res.append(i)
    #    else:
    #        res.append(i+1)
    #    i += 1
    #combined = list( zip(res, aList) )
    #print( combined )
    #sort = sorted(range(len(res)), key=lambda res:aList[res])
    print(aList)
    #key = dict(zip(aList,res))
    #print('')
    #res.sort(key=aList.get)
    res = sorted(res, key=lambda x: aList )
    #print('')
    #combined.sort()
    print( res )
    list(lambda x: aList)
    print('')
    #res = [ n for x, n in combined]
    #res.sort(key=aList,reverse=True)
    return res

#a = input('asd: ')
# 6. Write a function transpose(arr) that takes as a parameter a two-dimensional array, represented as a list of lists. The function should return the
def transpose(arr):
    return [ list(g) for g in zip(*arr) ]

# 7. Write a function scramble that takes two lists of integers, L = [l0, l1,..., ln] and I = [i0, i1,..., in], as arguments. The list I contains all the integers from 0 to n -1 (in some order). The function returns the list M = [m0, m1,..., mn], where mk = lik.
def scramble(list1, list2):
    returnList = [None] * len(list1)
    i = 0
    for x in list2:
        returnList[i] = list1[x]
        i += 1
    return returnList

# 8. Write a function excel_index(s) that takes a string, containing an Excel column index, i.e. a sequence of the letters from A to Z in upper case. The function returns the numerical index of that column.
def excel_index(s):
    i = len(s) - 1
    seet = 0
    pos = 0
    while ( i >= 0 ):
        pos += ( ( ord( s[seet] ) - 64 ) * (26**i) )
        i -= 1
        seet += 1
    return pos
    

# 9. Write a function birthdays(s) that takes a string, containing multiple lines. Each line of the string contains a ten digit (personal) ID number. The function returns a list of tuples. For each shared birthday, the list should contain a tuple containing all the kennitalas of the people who have that birthday. Note that the order in which the tuples appear in the list does not matter, and neither does the order of the ID numbers within each tuple.
def birthdays(s):
    from itertools import groupby
    import re
    if ( s == '' ):
        return ()
    matchList = []
    workList = []
    workList = sorted(s.split())
    #print(s)
    print(workList)
    for x in workList:
        print( re.search(r'\d'[0:4], x) )
    #    print(x[0:4])
    #    print( workList.count( x[0:4] ) )
    for x in groupby([sorted(workList[0:4])]):
                     print(x)
    return matchList
