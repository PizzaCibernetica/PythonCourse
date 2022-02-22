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
# XML doesn't care about white spaces other than in the text area

# XML Terminology
# Tags indicate the beginning and ending of elements
# Attributes - Keyword/value pairs on the opening tag of XML
# Serialize / De-Serialize - Convert data in one program into a common format that can
#  be stored and/or transmitted between systems in a programming language-independent manner


# hierarchical structure in XML 
# parent nodes and child nodes

# complex element (a tag that include other tags)
# <person>
#   <name>Noah</name>
#   <phone>622 7421</phone>
# </person>

# simple element (a tag that include data)
#   <name>Chuck</name>
#   <phone>303 4456</phone>


# XML as a tree

# you can only have one text node
# you can have several attribute nodes

#               A
#             /   \
#            B     C
#           !     /  \
#           X    D    E
#                !    !
#                Y    Z

# XML as Paths

#   /a/b   = path to x
#   /a/c/d = path to y
#   /a/c/e = path to z



# XML Schema
# Describing a “contract” as to what is acceptable XML


