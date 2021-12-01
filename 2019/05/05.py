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
         ints[ints[i+1]] = inputReg
         if debug:
            print '\tValue [{}] stored at address [{}]'.format(inputReg, ints[i+1])
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

inputData = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,57,23,224,101,-1311,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1102,57,67,225,102,67,150,224,1001,224,-2613,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,2,179,213,224,1001,224,-469,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1001,188,27,224,101,-119,224,224,4,224,1002,223,8,223,1001,224,7,224,1,223,224,223,1,184,218,224,1001,224,-155,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1101,21,80,224,1001,224,-101,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,1101,67,39,225,1101,89,68,225,101,69,35,224,1001,224,-126,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1102,7,52,225,1102,18,90,225,1101,65,92,225,1002,153,78,224,101,-6942,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1101,67,83,225,1102,31,65,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1007,226,226,224,102,2,223,223,1005,224,329,1001,223,1,223,108,677,226,224,1002,223,2,223,1005,224,344,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,359,1001,223,1,223,1107,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,389,101,1,223,223,8,677,677,224,102,2,223,223,1006,224,404,1001,223,1,223,1008,226,226,224,102,2,223,223,1006,224,419,1001,223,1,223,107,677,226,224,102,2,223,223,1006,224,434,101,1,223,223,7,226,226,224,1002,223,2,223,1005,224,449,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,1107,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,494,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,1008,677,226,224,102,2,223,223,1006,224,539,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,554,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,584,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,599,1001,223,1,223,1007,226,677,224,102,2,223,223,1005,224,614,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,629,1001,223,1,223,107,226,226,224,102,2,223,223,1005,224,644,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,659,101,1,223,223,107,677,677,224,1002,223,2,223,1005,224,674,1001,223,1,223,4,223,99,226]

debug = False
print 'Test 1 ...'
inputData = [3,9,8,9,10,9,4,9,99,-1,8]
assert main(inputData, 8, debug) == 1
assert main(inputData, 7, debug) == 0
assert main(inputData, 9, debug) == 0
print 'Test 2 ...'
inputData = [3,9,7,9,10,9,4,9,99,-1,8]
assert main(inputData, 7, debug) == 1
assert main(inputData, 8, debug) == 0
assert main(inputData, 9, debug) == 0
print 'Test 3 ...'
inputData = [3,3,1108,-1,8,3,4,3,99]
assert main(inputData, 7, debug) == 0
assert main(inputData, 8, debug) == 1
assert main(inputData, 9, debug) == 0
print 'Test 4 ...'
inputData = [3,3,1107,-1,8,3,4,3,99]
assert main(inputData, 7, debug) == 1
assert main(inputData, 8, debug) == 0
assert main(inputData, 9, debug) == 0
print 'Test 5 ...'
inputData = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
assert main(inputData, 0, debug) == 0
assert main(inputData, 1, debug) == 1
assert main(inputData, 2, debug) == 1
assert main(inputData, 3, debug) == 1
inputData = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
assert main(inputData, 0, debug) == 0
assert main(inputData, 1, debug) == 1
assert main(inputData, 2, debug) == 1
assert main(inputData, 3, debug) == 1
print 'Test 6 ...'
inputData = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
assert main(inputData, 7, debug) == 999
assert main(inputData, 8, debug) == 1000
assert main(inputData, 9, debug) == 1001

inputData = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,57,23,224,101,-1311,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1102,57,67,225,102,67,150,224,1001,224,-2613,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,2,179,213,224,1001,224,-469,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1001,188,27,224,101,-119,224,224,4,224,1002,223,8,223,1001,224,7,224,1,223,224,223,1,184,218,224,1001,224,-155,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1101,21,80,224,1001,224,-101,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,1101,67,39,225,1101,89,68,225,101,69,35,224,1001,224,-126,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1102,7,52,225,1102,18,90,225,1101,65,92,225,1002,153,78,224,101,-6942,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1101,67,83,225,1102,31,65,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1007,226,226,224,102,2,223,223,1005,224,329,1001,223,1,223,108,677,226,224,1002,223,2,223,1005,224,344,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,359,1001,223,1,223,1107,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,389,101,1,223,223,8,677,677,224,102,2,223,223,1006,224,404,1001,223,1,223,1008,226,226,224,102,2,223,223,1006,224,419,1001,223,1,223,107,677,226,224,102,2,223,223,1006,224,434,101,1,223,223,7,226,226,224,1002,223,2,223,1005,224,449,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,1107,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,494,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,1008,677,226,224,102,2,223,223,1006,224,539,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,554,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,584,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,599,1001,223,1,223,1007,226,677,224,102,2,223,223,1005,224,614,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,629,1001,223,1,223,107,226,226,224,102,2,223,223,1005,224,644,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,659,101,1,223,223,107,677,677,224,1002,223,2,223,1005,224,674,1001,223,1,223,4,223,99,226]
print 'First result: {}'.format(main(inputData, 1, False))
print 'Second result: {}'.format(main(inputData, 5, False))