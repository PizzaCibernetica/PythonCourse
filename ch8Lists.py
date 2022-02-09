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

# Is somthing in a List?




# Exercize 8.4

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
# print(lst)
for line in fh:
    # print(line)
    words = line.split()
    for word in words:
        if word in lst: continue
        lst.append(word)
    # print(words)
    
    # lst.append(word)
lst.sort()
print(lst)


