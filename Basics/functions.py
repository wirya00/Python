#Defining function with def
def greet():
    print('Hello')

greet()

#Parameters '()'
def greet1(name):
    print('Hello', name)

greet1('Wirya')

#Return values
def sum(a, b):
    c = a + b
    return c

number = sum(1, 2)
print(number)

#Default arguments ('argument'='value')
def greet2(name="Guest"):
    print('Hello', name)

greet2()
greet2('Rendi')

#Keyword arguments
def describe(name, age):
    print('Hello', name, 'Your age is', age)

 #Order doesnt matter when involving keyword
describe(age='17', name='Wirya')

#SCOPE
 #Local Scope
def test():
    x = 10
    print(x)
    #x Only exists inside this function
test()

 #Global Scope
x = 5
def show():
    print(x)
    #Functions can read global variables(outside function)
show()

 #Modifying global variable
def change():
    #global allows modification inside functions
    global x
    x = 10

change()
print(x)

#Lambda functions
 #Normal function:
def square(x):
    return x * x
 #Lambda function:
square = lambda x: x * x
 #Usage:
print(square(4))
 #Lambda structure:
 #lambda paramters: expression