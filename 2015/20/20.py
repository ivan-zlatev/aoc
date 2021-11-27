#!/usr/bin/python

import re

def main(puzzle):
   presents = 0
   house = 0
   while presents <= puzzle:
      house += 1
      presents = 0
      for i in factors(house):
         presents += i*10
      if house % 1000 == 0:
         print 'House: {}\tPresents: {}'.format(house, presents)
   print 'House: {}\tPresents: {}'.format(house, presents)

def main2(puzzle):
   presents = 0
   house = 0
   elfs = dict((el,0) for el in [i for i in range(1000000)])
   finished = []
   while presents <= puzzle:
      house += 1
      presents = 0
      facts = [num for num in factors(house) if num not in finished]
      for i in facts:
         if elfs[i] < 50:
            elfs[i] += 1
            presents += i*11
         else:
            finished.append(i)
      if house % 10000 == 0:
         print 'House: {}\tPresents: {}'.format(house, presents)
   print 'House: {}\tPresents: {}'.format(house, presents)

#def factors(num):
#   facts = []
#   for i in range(1, num+1):
#      if num % i == 0:
#         facts.append(i)
#   return facts

from math import sqrt
def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

puzzle = 33100000
#puzzle = 100000

#main(puzzle)
main2(puzzle)
