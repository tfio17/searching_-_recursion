#
#
## Tom
#
## implement power function recursively
#
#

def myPow(num,power):
    if power == 1:
        return num
    else:
        return num * myPow(num, power-1)

#main

a = myPow(7,3)
print(a)

b = myPow(2,6)
print(b)

c = myPow(3,3)
print(c)
