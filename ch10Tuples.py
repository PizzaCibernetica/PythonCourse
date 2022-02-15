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

(0, 1, 2) < (5, 1, 2)
True

