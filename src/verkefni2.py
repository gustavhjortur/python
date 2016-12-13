# 1. Write a function process_ls(output) that takes as a parameter a single string, which contains output from running ls -l in a directory. The function should return a list of all the files in the directory, ordered by size in descending order. Files with equal size should be ordered by the file name in ascending order.
import re
def process_ls(output):
    #print(output.sort)
    #for x in output:
    #listi = list(output.split(sep='\n'))
    # All directorys thrown out and files added to list
#    listi = list( filter(lambda n: n[0:1] != 'd', (list(output.split(sep='\n',s))) ) )
    #listinn = []
    #for x in output:
    #    listinn.append
    listi = list( filter(lambda n: n[0:1] != 'd', (list( x for x in output.split('\n'))) ) )
#    lis = list( filter(lambda n: n[27:29], ( n for n in listi) ) )
    #print(output)
    #print(listi)
  #  lis = []
    numb = int
    safn = []
    for x in listi:
        x = " ".join(x.split())
        x = " ".join(x.split('\''))
        x = " ".join(x.split(']'))
        x = " ".join(x.split('['))
        numb = int(*map(int, re.split(' ', x.strip())[4:5]))
        #numb = 5
        #print(numb)
        #lis.append( ( str(re.split(' ', x.strip(), maxsplit=8)[4:]) ) )
        safn.append([numb, str(re.split(' ', x.strip(), maxsplit=8)[-1])] )
    #newList = [[l[i] for i in listi] for l in listi]
  #  print(safn)
    l2 = sorted(safn, key=lambda x: (x[1]).lower())
    print(l2)
    #print(safn.sort(key=lambda x: (x[1]).lower()))
    l3 = sorted(l2, key=lambda x: x[0], reverse=True)
  #  print()
  #  print(safn)
    #numbers = []
    #for x in lis:
    #    x = " ".join(x.split())
    #    x = " ".join(x.split('\''))
    #    x = " ".join(x.split(']'))
    #    x = " ".join(x.split('['))
    #    x = ",".join(x.split(' , '))
        #t = str(re.split(', ', x.strip())[0:1] )
        #numbers.append( list(map(int, re.split(', ', x.strip())[-1])) )
    #    print('\t', x)
        #numbers.append( int( map(int, y) for y in t ) )
    #lis.sort(reverse=True )
    #numbers.sort()
    #print( sorted(lis, reverse=True, key=lambda x: x[0]) )
    #numb = list(int((y) for y in x for x in numbers ))
    #print (l)
    #return list( filter(lambda n: n[0:1] != 'd', listi ) )
    #l2 = str()
    l = []
    #print()
    for x in l3:
            #x = " ".join(x.split(']'))
            x = re.sub('\]', '', str(x))
            x = re.sub('\[', '', str(x))
            x = re.sub('\"', '', str(x))
    #        print(x)
    #        l2 += (str(re.split(', ', str(x), maxsplit=2)[-1]))
            l.append((re.split(', ', (x), maxsplit=2)[-1]))
    lis = []
    for x in l:
    #    print( re.sub(r'\'', '', x) )
        lis.append( re.sub(r'\'', '', x) )
    #print('\t', lis)
    #print( re.sub(r'\'\'', '\' \'', l2) )
    #print(l2)
    return lis

# 2. Sorting Icelandic Names
import locale
def sort_names(names):
    import locale
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    alphabet = u'aáàAâÂbBcCçÇdDeéEfFgGğĞhHiİîÎíīıIjJkKlLmMnNóoOöÖpPqQrRsSşŞtTuUûúÛüÜvVwWxXyYzZþÞæÆöÖ'
    print(names)
    name = sorted(names, key=lambda x: (x[0], x[:-1]) )
    lykill = []
    for x in names:
        #print(x.split()[-1])
        i1 = str(x.split()[0]).lower()
        #print(i1)
        i2 = str(x.split()[-1]).lower()
        #print(i2)
        i3 = (str(x.split()[1:]).lower()).strip('[]\'')
        i3 = re.sub('\',\ \'', '', i3)
        #print(i3)
        #print(i1 + i2 + i3)
        lykill.append(  i1 + i2 + i3 )
    #lyk = list(lykill)
    print(alphabet)
    print()
    print(alphabet.index('X'))
    d = {i:alphabet.index(i) for i in alphabet}
    print( sorted( name, key=lambda x: d.get(x) ) )
    #names.sort()
    #print( sorted( names, key=locale.strxfrm(lykill) ) )  
    #name = sorted(names, key=lambda x: for x in lykill[x] )
    print(name)
    return name

##sort_names(['Þórir Jakob Olgeirsson',
##    'Arnar Björn Pálsson',
##    'Eyþór Snær Tryggvason',
##    'Árni Jóhannsson',
##    'Eyþór Traustason',
##    'Arnar Bjarni Arnarson',
##    'Þórhildur Þorleiksdóttir'])

# 3. Poker hands
def rank_hand(hand):
    return []




# 4. countdown leist af Hjalta
import itertools
def countdown(dfile, letters):
    with open(dfile) as f:
        words = set(f.read().splitlines())
    result = set()
    for n in range(4,10):
        for p in itertools.permutations(letters, n):
            st = ''.join(p)
            if st in words:
                result.add(st)
    return sorted(result)

##print(countdown('data/all_words_no_short.txt', 'pythonxyz'))
##print(countdown('data/all_words_no_short.txt', 'countdown'))
##print(countdown('data/all_words_no_short.txt', 'kkkkkkkkk'))

# 5.   leist af Hjalta
import itertools
def insert_operators(seq, target):
    all_ops = ['+', '-', '']
    sseq = [str(x) for x in seq]
    for ops in itertools.product(all_ops, repeat=len(seq)-1 ):
        pairs = [ ''.join(t) for t in zip(sseq,ops) ]
        pairs.append(sseq[-1])
        expr = ''.join(pairs)
        if eval(expr) == target:
            return '%s=%d' % (expr, target)
    return None



##print( insert_operators([14,8,2,17,5,9],83) )
##print( '14+82-17-5+9=83\n' )
##print( insert_operators([34,9,82,21,32],32850) )
##print ( '34982-2132=32850' )
##print( insert_operators([1,2,3],5) )
# None
assert insert_operators([1,2,3],5) is None

def start_with3(n):
    return str(n)[0] == '3'

# 6.   Leist af Hjalta
import re
lenglish = re.compile('[a-z]+')
def hangman(dfile, state, guessed):
    with open(dfile) as f:
        words = f.read().splitlines()
    results = []
    for word in words:
        if not lenglish.fullmatch(word):
            continue
        if len(word) != len(state):
            continue
        for s, w in zip(state, word):
            if s != '-' and s != w:
                break
            if s == '-' and w in guessed:
                break
        else:
            results.append(word)
    return results

##print(hangman( 'data/all_words_no_short.txt', 's-a--o--s', 'aeiosu') )
##print(hangman( 'data/all_words_no_short.txt', 'hamster', 'hamster') )
##print(hangman( 'data/all_words_no_short.txt', '-------', 'aeiou') )

# 7.     Leist af Hjalta
import re
special_finder = re.compile('[+>]')

def star_split(elem):
    n = 1
    if '*' in elem:
        elem, n = elem.split('*')
        n = int(n)
    return n, elem

def zen_expand(code):
    if code == '':
        return ''
    m = special_finder.search(code)
    if not m:
        n, elem = star_split(code)
        return n * '<{0}></{0}>'.format(elem)
    else:
        oper = code[m.start()]
        elem, _, rest = code.partition(oper)
        n, elem = star_split(elem)
        
        if oper == '+':
            return (n * '<{0}></{0}>'.format(elem) + zen_expand(rest))
        else:
            return n * '<{0}>{1}</{0}>'.format(elem, zen_expand(rest))
    return None

test_cases = [
    ("", ""),
    ("dd", "<dd></dd>"),
    ("dd+div", "<dd></dd><div></div>"),
    ("dd>div", "<dd><div></div></dd>"),
    ("dd*3+div", "<dd></dd><dd></dd><dd></dd><div></div>"),
    ("a+div+p*3", "<a></a><div></div><p></p><p></p><p></p>"),
    ("table>tr*3>td*2", "<table><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>"),
    ("html>head+body>div+div+p>ul>li*3>a", "<html><head></head><body><div></div><div></div><p><ul><li><a></a></li><li><a></a></li><li><a></a></li></ul></p></body></html>")
]

for tc, exp in test_cases:
    res = zen_expand(tc)
    print(res)
    print(exp)
    assert res == exp
    print('-- passed --')

##print(zen_expand("a+div+p*3"))
##print('"<a></a><div></div><p></p><p></p><p></p>"\n')
##print(zen_expand("dd") )
##print('"<dd></dd>"\n')
##print( zen_expand("table>tr*3>td*2") )
##print('"<table><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>"\n')








