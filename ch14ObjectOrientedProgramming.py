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
