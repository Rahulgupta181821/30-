language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

greeting = 'Hello, World!'
print(greeting[::-3]) # skipping 2 characters from the right
print(greeting[::-2])#skipping 1 characters from the right


web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
web={'name':'rahul',
     'lName':'gupta'
     }
result = ' '.join(web.values())
print(result) 

challenge = '   thirty days of pythoonnn   '
print(challenge.strip(' '))
# it removes all the beginning and end of the characters to pass in the argument.
