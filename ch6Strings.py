# This chapter will talk about strings

from turtle import width


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

# Slicing strings

# We can also look at any continous section of any string using a colon separator
# The second number is one beyond the end of the slice - "up to but not including"
# If the second number is behiond the end of the string, it stop at the end (no traceback)

# s[0:4](es sub zero to 4)

str = 'Monty Python'
print(str[0:4])     # print Mont
print(str[6:7])     # print P
print(str[6:20])    # print Python


# If we leave off the first number or hte last number of the slice, it is assumed to be the beginning or end of hte string respectively

print(str[3:])      # print ty Python
print(str[:2])      # print Mo      from begining to 2 not included
print(str[8:])      # print thon    from 8 to end 
print(str[:])       # print the whole string Monty Python

# String concatenation 

# When the + operator is applied to string, it means concatenate

a = 'Hello'
b = a + 'There'
print(b)    # will print HelloThere

c = a + ' ' + 'There'
print(c)    # will print Hello There

# Using in as a logical Operator
# The in keyword can also be used to check to see if one string is "in" another string
# The in expression is a logical expression that 
# returns True or False and can be used in an if statement

fruit = 'banana'
'n' in fruit    # True
'm' in fruit    # False
'nan' in fruit  # True
if 'a' in fruit :
    print('Found it!')  # this will print

# you can compare strings but it is a lexographycal comparison


# STRING LIBRARY

# Python has a number of functions which are in the string library

# These functions are already built into every string - 
# - we invoke them by appending the function to the string variable

# These fucntions do not modify the original string, 
# instead they return a new string that has been altered

greet = 'Hello Bob'
zap = greet.lower()
print(zap)                  # will print hello bob
print(greet)                # will print Hello Bob
print('Hei There'.lower())  # will print hei there


# https://docs.python.org/3/library/stdtypes.html#string-methods  dir(stuff)

stuff = 'Hello World'

print(type(stuff))

dir(stuff)


# the following are very useful string library methods

# str.capitalize()
# str.center(width[, fillchar])
# str.endswith()
# str.find()
# str.lstrip([chars])
# str.replace(old, new[, count])
# str.lower()
# str.rstrip([char])
# str.strip()
# str.upper()


# Searching a string
# FIND
# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found within the slice s[start:end]. 
# Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
# We use the find() function to search for a substring within another string
# find() finds the first occurrence of the substring
# if the substring is not found, find() return -1
# Remember that the string position starts at zero

#  Making everything upper case 

# .upper() 
# .lower()

greet = 'Hello Bob'
nstr = greet.upper()
print(nstr)   

greet = 'Hello Bob'
nstr = greet.lower()
print(nstr) 


# Search and Replace 
# THIS IS SUPER USEFUL
# The replace() function is like a "search and replace" operation in a word processor
# It replaces all occurrences of the search string with the replacement string
 
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)         # will print Hello Jane  --- and greet string is unchanged

nstr = greet.replace('o','X')
print(nstr)         # will print HellX BXb

# Strips is also very useful
# sometimes we want to take a string and remove whitespaces at the beginning and/or end

# lstrip() remove at left
# rstrip() revove at right
# strip() remove both beginning and ending whitespaces

# Prefixes
line = 'Please have a nice day'
line.startswith('Please')   # this is a question it will return a T/F
# True
line.startswith('p')
# False


# Exercise 6.5


# my solution
text = "X-DSPAM-Confidence:    0.8475"
print(text)
text = text.lower()
print(text)
marker = text.find("0.8475")
print(marker)
newtext = text[23:29]
print(newtext)
output = float(newtext)
print(output)


# Professor solution
str = "X-DSPAM-Confidence:    0.8475"
marker = str.find(':')
piece = str[marker+2:]
value = float(piece)
print(value)
