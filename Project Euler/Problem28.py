#!/usr/bin/python -tt
import sys
from operator import add
import time
import pe_lib
start_time = time.clock()

#main iterative while loop
N=1
cond = True
diagonal_list = [1]
primecounter = 0

while cond:
	#build the list of diagonal elements
	diagonal_list.append(diagonal_list[-1]+N+1)
	diagonal_list.append(diagonal_list[-1]+N+1)
	diagonal_list.append(diagonal_list[-1]+N+1)
	diagonal_list.append(diagonal_list[-1]+N+1)
	N = N +2
	if N == 10**3+1:
		cond = False

print 'answer = ', sum(diagonal_list)
print 'clock time = ', time.clock() - start_time, "seconds"


