#!/usr/bin/python -tt
import sys
import time
import pe_lib
from collections import Counter
start_time = time.clock()

n = 2
cond = True
threshold = 500
while cond:
  N = n*(n+1)/2
  power_list = Counter(pe_lib.prime_factors(N)).values()
  sigma = 1
  for i in range(len(power_list)):
    sigma = sigma * (1 + power_list[i])
    if sigma > threshold:
      cond = False
      answer = N
  else:
    n = n + 1

print 'answer = ', answer
print 'clock time = ', time.clock() - start_time, "seconds"
