# age = int(input('Enter your age:'))
# if age> 18:
#     print('You are old enough to learn to drive.')
# else:
#     print(f'You need {18-age} years to learn to drive.')


# my_age = 25  # Assume my age is 25 for demonstration
# your_age = int(input("Enter your age: "))

# if my_age > your_age:
#     age_difference = my_age - your_age
#     if age_difference == 1:
#         print("I am older than you by 1 year.")
#     else:
#         print("I am older than you by", age_difference, "years.")
# elif your_age > my_age:
#     age_difference = your_age - my_age
#     if age_difference == 1:
#         print("You are", age_difference, "year older than me.")
#     else:
#         print("You are", age_difference, "years older than me.")
# else:
#     print("We are the same age.")

a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
if a> b:
   print(f'{a} is greater than {b}')
elif a < b:
    print(f'{b} is greater than {a}')
else:
    print(f'{a} is equal to {b}')
    
#Level
score = int(input("Enter your score: "))
if score>=80 and score<=100:
    print('A')
elif score>=70 and score<=89:
    print('B')
elif score>=60 and score<=79:
    print('C')
elif score>=50 and score<=59:
    print('D')
else:
    print('F')

month = input("Enter your month: ")
month = month.lower()
if month in['september','october','November']:
    print('The season is Autumn')
elif month in ['december','january','february']:
    print('The season is Winter')
elif month in ['march','april','may']:
    print('The season is Spring')
elif month in ['june','august','september']:
    print('The season is Summer')
else:
    print('The month is invalid')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter fruit')
if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print(f'{fruit} is already in the list')


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    print(person['skills'][len(person['skills'])//2])
    if 'Python' in person['skills']:
        print(person['skills'])
if len(person['skills'])==2:
    if ['JavaScript', 'React'] in person['skills']:
        print('He is a front-end developer.')
elif ['Node','Python','MongoDB'] in person['skills']:
    print('He is a back-end developer.')
elif ['React','Node','MongoDB'] in person['skills']:
    print('He is a full-stack developer.')
else:
    print('unknown title')
if 'is_marred' in person:
    if 'Finland' == person['country']:
        print("Hello")
        print(f'''{person['first_name']}  {person['last_name']} lives in {person['country']}. He is married.''')