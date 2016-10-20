#!/usr/bin/python -tt
import sys
import time
start_time = time.clock()

number = 600851475143
print number
primelist = [1]

i=2
while number > 1: #and i*i < number:
	if number % i	== 0:
		primelist.append(i)
		number = number/i
	else:
		i = i + 1

print 'answer = ', max(primelist)
print 'clock time = ', time.clock() - start_time, "seconds"

#Q: The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
