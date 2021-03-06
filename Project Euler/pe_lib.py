#function library for Project Euler problems
import sys
import math
#import itertools

#return prime factorization of a number
def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
                factors.append(i)
        i += 1
    if n > 1:
        factors.append(n)
    return factors

#test whether a number n is prime
def primeQ(n):
  if n <=1:
    return False
  elif n <=3:
    return True
  elif n % 2 == 0 or n % 3 == 0:
    return False
  i=5
  while i*i <= n:
    if n % i == 0 or n % (i+2) == 0:
      return False
    i = i + 6
  return True

#generate list of primes < n in ascending order using the sieve of Erastosthenes
def primes(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

#Euler Totient function, does not call previously defined prime factorization so a) it is more self-contained, b) a tiny bit faster
def phi(n):
    result = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
        i += 1
    if n > 1:
        result -= result // n
    return result



