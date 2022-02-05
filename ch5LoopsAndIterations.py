# Repeated Steps

from ast import IsNot
from multiprocessing.sharedctypes import Value
from operator import is_not
from turtle import done


n = 5 # n is our iteration variable
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff!')
print(n)

# Infinite loop is a loop that doesn't exit

# example

n = 5
while n > 0 :
    print("Lather")
    print("Rinse")
    break # needed to exit 
print("Dry off!")

# the following loop doesn't iterate at all

# zero trip loop

n = 0
while n > 0 :
    print("Lather")
    print("Rinse")
    break # needed to exit 
print("Dry off!")

# BREAKING OUT OF A LOOP
# 
# The break statement ends the current loop and jumps to the statement 
# immediately following the loop
# 
# it it like a loop test can happen anywhere in the body of the loop
# 

print("-- break --")
while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("Done!")

# BREAK means -> get out of this loop

# CONTINUE means -> stop this iteration/ we are done with this iteration

# Finishing an Iteration with continue 

# The continue statetment ends the current iteration and jumps to the top loop and starts the next iteration

print("-- Continue --")
while True:
    line = input("> ")
    if line[0] == "#" : # doesn't print comments
        continue
    if line == "done" :
        break
    print(line)
print("Done!")

# While loops are called "indefinite loops" because the keep 
# going until a logical condition becomes False 

# The loops we have seen so far are pretty easy to examine to see if 
# they will terminate or if they will be "infinite loops"

# Sometimes it is a little harder to be sure if a loop will terminate 
# -----------------------------------------------------------------
# Definite Loops

# Quite often we have a list of items of the lines in a file - 
# effectively a finite set of things

# We can write a loop to run once for each of the items in a set ising the python for construct

# These loops are called "definite loops" because they execute an exact number of times

# We say that "definite loops iterate through the members of a set"


# a simple definite loop
for i in [5,4,3,2,1] :
    print(i)
print("Blastoff!")

# a definite loop with Strings

friends = ["Mario", "Giovanna", "Diego"]
for friend in friends:
    print("Happy New Year to ", friend)
print("Done!d")

# ----------------------------------------------
# LOOP IDIOMS

# patterns on how we construct loops

# MAKING SMARTS LOOPS
# The trick is "knowing" something about the whole loop when you are stuck 
# writing code that only sees one entry at the time

# looping though a Set

print("---- LOOP IDIOMS ---")

print("Before")
for thing in [9,41,12,3,74,15]:
    print(thing)
print("After")


# use loops to find the largest value
# set a variable to -1 and compare the variable to the other number 
# replacing the value if hte number is greater 

largest_so_far = -1   #initilize variable to lowest number
print("Before", largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, "-  -",the_num)

print("After", largest_so_far)


# Counting in a loop
print("-- COUNTING IN A LOOP --")

# To count how many times we execute a loop, we introduce a counter variable 
# that starts at 0 and we add one to it each time through the loop.
 
zork = 0  # in general this variable is called count/counter
print("Before", zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + 1
    print(zork, thing)
print("After", zork)


# Summing in a loop
print("-- SUMMING IN A LOOP --")

# To add up a value we encounter in a loop, we introduce a sum variable that 
# starts at 0 and we add the value to the sum each time through the loop. 
 
zork = 0  # better variable name would be sum or total
print("Before", zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + thing
    print(zork, thing)
print("After", zork)


# Finding the Average in a loop
print("-- AVERAGE --")

# An average just combine the counting and sum patterns and divides when the loop is done

count = 0 
sum = 0 
print("Before, count is ", count , " and sum is ", sum)
for value in [9,41,12,3,74,15]:
    count = count + 1 
    sum = sum + value
    print(count, sum, value)
print("After the count is ", count, " and the sum is ", sum, " and the average is ", sum/count)

# filtering in a loop
print("--  FILTERING IN A LOOP  --")

# we use an if statement in the loop to catch / filter the values we are looking for.

print("Before")
for value in [9,41,12,3,74,15]:
    if value > 20:
        print("Large number is ", value)
print("After")

# Serching using a boolean variable 
# to search is a particular value is there

print("-- SEARCH using Boolean Variable --")

# if we just want to search and know if a value was found, we use a variable that starts
# at False and is set to True as soon as we find what we are looking for.

found = False
print("Before: the value of 'found' is ", found)
for value in [9,41,12,3,74,15]:
    if value == 3 :
        found = True
        # we can add a break to exit and make this loop more efficient
    print("found is:", found , "and the value is:", value)
print("After the value of found is :", found)

# smallest number

print("-- SMALLEST NUMBER --")

smallest = None   #initilize variable to None, because we cannot know the biggest number (None has only one value = none)
print("Before", smallest)
for value in [9,41,12,3,74,15]:
    if smallest is None:    # 'is' is stronger than == 
        smallest = value    # storing the first value of hte list in the varialble 
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)


# the "is" and "is not" operators are very useful in python
# pyhton has an "is" operator that can be used in logical expressions 
# implies "is the same as"
# Similar to, but stronger than ==
# "is not" also is a logical operator 

print("-- Example of 'is' amd 'is not' --")


if 0 == 0.0:
    print("Yes == ")    # this will print, because 0 and 0.0 are equal in value  
if 0 is 0.0:
    print("Yes 'is' ")  # this will not print, because 0 and 0.0 are not the same 'type' 
print(type(0))
print(type(0.0))
if 0 != 0.0:
    print("No !=")      # this will not print 
if 0 is not 0.0:
    print("No - Is Not")# this will print
