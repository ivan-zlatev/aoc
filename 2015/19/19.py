#!/usr/bin/python

import re

def main(inputDict, inputString):
   #print inputDict
   #print inputString
   dictionary = {}
   updatedStrings = {}
   for tmp in inputDict:
      orig = tmp.split(' ')[0]
      new  = tmp.split(' ')[1]
      if orig not in dictionary.keys():
         dictionary[orig] = [new]
      else:
         dictionary[orig].append(new)
   #print dictionary
   for key in dictionary.keys():
      for value in dictionary[key]:
         iter = re.finditer(key, inputString)
         index = [m.start(0) for m in iter]
         keyLen = len(key)
         for i in index:
            newString = inputString[:i] + value + inputString[i+keyLen:]
            if newString in updatedStrings.keys():
               updatedStrings[newString] += 1
            else:
               updatedStrings[newString] = 1
         print "'{}' found at '{}' and replaced by '{}'".format(key, index, value)
   #print updatedStrings
   print len(updatedStrings.keys())

def main2(inputDict, inputString):
   #print inputDict
   #print inputString
   dictionary = {}
   updatedStrings = {}
   for tmp in inputDict:
      orig = tmp.split(' ')[0]
      new  = tmp.split(' ')[1]
      if orig not in dictionary.keys():
         dictionary[orig] = [new]
      else:
         dictionary[orig].append(new)
   #print dictionary
   for key in dictionary.keys():
      for value in dictionary[key]:
         iter = re.finditer(key, inputString)
         index = [m.start(0) for m in iter]
         keyLen = len(key)
         for i in index:
            newString = inputString[:i] + value + inputString[i+keyLen:]
            if newString in updatedStrings.keys():
               updatedStrings[newString] += 1
            else:
               updatedStrings[newString] = 1
         print "'{}' found at '{}' and replaced by '{}'".format(key, index, value)
   #print updatedStrings
   print len(updatedStrings.keys())


inputDict = [
'Al ThF',
'Al ThRnFAr',
'B BCa',
'B TiB',
'B TiRnFAr',
'Ca CaCa',
'Ca PB',
'Ca PRnFAr',
'Ca SiRnFYFAr',
'Ca SiRnMgAr',
'Ca SiTh',
'F CaF',
'F PMg',
'F SiAl',
'H CRnAlAr',
'H CRnFYFYFAr',
'H CRnFYMgAr',
'H CRnMgYFAr',
'H HCa',
'H NRnFYFAr',
'H NRnMgAr',
'H NTh',
'H OB',
'H ORnFAr',
'Mg BF',
'Mg TiMg',
'N CRnFAr',
'N HSi',
'O CRnFYFAr',
'O CRnMgAr',
'O HP',
'O NRnFAr',
'O OTi',
'P CaP',
'P PTi',
'P SiRnFAr',
'Si CaSi',
'Th ThCa',
'Ti BP',
'Ti TiTi',
'e HF',
'e NAl',
'e OMg',
]

inputString = 'CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl'

#inputDict = [
#'H HO',
#'H OH',
#'O HH',
#]
#inputString = 'HOH'
#inputString = 'HOHOHO'

inputDict = [
'e H',
'e O',
'H HO',
'H OH',
'O HH',
]
inputString = 'HOH'
#inputString = 'HOHOHO'

#main(inputDict, inputString)
main2(inputDict, inputString)
