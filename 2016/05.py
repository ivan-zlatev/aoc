#!/usr/bin/python

import hashlib
import re

def main(string):
   i = 0
   passwd = []
   for i in range(8):
      passwd.append(' ')
   j = 0
   while True:
      res = hashlib.md5(string+str(i)).hexdigest()
      #print string + str(i), res
      if re.match('00000', res):
         if res[5] in ['0','1','2','3','4','5','6','7']:
            if passwd[int(res[5])] == ' ':
               if j < 7:
                  passwd[int(res[5])] = res[6]
                  print passwd
                  j += 1
               else:
                  passwd[int(res[5])] = res[6]
                  print passwd
                  print ''.join(passwd)
                  break
      i += 1
inputString = 'wtnhxymk'

#inputString = 'abc' #'05ace8e3'

main(inputString)
