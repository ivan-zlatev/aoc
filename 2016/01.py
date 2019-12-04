#!/usr/bin/python

def main(string):
   string = string.split(', ')
   coords = { 'x' : 0, 'y' : 0, 'dir' : 'N' }
   visits = []
   for s in string:
      xPlus = 0
      xMinus = 0
      yPlus = 0
      yMinus = 0
      if coords['dir'] == 'N': # last direction was north
         if s[0] == 'L': #turn left
            xMinus = int(s.split('L')[1])
            coords['dir'] = 'W'
         else: #turn right
            xPlus = int(s.split('R')[1])
            coords['dir'] = 'E'
      elif coords['dir'] == 'E': # last direction was east
         if s[0] == 'L': #turn left
            yPlus = int(s.split('L')[1])
            coords['dir'] = 'N'
         else: #turn right
            yMinus = int(s.split('R')[1])
            coords['dir'] = 'S'
      elif coords['dir'] == 'S': # last direction was south
         if s[0] == 'L': #turn left
            xPlus = int(s.split('L')[1])
            coords['dir'] = 'E'
         else: #turn right
            xMinus = int(s.split('R')[1])
            coords['dir'] = 'W'
      else: # last direction was west
         if s[0] == 'L': #turn left
            yMinus = int(s.split('L')[1])
            coords['dir'] = 'S'
         else: #turn right
            yPlus = int(s.split('R')[1])
            coords['dir'] = 'N'
      if not xPlus == 0:
         for i in range(xPlus):
            coords['x'] += 1
            if [coords['x'],coords['y']] in visits:
               print 'Coordinates with double visit: {}, distance from start:{}'.format([coords['x'],coords['y']], abs(coords['x'])+abs(coords['y']))
            else:
               visits.append([coords['x'],coords['y']])
      elif not xMinus == 0:
         for i in range(xMinus):
            coords['x'] -= 1
            if [coords['x'],coords['y']] in visits:
               print 'Coordinates with double visit: {}, distance from start:{}'.format([coords['x'],coords['y']], abs(coords['x'])+abs(coords['y']))
            else:
               visits.append([coords['x'],coords['y']])
      elif not yPlus == 0:
         for i in range(yPlus):
            coords['y'] += 1
            if [coords['x'],coords['y']] in visits:
               print 'Coordinates with double visit: {}, distance from start:{}'.format([coords['x'],coords['y']], abs(coords['x'])+abs(coords['y']))
            else:
               visits.append([coords['x'],coords['y']])
      else:
         for i in range(yMinus):
            coords['y'] -= 1
            if [coords['x'],coords['y']] in visits:
               print 'Coordinates with double visit: {}, distance from start:{}'.format([coords['x'],coords['y']], abs(coords['x'])+abs(coords['y']))
            else:
               visits.append([coords['x'],coords['y']])
   print coords
   print abs(coords['x']) + abs(coords['y'])


inputString = "L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4"
main(inputString)
