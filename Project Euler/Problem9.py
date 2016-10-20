#!/usr/bin/python -tt
import sys
import time
start_time = time.clock()

#solving for a**2 + b**2 = c**2 and a + b + c = 1000 we can find an explicit solution for (b,c) in terms of a
#it remains to pick a natural number a such that b,c are also natural numbers

p = 1000 # this is the sum total

for a in range(1,p):
	b = p*(p-2*a)/(2*(p-a))
	c = (p**2-2*a*p+2*a**2)/(2*(p-a))
	if a+b+c == p and a < b < c:
		#print [a,b,c]	
		answer = a*b*c

print 'answer = ', answer
print 'clock time = ', time.clock() - start_time, "seconds"

#Q: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#a**2 + b**2 = c**2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
