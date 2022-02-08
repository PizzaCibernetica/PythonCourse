# Files chapter from Python for Everybody

print("Chapter 8 -- Files")

# We are going to mainly use text files - which can be thpought as a sequence of lines

# Opening a file 

print('Opening a file')

# Before we can read the content of a file, we must tell Python which file we are going to work with
# and what we will be doing with thw file

# This is done with the open() function

# open() returns a "file handle" - a variable used to perform operation on a file

# Similar to "File -> Opne" in word processor


#   USING OPEN

# handle = open(filename, mode)    fhand = open('mbox.txt', 'r')  r for read w to write
# returns a handle use to manipulate the file 
# filename is a string
# mode is optional and should be 'r' is we are planning to read the file and 
# 'w' if we are going to write the file

# What is a handle 
# a handle is a wrapper that interact between the program and the actual file

fhand = open('stuff.txt') # if the file is missing the code will blow and throw a traceback
print(fhand)

#fhand = open("testfile.txt", "x")  # x to create a file 
#fhand.close()

# fhand = open("testfile.txt", "a")
# fhand.write("This is the first line")
# fhand.close()

# f = open("testfile.txt","r")
# print(f.read())




score = input("Enter Score: ")
fs = float(score)

if fs > 1.0:
    print("Out of range... above")
    exit()
elif fs < 0:
    print("Oot of range... below")
    exit()
else:
    if fs >= 0.9:
        print("A") 
    elif fs >= 0.8:
        print("B")
    elif fs >= 0.7:
        print("C")
    elif fs >= 0.6:
        print("D")
    else:
        print("F")


# file read

#fileHandle = open('filename.txt')
#for line in fileHandle:
#    line = line.rstrip()
#    if not '@icloud.com' in line:
#        continue
#    print(line)
