#!/usr/bin/python -tt
import sys
import time
import math
from collections import Counter
list=[]
start_time = time.clock()

#make a list of tuples of the form (n,d(n))
#accidentally, the way I did this nicely gets around the issue that the amicable pairs (a,b) were defined with the condition that d(a) = b and d(b) = a, WITH a!=b (!!) By using a strict inequality, I handle the special cases where a=b, as in (6,6) or (28,28), these are known as perfect numbers.
divisor_list = []
for n in range(1,10**4):
  divisor_sum = 0
  for i in range(1,n/2+2):
    if n % i == 0:
      divisor_sum += i
  divisor_list.append((n,divisor_sum))

print divisor_list
#now rebuild the list so that the first tuple index is always larger than the second, allowing me to identify duplicates
divisor_list2 = []
for i in range(len(divisor_list)):
 divisor_list2.append(( max(divisor_list[i][0],divisor_list[i][1]), min(divisor_list[i][0],divisor_list[i][1]) ))

#throw away all non-duplicates: these are the amicable numbers
amicable_pairs = [k for k,v in Counter(divisor_list2).items() if v>1]

#compute their sum
amicable_sum = 0
for i in range(len(amicable_pairs)):
  amicable_sum += amicable_pairs[i][0] + amicable_pairs[i][1] 

print 'answer = ', amicable_sum
print 'clock time = ', time.clock() - start_time, "seconds"

#Q: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
