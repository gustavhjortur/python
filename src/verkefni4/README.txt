This is a Python schript to take a collection of video files and move them and structure them in to folders. (https://github.com/gustavhjortur/python/tree/master/src/verkefni4)

To use this script in M$ Windós: TBD...??? (also the path name issue)
To use this script Mac/Linux run: "./clean $NAME_OF_FILE_FOLDER $NAME_OF_DESTINATION"

NAME_OF_FILE_FOLDER is the name of the location of the video file collection fi. Downloads/
NAME_OF_DESTINATION is the name of the folder that the files should be copyed to fi. Destination/

This was created on Fedora21 native Python3.3.2 with no extra libraries.

files are put into folders based on the file name:
if the name seems to match a TV series they are sorted into name/seris number, or put into Movies except the following:
- .txt files are moved to the last used folder
- .mp3 and .ogg files are moved to the 'Music' folder
- .jpg, .png, and .gif files are moved to the 'Pictures' folder
- torrent, .nfo, .mta, .part files are moved to the 'Trash' folder

exit code: 0 == Normal
exit code: 1 == Folder issue (read or write)

ToDo
- fix use of path names
- impliment argparser to do proper argument handling (like grown-ups do).
- delete empty directoryes
