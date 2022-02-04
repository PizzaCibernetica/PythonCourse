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


for i in [5,4,3,2,1] :
    print(i)
print("Blastoff!")