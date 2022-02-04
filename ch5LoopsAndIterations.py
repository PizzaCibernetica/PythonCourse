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

print("Hello line 40")
while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("Done!")