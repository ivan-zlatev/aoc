#!/tool/pandora64/bin/python

def main(lowerLimit, upperLimit):
   passed = 0
   failed = 0
   for i in range(lowerLimit, upperLimit+1):
      same = False
      incr = True
      s    = str(i)
      #print ''
      #print s
      for c in range(len(s)-1):
         if s[c] == s[c+1]:
            if c == 0:
               #print 'if'
               if not s[c] == s[c+2]:
                  same = True
            elif c == len(s)-2:
               #print 'elif'
               if not s[c] == s[c-1]:
                  same = True
            else:
               #print 'else'
               if not s[c-1] == s[c] and not s[c+2] == s[c]:
                  same = True
         #print c, s[c], same
         if not int(s[c]) <= int(s[c+1]):
            incr = False
      if same and incr:
         #print '[{}] passes the requirements'.format(i)
         passed += 1
      else:
         #print '[{}] failes the requirements'.format(i)
         failed += 1
   print '[{}] passed the requirements. [{}] failed the requirements.'.format(passed, failed)

# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).


# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).

# How many different passwords within the range given in your puzzle input meet these criteria?

main(165432, 707912)
main(112233,112233)
main(123444,123444)
main(111122,111122)
