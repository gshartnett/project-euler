#!/usr/bin/python -tt
import sys
import time
start_time = time.clock()

def sum_digits(n):
	r = 0
	while n:
		n, r = n // 10, r + n % 10
	return r

ablist = []
for a in range(2,100):
	for b in range(2,100):
		ablist.append( (sum_digits(a**b), a, b, a**b) )

print 'answer = ', sorted(ablist)[-1][0]
print 'clock time = ', time.clock() - start_time, "seconds"

#Q: A googol 10**100 is a massive number: one followed by one-hundred zeros; 100**100 is almost unimaginably large: one followed by #two-#hundred zeros. Despite their size, the sum of the digits in each number is only 1.
#Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
