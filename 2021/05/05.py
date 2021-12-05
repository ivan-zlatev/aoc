#!/usr/bin/python3

import copy

def puzzle1(inputData, arraySize):
    grid = [ [0] * arraySize for _ in range(arraySize)]
    for points in inputData:
        if points[0][1] == points[1][1]:
            grid = updateHorizontalLine(grid, points)
        elif points[0][0] == points[1][0]:
            grid = updateVerticalLine(grid, points)
    return getOvelappingPoints(grid)

def puzzle2(inputData, arraySize):
    grid = [ [0] * arraySize for _ in range(arraySize)]
    for points in inputData:
        if points[0][1] == points[1][1]:
            grid = updateHorizontalLine(grid, points)
        elif points[0][0] == points[1][0]:
            grid = updateVerticalLine(grid, points)
        else:
            grid = updateDiagonalLine(grid, points)
    return getOvelappingPoints(grid)

def updateHorizontalLine(grid, points):
    for i in range(min(points[0][0], points[1][0]), max(points[0][0], points[1][0])+1):
        grid[points[0][1]][i] += 1
    return grid

def updateVerticalLine(grid, points):
    for i in range(min(points[0][1], points[1][1]), max(points[0][1], points[1][1])+1):
        grid[i][points[0][0]] += 1
    return grid

def updateDiagonalLine(grid, points):
    if points[0][0] > points[1][0]:
        xRange = range(points[0][0], points[1][0]-1, -1)
    else:
        xRange = range(points[0][0], points[1][0]+1, 1)
    yIncrease = points[0][1] < points[1][1]
    y = points[0][1]
    for x in xRange:
        grid[y][x] += 1
        if yIncrease:
            y += 1
        else:
            y -= 1
    return grid

def getOvelappingPoints(grid):
    counter = 0
    for row in grid:
        for col in row:
            if col >= 2:
                counter += 1
    return counter

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    arraySize = 0
    for i in range(len(inputData)):
        tmp = inputData[i].strip().split(' -> ')
        firstPoint = [int(tmp[0].split(',')[0]), int(tmp[0].split(',')[1])]
        secondPoint = [int(tmp[1].split(',')[0]), int(tmp[1].split(',')[1])]
        arraySize = max(max(max(firstPoint, secondPoint)), arraySize)
        inputData[i] = [firstPoint, secondPoint]
    print("\nPuzzle 1: " + str(puzzle1(copy.deepcopy(inputData), arraySize+1)))
    print("Puzzle 2: " + str(puzzle2(copy.deepcopy(inputData), arraySize+1)) + "\n")

readData("test.txt")
readData("input.txt")
