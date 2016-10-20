#!/usr/bin/python -tt
import sys
import time
import math
import pe_lib
start_time = time.clock()

def goldblach(n):
  goldblach_result = False
  if pe_lib.primeQ(n) or n % 2 == 0:
    print n, 'is either not prime or not odd!'
  else:
    m=1
    cond = True
    while cond and m <= math.floor(math.sqrt( (n-1)/2 )):
      k = n - 2*m**2
      if pe_lib.primeQ(k):
        goldblach_result = True
        cond = False
      else:
        m = m + 1
  return goldblach_result

bignum = 10**6
int_list = range(3,bignum+1,2)
prime_list = pe_lib.primes(bignum)
composite_list = list(set(int_list)-set(prime_list))
for i in composite_list:
  if not goldblach(i):
    print 'answer = ', i
    break

print 'clock time = ', time.clock() - start_time, "seconds"

