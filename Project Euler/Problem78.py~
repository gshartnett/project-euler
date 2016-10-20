#!/usr/bin/python -tt
import sys
import time
import pe_lib
start_time = time.clock()

#pentagon numbers less than or equal to n (I won't end up using this)
def pentagon(n):
  pent_list = [0]
  i = 1
  cond = True
  while cond:
    pent = (3*i**2-i)/2
    if pent <= n:
      pent_list.append(pent)
    else:
      cond = False
    pent = (3*i**2+i)/2
    if pent <= n:
      pent_list.append(pent)
    else:
      cond = False
    i = i + 1
  return pent_list

#use the recursive definition of partitions to generate a list of p[i] for i<=n
#won't use this either, for this problem I want a code that simply adds the last next item to this list, rather than generating it fresh each time
def partitions(n):
  part_list = [1]
  for k in range(1,n+1):
    part = 0
    i = 1
    cond = True
    while cond:
      pent_minus = i*(3*i-1)/2
      pent_plus = i*(3*i+1)/2
      if k >= pent_minus:
        part += ((-1)**(i-1) )*part_list[k-pent_minus]
      if k >= pent_plus:
        part += ((-1)**(i-1) )*part_list[k-pent_plus]
      if k < pent_plus and k < pent_minus:
        cond = False
        part_list.append(part)
      i = i + 1
  return part_list

#print pentagon(100)
#print partitions(10)

part_list = [1]
k = 1
cond2 = True
while cond2:
  part = 0
  i = 1
  cond = True
  while cond:
    pent_minus = i*(3*i-1)/2
    pent_plus = i*(3*i+1)/2
    if k >= pent_minus:
      part += ((-1)**(i-1) )*part_list[k-pent_minus]
    if k >= pent_plus:
      part += ((-1)**(i-1) )*part_list[k-pent_plus]
    if k < pent_plus and k < pent_minus:
      cond = False
      part_list.append(part)     
    i = i + 1
  if part % 10**6 == 0:
    answer = k
    cond2 = False
  else:
    k = k + 1

#print part_list[-1]

print 'answer = ', k
print 'clock time = ', time.clock() - start_time, "seconds"





