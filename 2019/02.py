#!/tool/pandora64/bin/python

import copy

def main(init):
   i = 0
   init[1] = 12
   init[2] = 2
   ints = copy.deepcopy(init)
   for noun in range(100):
      for verb in range(100):
         i = 0
         ints = copy.deepcopy(init)
         ints[1] = noun
         ints[2] = verb
         while i <= len(ints):
            if ints[i] == 1:
               #print 'Adding {} and {} and writing to address {}'.format(ints[ints[i+1]], ints[ints[i+2]], ints[i+3])
               ints[ints[i+3]] = ints[ints[i+1]] + ints[ints[i+2]]
            elif ints[i] == 2:
               #print 'Multiplying {} and {} and writing to address {}'.format(ints[ints[i+1]], ints[ints[i+2]], ints[i+3])
               ints[ints[i+3]] = ints[ints[i+1]] * ints[ints[i+2]]
            elif ints[i] == 99:
               #print 'Breaking... Result: [{}] noun: [{}] verb: [{}]'.format(ints[0], noun, verb)
               if ints[0] == 19690720:
                  print 'Breaking... Result: [{}] noun: [{}] verb: [{}]'.format(ints[0], noun, verb)
               break
            else:
               print 'ERROR i[{}] ints[i][{}]'.format(i, ints[i])
            i += 4

inputString = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0]
#inputString = [1,0,0,0,99]
#inputString = [2,3,0,3,99]
#inputString = [2,4,4,5,99,0]
#inputString = [1,1,1,4,99,5,6,0,99]
main(inputString)
