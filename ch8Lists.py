# This is the chapter about lists

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

