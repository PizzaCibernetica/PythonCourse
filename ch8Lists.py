# This is the chapter about lists

from doctest import Example


print("-- LISTS --")

# Algorithms        = a set of rules used to solve a problem
# Data Structures   = a particular way of organizing data in a computer

# What is not a "Collection"
# most of our variables have one value in them - when we put a new vlaue in the variable, 
# the old value is overwritten

# What is collection?
# somewhat like suitcases - we can put a lot of stuff min it , we can organize it , etc
# A "List" is a kind of "Collection"
# a collection allows us to put many values in a single "variable"
# a collection is nice because we can carry all many values around in one convenient package

friends = ['Joseph','Glenn','Sally']        # example of lists

carryon = ['socks', 'shirt', 'perfume']     # example of lists

# List Constants
# List constants are surrounded by square brackets and the elements in the list are separeted by commas
# A list element can be any Python object - even another list
# A list can be empty

print([1,24,76])            # can have numbers 
print(['red','yellow','blue']) # or strings
print( [ 1, [5,6], 7])      # it's a 3 item list   # can have a list inside of another list - 
print([])                   # empty list

# the for statement is a great way to iterate through lists 

friends = ['Joseph','Glenn','Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')
# equivalent loop
z = ['Joseph','Glenn','Sally']
for x in z :
    print('Happy New Year:', x)
print('Done!')

# Just like strings, we can get at any single element in a list using an index specified in square brackets
# they are zero based - therefore [0,1,2,3...]

friends = ['Joseph','Glenn','Sally']
print([1])      # print friends sub one

# Lists are mutable (Strings are NOT mutable)
# Strings are "immutable" - we cannot change the contents of a string - we must male a new string to make any change
# Lists are "mutable" - we can change an element of a list using the index operator

fruit = 'Banana'
# fruit[0] = 'b'  will get a traceback
print("fruit[0] = 'b'  # will get a traceback")

x = fruit.lower()
print(x)

lotto = [2,14,26,41,63]
print(lotto)

lotto[2] = 28
print(lotto)

# How long is a list?
# the len() function takes a list as a parameter and returns the number of elements in the list
# actually len() tells us the number of elements of any set or sequence (such as a string...)
# it will output an integer

greet = 'Hello Bob'
print(len(greet))
# 9

x = [1,2,'Joe',99]
print(len(x))
# 4

# RANGE 
# using the range function
# the range function returns a list of numbers that range from 0 to one less than the parameter

print(range(4))
# [0,1,2,3] from the class
# range(0,4) from VS Code

# we can construct an index loop using for and an integer iterator
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))

print(range(len(friends)))

# for i in range(10):
#     print(i)


# the following loops do hte same things
friends = ['Joseph', 'Glenn', 'Sally']

# this is cleaner - to be prefered 
for friend in friends:
    print('Happy New Year:', friend)

# this to be used if we need to have a index, and need to access specific index/value
# [0,1,2]  it will create an index 
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)


# Concatenating lists using +

# we can create a new list by adding two existing lists together

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c) 

print(a)

# lists can be sliced using   ":"
# similar to strings

# Remember: JUst like in strings, the second number is "up to but not including"
#  

t =[9,41,12,3,74,15]
print(t[1:3])   # will print index 1 all the way to 3 excluded, therefore index 1 and index 2

print(t[:4])    # will print from beginning to index 4 excludex, therfore index 0, 1, 2

print(t[:])     # this will print all

print(t[3:])    # this will print from index 3 to the end, therefore 3,4,5


# Lists Methods

# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].

# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

# list.clear()
# Remove all items from the list. Equivalent to del a[:].

# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

# list.count(x)
# Return the number of times x appears in the list.

# list.sort(*, key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

# list.reverse()
# Reverse the elements of the list in place.

# list.copy()
# Return a shallow copy of the list. Equivalent to a[:].

# Building a list from scratch

# we can create an empty list and then add elements using the append method
# the list stays in order and new elements are added at the end of hte list

stuff = list()  # create an empty list    <----
print(stuff)
stuff.append('book')
stuff.append(99)
print(stuff)

stuff.append('cookie')
print(stuff)

print('Examples')
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
# 2
print(fruits.count('tangerine'))
# 0
print(fruits.index('banana'))
# 3
print(fruits.index('banana', 4))  # Find next banana starting a position 4
# 6
fruits.reverse()
print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
print(fruits)
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
print(fruits.pop())
# 'pear'
print(fruits)

# Is something in a List?

# We have a in operator that let you check if an item is in a list
# these are logical operators that return True or False

# They do not modify the list   <--------

some = [1,9,21,10,16]

# 9 in some         -> will be True
print(9 in some)

# 15 in some        -> will be False
print(15 in some)

# 20 not in some    -> will be True
print(20 not in some)

# lIsts are in Order

# a list can hold many items and keeps those items in the order until we do something to change the order

# a list can be sorted (i.e.  change its order)

# the sort methos (unlike in strings) means "sort yuorself"

friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)      # will print ['Glenn', 'Joseph', 'Sally']
print(friends[1])


# Built-in functions and Lists

nums= [3, 41, 12, 9,74,15]
print(len(nums))    # prints the lenght of the LIst
# 6
print(max(nums))    # prints the largest value in the List
# 74
print(min(nums))    # prints the lowest value in the List
# 3
print(sum(nums))    # prints the sum of the values in the List
# 154
print(sum(nums)/len(nums))  # can calculate average
# 25.6

# Different ways to create loops / the folowing pieces of code will do the same thing 

# first ways 
total = 0
count = 0

while True:
    inp = input('Enter a number:')
    if inp == 'done': break
    value = float(inp)

    total = total + value
    count = count + 1

average = total / count

print('Average:', average)

# second way  -- THIS use more memory cause they values have to be stored simultaneously
numlist = list()        # creates an empty list

while True:
    inp = input('Enter a number:')
    if inp == 'done': break
    value = float(inp)

    numlist.append(value)           # add the value at hte end of the list

average = sum(numlist)/len(numlist) # calculate the average with sum() and len()

print('Average:', average)

# one difference is the amount of memory used. The first method use less memory because it calculates the 
# values each time , while the second method stores all the values in memory and than do the calculation 


# How Strings and Lists are related 
# 

# Best Friends: Strings and Lists

# split() breaks a string into parts and produces a list of strings. We think of these as words. 
# We can access a particular word or loop through all the words.
# split look at the spaces and breaks the strings into smaller strings , and stores them in a List

abc = 'With three words'
stuff = abc.split()
print(stuff)    # will print ['With', 'three', 'words']

print(len(stuff))   # will print 3

print(stuff[0])     # will print With 

# split() is a quick way to go from a line to words
# and you can loop though them
print(stuff)

for w in stuff:
    print(w)



# Exercize 8.4

# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# # print(lst)
# for line in fh:
#     # print(line)
#     words = line.split()
#     for word in words:
#         if word in lst: continue
#         lst.append(word)
#     # print(words)
    
#     # lst.append(word)
# lst.sort()
# print(lst)


