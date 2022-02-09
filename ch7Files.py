# Files chapter from Python for Everybody

from operator import index
from tkinter import N


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

#fhand = open('stuff.txt') # if the file is missing the code will blows-up and throw a traceback
#print(fhand)

# The newline character

# We use a special character called the "newline" to indicate when a line ends
# We represent it as \n in strings
# Newline is still one character - not two

stuff = "Hello\nWorld!"
print(stuff)        # print() also put a newline character at hte end by default

stuff = "X\nY"
print(stuff)

print(len(stuff))

# File Processing
print("-- File Processing --")

# a text file can be thought of a sequence of lines
# at the end of each line there is a character that we dont see (the \n newline )


# How to read files in Python
print("-- How to read files ni Python --")

# File handle as a sequence 
# A file handle open for read can be treated as a sequence of strings where each line 
# in the file is a string in a  sequence

# We can use the for statement to iterate through a sequence
# Remember - a sequence is an ordered set

xfile = open('mbox.txt')    # the file handle is named xfile 
for cheese in xfile:        # for each line in the file handle xline
    print(cheese)           # print each line

# Thing the we can do

# counting the lines in a file
# open a file read-only
# use a for loop to read each line
# count the lines and print out the number of lines

fhand = open("mbox.txt")
count = 0
for line in fhand:
    count = count + 1
print("Line count:", count)

# Reading the whole file 
# it is also possible to read the file as a series of characters, all in one go
# this approach can create a problem if the file is very big, cause this will lead to a variable
# depending on the size of the file, woth a very large amount of data
# 100K of characheter is good , 10 millions of line can lead to issues

fhand = open('mbox.txt')
inp = fhand.read()  # read method
print(len(inp))     # print the lenght of the file
print(inp[:20])

# Searching Through a File

# We can put an if statement in our for loop to only print lines that meet some criteria

fhand = open('mbox-short.txt')      # create the handle
for line in fhand:                  # go through each line of the file
    if line.startswith('From'):     # check if they statr with FROM
        print(line)                 # print the one that strat with From

# # we will get 
# From: abc@mail.com\n
# \n
# From: def@mail.it\n


# what we get is a list of email addresses separated by an empty line 

# each kine from the file has a newline at the end
# the print statement adds a newline to each line

# we can strip the whitespace from the right-hand side of the string using rstrip() from the string library
# the newline is considered "white space" and is stripped
# this is the corret way to do it 
print("Correct way to search through a file")

fhand =open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()        # this will strip the newline(invisible) character
    if line.startswith("From"):
        print(line)


# Skipping with continue
# this is a better version, because we can conveniently skip 

fhand = open("myfile.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    print(line)


    # Using in to select lines
# we can look for a string anywhere in a line as our selection criteria

fhand = open("mytextfile.txt")
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

# some time programs what to prompt to a file name
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1 
print('There were', count, 'subject lines in', fname)

# if the user type in bad file names 
# use a try except 

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()  # useful to stop executing because you detected some kind of error

count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1 
print('There were', count, 'subject lines in', fname)


 #fhand = open("testfile.txt", "x")  # x to create a file 
#fhand.close()

# fhand = open("testfile.txt", "a")
# fhand.write("This is the first line")
# fhand.close()

# f = open("testfile.txt","r")
# print(f.read())


# Exercize 7.2 

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
total = 0
try:
    fh = open(fname)
except:
    print("Wrong name")
    quit()

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    marker = line.find(":")
    piece = line[marker+2:]
    value = float(piece)    
    count = count + 1
    total = total + value

print("Average spam confidence:", total/count)
