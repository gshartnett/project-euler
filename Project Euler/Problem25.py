#!/usr/bin/python -tt
import sys
import time
import pe_lib
from collections import Counter
start_time = time.clock()

Fib1 = 1
Fib2 = 1
cond = True
n = 2
while cond and n < 10**4:
  Fib3 = Fib1 + Fib2
  Fib1 = Fib2
  Fib2 = Fib3
  n = n + 1
  if len(str(Fib3)) == 1000:
    cond = False
    answer = n

#print n, len(str(Fib3)), Fib3

print 'answer = ', answer
print 'clock time = ', time.clock() - start_time, "seconds"
