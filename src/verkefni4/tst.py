#!/usr/bin/env python3
import os, sys
from subprocess import call
from os import listdir, walk
from os.path import isfile, join
from shutil import copyfile
from shutil import move


'''
Funtion to take list of "video-files" in directory tree: inFolder
and try to figure out how to organice them into structured tree: outFolder
exit code: 0 == Normal
exit code: 1 == Read folder does not excist
'''

def parsNames(name):
    # Try to figure if it is a TV series
    return 'asd'

def clean(args):
    inFolder = args[1]
    outFolder = args[2]
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
    print(inFolder, ' ', outFolder)
    #print( list, '\n', len(list) )
    #if not os.path.exists(directory):
    #    os.makedirs(directory)
    return 0


#for arg in sys.argv:
#    print(arg)
#print(sys.argv[1])
#print(args)

clean(sys.argv)
#Read and list the incomming directory and file structure

#Pars names of incoming files






