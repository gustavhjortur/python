def duplicates(s):
    lis = []
    while ( len(s) > 0 ):
        if ( s.count(s[-1]) != 1 ):
            if ( lis.count(s[-1]) == 0 ):
                lis.append(s.pop())
            else:
                 s.pop()
        else:
            s.pop()
    return lis
