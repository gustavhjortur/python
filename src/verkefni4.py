#!/usr/bin/env python3
import os, sys
from subprocess import call
from os import listdir, walk
from os.path import isfile, join
from shutil import copyfile
from shutil import move

# Following used while testing to start with empty structure folder
os.system('rm -rf data/structured/*')

'''
Funtion to take list of "video-files" in directory tree: inFolder
and try to figure out how to organice them into structured tree: outFolder
exit code: 0 == Normal
exit code: 1 == Read folder does not excist

ToDo
- fix use of path names
- impliment argparser
'''
def notMovieOrTv(name):
    if ( name.lower().endswith('.mp3') ):
        return 1
    if ( name.lower().endswith('.ogg') ):
        return 1
    if ( name.lower().endswith('.txt') ):
        return 2
    if ( name.lower().endswith('.jpg') or
         name.lower().endswith('.png') or
         name.lower().endswith('.gif') ):
        return 3
    if ( 'orrent' in name or
         name.lower().endswith('.nfo') ):
        return 99
    return 0

def parsNames(name):
    # Try to figure if it is a TV series
    newName = 'Movies'
    seriesName = ''
    name = ( name.replace(' ', '.').replace('_', '.').replace('-', '.') )
    otherType = notMovieOrTv(name)
    if ( otherType ):
        if ( otherType == 1 ):
            return 'Music'
        if ( otherType == 2 ):
            return 'useLast'
        if ( otherType == 3 ):
            return 'Pictures'
        if ( otherType == 99 ):
            return 'Trash'
        #baseName = 'Music'
        #newName = baseName + seriesName
        return 'unknown'
    elif ( '#' in name ):
        print( '# ',  name.split('.#')[0], ' ', name[(name.index('#')+1):(name.index('#')+3)] )
        baseName = name.split('.#')[0]
        newName = baseName + seriesName
    elif ( 'S' in name ):
        #print('\t\tS found ', name)
        #print( 'S ',  name.split('.S')[0], ' ', name[(name.index('S')+1):(name.index('S')+3)] )
        #print( name.replace(' ', '_') )
        try:
            seriesName = '/Series' + str(int(name[(name.index('.S')+2):(name.index('.S')+4)]))
        except:
            try:
                seriesName = '/Series' + str(int(name[(name.index('.S')+2):(name.index('.S')+3)]))
            except:
                pass
        if ( seriesName ):
            baseName = (name.split('.S')[0]).title()
            return baseName + seriesName
        #if ('S' in name) or ( ('s' + name[name.index('s')+1] ) in name):
    elif ( '.s' in name ):
        if ( (name[(name.index('.s')+2):(name.index('.s')+4)] ).isdigit ):
            #print('\n', name, '\n')
            for x in name.split('.s'):
                try:
                    #print( name[(name.index('s')+1):(name.index('s')+3)] )
                    seriesName = '/Series' + str(int(name[(name.index('.s')+2):(name.index('.s')+4)]))
                    #seriesName = '/Series' + str(int(name[(name.index('s')+1):(name.index('s')+3)]))
                    #print('\t\t\t', seriesName)
                except:
                    try:
                        #print( name[(name.index('s')+1):(name.index('s')+3)] )
                        seriesName = '/Series' + str(int(name[(name.index('.s')+2):(name.index('.s')+3)]))
                        #seriesName = '/Series' + str(int(name[(name.index('s')+1):(name.index('s')+3)]))
                        #print('\t\t\t', seriesName)
                    except:
                        pass
            if ( seriesName ):
                baseName = (name.split('.s')[0]).title()
                return baseName + seriesName
    elif ( 'x' in name ):
        for x in name.split('x'):
            print(x)
            if ( (name[(name.index('x')+1):(name.index('x')+3)] ).isdigit() ):
                print('\t', name[(name.index('x')-2):(name.index('x')+3)], ' ', name, ' ', name.index('x'))
                print( '\t\t\t', name[name.index('x')-2:name.index('x')+3] )
                try:
                    seriesName = '/Series' + str(int(name[name.index('x')-2:name.index('x')]))
                    seperator = str(int(name[name.index('x')-2:name.index('x')]))
                    #numb = int( name[name.index('x')-2:name.index('x')] )
                    #print('\t\t\t\t first')
                except:
                    try:
                        seriesName = '/Series' + str(int(name[name.index('x')-1:name.index('x')]))
                        seperator = str(int(name[name.index('x')-1:name.index('x')]))
                        #numb = int( name[name.index('x')-1:name.index('x')] )
                        #print('\t\t\t\t seccond')
                    except:
                        pass
            if ( seriesName ):
                baseName = (name.split(str(seperator+'x'))[0]).title()
                print( '\t\t', baseName[:-1], ' ', seriesName, '\tNafnid mitt')
                return baseName[:-1] + seriesName
                #for x in name.split('.'):
                #print( '\t\t', baseName )
    #print()
    return newName

def findAllFiles(inFolder, outFolder, fileDict=dict()):
    f = []
    d = []
    if len(fileDict) != -1:
        for (dirpath, dirnames, filenames) in walk(inFolder):
            f.extend(filenames)
            d.extend(dirnames)
            #print('\t\t', dirnames, 'asd')
            for x in dirnames:
                findAllFiles( (inFolder + x), outFolder, fileDict )
            #dp.extend(dirpath)
            #print(filenames, '\t', inFolder, dirnames)
            lastDirectory = ''
            for x in filenames:
                #print( inFolder, ' ', x , ' ',parsNames(x) )
                newDirectory = parsNames(x)
                if (newDirectory == 'useLast' ):
                    newDirectory = lastDirectory
                directory = (outFolder + newDirectory)
                if not os.path.exists(directory):
                    os.makedirs(directory)
                # move or copy, select wisely
                #print(x, ' ', directory)
                # ToDo fix pathname slash for multi platform combatabilety
                copyfile( (inFolder + '/' + x), (directory + '/' + x) )
                #move( (inFolder + '/' + x), (directory + '/' + x) )
                lastDirectory = newDirectory
            break
    else:
        for (dirpath, dirnames, filenames) in walk(inFolder,'/',str(x for x in d)):
            f.extend(filenames)
            d.extend(dirnames)
            for x in dirnames:
                findAllFiles( (inFolder + x), fileDict)
            #dp.extend(dirpath)
            print(filenames, '\t',inFolder, dirnames)
            break
    #print()
    #print(len(f))
    for i in f:
        if fileDict.get( i ):
            #raise ItemExcistsError
            #fileDict[i] = tmp
            print( i, ' Already excists...')
            #print( '\t\t\t\tend ', i.endswith('.png') )
        else:
            fileDict[i] = inFolder
    return fileDict
def printInstructions():
    print('''
    To use this script run: "./clean $NAME_OF_FILE_FOLDER $NAME_OF_DESTINATION"
    NAME_OF_FILE_FOLDER is the name of the location of the video file collection
    NAME_OF_DESTINATION is the name of the folder the files should be copyed to
    ''')
    return 0

def clean(args):
    try:
        inFolder = args[1]
    except:
        printInstructions()
        return 1
    try:
        outFolder = args[2]
    except:
        printInstructions()
        return 1
    #if ( os.path.isdir(inFolder) != True):
    if ( os.path.isdir(inFolder) != True):
        print(inFolder, ' Is not a folder')
        return 1
    if not os.path.exists(outFolder):
                    os.makedirs(outFolder)
    if ( os.path.isdir(outFolder) != True):
        print(outFolder, ' is not a folder or could not been created')
        return 1

    #onlyfiles = [f for f in listdir(inFolder) if isfile(join(inFolder, f))]
    #print(onlyfiles, 'lengd: ',len(onlyfiles) )
    #print()
    list = ( findAllFiles(inFolder, outFolder) )
    print()
    #print( list, '\n', len(list) )
    print( len(list) )
    return 0





#os.system('rm -rf data/structured/*')
#clean(sys.argv)
#clean(['runner', 'data/Down/', 'data/structured/']) #62 files
clean(['runner', 'data/Download/', 'data/structured/']) #5198 files
