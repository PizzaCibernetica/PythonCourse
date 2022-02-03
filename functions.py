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