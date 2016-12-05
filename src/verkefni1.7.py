def scramble(l1, l2):
    ret = [None] * len(l1)
    i = 0
    for x in l2:
        ret[i] = l1[x]
        i += 1
    return ret
