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

