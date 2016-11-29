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
