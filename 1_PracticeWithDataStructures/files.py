# files.py
"""
NTEC 361
date: <ex: mm/dd/yyyy>
<your name>
"""

# general instructions: 
#   - update the file comment header above
#   - print a blank line between sections of output
#   - Add your comments using triple quotes. Example:
''' student comment'''

def main():
    # we want to see what is going on in the file system.
    # open file explorer and navigate to your working directory. 
    # you should see just the files in the repo.

    '''
    - creation
    '''
    # files are created with the open function.
    # look at the different modes that can be used with this function
    # https://docs.python.org/3/library/functions.html#open

    # We will use the following file name in this exercise
    fileName = "myFile.txt"

    # try the following code:
    try:
        infile = open(fileName)
    except Exception as error:
        print(type(error), error)
    print()

    # try the following code:
    try:
        infile = open(fileName, 'r')
    except Exception as error:
        print(type(error), error)
    print()

    # What errors did you get? Add a comment here and a copy of the output:

    # The default mode for open() is 'r', so the statements above are really
    # the same code. Logically a file must exist in order for us to read it.

    # Now write the same code but change the mode to 'a'
    # your code here

    # close the file

    # use file explorer to find where this file created. Indicate that
    # location in a comment below.

    # Using a text editor, edit the text file that was created to add 
    # some text - a few lines of gibberish. Don't forget to close the file
    # in the text editor.

    # Now write the same code but change the mode to 'w'
    # your code here. 

    # close the file

    # Open the text file in a text editor and view the contents
    # add a comment here describing the contents:


    '''
    - element access
    - traversal
    '''

    # NOTE on file names
    #   VS Code runs the program from the root of the folder structure. 
    #   That means that this file is run from the folder above.
    #   Note that the filename in the line below uses relative pathing.
    #   It includes both the folder and filename for sample.txt.
    # Do not change the filename below.
    fileName = "1_PracticeWithDataStructures\\sample.txt"

    # View the file in a text editor.

    # There are several ways to read a file

    ''' Method 1: read() '''
    # open your book to p. 161 (section 5.9.2) and replicate the code at the 
    # center of the page that opens, reads, and prints the file. Use "infile" 
    # again as the file handle

    # compare the program output with what you see in a text editor.
    # are they the same? Add your answer in a comment here:

    # add a print statement that prints the length of data
    # this demonstrates that data is one big string.
    # you might try counting the characters to see if the length includes
    # line feeds.

    # closing the file - uncomment the line below when you get here
    #infile.close()

    ''' Method 2: readlines() '''
    # uncomment the code below and run this program
    '''
    infile = open(fileName)
    data = infile.readlines()
    print(data)
    print()
    infile.close()
    '''
    # answer the following questions:
    # what type is data?
    # how is it different from the data in Method 1?
    # Do the strings have escape characters?

    # write a for loop that uses data as the sequence and prints out
    # the text lines. What do you have to do in the print statement 
    # to make the ouput look like what you see in a text editor?

    # your code here

    # closing the file - uncomment the line below when you get here
    #infile.close()

    ''' Method 3: readline() '''
    # uncomment the following code, then add comments above each line
    # of code to describe what that line does
    '''
    infile = open(fileName)
    line = infile.readline()
    while line != "":
        print(line[:-1])
        line = infile.readline()
    infile.close()    
    '''

    ''' Method 4: using the file handle as a sequence '''
    # replicate the last section of code on p. 162 that uses infile as the
    # sequence in the for loop.
    # your code here


    '''
    - element insertion
    - element updates
    '''
    # these are really just writing to a file.
    # open a file named "mydata.txt" for writing using the 
    # file handle "outfile"

    # Write several lines of gibberish to the file and close it.

    # view the new file in a text editor to verify that the program worked.


main()