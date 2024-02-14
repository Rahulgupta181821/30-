
import math
import sys
sys.path.append('G:/30-day-of-Python')
from data.countries_data import list_items


def add_two_numbers(arg1, arg2):
    return arg1 + arg2

print(add_two_numbers(1, 2))

def area_of_circle(arg):
    return math.pi * arg **2
print(area_of_circle(5))

def add_all_nums(*arg):
    total = 0
    for i in arg:
        total += i
    return total
print(add_all_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def convert_celsius_to_fahrenheit(tem_in_cel):
    return (tem_in_cel*9//5) + 32
print(convert_celsius_to_fahrenheit(35))

def check_season(month):
    month = month.lower()
    if month in ["march",'april','may']:
        print('The season is Spring.')
    elif month in ["june",'july','august']:
        print('The season is Summer.')
    elif month in ["september",'october','november']:
        print('The season is Autumn.')
    elif month in ["december",'january','february']:
        print('The season is Winter.')
    else:
        print('The season is invalid.')
check_season('OctOber')

def calculate_slope (A, B):
    # Ax + By + c =0
    if B==0:
        print('The slope of the line is undefined.')
    return -(A/B)
print(calculate_slope(2,3)) 

def solve_quadratic_eqn(A,B,C):
    counter = B**2 - 4*A*C
    if counter<0:
        print('The quadratic equation has no real roots.')
    elif counter==0:
        x1 = -B/(2*A)
        print(f'The roots are {x1}')
    else:
        x1 = (-B+math.sqrt(counter))/(2*A)
        x2 = (-B-math.sqrt(counter))/(2*A)
        print(f'The roots are {x1} and {x2}')
print(solve_quadratic_eqn(1,-3,2))

def print_list(arr):
    for itm in arr:
        print(itm)
print_list(["Rahul",22,'BBDNITM','Lucknow',True])


def reverse_list(arr):
    l=0
    r=len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr
arr=[1,2,3,4,5,6,7,8,9,10]
print(reverse_list(arr))
print(arr)
# if we pass array argument then it doesn't copy an array it only copy the reference of array. 

def capitalize_list_items(arr):
    for itm in range(len(arr)):
        arr[itm] = arr[itm].capitalize()
    return arr
arr=['apple','orange','papaya','mango','seagreen']
print(capitalize_list_items(arr))
print(arr)

def add_item(arr,item):
    arr.append(item)
    return arr
# print(add_item(arr,'patato'))

def remove_item(arr,item):
    if item in arr:
       arr.remove(item)
       return arr
    else:
        return 'item not found'

# print(remove_item(arr,'Mango'))

def sum_of_numbers(nums):
    sum=0
    for i in range(nums+1):
        sum+= i
#     return sum
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050

# Level 3
def is_prime(num):
    counter=0
    for i in range(1,math.floor(math.sqrt(num))+1):
        if num%i==0:
            counter+=1
            if num//i!=i:
                counter+=1
    if counter==2:
        return True
    return False

# print(is_prime(2))

def unique_items(arr):
    for i in range(len(arr)):
        for  j in range(i+1,len(arr)):
            if arr[i]^arr[j]==0:
              return 'duplicate items'
    return 'unique items'
arr=[1,2,3,4,5]
# print(unique_items(arr))

def unique_data_type(arr):
    for i in range(len(arr)):
        for  j in range(i+1,len(arr)):
            if type(arr[i])==type(arr[j]):
                return 'duplicate items'
    return 'unique items'
arr=[1,'rahul',2]
# print(unique_data_type(arr))

def valid_variable(item):
    return item.isidentifier()
# print(valid_variable('jtgksf'))
# print(list_items)
def mostspoken(list):
    lan = {}
    for itm in range(len(list_items)):
        for j in  range(len(list_items[itm]['languages'])):
            if list_items[itm]['languages'][j] in lan:
                lan[list_items[itm]['languages'][j]]+=1
            else:
                lan[list_items[itm]['languages'][j]]=1
    rev_sorted = sorted(lan.items(), key = lambda l: l[1], reverse=True)
    return rev_sorted[:10]
# print(mostspoken(list_items))
# print(len(list_items[0]['languages']))

def most_population_country(list_items):
    dicte={}
    for itm in range(len(list_items)):
        dicte[list_items[itm]['name']] =list_items[itm]['population']
    rev_sorted = sorted(dicte.items(), key = lambda l: l[1], reverse=True)
    return rev_sorted[:10]

print(most_population_country(list_items))
