def flatten(aList):
    res = list(range(len(aList)))
    res = sorted(res, key=lambda x: aList[res.index(x)])
    return res



([166, 625, 126, 111, 176, 531, 745, 295, 856, 589, 401, 498, 573, 522, 136],)


