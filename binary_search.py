#
#
## Tom
#
## Binary search example
#
#

def bsearch(x, nums):
    item = 0
    low = 0
    high = len(nums)-1
    c = 0

    while low <= high:              # while there is a range to search
        print("Step counter: ", c,item)
        mid = (low + high)//2       # position of the guess
        item = nums[mid]
        print("The Mid:",item)

        if x == item:               # found it!
            return mid

        elif x < item:              # x is in the lower half of the range
            high = mid -1           #   move the bottom marker up
            c = c + 1               #   increase the step counter

        else:                       # x is in the upper half
            low = mid +1            #   move the bottom half up
            c = c + 1               #   up the step counter
    return -1                       # x is not found

MyNums = list(range(1,1000000))

x = bsearch(99999,MyNums)
print(x)
print("The number is found!: ", MyNums[x])
