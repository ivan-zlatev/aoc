#!/usr/bin/python

import copy
import re
import math

def main(data):
   arrayData = []
   cycles = 6
   arraySize = len(data) + cycles*4
   print arraySize
   arrayOrigin = arraySize/2
   for z in range(arraySize):
      arrayData.append([])
      for y in range(arraySize):
         arrayData[z].append([])
         for x in range(arraySize):
            arrayData[z][y].append([])
            arrayData[z][y][x] = '.'
   x = z = arrayOrigin
   y = arrayOrigin
   for row in data:
      for i in range(len(row)):
         arrayData[z][y][x] = row[i]
         x += 1
      x = arrayOrigin
      y += 1
   while cycles > 0:
      print cycles
      arrayData = simulateCycle(arrayData)
      cycles -= 1
   activeCubes = 0
   for z in range(arraySize):
      for y in range(arraySize):
         activeCubes += ''.join(arrayData[z][y]).count('#')
   print "Q1: {}".format(activeCubes)

def main2(data):
   arrayData = []
   cycles = 6
   arraySize = len(data) + cycles*4
   print arraySize
   arrayOrigin = arraySize/2
   for w in range(arraySize):
      arrayData.append([])
      for z in range(arraySize):
         arrayData[w].append([])
         for y in range(arraySize):
            arrayData[w][z].append([])
            for x in range(arraySize):
               arrayData[w][z][y].append([])
               arrayData[w][z][y][x] = '.'
   x = y = z = w = arrayOrigin
   for row in data:
      for i in range(len(row)):
         arrayData[w][z][y][x] = row[i]
         x += 1
      x = arrayOrigin
      y += 1
   while cycles > 0:
      print cycles
      arrayData = simulateCycle2(arrayData)
      cycles -= 1
   activeCubes = 0
   for w in range(arraySize):
      for z in range(arraySize):
         for y in range(arraySize):
            activeCubes += ''.join(arrayData[w][z][y]).count('#')
   print "Q1: {}".format(activeCubes)

def simulateCycle(arrayData):
   tmpArray = copy.deepcopy(arrayData)
   for z in range(0, len(arrayData)-1):
      for y in range(0, len(arrayData[0])-1):
         for x in range(0, len(arrayData[0][0])-1):
            True
            #print "Active neighbours: {}".format(getActiveNeighbours(arrayData, x,y,z))
            activeNeighbours = getActiveNeighbours(arrayData, x,y,z)
            if arrayData[z][y][x] == '#':
               if activeNeighbours == 2 or activeNeighbours == 3:
                  True
               else:
                  tmpArray[z][y][x] = '.'
            else:
               if activeNeighbours == 3:
                  tmpArray[z][y][x] = '#'
   return tmpArray

def simulateCycle2(arrayData):
   tmpArray = copy.deepcopy(arrayData)
   for w in range(0, len(arrayData)-1):
      for z in range(0, len(arrayData[0])-1):
         for y in range(0, len(arrayData[0][0])-1):
            for x in range(0, len(arrayData[0][0][0])-1):
               True
               #print "Active neighbours: {}".format(getActiveNeighbours2(arrayData, x,y,z,w))
               activeNeighbours = getActiveNeighbours2(arrayData, x,y,z,w)
               if arrayData[w][z][y][x] == '#':
                  if activeNeighbours == 2 or activeNeighbours == 3:
                     True
                  else:
                     tmpArray[w][z][y][x] = '.'
               else:
                  if activeNeighbours == 3:
                     tmpArray[w][z][y][x] = '#'
   return tmpArray

def getActiveNeighbours(arrayData, originX, originY, originZ):
   activeNeighbours = 0
   for z in range(originZ-1, originZ+2):
      for y in range(originY-1, originY+2):
         for x in range(originX-1, originX+2):
            if x != originX or y != originY or z != originZ:
               if arrayData[z][y][x] == '#':
                  activeNeighbours += 1
   return activeNeighbours

def getActiveNeighbours2(arrayData, originX, originY, originZ, originW):
   activeNeighbours = 0
   for w in range(originW-1, originW+2):
      for z in range(originZ-1, originZ+2):
         for y in range(originY-1, originY+2):
            for x in range(originX-1, originX+2):
               if x != originX or y != originY or z != originZ or w != originW:
                  if arrayData[w][z][y][x] == '#':
                     activeNeighbours += 1
   return activeNeighbours

inputData = [
   ".#.",
   "..#",
   "###",
]
main(inputData)
main2(inputData)

inputData = [
   ".##.##..",
   "..###.##",
   ".##....#",
   "###..##.",
   "#.###.##",
   ".#.#..#.",
   ".......#",
   ".#..#..#",
]

main(inputData)
main2(inputData)

