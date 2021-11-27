#!/usr/bin/python

def main(strings):
   regA = 1
   regB = 0
   i = 0
   while i < len(strings):
      s = strings[i]
      #print '\nPC: {}\tregA: {}\tregB: {}'.format(i, regA, regB)
      #print s
      i += 1
      instr = s.split(' ')
      if instr[0] == 'hlf':
         if instr[1] == 'a':
            regA = max(0, int(regA/2.0))
         elif instr[1] == 'b':
            regB = max(0, int(regB/2.0))
         else:
            print "ERROR, unknown istruction given: [{}] [{}]".format(instr[0], s)
      elif instr[0] == 'tpl':
         if instr[1] == 'a':
            regA = int(regA*3.0)
         elif instr[1] == 'b':
            regB = int(regB*3.0)
         else:
            print "ERROR, unknown istruction given: [{}] [{}]".format(instr[0], s)
      elif instr[0] == 'inc':
         if instr[1] == 'a':
            regA += 1
         elif instr[1] == 'b':
            regB += 1
         else:
            print "ERROR, unknown istruction given: [{}] [{}]".format(instr[0], s)
      elif instr[0] == 'jmp':
         i -= 1
         i += int(instr[1])
      elif instr[0] == 'jie':
         if instr[1] == 'a,':
            if regA % 2 == 0:
               i -= 1
               i += int(instr[2])
         elif instr[1] == 'b,':
            if regB % 2 == 0:
               i -= 1
               i += int(instr[2])
         else:
            print "ERROR, unknown istruction given: [{}] [{}]".format(instr[0], s)
      elif instr[0] == 'jio':
         if instr[1] == 'a,':
            if regA == 1:
               i -= 1
               i += int(instr[2])
         elif instr[1] == 'b,':
            if regB == 1:
               i -= 1
               i += int(instr[2])
         else:
            print "ERROR, unknown istruction given: [{}] [{}]".format(instr[0], s)
      else:
         print "ERROR, unknown istruction given: [{}] [{}]".format(instr[0], s)
      print 'PC: {}\tregA: {}\tregB: {}'.format(i, regA, regB)


inputString = [
   'jio a, +19',
   'inc a',
   'tpl a',
   'inc a',
   'tpl a',
   'inc a',
   'tpl a',
   'tpl a',
   'inc a',
   'inc a',
   'tpl a',
   'tpl a',
   'inc a',
   'inc a',
   'tpl a',
   'inc a',
   'inc a',
   'tpl a',
   'jmp +23',
   'tpl a',
   'tpl a',
   'inc a',
   'inc a',
   'tpl a',
   'inc a',
   'inc a',
   'tpl a',
   'inc a',
   'tpl a',
   'inc a',
   'tpl a',
   'inc a',
   'tpl a',
   'inc a',
   'inc a',
   'tpl a',
   'inc a',
   'inc a',
   'tpl a',
   'tpl a',
   'inc a',
   'jio a, +8',
   'inc b',
   'jie a, +4',
   'tpl a',
   'inc a',
   'jmp +2',
   'hlf a',
   'jmp -7',
]

#inputString = [
#   'inc a',
#   'jio a, +2',
#   'tpl a',
#   'inc a',
#]

main(inputString)
