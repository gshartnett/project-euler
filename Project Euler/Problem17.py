#!/usr/bin/python -tt
import sys
import time
import math
import itertools
list=[]
start_time = time.clock()

#load the triangle from the text file
triangle_size = 'medium'
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

#implement a series of 'staggered' greedy algorithms, i.e.
#path 1 is just a greedy algorithm, path 2 chooses the lesser number as it's first 
path_history = []
path_sum = []
n = 1
for n in range(len(triangle)):
  j = 0
  given_path_sum = triangle[0][0]
  given_path_history = [triangle[0][0]]
  for i in range(1,n+1):
    given_path_sum = given_path_sum + min( triangle[i][j] , triangle[i][j+1] ) 
    given_path_history.append( min( triangle[i][j] , triangle[i][j+1] ) )
    if triangle[i][j] < triangle[i][j+1]:
      j += 0
    else:
      j += 1
  for i in range(n+1,len(triangle)):
    given_path_sum = given_path_sum + max( triangle[i][j] , triangle[i][j+1] ) 
    given_path_history.append( max( triangle[i][j] , triangle[i][j+1] ) )
    if triangle[i][j] > triangle[i][j+1]:
      j += 0
    else:
      j += 1
  path_history.append((n, given_path_history))
  path_sum.append((n, given_path_sum))

#print path_sum

#as a brute-force check, compute all possible paths
#first get a list of all possible paths, which are all possible binary strings of length N-1, if N is the depth of the graph
brute_path_list = ["".join(seq) for seq in itertools.product("01", repeat=N-1)]
brute_path_history = []
brute_path_sum = []
for n in range(len(brute_path_list)):
  j = 0
  given_path_sum = triangle[0][0]
  given_path_history = [triangle[0][0]]
  for i in range(1,len(triangle)):
    if brute_path_list[n][i-1] == '0':
      given_path_sum = given_path_sum + triangle[i][j]
      given_path_history.append(triangle[i][j])
      j += 0
    if brute_path_list[n][i-1] == '1':
      given_path_sum = given_path_sum + triangle[i][j+1]
      given_path_history.append(triangle[i][j+1])
      j += 1
  brute_path_history.append((n, given_path_history))
  brute_path_sum.append((n, given_path_sum))

brute_max_pathnum = sorted(brute_path_sum, key=lambda x: x[1])[-1][0]
brute_max_pathsum = sorted(brute_path_sum, key=lambda x: x[1])[-1][1]

#print brute_path_list[brute_max_pathnum]
#print brute_path_history[brute_max_pathnum]
#print brute_max_pathsum

print 'answer = ', brute_max_pathsum
print 'clock time = ', time.clock() - start_time, "seconds"





