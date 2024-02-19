# Normal function
# def greeting():
#     return 'Welcome to Python'
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# g = uppercase_decorator(greeting)
# print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''
This decorator function is a higher order function
that takes a function as a parameter

:: What is decoration?
=> adding things to something to make more attractive/ presentable.

:: What is decorator in python?
=> function which takes other functions as input, add additional functionalities and return result it.
=> it is callable python object which modifies other functions/class.
=> if we given a function and my task is to modify this particular task, without modifying the given function, we use decorator in python.
'''
# def printer():
#     print("welcome!")
#     print("welcome!")
# printer()

# but my task is print 3 times "welcome!", without modifying printer function.
# why can you not modify?, suppose this method is present in another module and we don't have access to change this functions then we use decorator.

""" 
def decor(func):
    def inner():
        func() # existing functionality.
        print("welcome!") # adding new functionality.
    return inner
def printer():
    print("welcome!")
    print("welcome!")
# inner = decor(printer)
# inner()
# or 
printer = decor(printer) #alias(same function name )
printer()

#OR
"""

from functools import reduce


def decor(func):
    def inner():
        func() # existing functionality.
        print("welcome!") # adding new functionality.
    return inner
@decor #we use above function call in @ decorator function.(printer = decor(printer)) In above the given task.
def printer():
    print("welcome!")
    print("welcome!")
printer()

def decor(adding):
    def inner():
        res=adding()
        c = float(input("Enter third number:"))
        result = res + c
        return result
    return inner
@decor
def adding():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a + b 
    return result
# but my task is adding 3 numbers without modifing the given function.

print(adding())


# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# @uppercase_decorator
# def greeting():
#     return 'Welcome to Python'
# g=uppercase_decorator(greeting)
# print(g())# WELCOME TO PYTHON
# print(greeting())



'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15

# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]