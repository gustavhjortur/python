# 1.



# 2.
def count_names(start):
    from urllib.request import urlopen
    import json
    res = urlopen('https://mooshak.ru.is/~python/names.json')
    d = (res.read().decode('utf-8') )
    print(json.loads(d).decode('utf-8'))
    
    return ()

    
nafnalisti = '''{"Nafn": "Linddís", "Fjoldi1": 1, "Fjoldi2": 1},
{ "Nafn": "Damjan", "Fjoldi1": 5, "Fjoldi2": 0},
{ "Nafn": "Bjarki", "Fjoldi1": 915, "Fjoldi2": 475},
{ "Nafn": "Þórhildur", "Fjoldi1": 374, "Fjoldi2": 38},
'''

count_names(nafnalisti)

#count_names('Bja')
#(3267, 1494)

#>>> count_names('Wat')
#(8, 2)

#>>> count_names('Snati')
#(0, 0)
