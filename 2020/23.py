#!/usr/bin/python

import copy
import re
import math
import sys

sys.setrecursionlimit(9999)

def main(data):
   cups = [int(x) for x in data]
   for i in range(100):
      cups = playRound(cups)
   oneIndex = cups.index(1)
   result = cups[oneIndex+1:] + cups[:oneIndex]
   print "Q1: {}".format(''.join([str(x) for x in result]))
   cups = [int(x) for x in data]
   for i in range(max(cups), 1000000):
      cups.append(i+1)
   for i in range(10000000):
      if i > 0 and i%100 == 0:
         print i
      cups = playRound(cups)
   oneIndex = cups.index(1)
   result = cups[oneIndex+1] * cups[oneIndex+2]
   print "Q2: {}".format(result)

def playRound(cups):
   currentCup = cups[0]
   removedCups = cups[1:4]
   cups = cups[4:]
   nextCup = currentCup-1
   try:
      nextCup = max([x for x in cups if x <= nextCup])
   except:
      nextCup = max(cups)
   nextCupIndex = cups.index(nextCup)+1
   cups = cups[:nextCupIndex] + removedCups + cups[nextCupIndex:] + [currentCup]
   return cups

inputData = '389125467'
main(inputData)

inputData = '326519478'
main(inputData)

