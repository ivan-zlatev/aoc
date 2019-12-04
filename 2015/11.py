#!/tool/pandora64/bin/python

import re

def main(string):
   print 'Old Pass: {}'.format(string)
   newPass = increment(string)
   res = checkValidity(string,newPass)
   while res == False:
      newPass = increment(newPass)
      res = checkValidity(string,newPass)
   print 'Testing: {} Result: {}\n'.format(newPass, res)

def increment(string):
   lettersWeight1 = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
   lettersWeight2 = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f', '6':'g', '7':'h', '8':'i', '9':'j', '10':'k', '11':'l', '12':'m', '13':'n', '14':'o', '15':'p', '16':'q', '17':'r', '18':'s', '19':'t', '20':'u', '21':'v', '22':'w', '23':'x', '24':'y', '25':'z'}
   string = string[::-1]
   chars = []
   for i in range(len(string)):
      chars.append(string[i])
   if lettersWeight1[chars[0]] == 25:
      chars[0] = lettersWeight2['0']
      overflow = 1
   else:
      chars[0] = lettersWeight2[str(lettersWeight1[chars[0]]+1)]
      overflow = 0
   for i in range(1, len(chars)):
      if overflow == 1:
         if lettersWeight1[chars[i]] == 25:
            chars[i] = lettersWeight2['0']
            overflow = 1
         else:
            chars[i] = lettersWeight2[str(lettersWeight1[chars[i]]+1)]
            overflow = 0
   string = ''
   for char in chars:
      string += char
   return string[::-1]

def checkValidity(passwdOld, passwdNew):
   #first check - Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count
   lettersWeight = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
   oldWeight = {}
   newWeight = {}
   correct = False
   for i in range(len(passwdOld)):
      oldWeight[i] = lettersWeight[passwdOld[i]]
   for i in range(len(passwdNew)):
      newWeight[i] = lettersWeight[passwdNew[i]]
   if len(passwdOld) == len(passwdNew):
      for i in range(len(passwdOld)-2):
         if newWeight[i] == newWeight[i+1]-1 and newWeight[i+1] == newWeight[i+2]-1:
            correct = True
   else:
      print '\tDifference in length between old[{}] and new[{}] password!'.format(len(passwdOld),len(passwdNew))
      correct = False
   #second check - Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
   if correct:
      forbiddenLetters = re.findall('i|o|l',passwdNew)
      if len(forbiddenLetters) > 0:
         #print '\t2nd check falure: {}'.format(forbiddenLetters)
         correct = False
      else:
         #print '\t2nd check pass!'
         True
   #third check - Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
   if correct:
      doubleLetters = []
      i = 0
      while i < len(passwdNew)-1:
         if passwdNew[i] == passwdNew[i+1]:
            doubleLetters.append('{}{}'.format(passwdNew[i],passwdNew[i+1]))
            i += 1
         i += 1
      if len(doubleLetters) >= 2:
         #print '\t3rd check pass!'
         True
      else:
         #print '\t3rd check falure: {}'.format(doubleLetters)
         correct = False
   if correct:
      return True
   else:
      return False

inputString = "hepxcrrq"
inputString = "hepxxyzz"


main(inputString)
#main2(inputString2)
