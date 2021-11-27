#!/usr/bin/python

import copy
import re
import math
import os
from time import sleep

def main(data):
   for c in range(len(data)):
      row = int(data[c])
      result = findLoopSize(row)
      data[c] = [row, result]
   print "Q1: encryption key is {}".format(transformNum(data[0][0], data[1][1]))

def transformNum(num, loops, divisor = 20201227):
   val = 1
   for i in range(loops):
      val *= num
      val = val%divisor
   return val

def findLoopSize(result, num = 7, divisor = 20201227):
   val = 1
   i = 0
   while val != result:
      i += 1
      val *= num
      val = val % divisor
   return i

inputData = [
   '5764801',
   '17807724',
]
main(inputData)

inputData = [
   '1717001',
   '523731',
]
main(inputData)
