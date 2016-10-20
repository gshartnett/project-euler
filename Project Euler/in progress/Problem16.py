#!/usr/bin/python -tt
import sys

power = 1000
bignum = 2**power
bigstr = str(bignum)
numlist = []

for i in range(len(bigstr)):
	numlist.append(int(bigstr[i]))

print sum(numlist)
