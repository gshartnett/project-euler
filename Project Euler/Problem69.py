#!/usr/bin/python -tt
import sys
import time
#import math
#import itertools
#from fractions import gcd
import pe_lib
start_time = time.clock()

#this code works (15s) but it is slower than the same algorithm implemented in Mathematica (6s)

N = 10**6
max_totient = 2/float(pe_lib.phi(2))
for n in range(2,N+1):
  if n/float(pe_lib.phi(n)) > max_totient:
    max_totient = n/float(pe_lib.phi(n))
    nmax = n
    #print nmax, max_totient

print 'answer = ', max_totient, ',  ', nmax
print 'clock time = ', time.clock() - start_time, "seconds"
