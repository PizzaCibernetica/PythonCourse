# Network Programming
print('--- Network Programming ---')



# Sockets in Python
print('--- Sockets in Pythons ---')
# In computer networking, an Internet socket or a network socket, is an endpoint of a
#  bidirectional inter-process communication flow across an Internet Protocol-based computer network,
#  such as the Internet.
# A socket is a 'phone plug' that can connect to the network 
# when you use the socket word in python, it means use the socket function

# https://docs.python.org/3/library/socket.html


# python has built-in support for TCP Sockets
import socket
from timeit import repeat

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# we are going to make a socket that goes through the internet 'socket.AF_INET',
#  and it's going to be a steam (one character after another, rathen than a block) 'socket.AF_STREAM'
# this line creates a socket but doesn't associated

mysock.connect( ('data.pr4e.org', 80) )
# this socket object, now makes the connection across the internet to the 'address' and 'port number' 


# Application protocol
print('--- Application Protocol ---')

# Since TCP (and Python) gives us a reliable socket, what do we want to do with the socket?  What problem do we want to solve?
#   Application Protocols
#       -  Mail
#       -  World Wide Web


# HTTP - Hypertext Transfer Protocol
# The dominant Application Layer Protocol on the Internet
# Invented for the Web - to Retrieve HTML,  Images, Documents, etc.
# Extended to retrieve data in addition to documents - RSS, Web Services, etc.  
# Basic Concept - Make a Connection - Request a document - Retrieve the Document - Close the Connection

# The HyperText Transfer Protocol is the set of rules to allow browsers
#  to retrieve web documents from servers over the Internet

# What is a Protocol?
# A set of rules that all parties follow so we can predict each other’s behavior
# And not bump into each other
#   - On two-way roads in USA, drive on the right-hand side of the road
#   - On two-way roads in the UK, drive on the left-hand side of the road

# a URL (uniformed resource locator) has in them a
# protocol              host                    document
# http://       www.websiteaddress.com          /page1.html


# Getting Data From The Server

# Each time the user clicks on an anchor tag with an href= value to switch to a new page,
#  the browser makes a connection to the web server and issues a “GET” request -
#  to GET the content of the page at the specified URL

# The server returns the HTML document to the browser, which formats and displays the document to the user


# Internet Standards

# The standards for all of the Internet protocols (inner workings) are developed by an organization
#   - Internet Engineering Task Force (IETF)
#   - www.ietf.org
#   - Standards are called “RFCs” - “Request for Comments” (meaning they are always looking for imput to better the standard)

# RFC 2616 defines the HTTP protocol
# https://datatracker.ietf.org/doc/html/rfc2616

# Making an HTTP request

#   Connect to the server like www.dr-chuck.com"
#   Request a document (or the default document)
#       GET http://www.dr-chuck.com/page1.htm HTTP/1.0
#       GET http://www.mlive.com/ann-arbor/ HTTP/1.0

#       GET     http://www.facebook.com     HTTP/1.0
#    Method     -Resource identifier-       protocol version 
#          1 space                     1 space
#  it requires only one space between method, resurce id, and protocol


# telnet www.dr-chuck.com 80
# telnet is a protocol not in use anymore 
# but in practice , it opens a socket
# then we aill need a HTTP request
# GET http://www.dr-chuck.com/page1.htm HTTP/1.0
# (better to copy and paste because if we type that in the computer my close the connection)
# press return twice


# writing a web browser with python
print('--- writing a web browser with python ---')
# An HTTP Request in Python

# create a socket and connect
import socket           
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# create the request and send it                # two return lines
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


while True:
    data = mysock.recv(512) # RECEIVE the data 512 characters at the time
    if (len(data) < 1):
        break
    print(data.decode(),end='')
mysock.close()

# This will be the result printed
# first the HTTP header
#  
# HTTP/1.1 200 OK
# Date: Fri, 18 Feb 2022 19:08:42 GMT
# Server: Apache/2.4.18 (Ubuntu)
# Last-Modified: Sat, 13 May 2017 11:22:22 GMT
# ETag: "a7-54f6609245537"
# Accept-Ranges: bytes
# Content-Length: 167
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: text/plain

# followed by the HTTP body

# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief



# About Characters and Strings…
print('--- About Characters and Strings… ---')

# Representing Simple Strings

# Each character is represented by a number between 0 and 256 stored in 8 bits of memory 
# We refer to "8 bits of memory as a "byte" of memory – (i.e. my disk drive contains 3 Terabytes of memory)
# The ord() function tells us the numeric value of a simple ASCII character

# the ordinal representation of = ord()

print(ord('H'))
# will print 72
print(ord('e'))
# will print 101
print(ord('\n'))
# will print 10



# ASCII was uni-byte characters set, ok to use in the 60s
# not enough in the 70s and later years
# adoption of Unicode  
# https://unicode.org/charts/


# Multi-Byte Characters

# To represent the wide range of characters computers must handle we represent characters with more than one byte
#   UTF-16 – Fixed length - Two bytes       (compressed set - a subset of unicode)
#   UTF-32 – Fixed Length - Four Bytes      (too large - the whole set of unicode)
#   UTF-8 – 1-4 bytes:                      (best practice to be used - dynamic lenght)
#       -  Upwards compatible with ASCII ( ASCII is 1 byte)
#       -  Automatic detection between ASCII and UTF-8
#       -  UTF-8 is recommended practice for encoding data to be exchanged between systems

# Two Kinds of Strings in Python

# In Python 3, all strings are Unicode


# Python 3 and Unicode

# In Python 3, all strings internally are UNICODE 
# Working with string variables in Python programs and reading data from files usually "just works"
# When we talk to a network resource using sockets or talk to a database we have to encode and decode data (usually to UTF-8)

# Python 3.5.1
# >>> x = b'abc'
# >>> type(x)
# <class 'bytes'>
# >>> x = '이광춘'
# >>> type(x)
# <class 'str'>
# >>> x = u'이광춘'
# >>> type(x)
# <class 'str'>

# when connecting to the internet and using sockets we have to be aware that there might be other encoding

# Python Strings to Bytes

# When we talk to an external resource like a network socket we send bytes,
#  so we need to encode Python 3 strings into a given character encoding

# When we read data from an external resource, we must decode it based on the character set
#  so it is properly represented in Python 3 as a string

# while True:
#     data = mysock.recv(512)
#     if ( len(data) < 1 ) :
#         break
#     mystring = data.decode()
#     print(mystring)


# An HTTP Request in Python

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()    # <== encoding
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())                                            # <== decode
mysock.close()


# Making HTTP Easier With urllib
print('--- Using urllib in Python ---\n')

# Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file

# urllib is a library that combine the idea of:
# opening a connection,
#  sending the GET request,
#  sending the newline,
#  retrieving the stuff,
#  breaking the header stuff 


import urllib.request, urllib.parse, urllib.error       # we have to import the library

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# there is no header



# You can treat it like a File...

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()                     # make a dictionary 
for line in fhand:                  # loop through 
    words = line.decode().split()   # remember to decode

    # word by word create a dictionary
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)


#Reading Web Pages
print('-- Reading Web Pages --\n')

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())


# Parsing HTML (a.k.a. Web Scraping)
print('\n--- Parsing HTML (a.k.a. Web Scraping) ---\n')

# What is Web Scraping?
# When a program or script pretends to be a browser and retrieves web pages,
#  looks at those web pages, extracts information, and then looks at more web pages
# Search engines scrape web pages - we call this “spidering the web” or “web crawling”


# Why Scrape?

# Pull data - particularly social data - who links to who?
# Get your own data back out of some system that has no “export capability”
# Monitor a site for new information
# Spider the web to make a database for a search engine

# Scraping Web Pages

# There is some controversy about web page scraping and some sites are a bit snippy about it.
# Republishing copyrighted information is not allowed
# Violating terms of service is not allowed


# The Easy Way - Beautiful Soup

# You could do string searches the hard way
# Or use the free software library called BeautifulSoup from www.crummy.com


# BeautifulSoup Installation

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

print('\n--- BeautifulSoup ---\n')
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup                       # inport BeautifulSoup

url = input('Enter - ')                             # Enter the URL
html = urllib.request.urlopen(url).read()           # read the whole thing (we are not looping)
soup = BeautifulSoup(html, 'html.parser')           # will parse and give back a soup object

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))




















# Exercize 1 - request-response cycle
print('--- Exercize 1 ---\n')

# create a socket and connect
import socket           
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# create the request and send it                # two return lines
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


while True:
    data = mysock.recv(512) # RECEIVE the data 512 characters at the time
    if (len(data) < 1):
        break
    print(data.decode(),end='')
mysock.close()

# HTTP/1.1 200 OK
# Date: Fri, 18 Feb 2022 19:21:16 GMT
# Server: Apache/2.4.18 (Ubuntu)
# Last-Modified: Sat, 13 May 2017 11:22:22 GMT
# ETag: "1d3-54f6609240717"
# Accept-Ranges: bytes
# Content-Length: 467
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: text/plain


# Exercize 2 - Scraping Numbers
print('\n--- Scraping Numbers ---\n')


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup                       # inport BeautifulSoup

url = input('Enter - ')                             # Enter the URL
html = urllib.request.urlopen(url).read()           # read the whole thing (we are not looping)
soup = BeautifulSoup(html, 'html.parser')           # will parse and give back a soup object

# Retrieve all of the anchor tags
tags = soup('span')                                 # create a list of tags
count = 0       # count variable
total = 0       # total variable
for tag in tags:
    num = int(tag.string)   # retrieve the content of the tag (string), convert it to an integer, save it into num
    
    total = total + num
    count = count + 1


print('Count',count)
print('Sum',total)

# Exercize 3 - Following links with python
print('\n--- Exrcize 3: Following links with python ---\n')


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup                       # inport BeautifulSoup
import ssl      

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')                             # Enter the URL
repeat = int(input('Enter repeat: '))
# print('repeat:', repeat)

position = int(input('Enter position: '))
# print('position:',position)

for i in range(repeat):
    html = urllib.request.urlopen(url, context=ctx).read()  # read the whole thing (we are not looping) # we have to add the context=ctx
    # we now have a long strings saved into "html" with \n characters at the end of each line
    soup = BeautifulSoup(html, 'html.parser')           # will parse and give back a soup object
    #print('-------- iteration ', (i+1),'---------')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags[:position]:
        url = tag.get('href', None)    
        name = tag.string
    print('Retrieving:',url)     
print('The answer to the assignment for this execution is:',name)
