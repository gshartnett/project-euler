#!/usr/bin/python -tt
import sys
import time
start_time = time.clock()

numstring = ''
for n in range(1,10**6+1):
	numstring = numstring + str(n)

prod = 1
for n in range(7):
	prod = prod * int(numstring[10**n - 1])

print 'answer = ', prod
print 'clock time = ', time.clock() - start_time, "seconds"
