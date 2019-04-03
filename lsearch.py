def lsearch(x, nums):
    c = 0
    i = 0

    while i < len(nums):
        c = c + 1
        if nums[i] == x:
            print(i)
            return i
        else:
            i = i + 1

#test

lsearch(3,[1,2,3,4,5])
