#!/usr/bin/python -tt
import sys
import time
import math
import itertools
list=[]
start_time = time.clock()

#load the triangle from the text file
triangle_size = 'large'
if triangle_size == 'small':
  filename = 'p067_triangle_small.txt'
if triangle_size == 'medium':
  filename = 'p067_triangle_medium.txt'
if triangle_size == 'large':
  filename = 'p067_triangle_large.txt'
with open('supplementary_files/' + filename, 'r') as myfile:
  triangle_string = [x.strip('\n') for x in myfile.readlines()]    

#convert the triangle into a list of numbers, rather than strings
triangle = []
for i in range(len(triangle_string)):
  j = 0
  triangle_given_line = []
  while j < len(triangle_string[i]):
    triangle_given_line.append( int(triangle_string[i][j] + triangle_string[i][j+1]) )

    j = j + 3
  triangle.append(triangle_given_line)
N = len(triangle)

#For problem 17 I tried to be clever and come up with a greedy algorithm, and it didn't work. Then I just solved the problem using a brute-force method, hoping to gain insight in how to pick the best path. From reading the forum for problem 17, I learned that if we don't care about the path, we can find the answer easily by working backwards 
for i in range(2,N+1):
  for j in range(len(triangle[-i])):
    triangle[-i][j] += max( triangle[-i+1][j], triangle[-i+1][j+1] )

print 'answer = ', triangle[0][0]
print 'clock time = ', time.clock() - start_time, "seconds"





