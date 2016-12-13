#Centris 2.0 - MySchool on the command line
##Assignmend deskription
Create an API and a command line interface (CLI) for MySchool. Through the API you could, e.g.,

    list all courses you are taking,
        list all your assignments,
            get information about an assignment,
                submit a solution to an assignment,
                    get your timetable.

                    Using your API you should then create a CLI. Examples might be
                    Get your timetable

                    centris2 timetable

                    List your assignments

                    centris2 assign list

                    List course assignments

                    centris2 assign list Python

                    Submit assignment

                    centris2 assign submit Python "Verkefni 5" -f verk5.zip -c "Skemmtilegasta verkefni ever! ^^"

                    Note

                    HTML forms that allow files to be uploaded, have the enctype attribute set to multipart/form-data, which specifies how the form data should be encoded when submitted to the server. If you use the requests library, it only encodes the data in this way if you specify a file to upload. If you only want to submit a comment to an assignment, and no files, then you must also submit an empty file to force the requests library to encode the data correctly. You can do this, for example, by including the named parameter files={ 'FILE': ('', '') } in the post request.

## ToDo :
- 
