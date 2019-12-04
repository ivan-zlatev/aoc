#!/usr/bin/python

def main(string):
   res = lookAndSay(string, 40)

def lookAndSay(string, recCounter):
   if recCounter == 0:
      return string
   else:
      data = [ [string[0], 1] ]
      counter = 0
      #print data
      for i in range(1, len(string)):
         if string[i] == data[counter][0]:
            data[counter][1] += 1
         else:
            counter += 1
            data.append([string[i], 1])
         #print data
      outString = ""
      for i in range(len(data)):
         outString = outString + str(data[i][1]) + str(data[i][0])
      recCounter -= 1
      print '{}\t{}'.format(recCounter,len(outString))
      lookAndSay(outString, recCounter)

inputString = "1321131112"

main(inputString)
#main2(inputString2)
