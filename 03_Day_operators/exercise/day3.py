# age=25
# height=162.3
# comp= 1-2j
# base= int(input("Enter the base:"))
# height=int(input("Enter the height:"))
# area = 0.5*base*height
# print(area)

# side_a= int(input("Enter the side a"))
# side_b= int(input("Enter the side b"))
# side_c= int(input("Enter the side c"))
# perimeter= side_a + side_b + side_c
# print("Perimeter",perimeter)

from math import pi, sqrt


length = int(input("Enter the length of the rectangle"))
width = int(input("Enter the width of the rectangle"))
area_rectangle= length * width
perimeter = 2*(length + width)
print('area_rectangle',area_rectangle)
print('perimeter',perimeter)

radius = int(input("enter the radius of the circle"))
area_of_circle= pi * radius * radius
print('area_of_circle',area_of_circle)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
y_intercept=-2
slop=2
x_intercept=-int(y_intercept/slop)
print(x_intercept,y_intercept,slop)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x_axis= (6-2)
y_axis= (10 -2)
m=int(y_axis/x_axis)
Euclidean_distance= sqrt(x_axis**2 + y_axis**2)
print("Euclidean distance",Euclidean_distance)
print("m",m)
print(slop is m)
# both slop and m are same object.

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# find the root of this quadratic equation
a1=1
b1=6
c1=9
discriminant= b1**2 - 4*a1*c1
if discriminant>=0:
    x1=int((-b1+sqrt(discriminant))/(2*a1))
    x2=int((-b1-sqrt(discriminant))/(2*a1))
    print("x1:",x1,"x2:",x2)
else:
    print("there is no real roots")


x='python'
y='dragon'
print(len(x)==len(y))
print(x is y)
if 'on' in x and 'on' in y:
    print("'on' is found in both 'python' and 'dragon'")
else:
    print("'on' is not found in both words")


# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence= 'I hope this course is not full of jargon.'
if 'jargon' in sentence:
    print('jargon is found in this sentence')
else:
    print('jargon is not found in this sentence')
    
if 'on' not in x and 'on' not in y:
    print("'on' is not found in both words")
else:
    print("'on' is found in both words")


length= len('python')
print("float",float(length))
print("string",str(length))

number=int(input("Enter a number to check a number is ever or odd."))
if number%2==0:
    print('Number is even.')
else:
    print('Number is odd.')
floor_division=7//3
if floor_division== int(2.7):
    print('floor division is equal to int converted 2.7')
else:
    print('It is not equal to int converted 2.7')

if type('10')== type(10):
    print('Both are same.')
else:
    print('Both are not same.')
var= int(9.8)
if var==10:
    print('Both are same.')
    print(var)
else:
    print('Both are not same.')
    print(var)
hours= int(input('Enter the hours:'))
rate = int(input('Enter the rate:'))
rate_per_hour= hours*rate
print('Your weekly rate is: %s'%rate_per_hour)

years= int(input('Enter number of years you have lived:'))
number_of_seconds= years*365*24*60*60
print('you have lived for %s seconds.'%number_of_seconds)


print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')