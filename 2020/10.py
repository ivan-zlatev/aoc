#!/usr/bin/python

import copy
import re
import math
from datetime import datetime

def main(data):
   jolts = 0
   adapters = copy.deepcopy(data)
   adapters.append(max(adapters)+3)
   adapters.sort()
   differences = []
   while len(adapters) > 0:
      if adapters[0] - jolts <= 3:
         differences.append(adapters[0] - jolts)
         jolts = adapters[0]
         adapters.pop(0)
   print "Q1: differences:\n\t1: {} \n\t2: {}\n\t3: {}\n\t1*3: {}".format(differences.count(1), differences.count(2), differences.count(3), differences.count(1)*differences.count(3))
   adapters = copy.deepcopy(data)
   adapters.append(max(adapters)+3)
   adapters.append(0)
   adapters.sort()
   addr = 0
   perms = {}
   while addr < len(adapters):
      perms[adapters[addr]] = []
      if addr < len(adapters)-1 and adapters[addr+1] - adapters[addr] <= 3:
         perms[adapters[addr]].append(adapters[addr+1])
      if addr < len(adapters)-2 and adapters[addr+2] - adapters[addr] <= 3:
         perms[adapters[addr]].append(adapters[addr+2])
      if addr < len(adapters)-3 and adapters[addr+3] - adapters[addr] <= 3:
         perms[adapters[addr]].append(adapters[addr+3])
      addr += 1
   print perms
   print "Q2: total number of distinct ways to arrange the adapters: {}".format(resolvePath(perms))

def resolvePath(data, key=0):
   counter = 0
   if data[key] == []:
      #print "{} found the end of one path".format(datetime.now())
      return 1
   else:
      for val in data[key]:
         counter = counter + resolvePath(data, val)
   return counter

inputData = [
   16,
   10,
   15,
   5,
   1,
   11,
   7,
   19,
   6,
   12,
   4,
]

main(inputData)

inputData = [
   28,
   33,
   18,
   42,
   31,
   14,
   46,
   20,
   48,
   47,
   24,
   23,
   49,
   45,
   19,
   38,
   39,
   11,
   1,
   32,
   25,
   35,
   8,
   17,
   7,
   9,
   4,
   2,
   34,
   10,
   3,
]

main(inputData)

inputData = [
   86,
   149,
   4,
   75,
   87,
   132,
   12,
   115,
   62,
   61,
   153,
   78,
   138,
   43,
   88,
   108,
   59,
   152,
   109,
   63,
   42,
   60,
   7,
   104,
   49,
   156,
   35,
   2,
   52,
   72,
   125,
   94,
   46,
   136,
   26,
   16,
   76,
   117,
   116,
   150,
   20,
   13,
   141,
   131,
   127,
   67,
   3,
   40,
   54,
   82,
   36,
   100,
   41,
   56,
   146,
   157,
   89,
   23,
   8,
   55,
   111,
   135,
   144,
   77,
   124,
   18,
   53,
   92,
   126,
   101,
   69,
   27,
   145,
   11,
   151,
   31,
   19,
   34,
   17,
   130,
   118,
   28,
   107,
   137,
   68,
   93,
   85,
   66,
   97,
   110,
   37,
   114,
   79,
   121,
   1,
]

main(inputData)

