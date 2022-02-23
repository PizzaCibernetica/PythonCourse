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

