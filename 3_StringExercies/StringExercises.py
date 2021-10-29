# String Exercises
"""
NTEC 361
date: <ex: mm/dd/yyyy>
<your name>
"""

# INSTRUCTIONS

# In the first part of this assignment, add a comment above each line of code
# describing what it does. Be specific. Use multiple comment lines if 
# you need to.
#
# In the second part (below the code provided) read the comments and 
# provide code to match the instructions.
#
# Make sure your file runs and generates the correct results.

def main():
    # example comment: define variable str1 with string "Hello"
    str1 = "Hello"
    # example comment: print out the 2nd letter of str1
    print(str1[1])

    # ASSIGNMENT QUESTIONS START HERE 
    # Add a comment above each line of code that describes what it does.
    print(str1[-2])
    print(str1[:3])
    print(str1[2:len(str1)-1])
    str2 = "World"
    print(str1+str2)

    # write code below to iterate over str1 and print each character
    # separated by a space in a single line
    # Your code goes here

    # write code below. Create 2 strings. Print each. Print concatenation 
    # of them.
    # Your code goes here

    # write code that demonstrates parsing of an input phrase into 
    # individual words.
    # Your code goes here

    # write code that gets pi from the math library and outputs as "3.14"
    # using string formatting.
    # Your code goes here

    # The following is only asking for comments to explain the code.
    # in the code below, what does line[:-1] evaluate to?
    # assume infile has been opened for reading a text file
    # assume infile is a text file with multiple lines each line ending with
    # a carriage return/linefeed character
    # NOTE: you are just being asked to answer the questions above. DO NOT
    # uncomment the code below.
    '''
    for line in infile:
        print(line[:-1])
    '''


main()
