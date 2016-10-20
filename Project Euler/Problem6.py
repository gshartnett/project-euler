#!/usr/bin/python -tt
import sys
import time
start_time = time.clock()

num = 100
intlist = range(1,num+1)
squarelist = [x**2 for x in intlist]
squaresum = sum(squarelist)
intsum = sum(intlist)

print 'answer = ', intsum**2 - squaresum
print 'clock time = ', time.clock() - start_time, "seconds"

##The sum of the squares of the first ten natural numbers is,
##12 + 22 + ... + 102 = 385
##The square of the sum of the first ten natural numbers is,
##(1 + 2 + ... + 10)2 = 552 = 3025
##Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385= 2640.
##Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
