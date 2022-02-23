# Object-Oriented Programming
print('---   Object-Oriented Programming   ---')

# A program is made up of many cooperating objects
# Instead of being the “whole program” -
#   each object is a little “island” within the program and cooperatively working with other objects
# A program is made up of one or more objects working together -
#   objects make use of each other’s capabilities


# Object
# An Object is a bit of self-contained Code and Data
# A key aspect of the Object approach is to break the problem into smaller understandable parts (divide and conquer)
# Objects have boundaries that allow us to ignore un-needed detail
# We have been using objects all along: String Objects, Integer Objects, Dictionary Objects, List Objects...

# Definitions
# Class - a template
# Method or Message - A defined capability of a class 
# Field or attribute- A bit of data in a class
# Object or Instance - A particular instance of a class 

# Terminology: Class
# Defines the abstract characteristics of a thing (object),
#  including the thing's characteristics (its attributes, fields or properties)
#  and the thing's behaviors (the things it can do, or methods, operations or features).
#  One might say that a class is a blueprint or factory that describes the nature of something.
#  For example, the class Dog would consist of traits shared by all dogs,
#  such as breed and fur color (characteristics), and the ability to bark and sit (behaviors).

# Terminology: Instance
# One can have an instance of a class or a particular object.
#  The instance is the actual object created at runtime.
#  In programmer jargon, the Lassie object is an instance of the Dog class.
#  The set of values of the attributes of a particular object is called its state.
#  The object consists of state and the behavior that's defined in the object's class.

# Terminology: Method
# An object's abilities. In language, methods are verbs.
#  Lassie, being a Dog, has the ability to bark. So bark() is one of Lassie's methods.
#  She may have other methods as well, for example sit() or eat() or walk() or save_timmy().
#  Within the program, using a method usually affects only one particular object;
#  all Dogs can bark, but you need only one particular dog to do the barking
# Method and Message are often used interchangeably.


# class is a reserved word


class PartyAnimal:
    x = 0

    def party(self) :
      self.x = self.x + 1
      print("So far",self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

# A Nerdy Way to Find Capabilities

# The dir() command lists capabilities
# Ignore the ones with underscores - these are used by Python itself
# The rest are real operations that the object can perform
# It is like type() - it tells us something *about* a variable

y = list()
type(y)
# will print <class 'list'>
dir(y)
# will print ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__',
#  '__doc__', … '__setitem__', '__setslice__', '__str__', 'append', 'clear', 'copy', 'count',
#  'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
 

# We can use dir() to find the “capabilities” of our newly created class.
# this is dir of the class we built before
print("Dir", dir(an))



# Playing with dir() and type()

# The dir() command lists capabilities
# Ignore the ones with underscores - these are used by Python itself
# The rest are real operations that the object can perform
# It is like type() - it tells us something *about* a variable



# Try dir() with a String
x = 'Hello there'
dir(x)
# will print ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__',
#  '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__',
#  '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__repr__', '__rmod__',
#  '__rmul__', '__setattr__', '__str__',
#  'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find',
#  'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join',
#  'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
#  'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


# Object Lifecycle
print('--- Object Lifecycle ---')

# Objects are created, used, and discarded
# We have special blocks of code (methods) that get called
#       -  At the moment of creation (constructor)
#       -  At the moment of destruction (destructor)
# Constructors are used a lot 
# Destructors are seldom used


# Constructor
# The primary purpose of the constructor is to set up some instance variables
#  to have the proper initial values when the object is created

class PartyAnimal:
   x = 0

   def __init__(self):                  # constructor
     print('I am constructed')

   def party(self) :
     self.x = self.x + 1
     print('So far',self.x)

   def __del__(self):                   # destructor
     print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains',an)

# The constructor and destructor are optional. The constructor is typically
#  used to set up variables. The destructor is seldom used.

# In object oriented programming, a constructor in a class is a
#  special block of statements called when an object is created



# Many Instances

# We can create lots of objects - the class is the template for the object
# We can store each distinct object in its own variable
# We call this having multiple instances of the same class
# Each instance has its own copy of the instance variables


class PartyAnimal:
   x = 0
   name = ""
   def __init__(self, z):
     self.name = z
     print(self.name,"constructed")

   def party(self) :
     self.x = self.x + 1
     print(self.name,"party count",self.x)

s = PartyAnimal("Sally")
j = PartyAnimal("Jim")

s.party()
j.party()
s.party()


# Inheritance

# When we make a new class - we can reuse an existing class and inherit all the capabilities
#   of an existing class and then add our own little bit to make our new class
# Another form of store and reuse
# Write once - reuse many times
# The new class (child) has all the capabilities of the old class (parent) - and then some more


# Terminology: Inheritance
# ‘Subclasses’ are more specialized versions of a class,
#  which inherit attributes and behaviors from their parent classes,
#  and can introduce their own.  


class PartyAnimal:                          # parent class
   x = 0
   name = ""
   def __init__(self, nam):
     self.name = nam
     print(self.name,"constructed")

   def party(self) :
     self.x = self.x + 1
     print(self.name,"party count",self.x)

class FootballFan(PartyAnimal):             # child class - footballFan inherits everything that is PartyAnimal
   points = 0
   def touchdown(self):
      self.points = self.points + 7
      self.party()
      print(self.name,"points",self.points)
# FootballFan is a class which extends PartyAnimal. It has all the capabilities of PartyAnimal and more.
 
# --- Definitions ---
# Class - a template
# Attribute – A variable within a class
# Method - A function within a class
# Object - A particular instance of a class
# Constructor – Code that runs when an object is created
# Inheritance - The ability to extend a class to make a new class.
