numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_negative_and_zero = [i for i in numbers if i<=0]
# print(filter_negative_and_zero)
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
single_list =[item for row in list_of_lists for number in row for item in number]
# print(single_list)
list_of_tuples = [(i,1,i,i*i,i**3,i**4,i**5) for i in range(11)]
# print(list_of_tuples)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_list =[[col[0].upper(),col[0][:3].upper(),col[1].upper()] for row in countries for col in row]
# print(new_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_list =[{'country': col[0].upper(),'city':col[1].upper()} for row in countries for col in row]
# print(new_list)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

new_list =[ col[0] + ' ' + col[1] for row in names for col in row]
print(new_list)
slope = lambda a,b: -a/b
print(slope(4,5))
