#!/usr/bin/python -tt
import sys
import time
import math
start_time = time.clock()

N = 20
answer = math.factorial(2*N)/(math.factorial(N))**2

print 'answer = ', answer
print 'clock time = ', time.clock() - start_time, "seconds"
