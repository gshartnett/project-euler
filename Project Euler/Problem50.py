#!/usr/bin/python -tt
import sys
import time
import pe_lib
start_time = time.clock()

n = 100
prime_list = pe_lib.primes(n)
prime_sum = sum(prime_list)

i = 0
cond = True
while cond:
  if not pe_lib.primeQ(prime_sum) or prime_sum > 1000:
    prime_sum += prime_list[-1-i]
    i = i + 1
  else:
    cond = False

print 'answer = ', prime_sum
print 'clock time = ', time.clock() - start_time, "seconds"
