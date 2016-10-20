#!/usr/bin/python -tt
import sys
import time
start_time = time.clock()

def primetest(number):
	factorlist = []
	i=2
	while number > 1: #and i*i < number:
		if number % i	== 0:
			factorlist.append(i)
			number = number/i
		else:
			i = i + 1
	if len(factorlist) == 1:
		cond1 = True
	else: 
		cond1 = False		
	return(cond1)

primelist = []
n = 2
while len(primelist) <= 10000:
	if primetest(n):
		primelist.append(n)
	n = n + 1	

print 'answer = ', primelist[-1]
print 'clock time = ', time.clock() - start_time, "seconds"

#Q: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10,001st prime number?
