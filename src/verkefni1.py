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
    list = []
    for x in strings:
        if ( x != '' ):
            list.append(x)
    return list

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
    
