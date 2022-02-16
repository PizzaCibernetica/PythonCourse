# Tuples


from operator import truediv


print('---   T U P L E S   ---')

# Tuples are another kind of sequence that function much like a list -
#  they have elements which are indexed stating at 0

x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

y = (1 , 9 , 2)
print(y)

print(max(y))

for iter in y:
    print(iter)

# Tuples are immutable
# Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string

# a list is mutable
x = [9, 8, 7]
x[2] = 6
print(x)

# a string is immutable
y = 'ABC'
# y[2] = 'D'  => this will throw a traceback
# Traceback (most recent call last):
#   File "/Users/Security/Documents/GitHub/PythonCourse/PythonCourse/ch10Tuples.py", line 28, in <module>
#     y[2] = 'D'
# TypeError: 'str' object does not support item assignment

z = (5, 4, 3)
# z[2] = 0  => this will throw a traceback
# Traceback (most recent call last):
#   File "/Users/Security/Documents/GitHub/PythonCourse/PythonCourse/ch10Tuples.py", line 35, in <module>
#     z[2] = 0
# TypeError: 'tuple' object does not support item assignment

# the reson they are not modifiable is for efficiency - they take less storage, faster to access, etc

# things NOT to do with tuples

x = (3, 2, 1)
# cannot do sort()
# x.sort()     
# Traceback (most recent call last):
#   File "/Users/Security/Documents/GitHub/PythonCourse/PythonCourse/ch10Tuples.py", line 46, in <module>
#     x.sort()
# AttributeError: 'tuple' object has no attribute 'sort'

#cannot do append()
# x.append(5)
# Traceback (most recent call last):
#   File "/Users/Security/Documents/GitHub/PythonCourse/PythonCourse/ch10Tuples.py", line 56, in <module>
#     x.append(5)
# AttributeError: 'tuple' object has no attribute 'append'

# Cannot do reverse()
# x.reverse()
# Traceback (most recent call last):
#   File "/Users/Security/Documents/GitHub/PythonCourse/PythonCourse/ch10Tuples.py", line 63, in <module>
#     x.reverse()
# AttributeError: 'tuple' object has no attribute 'reverse'

# If all you want to do is STORE a list and JUST LOOK at it => probably use a Tuple, cause it's more efficient 

t = tuple()
# dir(t)
# available meyhtods for tuple
# 'count', 'index'

l = list()
# dir(l)
# available methods for List
# 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'


# WHY DO WE LIKE THEM? 
# Tuple are more efficient
# Since python does not have to built tuple structures to be modifiable , 
# they are simpler and more efficient in terms of memory use and performance than lists

# So in our program when we are making "temporary variables" we prefer tuples over lists

# Tuples and Assigment

# we can also put a tuple on the left-hand side of an assignment statement
# we can even omit the parameter 

(x, y) = (4, 'fred')
print(y)            # fred

(a,b) = (99, 98)    # 99
print(a)

# Tuples and Dictionaries

# the item() method in dictionaries returns a list of (key, value) tuples

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)
# will print
# csev 2
# cwen 4

tups = d.items()
print(tups)
# will print
#dict_items([('csev', 2), ('cwen', 4)])

# Tuples are comparable

# the comparison operator work with tuples and other sequences. 
# If the first item is equal, python goes on to the next element, and so on, until it finds elemnts that differ.

if (0, 1, 2) < (5, 1, 2):       # will check the first, don't check the rest
    print('True')

if (0, 1, 200000) < (0, 3 , 2): # will check the first (even), check the second, don't check the rest 
    print('True')


if ('Jones', 'Sally') < ('Jones', 'Sam'): 
    print('True')


if ('Jones', 'Sally') > ('Adam', 'Sam'): # Just evaluate  the first letters
    print('True')


# Sorting Lists of Tuples

# we can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary

# first we sort the dictionary by the key using the items() method and sorted() function

d = {'a':10, 'c':22 , 'b':1}

print(d.items())   # dict_items([('a', 10), ('c', 22), ('b', 1)])

print(sorted(d.items()))    #[('a', 10), ('b', 1), ('c', 22)]  will sort only the keys

# using sorted()

# we can do this even more directly using the built-in function
#  sorted() that takes a sequence as a parameter and returns a sorted sequence

for k,v in sorted(d.items()):
    print(k,v)

# sort by values instead of key

# if we could construct a list of tuples of the form (value, key) we could sort by value
# we do this with a for loop that creates a list of tuples

c = {'a':10, 'b':1, 'c':22}

tmp = list()

for k,v in c.items():
    tmp.append( (v,k) ) # reverse order

print('tmp =',tmp)

tmp = sorted(tmp, reverse=True)

print(tmp)


# even a shorter version

c = {'a':10, 'b':1, 'c':22}

print( sorted( [ (v,k) in c.items() ] ) )

# https://wiki.python.org/moin/HowTo/Sorting/

# Print the most common words in a file 

fhand = open('romeo.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[words] = counts.get(word, 0) + 1 # idiom to make histogram
# ------------------ we have the histogram now ---------------------
lst = list()
for key,val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
# ------------------ now we have a list of tuples, value/key order
lst = sorted(lst, reverse=True)
# -------------- now we have a sorted  list -------------------------
for val, key in lst[:10]:   # pick only the first 10 entry of the list (which are the most common)
    print(key,val)          # print it in order by key ,value


# even a shorter version

c = {'a':10, 'b':1, 'c':22}

print( sorted( [ (v,k) in c.items() ] ) )

# list comprehension creates a dynamic list. In this case, we make a list of reversed tuples and then sort it.

# https://wiki.python.org/moin/HowTo/Sorting/


# Exercize 10.2
#  
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hours = dict()
for line in handle:
    line = line.strip()

    if line.startswith("From "):
        words = line.split()
        hour = words[5].split(':')[0]
        hours[hour] = hours.get(hour,0)+1

lst = list()
for key,val in hours.items():
    newtup = (val, key)
    lst.append(newtup)
# ------------------ now we have a list of tuples, value/key order
lst = sorted(lst, reverse=False)
# -------------- now we have a sorted  list -------------------------
for key, val in lst:   
    print(val,key)          # print it in order by  value, key




    