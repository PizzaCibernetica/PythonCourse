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