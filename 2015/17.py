#!/tool/pandora64/bin/python

import re
from itertools import combinations

def main(data):
   total = 0
   for i in range(1, len(data)+1):
      combs = combinations(data,i)
      for comb in list(combs):
         local = 0
         for elem in comb:
            local += elem
         if local == 150:
            total += 1
      print '{}:\t{}'.format(i, total)
   print '{}'.format(total)

inputData = [
50,
44,
11,
49,
42,
46,
18,
32,
26,
40,
21,
7,
18,
43,
10,
47,
36,
24,
22,
40,
]

main(inputData)
