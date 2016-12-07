from urllib.request import urlopen
import json
import re
def count_names(start):
    fjoldi1 = 0
    fjoldi2 = 0
    res = urlopen('https://mooshak.ru.is/~python/names.json')
    read_data = res.read().decode('utf-8')
    data = json.loads(read_data)
    leit = '^' + start
    for x in data:
        if re.search(leit, str(x.get('Nafn'))):
            fjoldi2 += ( x.get('Fjoldi2') )
            fjoldi1 += ( x.get('Fjoldi1') )
    return (fjoldi1, fjoldi2)
