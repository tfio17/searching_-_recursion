#
#
## Tom
#
## mySearches library
#
#

# bsearch that will return the index of the number in the list if found
#   and will return a -1 if not found
def bsearch(x, nums):
    item = 0
    low = 0
    high = len(nums)-1
    c = 0

    while low <= high:              # while there is a range to search
        #print("Step counter: ", c,item)
        mid = (low + high)//2       # position of the guess
        item = nums[mid]
        #print("The Mid:",item)

        if x == item:               # found it!
            print("Binary found it at: ", mid, "Number of steps: ", c, "")
            return mid, c

        elif x < item:              # x is in the lower half of the range
            high = mid -1           #   move the bottom marker up
            c = c + 1               #   increase the step counter

        else:                       # x is in the upper half
            low = mid +1            #   move the bottom half up
            c = c + 1               #   up the step counter
    print("Number not found")
    print("Binary Search took",c,"passes")
    return -1, c                       # x is not found


# linear search, will return the index of the number in the list
#   if found and will return -1 if not found

def lsearch(x, nums):
    c = 0
    for i in range(0,len(nums)):
        if x == nums[i]:
            c = c + 1
            print("Linear found it at: ", i, "Number of steps: ", c, "\n")
            return i
        else:
            c = c + 1

            
    
    print("Number not found")
    print("Linear Search took",c,"passes\n")
    return -1



    
