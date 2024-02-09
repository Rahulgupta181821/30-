# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Level 1
# print(len(it_companies))
# it_companies.add('Tiwitter')
# it_companies.update(("ChatGpt",'Meta','TCS','Infocis'))
# print(it_companies)
# it_companies.remove('Facebook')
# print(it_companies)
# it_companies.remove('Twit') # it gives keyError
# it_companies.discard('Twit')# it doesn't give any error message.
# it_companies.discard('Google')
# print(it_companies)


# Level 2 
c = A.union(B)
print(c)
print(A)
print(B)
# A.update(B)
# print(A)
print(A.intersection(B))
print(B.intersection(A))
print(A.issubset(B))
print(B.issubset(A))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

del A
del B
# print(A)

# Level 3

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(len(age_set))
print(len(age))
print(len(age)>len(age_set))

"""
String: It is collections of one or more characters between single quotes or double quotes.
If gives more than one sentences, then we use triple quotes.
String are immutable. If ones creates we don't want to change it.

List: A list is an ordered collections of different data types. 
It is mutable.It takes duplicate values.

Tuple: A tuple is an ordered collection of different data types.
It is immutable(or unchangeable), indexable.
If ones creates we don't want to change it.
It takes duplicate values.

Set: A set is an unordered collection of different data types.
It doesn't take duplicate values. 
It is unchangeable its value. It only add or remove items from the set.

"""

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence="I am a teacher and I love to inspire and teach people"
sentence_words = sentence.split(' ')
print(sentence_words)
sentence_set = set(sentence_words)
print(sentence_set)
print(len(sentence_set))
print(len(sentence_words))
dt ={}
st={}
print(type(st))
print(type(dt))