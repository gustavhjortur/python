def sum_two(a,b):
    return a + b

#Write a function mod_sum(n) that takes an integer as parameters and returns the sum of all multiples of 3 or 5 below n. 
def mod_sum(n):
    if n < 3:
        return 0
    count = int()
    count = 3
    summa = int()
    summa = 0
    while ( count < n ):
        if ( count % 3 == 0 ) or ( count % 5 == 0 ):
            summa += count
        count = count + 1
    return summa

#Write a function remove_empty that takes a list of strings and returns the same list, where empty strings have been removed.
def remove_empty( *strings ):
    print(strings)
    list = []
    for x in strings:
        list.append(x)
    return list

