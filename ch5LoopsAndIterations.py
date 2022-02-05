# Repeated Steps

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
 
zork = 0
print("Before", zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + 1
    print(zork, thing)
print("After", zork)

