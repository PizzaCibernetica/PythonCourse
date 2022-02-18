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
