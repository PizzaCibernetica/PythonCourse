big = max("Hello world")

small = min("Helloworld")

print("Big" , big)
print("Small" , small)


bignum = max(1,2,3,4,5)

print(bignum)

#this is comment to be deleted

# A parameter is a variable which we use in the function definition. It is a "handle" that 
# allows the code in the function to access the arguments for a particular invocation.

def greet(lang):
    if lang == 'es':
        print("Hola")
    elif lang == 'fr':
        print("Bonjour")
    else:
        print("Hello")

greet("en")

greet("es")

greet("fr")

# return values
# often a function will take its arguments, do some computation, 
# and return a value to be used as the value of the fucntion call in the calling expression.
# The return keyword is used for this.

def greet():
   return "Hello"

print(greet(), "Mario")
print(greet(), "Gioia")
print("line 42")

# A "fruitful" function is one that produces a result (or return value)
# The return statement ends the function execution and "sends back" the result of the function

def greet(lang):
    if lang == 'es':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour"
    else:
        return "Hello"

print(greet('en'), "Mike")

print(greet("es"), "Mario")

print(greet("fr"), "Sophie")

# Mutiple parameters/Arguments

#We can define more than one parameter in the function definition
# We simply add more arguments when we call the function 
#We match the nnumber and order of arguments and parameters

def addtwo(a,b):
    added = a + b
    return added

x = addtwo(3,5)
print(x)

print("The sum of 3 + 5 is ", x) 

# VOID (non-fruitful) functions

# When a function does not return a value, we call it a "void" function
# Functions that return values are "fruitful" functions
# Void functions are "not fruitful"


# Assignment

def computepay(h, r):
    if h > 40:
        ot = h - 40
        #print(ot)
        otr = r * 1.5
        #print(otr)
        pay = (40*r)+(ot*otr)
        #print(h*r)
        #print(ot*otr)
        return pay
    else:
        return (h*r)


hrs = float(input("Enter Hours:"))

rate = float(input("Enter rate per hour:"))
p = computepay(hrs, rate)
print("Pay", p)