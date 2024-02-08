

str1='Thirty'
str2= 'Days'
str3= 'of'
str4= 'Python'
finalString= str1+" " +str2 +" " + str3 +" " +str4
print(finalString)
print(' '.join([str1,str2,str3,str4]))

str1='Coding'
str2= 'For'
str3= 'All'
print(' '.join([str1,str2,str3]))
company="Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.capitalize())
print(company.swapcase())
print(company.title())
slice=company[0:6]
print(slice)
print(company.index(slice))
print(company.rindex(slice))
print(company.find(slice))
print(company.rfind(slice))
str_replace=company.replace(slice,'Python')
print(str_replace)
print(company)
str_replace_Everyone= str_replace.replace("All",'Everyone')
str_replace_Everyone2= re.sub(r'All','Everyone',str_replace)
# it uses regular expression to replace it
print(str_replace_Everyone)
print(str_replace_Everyone2)
print(company.split(' '))

company_2 ="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(company_2.split(','))

print(company[0])
print(company[10])
#  Create an acronym
original_name = "Python For Everyone"
acronym = ''.join( word[0] for word in original_name.split())
print(acronym)

#  Create an abbreviation
abbreviation = original_name.split()[0][:2] + '4' + original_name.split()[-1][0]
print(abbreviation)
original_name= "Coding For All"
acronym= ''.join( word[0] for word in original_name.split())
print(acronym)
abbreviation= original_name.split()[0][:2] + '4' + original_name.split()[-1][0]
print(abbreviation)
print(original_name.index('C'))
print(original_name.index('F'))
print(original_name.rindex('l'))
sentence= 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
start_index=sentence.find('because')
print(start_index)
end_index=sentence.rindex('because')
print(end_index)
print(sentence[start_index: end_index+len('because')])


text = "Coding For All"
substring = "Coding"

if text.startswith(substring):
    print("Yes, 'Coding For All' starts with the substring 'Coding'")
else:
    print("No, 'Coding For All' does not start with the substring 'Coding'")



if text.endswith(substring):
    print("Yes, 'Coding For All' ends with the substring 'Coding'")
else:
    print("No, 'Coding For All' does not ends with the substring 'Coding'")

text='   Coding For All      ' 
print(text.strip(' '))

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

arr=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(arr))

print('I am enjoying this challenge.\n\
I just wonder what is next.')

print('Name\tAge\tCountry\tCity\n\
Asabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
output='The area of a circle with radius {} is {:.0f} meters square.'.format(radius,area)
print(output)

a=8
b=6
print('{} + {}= {}'.format(a,b,a+b))
print('{} - {}= {}'.format(a,b,a-b))
print('{} * {}= {}'.format(a,b,a*b))
print('{} / {}= {:.2f}'.format(a,b,a/b))
print('{} % {}= {}'.format(a,b,a%b))
print('{} // {}= {}'.format(a,b,a//b))
print('{} ** {}= {}'.format(a,b,a**b))