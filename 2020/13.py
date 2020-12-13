#!/usr/bin/python

import copy
import re
import math

def main(data):
   myTime = int(data[0])
   earliest = [myTime*5, 0]
   buses = data[1].split(",")
   for bus in buses:
      if not bus == "x":
         bus = int(bus)
         multi = int(math.ceil(float(myTime)/float(bus)))
         res = bus*multi
         if res <= earliest[0]:
            earliest[0] = res
            earliest[1] = bus
   print "Q1: earliest bus I can take is {}. Minutes I have to wait: {}. Result: {}".format(earliest[1], earliest[0]-myTime, (earliest[0]-myTime)*earliest[1])
   indexed = []
   for i in range(len(buses)):
      if not buses[i] == "x":
         indexed.append([i, int(buses[i])])
   inc = indexed[0][1]
   curr = 0
   indexed = indexed[1:]
   time = 0
   while True:
      #print "current time: {}, increment: {}".format(curr, inc)
      if len(indexed) == 0:
         time = curr
         break
      curr += inc
      for i, b in indexed:
         if (curr+i)%b != 0:
            break
         else:
            inc = inc * b
            indexed = indexed[1:]
   print "Q2: earies timestamp is {}".format(time)
   print ""

inputData = [
   "939",
   "7,13,x,x,59,x,31,19",
]

main(inputData)

inputData = [
   "939",
   "17,x,13,19",
]
main(inputData)

inputData = [
   "939",
   "67,7,59,61",
]
main(inputData)

inputData = [
   "939",
   "67,x,7,59,61",
]
main(inputData)

inputData = [
   "939",
   "67,7,x,59,61",
]
main(inputData)

inputData = [
   "939",
   "1789,37,47,1889",
]
main(inputData)

inputData = [
   "1015292",
   "19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,743,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,643,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23",
]

main(inputData)

