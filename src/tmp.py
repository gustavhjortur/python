import re
def process_ls(output):
    listi = list( filter(lambda n: n[0:1] != 'd', (list( x for x in output.split('\n'))) ) )
    numb = int
    safn = []
    for x in listi:
       x = " ".join(x.split())
       x = " ".join(x.split('\''))
       x = " ".join(x.split(']'))
       x = " ".join(x.split('['))
       numb = int(*map(int, re.split(' ', x.strip())[4:5]))
       safn.append([numb, str(re.split(' ', x.strip(), maxsplit=8)[-1])] )
    safn.sort(key=lambda x: (x[1]).lower())
    safn.sort(reverse=True)
    l2 = sorted(safn, key=lambda x: (x[1]).lower())
    l3 = sorted(l2, key=lambda x: x[0], reverse=True)
    l = []
    for x in l3:
        x = re.sub('\]', '', str(x))
        x = re.sub('\[', '', str(x))
        x = re.sub('\"', '', str(x))
        l.append((re.split(', ', (x), maxsplit=2)[-1]))
    lis = []
    for x in l:
        lis.append( re.sub(r'\'', '', x) )
    return lis
