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

# Description of the legal format of an XML document
# Expressed in terms of constraints on the structure and content of documents
# Often used to specify a “contract” between systems - “My system will only accept XML that conforms to this particular Schema.”
# If a particular piece of XML meets the specification of the Schema - it is said to “validate”


# XML document          - sent to \
#                                 XML validator (which make sure teh document follows the schema contract)
# XML schema contract   - sent to /


# XML Document example
# <person>
#    <lastname>Severance</lastname>
#    <age>17</age>
#    <dateborn>2001-04-17</dateborn>
# </person>

# XML Schema Contract example 
# <xs:complexType name=”person”>
#   <xs:sequence>
#     <xs:element name="lastname" type="xs:string"/>
#     <xs:element name="age" type="xs:integer"/>
#     <xs:element name="dateborn" type="xs:date"/>
#    </xs:sequence>
# </xs:complexType>

# XML schema is a partincular format of XML 

# Many XML Schema Languages
# Document Type Definition (DTD)
# -  http://en.wikipedia.org/wiki/Document_Type_Definition
# Standard Generalized Markup Language (ISO 8879:1986 SGML)
# -  http://en.wikipedia.org/wiki/SGML
# XML Schema  from W3C - (XSD)
# -  http://en.wikipedia.org/wiki/XML_Schema_(W3C)



# XSD XML Schema (W3C spec)
# We will focus on the World Wide Web Consortium (W3C) version
# It is often called “W3C Schema” because “Schema” is considered generic
# More commonly it is called XSD because the file names end in .xsd
# http://www.w3.org/XML/Schema


# XSD Structure

# xs:element        => simple element  <xs:element name="lastname" type="xs:string"/>
#                                       <lastname>Sever</lastname>
# xs:sequence       => indicate a sequence of elements
#
# xs:complexType    => <xs:complexType name=”person”>
#                       <person>


# XSD Constraints
# attributes like   minOccurs="1"  or   maxOccurs="1"
# if the ekement happens twice => error


# XSD Data Types

# < xs:element name="customer" type="xs:string"/>       just a string, like a name
# <xs:element name="start" type="xs:date"/>             a date , like 2022-02-28 
# <xs:element name="startdate" type="xs:dateTime"/>     date and time, like 2022-02-28T09:30:10Z
# <xs:element name="prize" type="xs:decimal"/>          decimals, 0.0234
# <xs:element name="weeks" type="xs:integer"/>          integer

# It is common to represent time in UTC/GMT, given that servers are often scattered around the world
# Z at the end of the date time means UTC/GMT  (greenwitch time or ZULU time)


# first example 

import xml.etree.ElementTree as ET      # element tree

# the ''' 3 quotes is a way to ignore every other ' "  in between - similar to read a whole file
data = '''<person>          
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data) # create a nobject (tree) that we can query later on
print('Name:',tree.find('name').text)           # tree.find the tag  name and get the text of it
print('Attr:',tree.find('email').get('hide'))   # 

# second example 
import xml.etree.ElementTree as ET
inputdata = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(inputdata)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))












# Extracting data from XML
print('--- Ex 1 - Extracting data from XML ---')

import xml.etree.ElementTree as ET  
import urllib.request, urllib.parse, urllib.error

url = input('Enter location:')                             # prompt to enter the URL

print('Retrieving ', url)
xmldata = urllib.request.urlopen(url).read()  

tree = ET.fromstring(xmldata)
counts = tree.findall('.//count')
print('Count:', len(counts))            # get the numbers of elements
sum = 0

for count in counts:
    sum = sum + int(count.text)

print('Sum:',sum)
    