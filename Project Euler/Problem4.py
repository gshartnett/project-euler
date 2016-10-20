#!/usr/bin/python -tt
import sys
import time
start_time = time.clock()

palindromelist = []

for a in range(10,999):
	for b in range(10,999):
		c = a*b
		cstring = str(c)
		dignum = len(cstring)
		palincheck = True
		i = 0
		while palincheck and i <= dignum-1:
			if cstring[i] != cstring[-1-i]:
				palincheck = False
			else: i = i + 1
			if i == dignum:
				palindromelist.append(c)

print 'answer = ', max(palindromelist)
print 'clock time = ', time.clock() - start_time, "seconds"
