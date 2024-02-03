# Day 2:30 Days of python Programming
# Level 1

import math

first_name='Rahul'
last_name="Gupta"
full_name='Rahul Kumar'
country='India'
city='Delhi'
age=25
year=2024
is_married=False
is_true=True
is_light=False
school_name, class_name, city, state='BBDNITM',"B3",'Lucknow','UP'
print(school_name,class_name,city,state)

# Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type(school_name))
print(type(class_name))
print(type(city))
print(type(state))
print(len(first_name))
print(len(first_name)==len(last_name))

num_one = 5
num_two=4
total= num_one + num_two
dif = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one**num_two
floor_division= num_one // num_two

print(total)
print(dif)
print(product)
print(division)
print(remainder)


radius= 30
area_of_circle = math.pi *radius * radius
print(area_of_circle)
circum_of_circle = 2*math.pi *radius
print(circum_of_circle)
radius = input("Enter the radius of the circle:")
print(type(radius))
radius = int(radius)
area_of_circle = math.pi *radius * radius
print(area_of_circle)

# first_name = input("Enter the first name")
# last_name = input("Enter the last name")
# country = input("Enter the country")
# age = input("Enter the age")
# help('keyword')

print(abs(-3 + 4j))
# 5.0

'''
Return the absolute value of a number. The argument may be an integer, a floating point number, or an object implementing __abs__(). 
If the argument is a complex number, its magnitude is returned.

'''
print(all([1,2,3,4,0]))
# False because of 0.
# Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:

'''
 any(iterable):Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:
'''


'''

chr(i):
Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. 
This is the inverse of ord().
The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16). ValueError will be raised if i is outside that range.

'''