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
'''

def parsNames(name):
    # Try to figure if it is a TV series
    newName = 'Movies'
    seriesName = ''
    if ('S' in name):
        print('\t\tS found ', name)
        print( name.split('.S')[0], ' ', name[(name.index('S')+1):(name.index('S')+3)] )
        #try:
        seriesName = '/Series' + str(int(name[(name.index('S')+1):(name.index('S')+3)]))
        #except:
        pass
        baseName = name.split('.S')[0]
        newName = baseName + seriesName
        #if ('S' in name) or ( ('s' + name[name.index('s')+1] ) in name):
    elif ('s' in name):
        if  (name[(name.index('s')+1):(name.index('s')+3)] ).isdigit:
            print('\n', name, '\n')
            for x in name:
                try:
                    seriesName = '/Series' + str(int(name[(name.index('s')+1):(name.index('s')+3)]))
                except:
                    pass
            baseName = name.split('.s')[0]
            newName = baseName + seriesName
    print()
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
            for x in filenames:
                print( inFolder, ' ', x , ' ',parsNames(x) )
                directory = (outFolder + parsNames(x))
                if not os.path.exists(directory):
                    os.makedirs(directory)
                # move or copy, select wisely
                print(x, ' ', directory)
                # ToDo fix pathname slash for multi platform combatabilety
                copyfile( (inFolder + '/' + x), (directory + '/' + x) )
                #move( (inFolder + '/' + x), (directory + '/' + x) )
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
    print()
    #print(len(f))
    for i in f:
        if fileDict.get( i ):
            #raise ItemExcistsError
            #fileDict[i] = tmp
            print( i, ' Already excists...')
            print( '\t\t\t\tend ', i.endswith('.png') )
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
  #  for (x) in list:
  #      print(x)
  #  print(list)
    #directory = (outFolder + 'asd/asd/asd')
    #if not os.path.exists(directory):
    #    os.makedirs(directory)
    return 0

#Read and list the incomming directory and file structure

#Pars names of incoming files








#os.system('rm -rf data/structured/*')
clean(sys.argv)
#clean(['runner', 'data/Down/', 'data/structured/']) #62 files
#clean('data/Download/', 'data/structured/') #5198 files
