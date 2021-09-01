import math
import sys
import os
sys.path.append('mines')
from primes import *

# global variable declaration

def findPrimes(primeRange):
  # we will add primes as we find them here, for iteration when a number 
  # is not prime because of two primes multiplied together. 
  primes = toTest.copy()
  primeStill = "false"

  i = numbersIterated
  lim = numbersIterated+primeRange
  # subtract 4 because we use 2, 3, 5, 7 to compare earlier, so we already
  # have those (reduce runtime)
  while i < lim:
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
      elif (i in toTest):
        primes.append(i)
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
              with open(os.getcwd()+'/mines/primes.py', 'w') as f:
                f.write('# list length='+str(len(primes))+'\nnumbersIterated = '+str(i)+'\ntoTest = '+str(primes))
              f.close()
            break
    i = i + 1
  return None

findPrimes(1000)
