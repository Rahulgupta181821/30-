# try:
#     print(10+'5')
# except:
#     print("Something went wrong")
# try:
#     name= input('Enter your name')
#     year_born = input('Year you were born:')
#     age = 2019-year_born
#     print(f'You are {name}. And your age is {age}.')
# except:
#     print("Something went Wrong")

# try: 
#     name = input('Enter your naem: ')
#     year_born= input('Enter you were born:')
#     age = 2019 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print("Type error occured")
# except ValueError:
#     print('Value error occured')
# except ZeroDivisionError:
#     print('Zero division error occured.')
# else:
#     print('I usually run with the try block')
# finally:
#     print('I always run.')


# try:
#     name= input('Enter your name: ')
#     year_born = input('Year of born: ')
#     age = 2024- year_born
#     print(f'You are {name}. And your age is {age}.')
# except Exception as e:
#     print(e)


# def sum_of_five_nums(a,b,c,d,e):
#     return a+b+c+d+e
# lst = [1,2,4,5,5]
# # print(sum_of_five_nums(lst))
# print(sum_of_five_nums(*lst))

# numbers = range(2,7)
# print(list(numbers))
# args= [2, 7]
# numbers = range(*args)
# print(len(numbers))

# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# fin, sw, nor, *rest = countries
# print(fin, sw, nor, rest)

# numbers=[1,2,3,4,5,6,7]
# one, *middle, last= numbers
# print(one, middle, last)

# def unpacking_person_info(name,country, city, age):
#     return f'{name} lives in {country}, {city}. He is {age} year old.'
# dct = {'name':'Rahul', 'country': 'Finland', 'city': 'Helsinki', 'age':250}
# print(unpacking_person_info(**dct))


# def sum_all(*args):
#     s=0
#     for i in args:
#         s+=i
#     return s
# print(sum_all(1,2,3))
# print(sum_all(1,2,3,4,5,6,7,8,9,10,11,12))

# def packing_person_info(**kwargs):
#     for key in kwargs:
#         print(f'{key} = {kwargs[key]}')
#     return kwargs
# print(packing_person_info(name='Rahul',country="India",city="Delhi",age=250))

# lst_one=[1,2,3]
# lst_two=[4,5,6]
# lst=[0,*lst_one,*lst_two]
# print(lst)

for index, item in enumerate([20,30,40,50]):
    print(index,item)



fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges=[]
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruits':f,'veg':v})
    
print(fruits_and_veges)

