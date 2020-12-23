#!/usr/bin/python

import copy
import re
import math
import sys

sys.setrecursionlimit(9999)

cups = dict()

def main(data):
   global cups
   for i in range(len(data)):
      x = int(data[i])
      if i < len(data)-1:
         cups[x] = int(data[i+1])
      else:
         cups[x] = int(data[0])
   index = int(data[0])
   for i in range(100):
      index = playRound(index)
   plusOne = cups[index]
   plusTwo = cups[plusOne]
   result = []
   index = 1
   for i in range(1, len(cups)):
      result.append(str(cups[index]))
      index = cups[index]
   print "Q1: {}".format(''.join([str(x) for x in result]))
   #return 0
   cups = dict()
   for i in range(len(data)):
      x = int(data[i])
      if i < len(data)-1:
         cups[x] = int(data[i+1])
      else:
         cups[x] = len(data)+1
   for i in range(len(data)+1, 1000001):
      if i < 1000000:
         cups[i] = i+1
      else:
         cups[i] = int(data[0])
   index = int(data[0])
   for i in range(10000000):
      index = playRound(index)
   plusOne = cups[1]
   plusTwo = cups[plusOne]
   result = plusOne * plusTwo
   print "Q2: {}".format(result)

def playRound(index):
   global cups
   #print index, cups
   plusOne = cups[index]
   plusTwo = cups[plusOne]
   plusThree = cups[plusTwo]
   try:
      if index-1 > 0:
         if index-1 not in [index, plusOne, plusTwo, plusThree]:
            destination = index-1
         elif index-2 > 0 and index-2 not in [index, plusOne, plusTwo, plusThree]:
            destination = index-2
         elif index-3 > 0 and index-3 not in [index, plusOne, plusTwo, plusThree]:
            destination = index-3
         else:
            destination = max([x for x in cups.keys() if x not in [index, plusOne, plusTwo, plusThree] and x < index])
      else:
         #print "I'm in try else, index is {}, plusOne {}, plusTwo {}, plusThree {}".format(index, plusOne, plusThree, plusThree)
         destination = max([x for x in cups.keys() if x not in [index, plusOne, plusTwo, plusThree] and x < index])
   except:
      #print "I'm in except"
      destination = max([x for x in cups.keys() if x not in [index, plusOne, plusTwo, plusThree]])
   cups[index] = cups[plusThree]
   cups[plusThree] = cups[destination]
   cups[destination] = plusOne
   return cups[index]

inputData = '389125467'
#main(inputData)

inputData = '326519478'
main(inputData)

