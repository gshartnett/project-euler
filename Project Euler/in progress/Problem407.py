#!/usr/bin/python -tt
import sys
import time
start_time = time.clock()

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

#first pass at defining the M(n) function
nmax = 10**5
Mnsum = 0
#Mnlist = []

for n in range(1,nmax+1):
	cond = True
	i = n-1
	if primality_test(n):
		Mnsum = Mnsum + 1
		#Mnlist.append(1)
	else:
		while cond:		
			if (i**2 - i) % n == 0:
				Mnsum = Mnsum + i
				#Mnlist.append(i)
				cond = False
			i = i - 1

#print Mnlist
print Mnsum
print 'clock time = ', time.clock() - start_time, "seconds"

