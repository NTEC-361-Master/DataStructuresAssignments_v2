# problem-4.py
"""
NTEC 361
date: <ex: mm/dd/yyyy>
<your name>
"""

"""
INSTRUCTIONS:

READ ALL OF THE INSTRUCTIONS BEFORE YOU START WORKING ON THE CODE

0) The code below will not run. Your job is to fix it.
1) The code below contains 3 errors.
2) Your job is to fix the errors and to place a comment above the line that
   contained the error and tell me what you changed to fix the problem.
3) Make sure the code runs
"""

# define a function named main


def main():
    # print out a message
    print("This program illustrates a chaotic function")
    # ask the user for input
    x = evalinput("Enter a number between 0 and 1: "))
    # loop 10 times
    for i inrange(10)
        # calculate value of x
        x=3.9 * x * (1 - x)
        # print out new value of x
        print(x)

# call the main function defined above
main()
