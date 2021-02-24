import math #gives access to functions within the math module

def my_function():
    print("my function")

def another_function(val):
    return val * 100

def repeat_print(s, times):
    print(s * times)

def hypotenuse(x , y):
    return math.sqrt(x ** 2 + y **2) #sqrt is the square root function within math

my_function()

a = another_function(5)
print('a: ' + str(a))

repeat_print('$', 5)

b = 5
print('hypotenuse: ' + str(hypotenuse(a, another_function(b))))