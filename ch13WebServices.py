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

from cgi import print_environ
from itertools import count
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


# JavaScript Object Notation
print('---   JavaScript Object Notation   ---')


# XML better for high hierarchical documents
# JSON better for pulling out data without much fuss

# JSON is not an RFC or a framework, it's just derived from JavaScript
# https://www.json.org/json-en.html


# JSON example 1
import json
data = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)         # loads = load from string
# info is a dictionary becuase of { }
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])    # info sub email sub hide
# JSON represents data as nested “lists” and “dictionaries”

# JSON example 2
import json
jsondata = '''[        
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

info = json.loads(jsondata)
# info is a list [] of 2 items, dictionaries {}
print('User count:', len(jsondata))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])



# Web Services - SOA 
print('\n--- Service Oriented Approach ---\n')


# Service Oriented Approach
# Most non-trivial web applications use services
# They use services from other applications
#       -  Credit Card Charge
#       -  Hotel Reservation systems
# Services publish the “rules” applications must follow to make use of the service (API)


# Multiple Systems

# Initially - two systems cooperate and split the problem
# As the data/service becomes useful -
#   multiple applications want to use the information / application

# Application Program Interface
print('\n--- Application Program Interface ---\n')

# The API itself is largely abstract in that it specifies an interface and
#   controls the behavior of the objects specified in that interface.
#   The software that provides the functionality described by an API is said to be
#   an “implementation” of the API.  An API is typically defined in terms of the
#   programming language used to build an application. 

# Google API documentation on GeoCoding
# https://developers.google.com/maps/documentation/geocoding?hl=en

# type this in 
# http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI
# goggle will give you back (after authentication and usage of API) a JSON like the following
{
    "status": "OK",
     "results": [
        {
            "geometry": {
                "location_type": "APPROXIMATE",
                 "location": {
                    "lat": 42.2808256,
                     "lng": -83.7430378
                }
            },
            "address_components": [
                {
                    "long_name": "Ann Arbor",
                     "types": [
                        "locality",
                         "political"
                    ],
                    "short_name": "Ann Arbor"
                }
             ],
             "formatted_address": "Ann Arbor, MI, USA",
             "types": [
                "locality",
                "political"
            ]
        }
    ]
}

# example of application to do the above
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)



# API Security and Rate Limiting

# The compute resources to run these APIs are not “free”
# The data provided by these APIs is usually valuable
# The data providers might limit the number of requests per day, demand an API “key”, or even charge for usage
# They might change the rules as things progress...


# Twitter
# 
import urllib.request, urllib.parse, urllib.error               # import URL library
import twurl                                                    # import library to deal with twitter
import json                                                     # import library to deal with JSON

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'   # twitter API interface

while True:
    print('')
    acct = input('Enter Twitter Account:')                      # ask for twitter account
    if (len(acct) < 1): break                                   # if we hit "enter" we are gonna break out
    url = twurl.augment(TWITTER_URL,                            # twurl will sign you in
                        {'screen_name': acct, 'count': '5'})    # first 5 friends of this particular screen name
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)                    # open the url
    data = connection.read().decode()                           # decode the url
    headers = dict(connection.getheaders())                     # url open hide the headers by default , we ask the headers now
    print('Remaining', headers['x-rate-limit-remaining'])       # x-rate-limit-remaining => will telll me how many requests are left
    js = json.loads(data)                                       # parse the JSON data 
    print(json.dumps(js, indent=4))                             # print the data so we can debug it, indent=4 => to print in nice way easier to read and understand

    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print('  ', s[:50])

# this is the out put

# Enter Twitter Account:drchuck
# Retrieving https://api.twitter.com/1.1/friends ...
# Remaining 14
# {
    # "users": [
    #     {
    #         "status": {
    #             "text": "@jazzychad I just bought one .__.",
    #              "created_at": "Fri Sep 20 08:36:34 +0000 2013",
    #          },
    #          "location": "San Francisco, California",
    #          "screen_name": "leahculver",
    #          "name": "Leah Culver",
    #      },
    #      {
    #         "status": {
    #             "text": "RT @WSJ: Big employers like Google ...",
    #              "created_at": "Sat Sep 28 19:36:37 +0000 2013",
    #          },
#              "location": "Victoria Canada",
#              "screen_name": "_valeriei",
#              "name": "Valerie Irvine",
#      ],
# }
# Leahculver
#    @jazzychad I just bought one .__._
# Valeriei
#    RT @WSJ: Big employers like Google, AT&amp;T are h
# Ericbollens
#    RT @lukew: sneak peek: my LONG take on the good &a
# halherzog 
#   Learning Objects is 10. We had a cake with the LO,

# oAuth code

import urllib
import oauth
import hidden

def augment(url, parameters) :                  # called augment because it augment the url
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'], secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'],secrets['token_secret'])
    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,
         token=token, http_method='GET', http_url=url, parameters=parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
    return oauth_request.to_url()


# Summary
# Service Oriented Architecture - allows an application to be broken into parts and distributed across a network 
# An Application Program Interface (API) is a contract for interaction
# Web Services provide infrastructure for applications cooperating (an API) over a network - SOAP and REST are two styles of web services
# XML and JSON are serialization formats


# Exercize 1 - Extracting data from XML
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
    

# Exercize 2 - Extracting Data from JSON
print('--- Extracting Data from JSON ---')

import json 
import urllib.request, urllib.parse, urllib.error

url = input('Enter location:')                             # prompt to enter the URL

print('Retrieving ', url)
jsondata = urllib.request.urlopen(url).read()  

infoJson = json.loads(jsondata)

sum = 0
count = 0

for whatever in infoJson['comments']:
    sum = sum + int(whatever['count'])
    count = count + 1
    
print('Count:',count)
print('Sum:',sum)



# Exercize 3 - Calling a JSON API
print('--- Exercize 3 - Calling a JSON API ---')

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)