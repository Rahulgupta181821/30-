import re
# paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
# pattern = r'\w+'
# matches = re.findall(pattern,paragraph)
# # print(len(matches))
# setItem = set(matches)
# # print(len(setItem))
# dictItem = {}
# for item in matches:
#     if item not in dictItem:
#         dictItem[item]=1
#     else:
#         dictItem[item]+=1

# arr=[]
# for item,value in dictItem.items():
#     arr.append((value,item))
# # print(arr)
# arr = sorted(arr,key = lambda x: x[0],reverse=True)
# print(arr)



# txt='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
# pattern =r'-?\d+'
# matches =re.findall(pattern,txt)
# print(matches)
# matches = list(map(lambda x: int(x),matches))
# print(matches)
# distance = max(matches)-min(matches)
# print(distance)

# level 2

def is_valid_variable(txt):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    matches = re.findall(pattern,txt)
    if len(matches)==1:
        return True
    return False
# print(is_valid_variable('first_name')) # True
# print(is_valid_variable('first-name')) # False
# print(is_valid_variable('1first_name')) # False
# print(is_valid_variable('firstname')) # True
# print(is_valid_variable('_')) # True
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(sentence):
    # pattern =r'[@$%^&#*.;?]'#or
    pattern = r'[^a-zA-Z\s]'
    text = re.sub(pattern,'',sentence)
    return text
cleaned_text = clean_text(sentence)
print(cleaned_text)
def most_frequent_words(sentence):
    pattern = r'\w+'
    matches = re.findall(pattern,sentence)
    set_item = set(matches)
    dict_item = {}
    for item in matches:
        if item not in dict_item:
            dict_item[item]=1
        else:
            dict_item[item]+=1
    arr=[]
    for item,value in dict_item.items():
        arr.append((value,item))
    arr = sorted(arr,key = lambda x: x[0],reverse=True)
    return arr[:3]
print(most_frequent_words(cleaned_text))
