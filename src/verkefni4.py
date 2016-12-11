#!/usr/bin/env python3
import os, sys
from subprocess import call
from os import listdir, walk
from os.path import isfile, join
from shutil import copyfile
from shutil import move

# Following used while testing to start with empty structure folder
#os.system('rm -rf data/structured/*')

'''
Funtion to take list of "video-files" in directory tree: inFolder
and try to figure out how to organice them into structured tree: outFolder
exit code: 0 == Normal
exit code: 1 == Read folder does not excist

This can be downloaded from:
https://github.com/gustavhjortur/python/tree/master/src/verkefni4

ToDo
- fix use of path names, each spot has comment: #ToDo fix pathname
- impliment argparser
- delete empty directoryes
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
         name.lower().endswith('.nfo') or
         name.lower().endswith('.mta') or
         name.lower().endswith('.part') ):
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
        return 'unknown'
    elif ( '#' in name ):
        baseName = name.split('.#')[0]
        newName = baseName + seriesName
    elif ( 'S' in name ):
        try:
            #ToDo fix pathname
            seriesName = '/Series' + str(int(name[(name.index('.S')+2):(name.index('.S')+4)]))
        except:
            try:
                #ToDo fix pathname
                seriesName = '/Series' + str(int(name[(name.index('.S')+2):(name.index('.S')+3)]))
            except:
                pass
        if ( seriesName ):
            baseName = (name.split('.S')[0]).title()
            return baseName + seriesName
    elif ( '.s' in name ):
        if ( (name[(name.index('.s')+2):(name.index('.s')+4)] ).isdigit ):
            for x in name.split('.s'):
                try:
                    #ToDo fix pathname
                    seriesName = '/Series' + str(int(name[(name.index('.s')+2):(name.index('.s')+4)]))
                except:
                    try:
                        #ToDo fix pathname
                        seriesName = '/Series' + str(int(name[(name.index('.s')+2):(name.index('.s')+3)]))
                    except:
                        pass
            if ( seriesName ):
                baseName = (name.split('.s')[0]).title()
                return baseName + seriesName
    elif ( 'x' in name ):
        for x in name.split('x'):
            if ( (name[(name.index('x')+1):(name.index('x')+3)] ).isdigit() ):
                try:
                    #ToDo fix pathname
                    seriesName = '/Series' + str(int(name[name.index('x')-2:name.index('x')]))
                    seperator = str(int(name[name.index('x')-2:name.index('x')]))
                except:
                    try:
                        #ToDo fix pathname
                        seriesName = '/Series' + str(int(name[name.index('x')-1:name.index('x')]))
                        seperator = str(int(name[name.index('x')-1:name.index('x')]))
                    except:
                        pass
            if ( seriesName ):
                baseName = (name.split(str(seperator+'x'))[0]).title()
                return baseName[:-1] + seriesName
    return newName

def findAllFiles(inFolder, outFolder, counter=0 ):
    for (dirpath, dirnames, filenames) in walk(inFolder):
        for x in dirnames:
            counter = findAllFiles( (inFolder + x), outFolder, counter )
        lastDirectory = ''
        for x in filenames:
            newDirectory = parsNames(x)
            if (newDirectory == 'useLast' ):
                newDirectory = lastDirectory
            directory = (outFolder + newDirectory)
            if not os.path.exists(directory):
                os.makedirs(directory)
            # ToDo fix pathname slash for multi platform combatabilety
            copyfile( (inFolder + '/' + x), (directory + '/' + x) )
            #move( (inFolder + '/' + x), (directory + '/' + x) )
            counter += 1
            #print( '-', counter, '-', end="")
            lastDirectory = newDirectory
        break
    return counter

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
    if ( os.path.isdir(inFolder) != True):
        print(inFolder, ' Is not a folder')
        return 1
    if not os.path.exists(outFolder):
                    os.makedirs(outFolder)
    if ( os.path.isdir(outFolder) != True):
        print(outFolder, ' is not a folder or could not been created')
        return 1
    counter = findAllFiles(inFolder, outFolder)
    print( counter, 'files moved' )
    return 0





#For test in "ide" (like idle) lin 2 or 3 below kan be used
clean(sys.argv)
#clean(['runner', 'data/Down/', 'data/structured/']) #62 files
#clean(['runner', 'data/Download/', 'data/structured/']) #5198 files
