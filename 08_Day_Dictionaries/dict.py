# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#         }
# }
# person['job_title'] = 'Instructor'
# person['skills'].append('HTML')
# print(person)
# person['skills'][1]="Rahul"
# print(person)
# print(person.popitem())
# print(person['age'])

# # syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# syntax
dct = {'key1':'value1', 'key2':['value2',88], 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy['key2'][1] = 'rahul'
print(dct)
print(dct_copy)
'''
{'key1': 'value1', 'key2': ['value2', 'rahul'], 'key3': 'value3', 'key4': 'value4'}
{'key1': 'value1', 'key2': ['value2', 'rahul'], 'key3': 'value3', 'key4': 'value4'}
deep copy only one level
'''
dct_copy['key2'] = 'rahul'
print(dct)
print(dct_copy)
'''
please see both key2 in above and below example
{'key1': 'value1', 'key2': ['value2', 'rahul'], 'key3': 'value3', 'key4': 'value4'}
{'key1': 'value1', 'key2': 'rahul', 'key3': 'value3', 'key4': 'value4'}
'''