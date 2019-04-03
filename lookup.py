#
#
## Tom
#
## lookup function
#
#

# import the search functions
# read in the file rands.txt
# search for (78700, 3333, 1118)

# import search functions
import mySearches

# Choose file to read
infile = 'rands.txt'

# open/read/close
f = open(infile, 'r')
data = f.read()
f.close()

# clean

data = data.replace('\n','\t')
data = data.split('\t')
myList = [int(x) for x in data]
myList.sort()

# search

print("Looking for: ", 78700)
mySearches.bsearch(78700,myList)
mySearches.lsearch(78700,myList)

print("Looking for: ", 3333)
mySearches.bsearch(3333,myList)
mySearches.lsearch(3333,myList)

print("Looking for: ", 1118)
mySearches.bsearch(1118,myList)
mySearches.lsearch(1118,myList)
