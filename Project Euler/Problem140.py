#!/usr/bin/python -tt
import sys
from operator import add
import time
import math
import matplotlib.pyplot as plt
start_time = time.clock()

##Notes
#I ended up resorting to Mathematica to solve Diophantine equations :( 
#So this code is not complete.
Aglist = []
Ag = 1
while len(Aglist) < 14:
  det = 1 + 14*Ag + 5*Ag**2
  if math.sqrt(det) == math.floor(math.sqrt(det)):
    Aglist.append(Ag)
  Ag += 1

print Aglist
print [i % 2 for i in Aglist]
print [i % 5 for i in Aglist]
print [i % 7 for i in Aglist]
print 'answer = ', sum(Aglist)
print 'clock time = ', time.clock() - start_time, "seconds"
print [math.log(i) for i in Aglist]
#plt.plot([math.log(i) for i in Aglist],'-o')
plt.plot([i for i in Aglist],'-o')
#plt.ylabel('cv_error')
plt.show()

