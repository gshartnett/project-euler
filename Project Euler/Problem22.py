#!/usr/bin/python -tt
import sys
import time
start_time = time.clock()

#load the string of names into a string, then turn that string into a list of names
#some massaging is needed to eliminate the parentheses surrounding each entry
big_string = []
with open('supplementary_files/p022_names.txt', 'r') as myfile:
    big_string = myfile.read()

name_list = big_string.split("\",\"")
name_list[0] = name_list[0][1:]
name_list[-1] = name_list[-1][:-2]

#sort into alphabetical order
name_list_sort = sorted(name_list)

#get the weighted sum they ask for
counter = 0
for i in range(len(name_list_sort)):
	counter = counter + (1+i)*sum([ord(c)-64 for c in name_list_sort[i]])

print 'answer = ', counter
print 'clock time = ', time.clock() - start_time, "seconds"

