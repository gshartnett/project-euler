#!/usr/bin/python -tt
import sys
import time
start_time = time.clock()

def collatz_length(n):
	sequence_list = [n]
	if n <= 1:
		return 'argument should be greater than 1!'	
	while n != 1:
		if n % 2 == 0:
			n = n/2
		else:
			n = 3*n + 1
		sequence_list.append(n)
	return len(sequence_list)
	#return sequence_list

length_list = []
for n in range(2,10**6):
	length_list.append((collatz_length(n),n))

print 'answer = ', sorted(length_list)[-1][1]
print 'clock time = ', time.clock() - start_time, "seconds"
