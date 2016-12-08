import os
from subprocess import call


def clean(inFolder, outFolder):
    '''
    Funtion to take list of "video-files" in directory tree: inFolder
    and try to figure out how to organice them into structured tree: outFolder
    exit code: 0 == Normal
    exit code: 1 == Read folder does not excist
    exit code: 2 == Out folder does not excist
    exit code: 3 == 
    exit code: 4 == 
    exit code: 5 == 
    exit code: 6 == 
    '''
    if ( os.path.isdir(inFolder) != True):
        print(inFolder, ' Is not a folder')
        return 1
    if ( os.path.isdir(outFolder) != True):
        print(outFolder, ' is not a folder')
        return 1
    return 0

#Read and list the incomming directory and file structure

#Pars names of incoming files








os.system('rm -rf data/structured/*')
clean('data/Down/', 'data/structured/')
#clean('data/Download/', 'data/structured/')
