#!/usr/bin/python

import math

def main(fileName):
   data = []
   with open(fileName) as fp:
      line = fp.readline().strip()
      while line:
         tmp = int(math.floor(float(line)/3)-2)
         data.append(tmp)
         line = fp.readline().strip()
   print data
   res = 0
   for i in data:
      res += i
   print res

def main2(fileName):
   data = []
   with open(fileName) as fp:
      line = fp.readline().strip()
      while line:
         tmp = calculateFuel(int(line), int(math.floor(float(int(line)/3)-2)))
         data.append(tmp)
         line = fp.readline().strip()
   print data
   res = 0
   for i in data:
      res += i
   print res

def calculateFuel(mass, fuel):
   if fuel <= 0:
      return 0
   return fuel + calculateFuel(mass, int(math.floor(float(fuel)/3)-2))

#main('01.txt')
main2('01.txt')
