def flatten(aList):
    res = list(range(len(aList)))
    combined = list( zip(aList, res) )
    combined.sort()
    return [ n for x, n in combined ]
