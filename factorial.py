#
#
## Tom
#
## recursion w/ factorial
#
#

def myfact(n):
    if n == 0:
        return 1
    else:
        return n * myfact(n-1)

#********************************


def dofact():
    print("*****************")
    x = 8
    print(" Value = ",x," and Factorial of Value = ",myfact(x))
    print("*****************")

#********************************

# run
dofact()
