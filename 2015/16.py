#!/usr/bin/python

import re

def main(dataFile):
   results = {
      'children'     : 3,
      'cats'         : 7,
      'samoyeds'     : 2,
      'pomeranians'  : 3,
      'akitas'       : 0,
      'vizslas'      : 0,
      'goldfish'     : 5,
      'trees'        : 3,
      'cars'         : 2,
      'perfumes'     : 1,
   }
   data = {}
   with open(dataFile, 'r') as file:
      line = file.readline().replace('\n', '')
      while line:
         sue = int(line.split(': ')[0].split(' ')[1])
         tmp = ' '.join(line.split(': ')[1:]).split(', ')
         data[sue] = {
            tmp[0].split(' ')[0] : int(tmp[0].split(' ')[1]),
            tmp[1].split(' ')[0] : int(tmp[1].split(' ')[1]),
            tmp[2].split(' ')[0] : int(tmp[2].split(' ')[1]),
         }
         line = file.readline().replace('\n', '')
   for sue in data.keys():
      cnt1 = 0
      cnt2 = 0
      for mem in data[sue].keys():
         if data[sue][mem] == results[mem]:
            cnt1 += 1
      if cnt1 > 2:
         print '{} {}'.format(cnt1,sue)


main("16.txt")
