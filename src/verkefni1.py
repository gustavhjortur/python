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
def remove_empty( strings ):
    print(strings)
    list = []
    for x in strings:
        #list.append(x)
        if ( x != '' ):
            list.append(x)
    return list

#Write a function reverse_words(s) that takes a string as a parameter. The string contains a single line (i.e. the string contains no \n). The function returns the string s, where the order of the words in the string have been reversed. The words are separated by single space. 
def reverse_words(s):
    if s == '' or s == ' ':
        return ''
    listi = []
    listi = s.split(' ')
    i = int()
    st = str()
    i = -1
    while ( i >= ( len(listi) * -1 ) ):
        st += listi[i]
        st += ' '
        i -= 1
    print( st.split() )
    return st
