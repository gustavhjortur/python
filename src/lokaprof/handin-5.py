def splitProp(list):
    if ':' not in list:
        return ''
    retValue = []
    for x in list.strip().split(';'):
        if x == '':
            continue
        k = x.split(':')[0].strip()
        v = x.split(':')[1].strip()
        retValue.append((k,v))
    return retValue

def css_properties(css):
    rawList = (css.replace('\n', '').split('{'))
    propList = []
    for x in rawList:
        propList.append( x.split('}', maxsplit=1)[0] )
    retValue = []
    for x in propList:
        tmp = ( splitProp(x) )
        for x in tmp:
            retValue.append(tuple(x))
    return retValue