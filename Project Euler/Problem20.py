#!/usr/bin/python -tt
import sys
import time
import math
list=[]
start_time = time.clock()

n = 100
bignum = math.factorial(n)
bigstring = str(bignum)
answer = 0
for i in range(len(bigstring)):
  answer += int(bigstring[i])

print 'answer = ', answer
print 'clock time = ', time.clock() - start_time, "seconds"

#Q: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
