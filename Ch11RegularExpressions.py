# --- REGULAR EXPRESSIONS ---

print('---  Regular Expressions  ---')

# In computing, a regular expression, also referred to as "regex" or 
# "regexp", provides a concise and flexible means for matching strings
#  of text, such as particular characters, words, or patterns of characters. 
# A regular expression is written in a formal language that can be 
# interpreted by a regular expression processor.

# Really clever "wild card" expressions for matching and parsing strings.

# UNDERSTANDING REGULAR EXPRESSIONS
# very powerful and quite cryptic
# fun once you understand them
# Regular expressions are a language unto themselves
# A lannguage of "marker characters" - programming with characters
# It is kind of an "old school" language - compact

# Find and Search

# Python Regular Expression Quick Guide

# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one or more times (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end

# THE REGULAR EXPRESSION MOFULE

# Before you can use regular expressions in your program, you must import the library using “import re”

import re
from xml.dom.minidom import CharacterData

# You can use re.search() to see if a string matches a regular expression, 
# similar to using the find() method for strings
# You can use re.findall() to extract portions of a string that match your regular expression, 
# similar to a combination of find() and slicing:  var[5:10] 

# Using re.search() Like find()

print('--- Using find() ---')

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)
# find() will return -1 if not found

print('--- Using search ---')


hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line) :
        print(line)


# Using re.search() Like startswith()
print('--- Using re.search() Like startswith() ---')

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)


# We fine-tune what is matched by adding special characters to the string


hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) :  # ==> we have to add the carat ^ , which means fro mthe begining of the line
        print(line)

# by adding the carat it will check the beginning of a line and will disregard any From found in the middle/end 


# Wild-Card Characters
print('--- Wild-Card Characters ---')

# The dot character matches any character
# If you add the asterisk character, the character is “any number of times”

# X-Sieve: CMU Sieve 2.3
# X-DSPAM-Result: Innocent
# X-DSPAM-Confidence: 0.8475
# X-Content-Type-Message-Body: text/plain
# ^



# ^X.*:
# ^ = match the start of a line
# . = match any character
# * = many times
# explanation:
# match any line that "start with" an "X", followed by "many characters", and end with a ":"


#Fine-Tuning Your Match
print('--- Fine-Tuning Your Match ---')

# Depending on how “clean” your data is and the purpose of your application,
#  you may want to narrow your match down a bit


# X-Sieve: CMU Sieve 2.3                    <== match
# X-DSPAM-Result: Innocent                  <== match
# X-Plane is behind schedule: two weeks     <== match
# X-: Very short                            <== NO match


# ^X.*:   ==>   ^X-\S+:

# ^     Matches the beginning of a line
# X-    charachter to match
# \S    Matches any non-whitespace character
# +     Repeats a character one or more times

# explanation
# match any line that "start with" a "X-",
#  any character "other than white space" "one or more time" (one or more times non white space characters) 
#  end with ":"  

# X-Sieve: CMU Sieve 2.3                    <== match
# X-DSPAM-Result: Innocent                  <== match
# X-Plane is behind schedule: two weeks     <== NO match becuase of white spaces


# Matching and Extracting Data
print('--- Matching and Extracting Data ---')

# re.search() returns a True/False depending on whether the string matches  the regular expression
# If we actually want the matching strings to be extracted, we use re.findall()


# [0-9]+   
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
# ['2', '19', '42']
