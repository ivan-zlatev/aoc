#!/usr/bin/python

import copy
import re
import math
import os
from time import sleep

gridSize = 300
grid = []
for q in range(gridSize):
   grid.append([])
   for r in range(gridSize):
      grid[q].append('.')
gridOrigin = gridSize/2

def main(data):
   global grid, gridOrigin, gridSize
   #evalTilePath(gridOrigin, gridOrigin, [])
   for row in data:
      evalTilePath(gridOrigin, gridOrigin, splitTilePath(row).split(' ')[:-1])
   result = 0
   for q in range(gridSize):
         result += grid[q].count('#')
         #print ''.join(grid[q])
   print "Q1: {}".format(result)
   sleep(1)
   for i in range(100):
      changeDay()
   result = 0
   for q in range(gridSize):
         result += grid[q].count('#')
         #print ''.join(grid[q])
   print "Q2: {}".format(result)

def changeDay():
   global grid, gridSize
   oldGrid = copy.deepcopy(grid)
   for q in range(1, gridSize-1):
      for r in range(1, gridSize-1):
         inverted = getNeigbours(q, r, oldGrid)
         if oldGrid[q][r] == '#':
            if inverted == 0 or inverted > 2:
               grid[q][r] = '.'
         else:
            if inverted == 2:
               grid[q][r] = '#'

def getNeigbours(q, r, grid):
   inverted = 0
   if grid[q+1][r] == '#': # e
      inverted += 1
   if grid[q][r+1] == '#': # se
      inverted += 1
   if grid[q-1][r+1] == '#': # sw
      inverted += 1
   if grid[q-1][r] == '#': # w
      inverted += 1
   if grid[q][r-1] == '#': # nw
      inverted += 1
   if grid[q+1][r-1] == '#': # ne
      inverted += 1
   return inverted

def evalTilePath(q, r, directions):
   global grid
   if len(directions) == 0:
      if grid[q][r] == '.':
         grid[q][r] = '#'
      else:
         grid[q][r] = '.'
   else:
      if directions[0] == 'e':
         return evalTilePath(q+1, r, directions[1:])
      elif directions[0] == 'se':
         return evalTilePath(q, r+1, directions[1:])
      elif directions[0] == 'sw':
         return evalTilePath(q-1, r+1, directions[1:])
      elif directions[0] == 'w':
         return evalTilePath(q-1, r, directions[1:])
      elif directions[0] == 'nw':
         return evalTilePath(q, r-1, directions[1:])
      elif directions[0] == 'ne':
         return evalTilePath(q+1, r-1, directions[1:])
      else:
         print "ERROR, Unknown direction: {}".format(direction[0])

def splitTilePath(path):
   if re.match("^(se)|(sw)|(nw)|(ne)", path):
      path = path[:2] + ' ' + splitTilePath(path[2:])
   elif re.match("^[ew]", path):
      path = path[:1] + ' ' + splitTilePath(path[1:])
   return path

inputData = [
   'sesenwnenenewseeswwswswwnenewsewsw',
   'neeenesenwnwwswnenewnwwsewnenwseswesw',
   'seswneswswsenwwnwse',
   'nwnwneseeswswnenewneswwnewseswneseene',
   'swweswneswnenwsewnwneneseenw',
   'eesenwseswswnenwswnwnwsewwnwsene',
   'sewnenenenesenwsewnenwwwse',
   'wenwwweseeeweswwwnwwe',
   'wsweesenenewnwwnwsenewsenwwsesesenwne',
   'neeswseenwwswnwswswnw',
   'nenwswwsewswnenenewsenwsenwnesesenew',
   'enewnwewneswsewnwswenweswnenwsenwsw',
   'sweneswneswneneenwnewenewwneswswnese',
   'swwesenesewenwneswnwwneseswwne',
   'enesenwswwswneneswsenwnewswseenwsese',
   'wnwnesenesenenwwnenwsewesewsesesew',
   'nenewswnwewswnenesenwnesewesw',
   'eneswnwswnwsenenwnwnwwseeswneewsenese',
   'neswnwewnwnwseenwseesewsenwsweewe',
   'wseweeenwnesenwwwswnew',
]
#main(inputData)

inputData = [
   'seseswnwseneweseswseswnwnese',
   'neneeneseneeeesenewwne',
   'swswswneswsewswseswesewswseswneeswswnwsw',
   'eneeswnwneneenwneneneeneneswnwneswne',
   'seeseseeeeseenenenwswseweese',
   'seswweseseseswseswneswwnwswswseneswnw',
   'wswseswswneeswswsw',
   'wnewnwnewwwwwwwwwsewwsw',
   'wseswnenwneswwnwseeenwnwnwewesewse',
   'seweseseneeeseeswsenwseeenwseeeew',
   'seswswnwswswswnesesesewseeneseswsesesesw',
   'wsenewsenwwnewswwewnwnwsewwwsw',
   'swwwnewnwwseswswnwswenwswseeswesw',
   'senenwswwnwnewwseseseswswwweneswwne',
   'nwseseeeesweee',
   'swwswswswwswswsweswnwwswsw',
   'sewnwswneneneenenewneeneeneneswwee',
   'swenenwswnwnenwnwnwenwnenesenwnenwnwnwwnw',
   'eweeneswnesenesewneneeeneseneneew',
   'enesesenwsweeeeeenwnwnwsweswew',
   'nweeeswneswenwseswnweeeneenenesw',
   'neeeswnwnenwnewnwnwswenwwwnwsesenw',
   'neswnwenwneswnwnwnwneswnesenwnw',
   'neeseeweneeswweeswneneneeneenenw',
   'nenwnenwnenwewnewsenwnwnwnwnene',
   'nwewnwnwwnenwnwwnwnwwnwwenwnwsenw',
   'seseswsewneswseseseseseswwseseswe',
   'eseswnewenwwnenene',
   'wswneneswswsewnwseswswswseswswwwswswne',
   'neeswneneewnenenenenwnewneeeneneswse',
   'eneeneneneneeeneneenewsene',
   'eneweewwsenesene',
   'nwenwenwnwswnenwsenwnesenenenenwnesw',
   'wesenesenewweewwwswwnwsew',
   'eeswneeewsewneneneweneeneene',
   'eeswswswnwweswnenwsw',
   'swesewnwneswseesesesesesenwsenwesee',
   'enwsenwnwswnwwnwseseseseeswewnesenw',
   'eeseeeseenwseenweeeenwesese',
   'nenwnwswneneswneenenwneneswnenwnwnwnenee',
   'ewswwswwswewwnwwenww',
   'swnenenwnenenenesenenesewnenwnenwesenesw',
   'nwseeenwnwwnwnwenwswnwswnwnwneenwnew',
   'ewwnwwwwnwswnwnenwsenwnwewnwww',
   'eswwwseewsewweeswwnwnwwenwwwne',
   'wswseswswswnenwswwswswnewswswse',
   'nwnenwseseswsesesenwseseseweswew',
   'swesweenenwnwnenwnenwwneneseenenwsw',
   'wswwwswneswwwswwewnenwswwwew',
   'wsewwwnwwwwnwsenenewnwewwsw',
   'wswswwesweswnwswwwswswsweswswswsw',
   'eswswwnwwswsesweswswswneswswnwnwsesw',
   'neenwsewwswneseswwseswnwwwwswww',
   'enwseweseseseeswseneneseswseswneee',
   'swnwswswneseswswswsesewseseneneseswsee',
   'wsenwwswwwnwswwwwneswewwneww',
   'nweswsweeewnenesee',
   'swsweswnwswseneswswswseswswswsw',
   'swsewseswseeseneeswswwswswnenenwnesesw',
   'seeeenenewenenenenesew',
   'nwnesewsesesenwsesenwsenwnwnenwnenwnww',
   'enwswsewnesesesenwe',
   'nwnwnesenwwwwnwnw',
   'nenesenewneenenenenwswneenesenenwnewne',
   'wnwnesenenwesewsenenenenwneeeneswse',
   'wwswswswswswswwswwswesww',
   'enwsesesewseeesweneeeswesesweenw',
   'wwnwseneneneeenewswnwnwneswsenewnwsenw',
   'swswswswswswewswswwswsww',
   'nenwwnenwsenwnwswseswnwneneseseesenww',
   'seeseeseeeesenewseswweseseswnenese',
   'wwsewwwewneeswnwwwewwwenesw',
   'wenewseeeneneenenenenenwswswnenwnee',
   'neswnwnwesesenwswewneewsenwesweswswse',
   'nesweewswsewswnesewnewswwwwwsw',
   'nwneeeneseneneeneswenenwswnewsenwe',
   'swswswswnwswwswswesweeesenwswwswse',
   'senenwewnenenenenwnwneneswneenenenewne',
   'senwseneesweeesenenwseseseneewwe',
   'ewwwwwnesenesenwnwsewsesenenewswnw',
   'sewswswswseneswseseswseswneswswse',
   'eenwneneeeeeewswneseneeew',
   'swwwwseswswnweswwnwenenweenwseeene',
   'eeneeeeswnwneseenwesweeenweee',
   'enwwwwnwnwwwnwnwneseswswnwnwnwwenwnw',
   'wwwswswswswwswewswsw',
   'swwwwnesewswewwswneswseenw',
   'seeneeeeeweeeseee',
   'swneswwnwsenweswnweswswnwseeseseseswnw',
   'swswseswnwswswsweseswnwswswswneswsesew',
   'neneswswwwwwswwnwswswwswsesweswsesw',
   'sweneswnesenenwnenwesenewnwnewnwwene',
   'nwnwnenenwwnesweeswnwswseseneseewnw',
   'nenwnenenwneneneswneneenenwswnenw',
   'nwseswseswwwswnwneswswwswwwwswnese',
   'esenwenwnwwnewnwnwneswnwnwwnwnwnwnw',
   'wwwswsenwwswwwwwwnwnwwsewwe',
   'wesenweneeeseswseeneswswnenwwesw',
   'swswnwseseswsenwnenwnwseewweswswseene',
   'swswnewswswneswswswsenwweswwswswswsww',
   'eswwnenwnwneewenweswswnewweswese',
   'seneenwsewwnwnee',
   'swswswswsenwsweswswswenwswsenwswsesesw',
   'nwnweenwnwnenwnwneswswnwnwsenwnwnwnwnwne',
   'wnwwnwwwwwwsew',
   'nwswnwnwnenenwnwnwswnwseneswnwnwnwne',
   'newwneeeswseneeneneneneweeeenene',
   'eeenwnwneeeeeeesweenwswwseew',
   'esenewwwwnwswswswswwwnwswswswww',
   'eeweeeseseeesee',
   'wewwnenewswwneseswwnwwwseswswww',
   'wweenenewswswnwwewwswwwswswsww',
   'seseeswneesewnwsenwsesesesenwwswnwsee',
   'nwnwnenwnenwnwnwsesenwnwnwwnwnenenwnwse',
   'eswswseseswwswseseswswnweseswenwsesw',
   'eeseneneeesenenwswwweewneenene',
   'swsenwwswnwnwnwswnwenweneswneeneswnw',
   'nenwenenewseneweewswneenesweene',
   'swwwwwwwnwswew',
   'seesenwesesesewnwsenweseseswseswsee',
   'nenenwnwnenewnwnwnenwseswnwnwnwnenwseswse',
   'neneeeenwwweseseswewseesenwswnw',
   'enewesenenesenwwsesweneeneeneenenee',
   'seeeeeneewseewseseeeeesesewnw',
   'wwswswswswwwnwwewswsw',
   'wswnwnenweswnwnwnwnwnwnwsenwewse',
   'nwnwnwnwswnenenwenwenwnwneseswnwnwnenwne',
   'ewswswswwnwswswwswnwswswswswwwsesenwne',
   'wnwsenesenwsenwesewewseswnwnenwneswne',
   'nesweenenwneeneseeeneneseenewneenw',
   'nwswswswesenwsenwesweseswsewswesenwsw',
   'sweswneneeneswnwesenwwnwseeseswwnw',
   'enwnwnwnwnenwnwnwnenwwnwesewnwnwsenwnw',
   'eneseweeeneneneswwseneswweswswsw',
   'swswwwseneeseeewnwwseswnwswenwneswnw',
   'senewwswsesenewnwseseswswswneseneswsesw',
   'swnwnwnenwsenwsenwnwsenwnwwnwnwew',
   'seseseseswneesenweseeseswsesenwsewsese',
   'eewweeneneswswenenweneneeeesw',
   'ewneneeeseeeneneesweswenweswene',
   'wseeneseeswnwwesesesenwnwwsesee',
   'sesesesewseseneseseswnesesesenwsesenwse',
   'seseswseneneewseseseseseseesesee',
   'swswsesenwneeseswsesesesesesesew',
   'nenwseswswnesenewwnwenwseeeeneneenene',
   'neswneswswnewnwswnwseneeneneenwenwne',
   'swnwnwnwnwnwseenewnenenwnwnwnweewnwnw',
   'swnwnewnwwnwnwwnewswwsewwnwswnewew',
   'nwnenwswnenwnwnwnenesenwsenenwnenenesenwnw',
   'nenwewseswneweesweseeenweswswnw',
   'swsweswseeswwswswswneswwwnwnwswnwse',
   'swwwswwsewenewsewswswwnewnwswnw',
   'swenenwnweswnwswwswwwnwweswnewnw',
   'nwnenwnwnwnwwenenwnwsenenewenwnwswnesw',
   'neesewswnwswseswnwenenwwswswswswewse',
   'seseseseeeseseseswnw',
   'swswenwswnenwnwnenwnwnwsenenwnwnenenwnwnew',
   'wseseeeseseneseswesesesesese',
   'seswseseseseswneswnwwseseseswesw',
   'nwnwnwnwenweswsesenwswnwnwnwnwnwewswnwne',
   'swneneenenwnenenewneneeweeeeswnese',
   'wwnwnewwwwwswwww',
   'eseeeseeeeenwewseenwesenwwse',
   'seswseswneswseswswswwseswsw',
   'wneswseswswnwswneseswsweswneswwswswsesw',
   'wswwnwnwnwnwnesweswseswseswenwwswew',
   'neeeeswneeswnweeeeeeesweee',
   'neswswnwswesenwsenesenwsewseewswswne',
   'newseesesesenwsenwewsewsese',
   'sewseenwseseseswseseeswseseseneenwse',
   'weseneeeeeesewneseneeswewsew',
   'wswnwnwsewnwnwenwewwnwsesenwnenwnwnw',
   'senenenenenewnenwnwse',
   'seseseseseswsesenesesesesewsenwseneese',
   'swwneewwneswsewseseeneenwsenenese',
   'swnwnwneswseswsweswewneswnewnweseswsw',
   'swswswswseeswswnwseswswnw',
   'nenwseneenwneneenwneneneswseseeneswenw',
   'swneswswwswswseswswswswnweswewswswe',
   'swnenenwneswenenewnwnwnenenenese',
   'nwswswnewseswnwswnwwwesweeswesese',
   'nwenwnwnwnenwnwnesenwnwnwswnwnwsesenese',
   'sweewwnwswesewnenwswww',
   'eweneeswwswneeneeeseesenenwnee',
   'nwnwnwnwsewnwenwnwnweswwwnenwnwee',
   'seswswswwswnwwseneswswswswneswwswnene',
   'newnenenwnesenenesewneswnenwnwnwnenwne',
   'sewnenenenwneeswwenwneswnese',
   'swnwnwwnwnwnenwenenesenewneeswnenene',
   'swnenenesenewneneswsewwwwneesesee',
   'wewneneeneneswwwsenenesene',
   'wenwswswswnwwenwwwwenewnwnwwww',
   'wwewseswwwswswwwnewnewnwnwwwne',
   'swswwswswnwswnwswseswswswnwswswswseeswne',
   'wewswnweneeseseeweeeewwsene',
   'swsewwsenwseswewneswsesee',
   'seseswnwneneseesesesesesesenweewsesese',
   'seseseseswnesesesenwswsesew',
   'swnwseswewseswswswswswse',
   'wwesenwnwnweswswnwneewswnwneewse',
   'nwnwnwnwnwnesesenwnwsenewnwnwnwnwnwnwnw',
   'wswwwnenwswseswewwswswwnwwswswsw',
   'senenenewnenesenenenenenwenweese',
   'swneneeneswenewswnenwnweneesee',
   'neenenewneeewneneswseneseneneneene',
   'swnewswswsenwwswseswnweswswnwsweswsw',
   'ewwnwenwwwsewnwnwnwsesw',
   'seswseswswswseswsesenwsese',
   'neneswnweeeeeneeswwnwswseee',
   'swnenwnenwnwneswenenenwnenenweneneswnee',
   'nenenwnwneneneneswnenenwnwsenwnewesenwwe',
   'wwnwnwnenwwwwewseeswwwnwnwswnwnw',
   'neneeneeeeneneeeeewe',
   'nwneswweswswnesweesenwswswswswsesewse',
   'seewseneseneseseseswswewseeseenwsee',
   'nwswseswswseseswseswseswse',
   'swseewnwseswwwseeswswnesewneneese',
   'nwneeseeeneeeeeeee',
   'wwswenwwnwnwwwsenwwwwwnwsenew',
   'weneneneeneneswne',
   'nenwswneswswwswwwwwswenewwsesewsw',
   'sesesenenwneswwenesenewesweswseeenw',
   'sweewswwnwenwseseseenwsesw',
   'enwneenwewsenwnwwsewwwsww',
   'nwnweseneswneeneneneweswswwneseswnese',
   'nweseswneeseenwnenenesesenwenenenwwe',
   'nwwnwnwsenwnwnwenenwnwnwsenwswnwsenwwnw',
   'wewwwwseswnwsewwwnenwwwwsenesw',
   'seswseswswswswseseswnwswswesw',
   'sweswwnewneneneneneseneneneenwenene',
   'swwnwswswwwewswswenwwse',
   'senwenwnwwnwesesenwwnwnwnenwsenwnwnwne',
   'seseeeweseswwnenwsenesewnweseeese',
   'nwwewwnwnenwswnwsewswwnewenwnwnwnw',
   'eesweesenweewneeeeenwsweene',
   'newswesenwnewswneswswswseswswnwswnesw',
   'sesesewwsesewseseneeswsenesesenesese',
   'nwnwwswnwnenwwnwwnwnwneseswesenwswnwse',
   'wwnesewnwnesesewsewnwwneneswse',
   'eeweneeneweneeseeewneeeene',
   'neneswnenwnenenwnenenwnwnwene',
   'wwwseswswneenewseswseswwswnenesese',
   'nwnwnwnwseswwnwswnwnwsenwnwsenwsenenwnee',
   'newswswwwwseseneswwswswnewswwww',
   'seseseseneseseswswswseseesenesesewswnwse',
   'eeseswweseeenwsenesesesesesewsesee',
   'neenenenenenwnweesenwesenwenesenesee',
   'nwnwnwnenwswnwnwsenwnwnwnenewnwnw',
   'seswnewswswswswnwe',
   'eswnewneeneneneenenenwnenewnwewswse',
   'wnewnenenwnwseneneseswsewenwsesenwwwse',
   'eeseseweneseseewnesewnesesesenw',
   'seeneeeewseeeneewsesweeseee',
   'seseseswswsenwneeswnwswseseseswseswswnese',
   'sewwswswseneswnwwwwswwne',
   'nwnwnwnenwnwnwwnwnweswnwnwswenw',
   'seswnwseseswnwnwseseenenw',
   'newsewswnwwwneswsewneeeseswnwwenenw',
   'neneeswnenenewseesenewe',
   'seswneswsesewseeswse',
   'sesenwnewneneeeneneneenenenesewnenenenw',
   'wwneneswewswswsew',
   'sewwwnwnwnwwsenwnenwsesenww',
   'nwwnwnenenwwnwwswswswewseneesenewwnw',
   'eeswswneneneneeneeeeseeewneee',
   'wsewswwwnenwswnwswwsenenwenenw',
   'nwwnwwwwnwewnewwwsenwswwswenwne',
   'swsenesenwsesesewseswneeseseseseswsenw',
   'wswswswseeswswswswnwswneweseswswswswnw',
   'wnwnwwnwnwwnwnwwnwwswnwwenwwese',
   'swseesenwswnwsenwswsweeweenwneeenene',
   'neswnenewneneneneneneneneswnesenenesew',
   'wnwneenenewnenenesenwne',
   'senwnwseenesewseswwseswsweswsenenwsee',
   'nwnwnwwnwenwsweswwnwseenwwnwnwnwnw',
   'neseneneneswnwswsenewnewneenwsewnenenese',
   'nwseseswwswseesenesenese',
   'swsenwsewwneesewweswnenwneenwwnwse',
   'eswswwswnenewseseswnwseswswnewswswsesw',
   'wewneseeswwwnwneewnwswwswswwsesw',
   'swseeewseswwswswneswswnwswsw',
   'seewswwswwswsenwnwswwswnewswswswsww',
   'seswswswsesesenewswswsenwswswswneswswsw',
   'enwwwwswswwwswsewswnwnwseeswnwwsw',
   'seneseneswseswseseswwwsweseswnwesesese',
   'eswnesweswswswswnwswswswswwwsw',
   'eeeeweeseseneewe',
   'swnenwenwnwnenesewwswnwnwnwnwne',
   'seswneswswwwsewenewwswwswwwww',
   'seswseseswswswswswsenwsesenwneeewseswswse',
   'wwnwnwwwenwwnwnww',
   'seswseeseeseeneesesesewnese',
   'wnwnwwnesewwwswewsesewnwewwe',
   'swnwseswswswnweswneweswswswswswswnesw',
   'swseseseseseswswseswne',
   'nwswwwwnwswnwsesewenewwsesenwnenw',
   'swwnwsweeewnwnwwsweseswsw',
   'nwnwnwnweswnwsenwnwnwnwnwnwnwnww',
   'eswnenwswnwneeneee',
   'enweneeeeeeesenenee',
   'nwwnwweneeseenenenwnwnwwswswnenenw',
   'eeeneseesweeeewenwesweeee',
   'swswnewswwsesenwwswswwwwewneswswnesw',
   'seseseseseseseesesewesesewe',
   'neswwwwwneswwswwwwsewneneww',
   'wsewwwwwwnwnwnwwnwnww',
   'nenwneneneneneseneneenenenewneswnwesene',
   'swnwseseswswswseweswsweswswnwnesewseesw',
   'weswswneswseewwnwnwneseesese',
   'eewwnwnweswww',
   'swwwwwwwswsewwewswnewwneww',
   'senesesesenwnwnwnenewsenwnwnewnw',
   'nwnenwnwnenenwewseenwnwnenwnwwnewnw',
   'wwwweswwseneneseenwseswnwwnwwwnw',
   'nwnwwswnenwnwnwwwseewswnwnenweww',
   'neswnwnewneneeneneneneneneneneseswnesene',
   'eeenwewseeenwsewnwsewe',
   'nwnwwnwwnesenwnwnwnwnwnwsenwnwswnenwnw',
   'nwseswswswnewnenwnwneneenenwwneneeesw',
   'nwnwnwnwwswsenweenwnweenwnwnwswnwnww',
   'nwesweeeeenweeseweeeeewee',
   'swseseswseswswswswnwnwswswsweneswswsese',
   'swesesweeswswswnwwswswswsewse',
   'wswswweseswswswenwswnwswswnwwwwsw',
   'wsesesesenwswswnwseseseeseseesesesese',
   'wsenewwwwwwwwnewsew',
   'ewswwwwswwwwwnwweswww',
   'enwwnwnenwesewne',
   'wswswseswsesesenesesesese',
   'swseseseswseseseswswnewe',
   'swswnwnenenwswneneneneenenenenenwswnenw',
   'eneeseeseenewseeseewe',
   'nwneseswswswswswnwswswswswwneeseswswne',
   'swswsesesesenwseseesenew',
   'newnwsenwsenenwnwnenwnwnwnesenwwnwnw',
   'eneenenewwneneneneneneseneenesene',
   'wnwseweeenwswsewwneswwneenewewe',
   'nwnwnwwwnwwneenwsenenwseswnwswwnwnw',
   'nwnwswneneswnwnwnenwwnweswswwnwnenwnw',
   'neneenweseswseeewneweneenweseee',
   'eeneweseeeeenwsenweneeeeswswe',
   'ewsewswnwwwwnwneewseswneenewswwe',
   'eeweeesweeeneeeeswswseenwnwee',
   'nwnweswswsewwsenesweswwnwnwenwswe',
   'wwewwsesenwswnwwsenwnenwwnwsewwnw',
   'eewsewwnewwwwneswwwswswswww',
   'enwewswesenweenwneewseswseeee',
   'sesenewswwwweneneseeswnwnenwneee',
   'nwewnwsewnwnenwwnewwse',
   'eseeseseeesesesenwseneswneneswesew',
   'wswwseenewswenwwweswswnenww',
   'neseswseseeswswswwswswnwsenwsweseswswse',
   'eeswwenwnenwneeweseweswneswene',
   'nenwnenwnwnwneneswnenenenwneenenwswseswnw',
   'swneeeeseenweneseeweswneesenwenwsw',
   'nwnwnwsenwwnwsenwnwne',
   'newwnwsenwnewsewswnenwswwenenwnesese',
   'senwsenwnesenwnewnenwne',
]
main(inputData)

