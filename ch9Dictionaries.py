# DICTIONARIES
from pickle import LIST


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


