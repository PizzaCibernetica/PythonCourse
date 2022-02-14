# DICTIONARIES

from itertools import count


print('---  DICTIONARIES   ---')

# What is a Collection?

# A collection is nice because we can put more than one value in it and carry them all around in one convenient package

# We have a bunch of values in a single "variable"

# We do this by having more than one place "in" the variable

# We have ways of finding the differnt places in the variable


# What is not a collection?

# most of our variables have one value in them - when we put a new value in the variable - the old value is overwritten

#   $ pyhton
#   >>> x = 2  
#   >>> x = 4
#   print(x)
#   4               # the value is overwritten

# comparing LISTS and DICTIONARIES

 # List
 # is organized. It is a linear collection of values that stay in order

 # Dictionary
 # are messier, there is no real sense of order in Dictionaries. It is like a "bag" of values, each with its own label



 # Dictionaries 
 # Dictionaries are Pyhton's most powerful collection
 # Dictionaries allow us to do fast database-like operation in Python
 # Dictionaries have different names in different languages
 #      - Associative Arrays            : Perl/PHP
 #      - Properties or Map or HashMap  : Java 
 #      - Property Bag                  : C# / .NET
 #

 # Dictionaries

 # lists index their entries based on the position in the list
 # Dictionaries are like bags - no order
 # # So we index the things we put in the dictionary with a "lookup tag"
 # 

# python
# >>> purse = dict()
# >>> purse['money'] = 12
# >>> purse['candy'] = 3
# >>> purse['tissue'] = 75
# >>> print(purse)
# {'money': 12, 'tissue': 75, 'candy': 3}
# >>> print(purse['candy'])
# 3
# >>> purse['candy'] = purse['candy'] + 2
# >>> print(purse)
# {'money': 12, 'tissue': 75, 'candy': 5}
# >>> exit()

# Comparing Lists and Dictionaries

# Dictionaries are like lists except that they use keys instead of numbers to look up values
# both can have new items added to them
# 

# LIST                  VS      DICTIONARY

# >>> lst = list()              >>> ddd = dict()
# >>> lst.append(21)            >>> ddd['age'] = 21
# >>> lst.append(183)           >>> ddd['course']=182
# >>> print(lst)                >>> print(ddd)
# [21, 183]                     {'course': 182, 'age': 21}
# >>> lst[0] = 23               >>> ddd['age']=23
# >>> print(lst)                >>> print(ddd)
# [23, 183]                     {'course': 182, 'age': 23}


# Key   Value                   Key         Value
# [0]   21                      ['course']  182  
# [1]   183                     ['age']     21

# the values are the same but the key is different



# Dictionary Literals (Constants)

# Dictionary literals use curly braces and have a list of key:value pairs

# you can make an empty dictionary using empty curly braces

jjj = {'chuck' : 1 , 'fred' : 42 , 'jan' : 100 }
print(jjj)

ooo = {}    # empty dictionary - common constructor
print(ooo)


# Video 2
# common application of dictionary => counting frequency of things
# Most Common Name? 

# Many counters with dictionary
# the common idea of using dictionary is to use them to keep count of items

# one common use of dictionaries is counting how often we "see" something

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)      # will print {'csev': 1, 'cwen': 1}


ccc['cwen'] = ccc['cwen'] + 1   # the idea is to use it to keep count
print(ccc)      # will print {'csev': 1, 'cwen': 2}


# Dictionary Trsceback
# one thing you cannot do , and it is frustrating, you cannot look up something that is not there 
# it is an error to reference a key which is not in the dictionary

# ccc=dict()
# print(ccc['csev']) # this will trow a traceback

# we can use the in operator to see if a key is in the dictionary

# 'csev' in ccc
# False

# When we encounter a new name, we need to add a new entry in the dictionary and if this the second 
# or later time we have seen the name , we simply add one to the count in the dictionary under that name

counts = dict()
names =['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts) # this will output the data for the istagram


# the idea of checking if a name is in a dictionary is so common that there is a method for it 
# The GET method for dictionary
# The pattern of checking to see if a key is already in a dictionary and assuming a default value
#  is the key is not there is so common that there is a method calle get() that does this for us

# if name in counts:
#     x = counts[names]
# else:
#     x = 0

# this methods is built in python

x = counts.get(name,0) 

# Simplified counting with get()
# ---- YOU WILL USE THIS A LOT ---
# we can use get() and provide a default value of zero when the key is not yet in the dictionary - and then just add one

counts = dict()
names =['csev', 'cwen', 'csev', 'zqian', 'cwen', 'matt']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

# Video 3


# counting words in text
# the general pattern to count the words in a line of text is to split the line into words,
#  then loop through the words and use a dictionary  to track the count of each word independently

counts = dict()                     # start with empty dictionary

print('Enter a line of text:')      # ask for a line of text 
line = input('')                    # read the line in

words = line.split()                # use split to get a list of words

print('Words:', words)              # print it out 

print('Counting:')                  # counting the words
for word in words:
    counts[word] = counts.get(word,0) + 1

print('Counts', counts)


# define Loops and Dictionaries

# ways to loop thrugh a dictionary
# Even though dictionaries are not stored in order, we can write a for loop that goes through all the entries in a dictionary - 
# actually it goes through all of the keys in the dictionary and looks up the values 

counts = {'chuck': 1 , 'fred': 42 , 'jan':100}
for key in counts:
    print(key, counts[key]) 

# Retrieving lists of Keys and values
# there are a couple of methods that allow us to retrieve the keys
# you can get a list of keys, values, or items(both) from a dictionary

jjj = {'chuck': 1 , 'fred': 42 , 'jan':100}
print(list(jjj))    # turn this into a list

print(jjj.keys())      # get the keys 

print(jjj.values())     # get the values

print(jjj.items())      # get the item (list of key/vslue pairs)


# Bonus: two Iteration Variables!

# we loop through the key-value pairs in a dictionary using two iteration variables

# each iteration, the first variable is the key and the second variable is the corresponding  value for the key

jjj = {'chuck': 1 , 'fred': 42 , 'jan':100}
for aaa,bbb in jjj.items():                 # this is a python implementation not seen in other languages
    print(aaa,bbb)                          # you need to use items() for the two iteration variables



# how to find the most common word
name = input('Enter file name:')    # ask for a file name
handle = open(name)                 # create a handle to store the file data

counts = dict()                     # create a empty dictionary
for line in handle:                 # iteration variable that is going through the lines of the file
    words = line.spit()             # split that line into words - words is the list of words in one line
    for word in words:              # iterate through every word in the line
        counts[word] = counts.get(word, 0) + 1      # make a histogram to count the occurence of each word 

bigcount = None                         # instantiate a variable for the biggest count with value None  
bigword = None                          # instantiate a variable for the g=biggest word with vaue of None
for word,count in counts.items():       # for word and count going throug the key-value pairs 
    if bigcount is None or count > bigcount:    # if the bigcount is none jump in the loop OR if the count is bigger than the bigcount
        bigword = word                  # set the word in bigword
        bigcount = count                # set the count in bigcount

print(bigword, bigcount)


# Exercize 9.4

# Open the file and create a handle 
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# create a dictionary
counts = dict()

# loop through the  file and store values in the 
for line in handle:
    if line.startswith('From:'):
        words = line.split()    # slit the line into words - result is a From: and email@ddre.ss
        
        counts[words[1]] = counts.get(words[1], 0) + 1
        

bigcount = None                         # instantiate a variable for the biggest count with value None  
bigemail = None                          # instantiate a variable to keep track of the email with most count 
for word,count in counts.items():       # for word and count going throug the key-value pairs 
    if bigcount is None or count > bigcount:    # if the bigcount is none jump in the loop OR if the count is bigger than the bigcount
        bigemail = word                  # set the word in bigword
        bigcount = count                # set the count in bigcount

print(bigemail, bigcount)