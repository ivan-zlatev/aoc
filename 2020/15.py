#!/usr/bin/python

import copy
import re
import math

def main(data):
   for row in data:
      data, endTurn, result = row.split(':')
      endTurn = int(endTurn)
      data = [int(x) for x in data.split(',')]
      #print data, endTurn, result
      if result == '':
         print "Last number after {} turns is {}".format(endTurn, evalGame(data, endTurn))
      else:
         assert int(result) == evalGame(data, endTurn)

def evalGame(data, endTurn):
   numState = {
      "length": len(data),
      "lastNumber": data[-1],
      "lastIndex": dict(zip(data[:-1], range(len(data) - 1))),
   }
   turn = len(data)
   while turn < endTurn:
      lastNumber = numState["lastNumber"]
      if lastNumber in numState["lastIndex"]:
         prevIndex = numState["lastIndex"][lastNumber]
         newNumber = numState["length"] - prevIndex - 1
      else:
         newNumber = 0
      numState["lastIndex"][lastNumber] = numState["length"] - 1
      numState["lastNumber"] = newNumber
      numState["length"] += 1
      turn += 1
   return newNumber


inputData = [
   "0,3,6:10:0",
   "0,3,6:2020:436",
   "1,3,2:2020:1",
   "2,1,3:2020:10",
   "1,2,3:2020:27",
   "2,3,1:2020:78",
   "3,2,1:2020:438",
   "3,1,2:2020:1836",
   "0,14,1,3,7,9:2020:",
]

main(inputData)

inputData = [
   #"0,3,6:30000000:175594",
   #"1,3,2:30000000:2578",
   #"2,1,3:30000000:3544142",
   #"1,2,3:30000000:261214",
   #"2,3,1:30000000:6895259",
   #"3,2,1:30000000:18",
   #"3,1,2:30000000:362",
   "0,14,1,3,7,9:30000000:",
]

main(inputData)

