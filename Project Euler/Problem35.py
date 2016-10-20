#!/usr/bin/python -tt
import sys
import time
import pe_lib
from collections import Counter
start_time = time.clock()

digmax = 6
prime_list = pe_lib.primes(10**digmax)
prime_strlist = [str(i) for i in prime_list]
circ_list = [0]*len(prime_list)

for i in range(len(prime_list)):
  if len(prime_strlist[i]) == 1:
    circ_list[i] = 1
  if len(prime_strlist[i]) == 2:
    s = prime_strlist[i]
    if s[1] + s[0] in prime_strlist:
      circ_list[i] = 1
  if len(prime_strlist[i]) == 3:
    s = prime_strlist[i]
    if (s[1] + s[2] + s[0] in prime_strlist and s[2] + s[0] + s[1] in prime_strlist):
      circ_list[i] = 1
  if len(prime_strlist[i]) == 4:
    s = prime_strlist[i]
    if (s[1] + s[2] + s[3] + s[0] in prime_strlist and s[2] + s[3] + s[0] + s[1] in prime_strlist and s[3] + s[0] + s[1] + s[2] in prime_strlist):
      circ_list[i] = 1
  if len(prime_strlist[i]) == 5:
    s = prime_strlist[i]
    if (s[1] + s[2] + s[3] + s[4] + s[0] in prime_strlist and s[2] + s[3] + s[4] + s[0] + s[1] in prime_strlist and s[3] + s[4] + s[0] + s[1] + s[2] in prime_strlist and s[4] + s[0] + s[1] + s[2] + s[3] in prime_strlist):
      circ_list[i] = 1
  if len(prime_strlist[i]) == 6:
    s = prime_strlist[i]
    if (s[1] + s[2] + s[3] + s[4] + s[5] + s[0] in prime_strlist and s[2] + s[3] + s[4] + s[5] + s[0] + s[1] in prime_strlist and s[3] + s[4] + s[5] + s[0] + s[1] + s[2] in prime_strlist and s[4] + s[5] + s[0] + s[1] + s[2] + s[3] in prime_strlist and s[5] + s[0] + s[1] + s[2] + s[3] + s[4] in prime_strlist):
      circ_list[i] = 1

print 'answer = ', sum(circ_list)
print 'clock time = ', time.clock() - start_time, "seconds"
