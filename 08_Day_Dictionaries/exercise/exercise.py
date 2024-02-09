# dog={}
# print(dog)
# dog['name']='John'
# dog['color']='black'
# dog['breed']='pidbule'
# dog['legs']=4
# dog['age']=4
# print(dog)


student={'first_name':'Rahul',
          'last_name':'Gupta',
          'gender':'male',
          'age':25,
          'marital status': False,
          'skills':'Python',
          'country':'India',
          'city':'Delhi',
          'address':'pitampura'  
         }
print(student)
print(student.keys())
print(student.values())
print(len(student))
values= student.get('skills')
print(type(values))
student['skills']=['python','Java','JavaScript']
print(student['skills'])
print(student.items())
del student['skills']
print(student.get('skills'))
del student 
# print(student)