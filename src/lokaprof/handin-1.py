def split_n(lis, n):
    if ( len(lis) <= n ):
        return ( lis, [] )
    i = 0
    lis1 = []
    lis2 = []
    while i < n:
        lis1.append(lis[i])
        i += 1
    while i < len(lis):
        lis2.append(lis[i])
        i += 1
    return ( lis1, lis2 )