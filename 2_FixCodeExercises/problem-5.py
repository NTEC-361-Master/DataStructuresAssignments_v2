# problem-5.py
"""
NTEC 361
date: <ex: mm/dd/yyyy>
<your name>
"""

"""
INSTRUCTIONS:

READ ALL OF THE INSTRUCTIONS BEFORE YOU START WORKING ON THE CODE

0) The code below will not run. Your job is to fix it.
1) The code below contains 5 errors.
2) Your job is to fix the errors and to place a comment above the line that
   contained the error and tell me what you changed to fix the problem.
3) Make sure the code runs
"""


def main:
    print("This program calculates the future value of an investment.")
    print()

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))
    years = eval(input("Enter the number of years: ")

    print("Year   Value")
    print("------------")
    for i in range(years+1)
        # use string formatting to make output align like sample provided
        print("{0:3}   ${1:7.2f".format(i, principal))
        principal == principal * (1 + apr)

main()
