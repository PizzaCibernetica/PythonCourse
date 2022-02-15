# Tuples
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