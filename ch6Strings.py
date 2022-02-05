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