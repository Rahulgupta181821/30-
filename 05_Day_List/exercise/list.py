import sys
sys.path.append('G:/30-day-of-Python')
from data.countries import countries
# print(countries)
# lt=[]
# print(len(lt))
# lt=['Rahul','age',23,['Book','title'],{'city': 'Delhi',
#                                        'state':'up'}]
# print(lt,len(lt))

# print(lt[0])
# print(lt[len(lt)//2])
# print(lt[-1])

# mixed_data_types = ['rahul',23,'5.5',False, 'Delhi']
# it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
# print(mixed_data_types)
# print(len(it_companies))
# print(it_companies[0],it_companies[len(it_companies)//2],it_companies[-1])
# it_companies[1]='Meta'
# print(it_companies)
# it_companies.append("Boat")
# it_companies.insert(len(it_companies)//2,"Roadester")
# print(it_companies)

# for index, item in enumerate(it_companies):
#     if item != 'IBM':
#         it_companies[index] = item.upper()
# print(it_companies)
# print('#'.join(it_companies))
# print('IBM' in it_companies)
# print(it_companies.sort())
# print(it_companies)
# print(it_companies.reverse())
# print(it_companies)
# print(it_companies[0:3])
# print(it_companies[-3:])
# print(it_companies[len(it_companies)//2: len(it_companies)//2+1])
# print(it_companies.pop(0))
# print(it_companies.pop(len(it_companies)//2))    
# print(it_companies.pop(-1))
# print(it_companies.clear())
# del it_companies
# # print(it_companies)
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# front_end.extend(back_end)
# print(front_end)
# full_stack= front_end.copy()
# full_stack.append('Python')
# full_stack.append('Redux')
# print(full_stack)

# level 2
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ages.sort()
# minimum=min(ages)
# maximum=max(ages)
# ages.append(minimum)
# ages.append(maximum)
# print(ages)
# average = sum(ages)//len(ages)
# print(average)
# print(max(ages)-min(ages))
# print(min(ages)-average)

print(countries[len(countries)//2])
print(len(countries))
first_half=[]
second_half=[]
if len(countries)%2==0:
    first_half.extend(countries[:len(countries)//2])
    second_half.extend(countries[len(countries)//2:])
else:
    first_half.extend(countries[:len(countries)//2+1])
    second_half.extend(countries[len(countries)//2+1:])
print(len(first_half))
print(len(second_half))
new_countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_three, scandinavian = new_countries[:3], new_countries[3:]

print("First three countries:", first_three)
print("Scandinavian countries:", scandinavian)
