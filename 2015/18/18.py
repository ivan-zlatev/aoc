#!/usr/bin/python

import re
import copy

def main(strings):
   lightsArray = [[0 for col in range(len(strings[0]))] for row in range(len(strings))]
   for i in range(len(strings)):
      for c in range(len(strings[i])):
         if strings[i][c] == '#':
            lightsArray[i][c] = 1
   for step in range(100):
      state = copy.deepcopy(lightsArray)
      state[0][0] = 1
      state[0][len(state[0])-1] = 1
      state[len(state)-1][0] = 1
      state[len(state)-1][len(state[0])-1] = 1
      for i in range(len(state)):
         for c in range(len(state[i])):
            # Get neighbours
            if i == 0: # FIRST ROW
               if c == 0: # FIRST COL
                  neighbours = [0, 0, 0, 0, state[i][c+1], 0, state[i+1][c], state[i+1][c+1]]
               elif c == len(state[i])-1: # LAST COL
                  neighbours = [0, 0, 0, state[i][c-1], 0, state[i+1][c-1], state[i+1][c], 0]
               else: # INNER COL
                  neighbours = [0, 0, 0, state[i][c-1], state[i][c+1], state[i+1][c-1], state[i+1][c], state[i+1][c+1]]
            elif i == len(state)-1: # LAST ROW
               if c == 0: # FIRST COL
                  neighbours = [0, state[i-1][c], state[i-1][c+1], 0, state[i][c+1], 0, 0, 0]
               elif c == len(state[i])-1: # LAST COL
                  neighbours = [state[i-1][c-1], state[i-1][c], 0, state[i][c-1], 0, 0, 0, 0]
               else: # INNER COL
                  neighbours = [state[i-1][c-1], state[i-1][c], state[i-1][c+1], state[i][c-1], state[i][c+1], 0, 0, 0]
            else: # INNER ROW
               if c == 0: # FIRST COL
                  neighbours = [0, state[i-1][c], state[i-1][c+1], 0, state[i][c+1], 0, state[i+1][c], state[i+1][c+1]]
               elif c == len(state[i])-1: # LAST COL
                  neighbours = [state[i-1][c-1], state[i-1][c], 0, state[i][c-1], 0, state[i+1][c-1], state[i+1][c], 0]
               else: # INNER COL
                  neighbours = [state[i-1][c-1], state[i-1][c], state[i-1][c+1], state[i][c-1], state[i][c+1], state[i+1][c-1], state[i+1][c], state[i+1][c+1]]
            if state[i][c] == 1:
               True # stay ON only if 2 or 3 neighbours are ON; otherwise turn off
               if neighbours.count(1) == 2 or neighbours.count(1) == 3:
                  lightsArray[i][c] = 1
               else:
                  lightsArray[i][c] = 0
            else:
               False # turn ON only if 3 neighbours are ON; otherwise stay off
               if neighbours.count(1) == 3:
                  lightsArray[i][c] = 1
               else:
                  lightsArray[i][c] = 0
            #print '\t{}[{}] {} {} {}'.format(i, c, neighbours[0:3], neighbours[3:5], neighbours[5:])
   lightsArray[0][0] = 1
   lightsArray[0][len(state[0])-1] = 1
   lightsArray[len(state)-1][0] = 1
   lightsArray[len(state)-1][len(state[0])-1] = 1
   cnt = 0
   for i in lightsArray:
      print i
      for c in i:
         cnt += c
   print cnt


inputString = [
"#...##......#......##.##..#...##......##.#.#.###.#.#..#..#......####..#......###.#.#....#..##..###..",
"####..#.#...#....#.#####.##.##.#..#.......#....#.##...###.###..#.#.#........#..#.#.##...##..#.####.#",
"...#..##...#.#.###.#.###..#.##.####.###...#...........#.###..##.#.##.#.###...#.#..###....#.###.#..#.",
".#...##...####.#..#.....#..#...#.#.##...#...##..#.#.###....#..###.....##..#.###..###.....##..###...#",
"..##.#####....##..#.#..##.##..######...#..###.######.....#..##...#.#..##..##..#..#..#..##.#.#.#.#...",
".###.###.###...##...##..###..##.###.#.....##..##.#.#########...##..##.#..##.#..##..####..#.#.#.#####",
"#.#####..###.###.##.##.#...#.#.#.#..#.###...#..##.###.#...####.#..#.#.....###..#..####..#.#.#...##..",
"....#...##.....#....####.##.#.###..#.#.##..#.#...##.###.###..#.##..#.#.##..##..#.##.###..#.#.###.###",
"##.##...#.##...#.#..#.#..#...###...###.#..#..#.#####..###.#......#.....###.#####.#.#..#.#.#.##..#.#.",
"#.#..#.....#.....##.#..##...###..##...##...###.#.###.#..#.#.###...##..##..#.###...#.#######.#...#.#.",
"#.#.....####.#..#.##...#.##....#####.###.#.....#####....###..#........##..####...#...#.###....#..###",
"##.#.##..#.#.##.#.....##.#.....###.####.#..######.....####.#.#..##.#.##...#..#.#.....#.####.#.......",
"#..#..#.#..#.######.##..##.####.....##.#.##.#.######..#.#....#.#...#.#..#..#.#.###.#..#.#.#..#...###",
"####..####.#.#.###.....#.#.#.##..#.##.##.##.#..##..##.#.##.....#.#..#.####.....###.#..#.####.#.#..##",
"###.##..##.#.##..#..##...#.#####.##.#....##.####.#.##....#..###.#.#.##...#.....#.#.#.#.#..##.#.#..#.",
"......#..####...##.##...#.##.##...##..#..##.###..#...#..##...#.#....###.####...#.##.###.#.##.####.##",
"..#...#####.#.#..#.##....#..#...#..####.....###...##.###....#..#.###...#........#.#.##..#..#.#.....#",
"#######.#.#.###.###..######.##..#####.##.###.###....####.#..##.##...###.#..############.#.##....##.#",
"#.#...##.###.#.###..#.#.#.#.#.#..##..####.#..##.....#.##..#.##...##.#..##..#.#.#....##....##.#..#.#.",
"..#.#.####.....###..#######.#.#.#.#...##.#####.....##...##...##.###..######.###..#...####.#..###.###",
".#.##....#.#.##..##.#.##.##..######...#.....#..#.#.#.#.....#.#..##.#.#.......#######....#.......#...",
"..###.##.##..##....#.###...#.....##..##......###...##..###.##...##.###.#.#.#.###.###.#.#...###..#...",
".##.#.#...#...##.#.#...#..#..#.#...##.#.##...##..#....#.#..##.#..#.#..#.#.....#..#.#...#######.#.##.",
"...####....#.###.#..###..##...##..#.#.#.###...#..##.##.##..##.#...#..#.##.....#.#........#..#.#.####",
".....##..###...#....#.#.#.#...###.###...#.#...#.#.####....#..####...###..#..######..##.##..###.#####",
"#####.##..#....###.###....##.....#.#..#....#.#####.##.#.####.#.##...#..###...###..##...#.###.#####..",
"###.##..........########.######....####.###.#..##...#.##.####.#.....##..#####..###...#####.....#.#.#",
"##..#####.##.#.#####.#.##.##..#.##....########.#####.#...#.###.##...#.###.#.#..#....##.#..#...#.#.#.",
".##.#....#..#...#..#####..#..##.#......#..#....########...#..#...#.....####.#...##...#.###.#.#..##.#",
".##.##.#.##.#.##...#.#.#..##.##.###.#..##..#...###.##.###.#####.#.###..#..###.#...#.###.#...#..#.#.#",
".#..#..#.#..#..###..#....###.####.##.#.###.#.##.###.#.##.###.###...###...###.#...####...#.##.##.#.#.",
"###..##...###...#..##.#..#.#...##....###.##.##..#####....###..#..#....#..###.###.#...#.##...#.#.#..#",
"#....#.......##.....#.##...#..#.###.#.##..##..#.##..#.###..##.##...#####.#..#####..#####..#####....#",
".####.####....###..###.#.##.####.##.#...####.#.###.#.....#...####..#####.###..#.#.###.##.##...##..#.",
"####..##...##.########...##..###..#..###.##.#.#.#........#.#####.#...#.###.####.#..####..#.#.#....##",
"###.#..#...###.#..#..#.###...##..###.##.#.#...#..#...####..##....#.#..#..##.#.#...#####.###.#..#.#.#",
"...##....#.###.#.#..##...##.###.#..#..#......#...#.#..####.#.##..######.####.#...#..#..#..##.#.#.##.",
"##.####.#...#..#.#.##..##.#.#.###..##...####......#..######.#......#.##.#....##...###.#.#..#......##",
"#.....#...#######.##.#..#.#...###.#..#.####....#.#.##.#.##...###..#...#.###.##..#.###..#.##...#####.",
"#####.##...#..#.#.#.......#.##..#####..#####...###..##.#.#..###.#.#####.####..#.#..##...#.##...#.###",
".##.#..#######.###.#.####.....##...#.##.#.#..#...##....####......######.#..######.....##########.##.",
"##...#.#..#.##.###.#.#.#.##.###.##..##.##.##...#.#..###.#######..#.....#####..#....######.#..##..###",
".#.#.###.....#..##..#.#..##..#.###...###.#..##...#...#.#####.#.#####..###.#..#...##..#.#..#..####...",
".#......##..#.....####.###....##.###.....###.##........#.###.##..#..#.#######.#.######..##..###.....",
"..##.#.#..#.##...#.###.###...######..#..#.#..#....###.#.#....#..........#...##.##.##.#..##..#.#####.",
"###.###.#..#.##..##.#..#..##.....##.....#..#######.#..#.#.#.####.###..###.#.#..#.##.##.####.###.####",
"#.#.#..#....########.#..#..#...##..#.##..#.#..##..####...##.....#.##.#.#...########..#.###.#..#.#.##",
".##.....#...#.#...##.##....###...##..#.####...#..#.#..#..#.##..#.###.##.####.##..####.....##.#.....#",
"....####.#.##.#.##.#..##.#.######.##.####..#...####.#..###.#.#..#..##.#.#.....##.#####.#.####...#.#.",
"#..#####.#####.....##....######..##....#..#.#.###.#####.....##.##.####.#...##...#.##.#.#####.##.#...",
"##.####..###.#....#...#.#.#.#.###.#####.#.####..####...####......##..#..#..#.#.##...########....#...",
".###.#.#.#.#..####.##.#..######..#.#.###.....#.#......#.#.#.#..####.##...##.#####.#.##..##..#..#.#..",
".....###...#...#.####.###.#.#.#.#.....#....#.####.###.##.##.##.#######......#.####......#....##.....",
"##..#..#.#.##..#...#..##.##.##..###.#....##.##....####.#.##.###....#.##.#.#.##...##.###...#..#..####",
"...#.#..##..##.#...##.##...#.#......#.#.##..###....####.##...#.#.###.#..#..#.####..##..##..#####.###",
".##.##..##########.##...#.##.####.#.#######.##.#.##.##..#...##....########.###..##.##.##.#..##.#.#.#",
"#####.#....#.##..#.....#......##.##..#.##.###..##.......###..##.#.###.##.###....####.#..#.###..#.#.#",
".#...#..#.##....##....#...####....#...#..#...####...########.###.#..##.#.#.##..###..#.#.###.....##.#",
"##..##.....###......#..###.##.####.##.####.#.#....#..#...#..#.#..#.###.#...#...#..##.##...#..#######",
".....##..###..##...#####.#.#.....###.#.#..####...#.#.#..#..####..##.#..###.####.#....##..###....#..#",
"#.#.##.#....#.#####.#....##...#...##...##....#.#.......#....#..#...###.###.#.####..####....#.##.#.#.",
"..##...##..###.#.#.##.#..#....#.#.....##.###.#.###.###.....#...#.#..#######.#####..#.###...##......#",
"#......###..#....#.#..#.###.##.#...##..###.####.#.#....#.##..#.###..##.#..#####..##.###.....#..###..",
"##.#.##..##.###.#..##.....#.##.....###....##.####.######.#...#..###....#.#...#.##.....###....#..#.#.",
".##.#.#.#.##..#.#.#..##..#.###.####....#..###.######..####.#.....###.##..#...###.#..######.##.#.##..",
"...##.####.#..##.#####.##.#...##..#..#...#.#.#.#####...#....#..###...#..#....#.#.##.#.######.#..####",
"..#.#.#.#...#.######.#.....#..#.#..###....#.#.########...#....#.#.##..#...##...#.#..#.#.###....##...",
"#####..#..##..#..##..#..#.#.##.#....#####.####.##.#.###..##..##....#.....#.#####.#...#.#####.##.#.#.",
"#.#..#####...####.###.###.....####.###.....##...##...#..#..#######.#.##....##..####.....##...#..#..#",
"#.#.###.#.#..##..#....#.#...#.#.##.##..#.##.....##...#.#..##.......##.#.###..#####.#.##....#.##.....",
"...#.......#....#.#.####.#.###.###..#....#..##.#..####........#.##..#...#.#...###.#..#.#.#...#...#..",
"...##.#####.##.#.###.##.##.#.##..##.#.#.#.#.#.##.#..##...##.#.#..#..##.##.#####.#.###...#####..#..#.",
"#######.#..#..#....##.#.#..####.#..#..###...#..#.......###.#.#.####....#.###...#.#.###.#.#.#.#..###.",
"..##.##.#.##.###....###.##.#.###.#...#....#.####..###..###.#.#..#...##.#.#.#..##.###..###.#.##...###",
"######..######..##..##.#.#.##.##.#..##..#.#.#.##..#.#...#...#.#.#..######.#..#.#.######..#......##.#",
"#.#####.....#.......#########..###.##...#...##.#.#..#...#####...#...#..#.###.#..#.#...###.#.#.#...#.",
"#....##....###...##.##.#...##.........##.#.#..#.#.##.#.######.#####..#..###.###.#...#.#.##.######...",
"#.#...###.#.###.##.#.######.#######.###.##..#.#.#...######.##.####.##..#.#.#.#......##..##.........#",
"..###..##....#.....##...#.#.###.#.#.....##.#...###.####.#...#...##..##.#.#.####..###...######....#.#",
"..###.#.##.####.#..#.##....##..#####....#..##.##.#..#######...#.####...##.#.#.##.........#....#....#",
".##.#...#.####..#.#...#.##..######.##..##.#.###.##..###.###....##..#.##.##..##.#...###.##.##.###....",
"#...###.###.#..#....#.......#..#.....###..#.###.##.##....#.####.#.####.##..##..#..#.....#....##.#.#.",
".##.#..#..#.##.......#.####.#######.....#.##.##.#.....#.#..#....######.#..###.##.##.....#.####..##.#",
"###..#.###.#..####.....##....#..####....#.##.##..#...######.#########...#.#....##...###.#..#.##...#.",
"#..###..##..#.#.##.###.#.#.##...###.#...##.##..#.###....###..#.#...#.###..######.#..#.###..#..#..#.#",
".#........##.#.###..###.#.#.##.....##.##.#.#...##..#.##....###..#.#.#.#.##....#.##..#.#...###...#...",
"####.####..#....#.#.#..#..##.......##.####...###.##..#.#.##.#..##..######.......##.#.##..#...#.....#",
"..#..#..###..##.##..######.#..###..###.#.##..##.#..#####.#.#.#.##..#.##..##.##......####.#..........",
"...##.##..###.#...###....#.#.#.#.....#.##.....##...#...#......####...##.##....##.#..#.####.#..###.#.",
"..#.....####.#.###.#####..#..###..#..#.#...#####...###.###....#.###..#...#..#..#.#..#.##..##.#.#....",
"..##.#####...###.###.........#....##.####.##..#.#..#.#...#...##.##.##..#.#.##.########......#####...",
"...###.#.#..#...#.###.###.......##.###.#..#.##########...#..#.#.#.##.#.###...######..#.#...###.##...",
".#.#.#######.#..##.##..##...#...####...#..#####.#..##...###.#.#...#.##...#......#..##.####..#.....##",
".##.##.#.#......#######..###.....##.#.##..###......#....####...#.###.#.##.#........#..#....##.....##",
"#...#.###.#.##...##.####....#...#.###..#.#.....#.#....#.#.#.##...#.#..#####.#.#..#..#..#....#...####",
".....##...###......#####..##.##.##...##.#.#####..##...#.#.#.#.###...###.##.####..#.#..#.#..#.####.##",
"#..#..##.#.##.#.##.#.#.#..###....###.##.#.##.#...#.#..#...#....###.#..#.#.######.#...####..#..##.#.#",
"#..#.#..#...###.#..##.#...#...##.#......#...#..#..####..##.....#.###...#.#..#.#....#.#####.##.###...",
"###....#.#..#.#..###..#.##......#...#..#..##.#..###..##..#..#.####..#...########..##.#.##.#.#.#...#.",
".#.#.##.##.###..#...#.#....#..#.##..#.#.#.#.##.##.#####...#........####..###..####.#####..#.##.#.##.",
]


main(inputString)