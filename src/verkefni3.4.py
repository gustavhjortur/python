def parse_submissions(directory):
    import os, shutil, glob, re
    fileList = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == ('data.tcl'):
                fileList.append(os.path.join(root, file))
    data = []
    for x in fileList:
        file = open(str(x), 'r')
        content = file.read()
        file.close()
        if ( re.search('Classify Accepted', content) ):
            tmpData = content.splitlines()
            tmp = []
            tmp.append( int(*[x.split(maxsplit=3)[-1] for x in tmpData if 'Date' in x]) )
            tmp.append( *[x.split(maxsplit=3)[-1] for x in tmpData if 'Team' in x] )
            tmp.append( *[x.split(maxsplit=3)[-1] for x in tmpData if 'Problem' in x] )
            data.append( tmp )
    tuppluListi = []
    for x in sorted(data):
        tuppluListi.append( tuple( x[1:] ) )
    return tuppluListi
