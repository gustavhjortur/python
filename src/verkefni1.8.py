def excel_index(s):
    i = len(s) - 1
    seet = 0
    pos = 0
    while ( i >= 0 ):
        pos += ( ( ord( s[seet] ) - 64 ) * (26**i) )
        i -= 1
        seet += 1
    return pos
