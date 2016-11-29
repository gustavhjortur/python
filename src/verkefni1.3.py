def reverse_words(s):
    if s == '' or s == ' ':
        return ''
    listi = s.split()
    st = ' '.join(str(e) for e in listi[::-1] )
    return st

