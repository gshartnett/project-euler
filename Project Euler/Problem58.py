#!/usr/bin/python -tt
import sys
from operator import add
import time
start_time = time.clock()

##Notes
#I think that the bottleneck here is that the straightforward approach of building the whole square of side length N scales like N^2. If I could just build the diagonal directly, then it should scale like N.

#define a primality test
def primality_test(n):
	if n <=1:
		return False
	elif n <=3:
		return True
	elif n % 2 == 0 or n % 3 == 0:
		return False
	i=5
	while i*i <= n:
		if n % i == 0 or n % (i+2) == 0:
			return False
		i = i + 6
	return True

#main iterative while loop
N=1
cond = True
diagonal_list = [1]
primecounter = 0

while cond:
	#build the list of diagonal elements and run the primality test on each one
	diagonal_list.append(diagonal_list[-1]+N+1)
	if primality_test(diagonal_list[-1]):
		primecounter = primecounter + 1
	diagonal_list.append(diagonal_list[-1]+N+1)
	if primality_test(diagonal_list[-1]):
		primecounter = primecounter + 1	
	diagonal_list.append(diagonal_list[-1]+N+1)
	if primality_test(diagonal_list[-1]):
		primecounter = primecounter + 1
	diagonal_list.append(diagonal_list[-1]+N+1)
	if primality_test(diagonal_list[-1]):
		primecounter = primecounter + 1
	N = N +2
	
	#do the % test, exit if it succeeds
	if float(primecounter)/len(diagonal_list) < 0.10:
		cond = False

print 'answer = ', N
print 'clock time = ', time.clock() - start_time, "seconds"


