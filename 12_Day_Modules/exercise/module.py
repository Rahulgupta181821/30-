import math
import string
from random import *
str1 = string.ascii_letters + string.digits
# print(str1) 
def random_user_id():
  random_id=""
  for i in range(6):
    random_id = random_id +  str1[math.floor(random()*len(str1))]
    
  return random_id
# print(random_user_id())
def user_id_gen_by_user():
    no_of_char = int(input("Enter the number of characters"))
    no_of_Ids = int(input("Enter the number of IDS"))
    
    for itm in range(no_of_Ids):
       random_id="#"
       for i in range(no_of_char):
            random_id = random_id +  str1[math.floor(random()*len(str1))]
       print(random_id)

# user_id_gen_by_user()

def rgb_color_gen():
    r = math.floor(random()*256)
    g = math.floor(random()*256)
    b = math.floor(random()*256)
    return f"rgb({r},{g},{b})"
# print(rgb_color_gen())

def list_of_hexa_colors():
    hex_values='0123456789abcdef'
    hexa_color='#'
    for i in range(6):
        hexa_color += hex_values[math.floor(random()*len(hex_values))]
    return hexa_color
# print(list_of_hexa_colors())
def list_of_rgb_colors ():
    arr=[]
    while True:
        r = math.floor(random()*256)
        g = math.floor(random()*256)
        b = math.floor(random()*256)
        arr.append(f"rgb({r},{g},{b})")
        if len(arr) > math.floor(random()*256):
            break
    print(len(arr))
    return arr

# print(list_of_rgb_colors())

def shuffle_list(arr):
    for i in range(len(arr)):
        j = math.floor(random()*len(arr))
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    return arr
print(shuffle_list(['rahul',2,4,'abhishek',True,3.5]))

def random_number():
    arr=[]
    while(len(arr)<7):
        radom_digit = int(randint(0,9))
        if radom_digit not in arr:
            arr.append(radom_digit)
    return arr
print(random_number())