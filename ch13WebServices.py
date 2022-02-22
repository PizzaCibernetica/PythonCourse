# Web Services
print('---  Web Services  ---')
# Data on the Web

# With the HTTP Request/Response well understood and well supported,
#  there was a natural move toward exchanging data between programs using these protocols
# We needed to come up with an agreed way to represent data going between applications and across networks
# There are two commonly used formats: XML and JSON


# Sending Data Across the “Net”

# a.k.a.  “Wire Protocol” - What we send on the “wire”
# if we monitor the wire we would see this

# Agreeing on a “Wire Format”

# Python Dictionary    => serialize   ==> on the network ==> de-serialize ==> java HashMap
# serialization (or serialisation) is the process of translating a data structure
#  or object state into a format that can be stored or transmitted  in the "wire" and reconstructed later
# wire protocol can be XML, JSON

# JSON is simpler and easier
# XML is more precize 

# XML - Extensible Markup Language
# eXtensible Markup Language

# Primary purpose is to help information systems share structured data
# It started as a simplified subset of the Standard Generalized Markup Language (SGML), and is designed to be relatively human-legible

# in XML we get to name the tag what we choose

# Start Tag             <person> <name>
# End Tag               </person> </name>
# Text Content          Chuck   +1 734 303 4456
# Attribute             type="intl" 
# Self Closing Tag      />


# <person>
#   <name>Chuck</name>
#   <phone type="intl">
#      +1 734 303 4456
#    </phone>
#    <email hide="yes" />
# </person>

# syntax errors in XML are more severe than in HTML , if you send bad XML the far end would not understand it

# White Space
# Line ends do not matter.  White space is generally discarded on text elements.  We indent only to be readable.
