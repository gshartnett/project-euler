#!/usr/bin/python -tt
import sys
import time
start_time = time.clock()

def divisionsuccess(num):
	cond1 = True
	happy = False
	while cond1 == True:	
		for i in range(1,20):
			if num % i != 0:
				cond1 = False
		if cond1 == True:
			happy = True
		cond1 = False
	return happy

cond1 = True
n = 40
while cond1 and n < 10**9:
	if divisionsuccess(n):
		answer = n
		cond1 = False
	else:
		n = n + 20 #the number needs to be a multiple of 20
if cond1 == True:
	print('failed to find a solution, increase range')

print 'answer = ', answer
print 'clock time = ', time.clock() - start_time, "seconds"

#Q: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
