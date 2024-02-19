"""
Map: it takes two parameters function and an iterable and iterates over iterations and return a iterator.
filter: it filters out the iterable and returns the filtered iterable.
reduce: it takes two parameters like map and filter but it returns only one value.

highter oreder function: it is a function which takes a function as a parameter and returns a another function.
closures:Python allows a nesting function to access the outer scope of the enclosing function.
closure is created by nesting function inside another function and then returning the inner function. 
"""
import sys

sys.path.append('G:/30-day-of-Python')
from data.countries import countries
# print(countries)
def square(x):
    return x*x
def call_map(func,iterable):
    return map(func,iterable)
number = [1,2,3,4,5,6,7,8,9]
square_number= call_map(square,number)
# print(list(square_number))

def even_number(x):
    if x%2==0:
        return True
    return False
def call_filter(func,iterable):
    return filter(func,iterable)

number = [1,2,3,4,5,6,7,8,9]

# print(list(call_filter(even_number,number)))
from functools import reduce
def sum_number(a,b):
    return a+b
def call_reduce(func,iterable):
    return reduce(func,iterable)
# number = [1,2,3,4,5,6,7,8,9]
print(call_reduce(sum_number,number))
# for item in countries:
#     print(item)
# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for name in names:
#     print(name)
# for number in numbers:
#     print(number)
    
# Level 2
# country_upper = map(lambda x : x.upper(),countries)
# print(list(country_upper))
# print(list(map(lambda x : x**2,numbers)))
# print(list(map(lambda x: x.upper(),names)))
# print(list(filter(lambda x : 'land' in x, countries)))
# print(list(filter(lambda x: len(x)==6,countries)))
# print(list(filter(lambda x: len(x)>=6,countries)))
# print(list(map(lambda x : x.upper(),list(filter(lambda x: x[0]=='E',countries)))))
# print(type("sth"))
def get_string_lists (array):
    return list(filter(lambda x : type(x)==str, array ))

# array=[1,32,4,5,'Rahul',8,8.9,'mumbai','agara']
# print(get_string_lists(array))
# print(reduce(lambda a,b: a+b,numbers))
# countries1 = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# print(reduce(lambda a,b: a+ ', '+b,countries1))
def get_item(item):
    for i in ['land','ia','island','stan']:
        if i in item:
            return True
    return False
    
# print("hello",list(filter(lambda a: get_item(a)==True ,countries)))

arr= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']
def dict_with_starting_letter(countries):
    dict_of_countries=dict()
    for item in arr:
        array_of_countries= filter(lambda a : a[0].upper()==item,countries)
        dict_of_countries[item]=len(list(array_of_countries))
    return dict_of_countries
# print(dict_with_starting_letter(countries))   
def get_first_ten_countries(countries):
    return countries[:10] 
print(get_first_ten_countries(countries)) 
# print(countries[-10:])   
# Level 3
from data.countries_data import list_items
# print(list_items)   
# sorted_by_name = sorted(list_items,key= lambda x : x['name'])
# for x in sorted_by_name:
#     print(x['name'])  
# sorted_by_capital = sorted(list_items,key = lambda x : x['capital'])
# for x in sorted_by_capital:
#     print(x['name'],":",x['capital'])

# sorted_by_population = sorted(list_items,key = lambda x : x['population'],reverse=True)
# for x in sorted_by_population:
#     print(x['name'],":",x['population'])       


    
arr={}
for x in list_items:
    for item in x['languages']:
        if item not in arr:
            arr[item]=1
        else:
            arr[item]+=1
sorted_by_language = sorted(arr,key = lambda x : arr[x], reverse=True)
print(type(sorted_by_language))
print(sorted_by_language)
for key in sorted_by_language[:10]:
        print(f'{key}: {arr[key]}')
sorted_by_population = sorted(list_items,key= lambda x : x['population'], reverse=True)
print(sorted_by_population)
for item in sorted_by_population[:10]:
    print(item['name'],":",item['population'])