#!/usr/bin/python -tt
import sys
import time
import pe_lib
start_time = time.clock()

n = 2
for i in range(7830456): n = (n * 2) % 10000000000		
n = n * 28433 + 1 

print 'answer = ', str(n)[-10:]
print 'clock time = ', time.clock() - start_time, "seconds"





