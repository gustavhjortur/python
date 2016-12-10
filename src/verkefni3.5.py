def jam(texti):
    firstList = []
    for x in texti.splitlines():
        tmp = x.split(', ')[1:-1]
        first = (tmp[0]).split(' with ')
        tmp[0] = ''
        firstList.append(first[0])
        firstList.append(first[1])
        if ' and ' not in  tmp[1]:
            firstList.append(tmp[1])
            tmp[1] = ''
        try:
            if ' and ' in  tmp[2]:
                tmpList = (tmp[2]).split(' and ')
                for z in tmpList:
                    firstList.append(z)
                tmp[2] = ''
        except:
            pass
        i = 0
        isPlus = False
        for z in tmp:
            if ' and ' in z and isPlus:
                break
            if isPlus:
                firstList.append( z )
            if z.startswith('plus ') and isPlus == False:
                isPlus = True
                firstList.append( z.strip( 'plus ' ) )
        if tmp[-1].startswith('plus ') == False:
            first = (tmp[-1]).split(' and ')
            for y in first:
                firstList.append( y )
    returnDict = dict()
    for i in firstList:
        if i == '':
            pass
        elif returnDict.get( i ):
            tmp = returnDict[ i ]
            tmp += 1
            returnDict[i] = tmp
        else:
            returnDict[i] = int(1) 
    return returnDict
