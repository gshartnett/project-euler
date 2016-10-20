#!/usr/bin/python -tt
import sys
import time
import math
list=[]
start_time = time.clock()

n=10
repunit = ''
for i in range(n):
  repunit += '1'

answer = repunit
print 'answer = ', answer
print 'clock time = ', time.clock() - start_time, "seconds"

