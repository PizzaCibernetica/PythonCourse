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


