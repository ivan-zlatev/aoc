#!/tool/pandora64/bin/python

import hashlib

def main(string):
   i = 0
   while True:
      res = hashlib.md5(string + str(i)).hexdigest()
      if res[0] == "0":
         if res[1] == "0":
            if res[2] == "0":
               if res[3] == "0":
                  if res[4] == "0":
                     print "{}   {}   {}".format(string, str(i), res)
                     break
      i += 1

def main2(string):
   i = 0
   while True:
      res = hashlib.md5(string + str(i)).hexdigest()
      if res[0] == "0":
         if res[1] == "0":
            if res[2] == "0":
               if res[3] == "0":
                  if res[4] == "0":
                     if res[5] == "0":
                        print "{}   {}   {}".format(string, str(i), res)
                        break
      i += 1

inputString = "iwrupvqb"

main(inputString)
main2(inputString)
