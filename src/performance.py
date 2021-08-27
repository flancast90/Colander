# This file is for measuring the performance of the prime algorithm

# code for graph visualization of runtime
import matplotlib.pyplot as plt
import numpy as np
import timeit
import random

plt.rcParams['figure.figsize'] = [10, 6] # set size of plot

import math

ns = range(5, 200)
ts = [timeit.timeit('findPrimes(primeRange)',
                    setup='primeRange={}'.format(n),
                    globals=globals(),
                    number=1)
         for n in ns]
plt.plot(ns, ts, 'or')
plt.title("Prime Finder Performance")
plt.xlabel("No. of Primes Found")
plt.ylabel("Time (ms)")

def findPrimes(primeRange):
  # we will add primes as we find them here, for iteration when a number 
  # is not prime because of two primes multiplied together. 
  primes = [2, 3, 5, 7]
  primeStill = "false"

  togo = 0
  i = 0
  # subtract 4 because we use 2, 3, 5, 7 to compare earlier, so we already
  # have those (reduce runtime)
  while togo < primeRange-4:
    # number is odd (all primes are odd)
    if (i % 2 != 0):
      # we only need to go up to the floored sqrt of the number - 1, 
      # because nothing greater than the sqrt of the number will multiply
      # to equal it that wasn't already covered. Also, the - 1 is included along 
      # with the floor statement, since if it is divisible by the sqrt, it is
      # no longer prime.
      high = math.floor(math.sqrt(i))

      # bases define our simple odd numbers which provide
      # the first check we will divide for. 1 and 9 are not included,
      # because division by 1 will return the other number, and anything 
      # divisible by 9 is always divisible by 3.
      if ((i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0)):
        # number is not prime
        pass
      else:
        for j in primes:
          if j <= high:
            if (i % j == 0):
              # number is not prime
              primeStill = "false"
              break
            else:
              # number still is not proven to not be prime
              primeStill = "true"
          else:
            if (primeStill == "true"):
              primes.append(i)
              togo = togo+1
            break
    i = i+1
  return primes
