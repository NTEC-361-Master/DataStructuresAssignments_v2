# strings.py
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
    '''
    - creation
    '''
    # create two strings named "s1" and "s2"
    # create s1 using a literal string with at least 3 words in it
    # create s2 using the input() function. Enter a string with at 
    #    least 3 words in it for testing
    # your code below here

    # print both strings


    '''
    - element access
    - traversal
    '''
    # this next section demonstrates both access and traversal
    # write a for loop that prints individual characters from s1, each on 
    # a separate line.
    # print every third character starting with the second one.
    # DO NOT hard code the stop value - use len()
    # your code should use indexing
    # the output line should contain the value of the index as well as 
    # the character e.g. "2 a"
    # your code below here


    '''
    - element insertion
    '''
    # strings are immutable, but we can mimic changes using string operations
    # and forming a new string. For example insertion can be mimicked by using
    # slicing to split the original string into two parts and concatentation 
    # (+ operation) to form the new string with the inserted string between 
    # the two slices
    #
    # form two new string variables using slicing on s1 to get the first and 
    # third word. Don't use numbers for indexes. Use methods to find the 
    # indexes you need in your slice. 
    # see https://docs.python.org/3/library/stdtypes.html#string-methods

    # create a third variable with the string you want to insert

    # form a new string named "snew" using concatenation and print snew.


    '''
    - element deletion
    '''
    # the goal is to delete the word you just inserted from snew. But, we 
    # want to do everything programmatically. Follow the steps below to 
    # generate your two slices.
    # use the find() method to find the index of the word to delete.
    # see https://docs.python.org/3/library/stdtypes.html#string-methods
    # find the index of the beginning of the word you want to delte

    # use the find() method to find the word after the one you are deleting.

    # use the indexes to form two slices

    # use concatenation to form snew and print it


    '''
    - element updates
    '''
    # one form of update is replacing an old word with a new word. This is
    # so common Python has a method for it. Use the replace() method to 
    # replace a word in s1. Assign the new string to snew and print it.


main()