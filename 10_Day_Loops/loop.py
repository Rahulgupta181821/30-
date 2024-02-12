person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
# i=0;
# while i<11:
#     print(i)
#     i+=1
# for i in range(10,-1,-1):
#     print(i)
for i in range(7):
    for j in range(i+1):
        print("#",end="")
    print()
for i in range(7):
    for j in range(7):
        print("#",end=" ")
    print()
for i in range(11):
    print(f'{i} x {i} = {i*i}')
lt = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
# for itr in lt:
#     print(itr)
# for i in range(101):
#     if i%2==0:
#         print(i)
# for i in range(101):
#     if i%2!=0:
#         print(i)
# Level 2
sum=0
for i in range(101):
    sum += i
print(sum)

# even_sum=0
# odd_sum=0
# for i in range(101):
#     if i%2==0:
#         even_sum += i
#     else:
#         odd_sum += i
# print(f'The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.')

# Level 3
import sys
sys.path.append('G:/30-day-of-Python')
from data.countries import countries
for itr in countries:
    if 'land' in itr:
        print(itr)


lt = ['banana', 'orange', 'mango', 'lemon']
for itr in range(len(lt)-1,-1,-1):
    print(lt[itr])



import sys
sys.path.append('G:/30-day-of-Python')
from data.countries_data import list_items

counter=0
arr=[]
for itr in range(len(list_items)):
    if 'languages' in list_items[itr]:
        counter+=len(list_items[itr]['languages'])
        arr.extend(list_items[itr]['languages'])
print(counter)
count_languages={}
for itr in arr:
    if itr not in count_languages:
        count_languages[itr]=1
    else:
        count_languages[itr]+=1
zipped = zip(count_languages.keys(), count_languages.values())
zipped=list(zipped)
res = sorted(zipped, key= lambda x: x[1])
# print(res)
arr=[]
for itm in range(len(res)-1,len(res)-11,-1):
    arr.append(res[itm][1])
print(arr)
pop=[]
for itm in range(len(list_items)):
    if 'population' in list_items[itm]:
        pop.append(list_items[itm]['population'])
# print(pop)
pop= sorted(pop,reverse=True)
print(pop[0:11])