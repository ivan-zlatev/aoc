#!/tool/pandora64/bin/python

import re

def main(string):
   with open(string, 'r') as file:
      data = file.read().replace('\n', '')
   allNum = re.findall('[-]*[0123456789]+' ,data)
   totalSum = 0
   for num in allNum:
      totalSum += int(num)
   print 'Total Sum: {}'.format(totalSum)
   data = eval(data)
   for i in range(len(data)):
      print data[i]


main('12.txt')
#main2(inputString2)
