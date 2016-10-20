#!/usr/bin/python -tt
import sys
import time
start_time = time.clock()

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

#print primality_test(13)

primelist = []
for n in range(2,2*10**6):
	if primality_test(n):
		primelist.append(n)
	n = n + 1

print 'answer = ', sum(primelist)
print 'clock time = ', time.clock() - start_time, "seconds"

#Q: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.
