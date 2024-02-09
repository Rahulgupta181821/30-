tp = tuple()
print(tp)
brother=('Mohit','Golu','Chandan','Udey')
sister=('khus','Sal','Pink')
print(tp)
print(len(tp))
sibling=brother + sister
print(sibling)
print(len(sibling))
family_member= list(sibling)
family_member.extend(['GK Gupta','MD'])
family_member= tuple(family_member)
print(family_member)

# Level 2

sibling, parent = family_member[:7], family_member[7:]
print(sibling,parent)

fruits = ("apple", "orange", "Mango",'Banana')
vegitables=('onion','patato','tomato','ginger','garlic','radish')
animal=('Bear','tiger','lion','cat','Dog','cow','bull','buffalo')
food_stuff_tp= fruits + vegitables + animal
print(food_stuff_tp)

food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp)
print(food_stuff_tp[len(food_stuff_tp)//2])
lt_items= food_stuff_tp[:3] + food_stuff_tp[-3:]
print(lt_items)
del food_stuff_tp

# print(food_stuff_tp)
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)