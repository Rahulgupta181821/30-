from modules import generate_full_name,sum_two_nums
import os
print(generate_full_name('Rahul','Gupta'))
print(sum_two_nums(8,9))
# os.mkdir('directory_name')
# os.chdir('path')
# os.getcwd()
# os.rmdir('directory_name')
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
# print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3