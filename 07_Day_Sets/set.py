print('set')
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
print(st)
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
# vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot',{'Rahul':34})
""" 
Hashable Types:
In Python, a hashable type is an object whose hash value does not change over its lifetime. 
Immutable data types like integers, floats, strings, tuples, and frozensets are hashable. 
Mutable data types like lists, dictionaries, and sets are not hashable.
"""


"""
The Error Message:
When you encounter the error message "unhashable type: 'dict'", it means you're trying to use a dictionary as a key in another dictionary or as an element in a set. 
Since dictionaries are mutable and therefore not hashable, they cannot be used as keys in dictionaries or as elements in sets.
"""
fruits.update(vegetables)
print(fruits)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = ('item5', 'item6', 'item7', 'item8')
st3 = st1.union(st2)
print(st3)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st1.intersection(st2)) # {'item3', 'item2'}
print(st1)
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1)) # set()
print(st1.difference(st2)) # {'item1', 'item4'} => st1\st2