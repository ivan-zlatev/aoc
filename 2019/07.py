#!/usr/bin/python

import copy

def main(init, inputReg, debug):
   ints = copy.deepcopy(init)
   outputReg = 0
   i = 0
   while i <= len(ints):
      opCode = str(ints[i]).zfill(5)
      if debug:
         print '\t--------------------------------------------------------------------------------------'
         print '\ti={} OP={} ints={}'.format(i, opCode, ints)
      if opCode[-1:] == '1': # ADD
         params = getParams(i, ints)
         outAddr = ints[i+3]
         if debug:
            print '\tAdding {} and {} and writing to address {}'.format(params[0], params[1], outAddr)
         ints[outAddr] = params[0] + params[1]
         i += 4
      elif opCode[-1:] == '2': # MULT
         params = getParams(i, ints)
         outAddr = ints[i+3]
         if debug:
            print '\tMultiplying {} and {} and writing to address {}'.format(params[0], params[1], outAddr)
         ints[outAddr] = params[0] * params[1]
         i += 4
      elif opCode[-1:] == '3': # IN
         ints[ints[i+1]] = inputReg[0]
         if debug:
            print '\tValue [{}] stored at address [{}]'.format(inputReg, ints[i+1])
         inputReg = inputReg[1:]
         i += 2
      elif opCode[-1:] == '4': # OUT
         if len(str(ints[i])) == 1 or len(str(ints[i])) == 2:
            outputReg = ints[ints[i+1]]
         else:
            if str(ints[i])[0] == '0':
               outputReg = ints[ints[i+1]]
            else:
               outputReg = ints[i+1]
         if debug:
            print '\tOutput: [{}] from address [{}]'.format(outputReg, ints[i+1])
         print '\tOutput: [{}] from address [{}]'.format(outputReg, ints[i+1])
         i += 2
      elif opCode[-1:] == '5': #JIN
         params = getParams(i, ints)
         if not params[0] == 0:
            i = params[1]
         else:
            i += 3
         if debug:
            print '\tComparing {} == 0. PC set to {}'.format(params[0], i)
      elif opCode[-1:] == '6': #JIZ
         params = getParams(i, ints)
         if params[0] == 0:
            i = params[1]
         else:
            i += 3
         if debug:
            print '\tComparing {} == 0. PC set to {}'.format(params[0], i)
      elif opCode[-1:] == '7': #JLT
         params = getParams(i, ints)
         if params[0] < params[1]:
            ints[ints[i+3]] = 1
         else:
            ints[ints[i+3]] = 0
         i += 4
      elif opCode[-1:] == '8': #JEQ
         params = getParams(i, ints)
         if params[0] == params[1]:
            ints[ints[i+3]] = 1
         else:
            ints[ints[i+3]] = 0
         i += 4
      elif opCode[-2:] == '99':
         if debug:
            print 'Halting... outputReg = {}'.format(outputReg)
         return outputReg
      else:
         print '\tERROR i= {} OP_Code = {}'.format(i, ints[i])
         i += 1
      if debug:
         print '\ti={} OP={} ints={}'.format(i, opCode, ints)

def getParams(i, ints):
   opCode = str(ints[i]).zfill(5)
   if '1' not in opCode[:-2]:
      a = ints[ints[i+1]]
      b = ints[ints[i+2]]
      #c = ints[ints[i+3]]
   else:
      if opCode[-3:-2] == '1':
         a = ints[i+1]
      else:
         a = ints[ints[i+1]]
      if opCode[-4:-3] == '1':
         b = ints[i+2]
      else:
         b = ints[ints[i+2]]
      #if opCode[-5:-4] == '1':
      #   c = ints[i+3]
      #else:
      #   c == ints[ints[i+3]]
   return [a, b]

#inputData = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
#inputData = [3,23,3,24,1002,24,10,24,1002,23,-1,23, 101,5,23,23,1,24,23,23,4,23,99,0,0]
inputData = [3,8,1001,8,10,8,105,1,0,0,21,38,59,84,97,110,191,272,353,434,99999,3,9,1002,9,2,9,101,4,9,9,1002,9,2,9,4,9,99,3,9,102,5,9,9,1001,9,3,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,102,5,9,9,101,5,9,9,1002,9,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,4,9,99,3,9,102,5,9,9,1001,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99]
debug = False
#thrusters = [0,'']
#for a in range(5,10):
#   aRes = main(inputData, [a,0], debug)
#   for b in range(5,10):
#      if b not in [a]:
#         bRes = main(inputData, [b, aRes], debug)
#         for c in range(5,10):
#            if c not in [a,b]:
#               cRes = main(inputData, [c, bRes], debug)
#               for d in range(5,10):
#                  if d not in [a,b,c]:
#                     dRes = main(inputData, [d, cRes], debug)
#                     for e in range(5,10):
#                        if e not in [a,b,c,d]:
#                           eRes = main(inputData, [e, dRes], debug)
#                           if eRes > thrusters[0]:
#                              thrusters[0] = eRes
#                              thrusters[1] = ' '.join([str(a),str(b),str(c),str(d),str(e)])
#print thrusters

thrusters = [0,'']
for a in range(5,10):
   aRes = main(inputData, [a,0], debug)
print aRes
