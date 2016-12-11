This is a Python schript to take a collection of video files and move them and structure them in to folders.

To use this script in M$ Windós: TBD...??? (also the path name issue)
To use this script Mac/Linux run: "./clean $NAME_OF_FILE_FOLDER $NAME_OF_DESTINATION"

NAME_OF_FILE_FOLDER is the name of the location of the video file collection
NAME_OF_DESTINATION is the name of the folder that the files should be copyed to

This was created on Fedora21 native Python3.3.2 with no extra libraries.

exit code: 0 == Normal
exit code: 1 == Folder issue (read or write)

ToDo
- fix use of path names
- impliment argparser to do proper argument handling (like grown-ups do).
