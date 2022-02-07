# This chapter will talk about strings

print("-- Chapter 7 Strings --")

# Strings Data Type 
# a string is a sequence of characters
# a stringgs literal uses quotes 'Hello' or "Hello"
# For strings, + means "concatenate"
# When a string contains numbers, it is still a string
# We can convert numbers in a string into a number using int() method

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

str3 = '123'
# str3 = str3 + 1      # this will create a traceback error

x = int(str3) + 1
print(x)   # now it will print

# WE prefer to read data in using strings and then parse and convert the data as we need
# This give us more control over error situations and/or bad user input
# Raw imput numbers must be converted from strings

name = input("Enter:")  # we enter a name like Matt
print(name)             # this will print the name you enter


apple = input('Enter:') # we input a number 100
# x = apple - 10          # this willl throw a traceback
# correct way
x = int(apple) - 10
print(x)

# Looking inside Strings
# we can get at any character in a string using an index specified in square brackets
# the index value must be an integer and start with zero
# the index value can be an expression that is computed

# B A N A N A
# 0 1 2 3 4 5

fruit = 'banana'
letter = fruit[1]
print(letter)   # this will print a

x = 3
w = fruit[x -1] # index position 2
print(w)        # this will print n

#  a character too far
# you will get a python error if you attempt to index beyond the end of a string 
# so be careful when constructing index values and slices

zot = 'abc'
# print(zot[5])   # this will throw a traceback - index out of bound 
# to fix this we can use the lenght function, which is built in Python

# the len() function gives the lenght of a string 

fruit = 'banana'
print(len(fruit))   # this will print 6

# LEN is some stored code that we use. A funcion takes some input and produces an output

# LOOPING THROUGH STRINGS
# Using a while statement and an iteration variable, and the len() function, we can construct 
# a loop to look at each of the letters in a string individually

# the following example is a indefinite loop
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1   # unless you need to absolutely need to know the index number use a for loop

# we generally prefer a definite loop
fruit = 'banana'
for letter in fruit:
    print(letter)

# a definite loop suing a for statement is much more elegant 
# the iteration variable is completely taken care of by the for loop


# Looping and counting

# this is a simple loop that loops through aeach letter in a string and counts 
# the number of times the loop encounters the 'a' character

word = 'banana'
count = 0
for letter in word:         # iteration variable = letter
    if letter == 'a' :
        count = count + 1
print('I counted a, and the total is' ,count)

# the iteration variable "iterates" through the string and the block(or body)
# of code is executed once for each value in the sequence

# ADDITIONAL THINGS THAT WE CAN DO WITH A STRING

