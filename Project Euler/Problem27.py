#!/usr/bin/python -tt
import sys
import time
import pe_lib
#from collections import Counter
start_time = time.clock()

amax = 1000
bmax = 1000
blist = pe_lib.primes(bmax)
nlist = []
for b in blist:
  for a in range(-amax,amax):
    n = 0
    cond = True
    while cond:
      if pe_lib.primeQ(n**2 + a*n + b):
        n = n + 1
      else:
        cond = False
        nlist.append((n,a*b))

answer = sorted(nlist)[-1][1]
print 'answer = ', answer
print 'clock time = ', time.clock() - start_time, "seconds"
