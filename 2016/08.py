#!/usr/bin/python

def main(strings):
   xSize = 50
   ySize = 6
   grid = [[0 for col in range(xSize)] for row in range(ySize)]
   #for i in grid:
   #   print i
   #print ''
   for s in strings:
      #print s
      s = s.split(' ')
      if s[0] == 'rect':
         grid = drawRect(int(s[1].split('x')[0]), int(s[1].split('x')[1]), grid)
      elif s[0] == 'rotate':
         if s[1] == 'row':
            grid = shiftRow(int(s[2].split('=')[1]), int(s[4]), grid)
         else:
            grid = shiftCol(int(s[2].split('=')[1]), int(s[4]), grid)
      #for i in grid:
      #   print i
      #print ''
   counter = 0
   for i in grid:
      for c in i:
         counter += c
   for i in range(len(grid)):
      for j in range(len(grid[i])):
         if grid[i][j] == 1:
            print '#',
         else:
            print '.',
      print ''
   print 'ON pixels: {}'.format(counter)

def drawRect(rectX, rectY, grid):
   for x in range(rectX):
      for y in range(rectY):
         grid[y][x] = 1
   return grid

def shiftRow(Y, by, grid):
   grid[Y] = shift(grid[Y], by)
   return grid

def shiftCol(X, by, grid):
   col = []
   for y in grid:
      col.append(y[X])
   col = shift(col, by)
   i = 0
   for y in range(len(grid)):
      grid[y][X] = col[i]
      i += 1
   return grid

def shift(seq, n=0):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]

inputString = [
   'rect 1x1',
   'rotate row y=0 by 5',
   'rect 1x1',
   'rotate row y=0 by 5',
   'rect 1x1',
   'rotate row y=0 by 5',
   'rect 1x1',
   'rotate row y=0 by 5',
   'rect 1x1',
   'rotate row y=0 by 2',
   'rect 1x1',
   'rotate row y=0 by 2',
   'rect 1x1',
   'rotate row y=0 by 3',
   'rect 1x1',
   'rotate row y=0 by 3',
   'rect 2x1',
   'rotate row y=0 by 2',
   'rect 1x1',
   'rotate row y=0 by 3',
   'rect 2x1',
   'rotate row y=0 by 2',
   'rect 1x1',
   'rotate row y=0 by 3',
   'rect 2x1',
   'rotate row y=0 by 5',
   'rect 4x1',
   'rotate row y=0 by 5',
   'rotate column x=0 by 1',
   'rect 4x1',
   'rotate row y=0 by 10',
   'rotate column x=5 by 2',
   'rotate column x=0 by 1',
   'rect 9x1',
   'rotate row y=2 by 5',
   'rotate row y=0 by 5',
   'rotate column x=0 by 1',
   'rect 4x1',
   'rotate row y=2 by 5',
   'rotate row y=0 by 5',
   'rotate column x=0 by 1',
   'rect 4x1',
   'rotate column x=40 by 1',
   'rotate column x=27 by 1',
   'rotate column x=22 by 1',
   'rotate column x=17 by 1',
   'rotate column x=12 by 1',
   'rotate column x=7 by 1',
   'rotate column x=2 by 1',
   'rotate row y=2 by 5',
   'rotate row y=1 by 3',
   'rotate row y=0 by 5',
   'rect 1x3',
   'rotate row y=2 by 10',
   'rotate row y=1 by 7',
   'rotate row y=0 by 2',
   'rotate column x=3 by 2',
   'rotate column x=2 by 1',
   'rotate column x=0 by 1',
   'rect 4x1',
   'rotate row y=2 by 5',
   'rotate row y=1 by 3',
   'rotate row y=0 by 3',
   'rect 1x3',
   'rotate column x=45 by 1',
   'rotate row y=2 by 7',
   'rotate row y=1 by 10',
   'rotate row y=0 by 2',
   'rotate column x=3 by 1',
   'rotate column x=2 by 2',
   'rotate column x=0 by 1',
   'rect 4x1',
   'rotate row y=2 by 13',
   'rotate row y=0 by 5',
   'rotate column x=3 by 1',
   'rotate column x=0 by 1',
   'rect 4x1',
   'rotate row y=3 by 10',
   'rotate row y=2 by 10',
   'rotate row y=0 by 5',
   'rotate column x=3 by 1',
   'rotate column x=2 by 1',
   'rotate column x=0 by 1',
   'rect 4x1',
   'rotate row y=3 by 8',
   'rotate row y=0 by 5',
   'rotate column x=3 by 1',
   'rotate column x=2 by 1',
   'rotate column x=0 by 1',
   'rect 4x1',
   'rotate row y=3 by 17',
   'rotate row y=2 by 20',
   'rotate row y=0 by 15',
   'rotate column x=13 by 1',
   'rotate column x=12 by 3',
   'rotate column x=10 by 1',
   'rotate column x=8 by 1',
   'rotate column x=7 by 2',
   'rotate column x=6 by 1',
   'rotate column x=5 by 1',
   'rotate column x=3 by 1',
   'rotate column x=2 by 2',
   'rotate column x=0 by 1',
   'rect 14x1',
   'rotate row y=1 by 47',
   'rotate column x=9 by 1',
   'rotate column x=4 by 1',
   'rotate row y=3 by 3',
   'rotate row y=2 by 10',
   'rotate row y=1 by 8',
   'rotate row y=0 by 5',
   'rotate column x=2 by 2',
   'rotate column x=0 by 2',
   'rect 3x2',
   'rotate row y=3 by 12',
   'rotate row y=2 by 10',
   'rotate row y=0 by 10',
   'rotate column x=8 by 1',
   'rotate column x=7 by 3',
   'rotate column x=5 by 1',
   'rotate column x=3 by 1',
   'rotate column x=2 by 1',
   'rotate column x=1 by 1',
   'rotate column x=0 by 1',
   'rect 9x1',
   'rotate row y=0 by 20',
   'rotate column x=46 by 1',
   'rotate row y=4 by 17',
   'rotate row y=3 by 10',
   'rotate row y=2 by 10',
   'rotate row y=1 by 5',
   'rotate column x=8 by 1',
   'rotate column x=7 by 1',
   'rotate column x=6 by 1',
   'rotate column x=5 by 1',
   'rotate column x=3 by 1',
   'rotate column x=2 by 2',
   'rotate column x=1 by 1',
   'rotate column x=0 by 1',
   'rect 9x1',
   'rotate column x=32 by 4',
   'rotate row y=4 by 33',
   'rotate row y=3 by 5',
   'rotate row y=2 by 15',
   'rotate row y=0 by 15',
   'rotate column x=13 by 1',
   'rotate column x=12 by 3',
   'rotate column x=10 by 1',
   'rotate column x=8 by 1',
   'rotate column x=7 by 2',
   'rotate column x=6 by 1',
   'rotate column x=5 by 1',
   'rotate column x=3 by 1',
   'rotate column x=2 by 1',
   'rotate column x=1 by 1',
   'rotate column x=0 by 1',
   'rect 14x1',
   'rotate column x=39 by 3',
   'rotate column x=35 by 4',
   'rotate column x=20 by 4',
   'rotate column x=19 by 3',
   'rotate column x=10 by 4',
   'rotate column x=9 by 3',
   'rotate column x=8 by 3',
   'rotate column x=5 by 4',
   'rotate column x=4 by 3',
   'rotate row y=5 by 5',
   'rotate row y=4 by 5',
   'rotate row y=3 by 33',
   'rotate row y=1 by 30',
   'rotate column x=48 by 1',
   'rotate column x=47 by 5',
   'rotate column x=46 by 5',
   'rotate column x=45 by 1',
   'rotate column x=43 by 1',
   'rotate column x=38 by 3',
   'rotate column x=37 by 3',
   'rotate column x=36 by 5',
   'rotate column x=35 by 1',
   'rotate column x=33 by 1',
   'rotate column x=32 by 5',
   'rotate column x=31 by 5',
   'rotate column x=30 by 1',
   'rotate column x=23 by 4',
   'rotate column x=22 by 3',
   'rotate column x=21 by 3',
   'rotate column x=20 by 1',
   'rotate column x=12 by 2',
   'rotate column x=11 by 2',
   'rotate column x=3 by 5',
   'rotate column x=2 by 5',
   'rotate column x=1 by 3',
   'rotate column x=0 by 4',
]

#inputString = [
#   'rect 3x2',
##   ###....
##   ###....
##   .......
#   'rotate column x=1 by 1',
##   #.#....
##   ###....
##   .#.....
#   'rotate row y=0 by 4',
##   ....#.#
##   ###....
##   .#.....
#   'rotate column x=1 by 1',
##   .#..#.#
##   #.#....
##   .#.....
#]

main(inputString)
