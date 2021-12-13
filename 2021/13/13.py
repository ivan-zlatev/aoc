#!/usr/bin/python3

from time import perf_counter_ns
import copy

def puzzle1(data, folds):
    maxX = max([x[0] for x in data])+1
    maxY = max([y[1] for y in data])+1
    grid = [ ['.'] * maxX for _ in range(maxY)]
    grid = fillGrid(grid, data)
    for fold, val in folds[:1]:
        if fold == 'x':
            grid = foldGridX(grid, val)
        else:
            grid = foldGridY(grid, val)
    return countDots(grid)

def puzzle2(data, folds):
    maxX = max([x[0] for x in data])+1
    maxY = max([y[1] for y in data])+1
    grid = [ ['.'] * maxX for _ in range(maxY)]
    grid = fillGrid(grid, data)
    for fold, val in folds:
        if fold == 'x':
            grid = foldGridX(grid, val)
        else:
            grid = foldGridY(grid, val)
    for i in grid:
        print(''.join([x if x == '#' else ' ' for x in i]))
    print()
    return "^^^ READ THE TEXT ^^^"

def fillGrid(grid, points):
    for x, y in points:
        grid[y][x] = '#'
    return grid

def foldGridX(grid, X):
    for y in range(len(grid)):
        offset = 1
        for x in range(X, len(grid[y])-1):
            if grid[y][X+offset] == '#':
                grid[y][X-offset] = '#'
            offset += 1
        grid[y] = grid[y][:-X-1]
    return grid

def foldGridY(grid, Y):
    offset = 1
    while offset < len(grid)-Y:
        for x in range(len(grid[0])):
            if grid[Y+offset][x] == '#':
                grid[Y-offset][x] = '#'
        offset += 1
    grid = grid[:-Y-1]
    return grid

def countDots(grid):
    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                result += 1
    return result

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    data = []
    folds = []
    for i in inputData:
        if ',' in i:
            data.append([int(x) for x in i.strip().split(',')])
        elif '=' in i:
            row = i.strip().split(' ')[-1].split('=')
            folds.append([row[0], int(row[1])])
    START = perf_counter_ns()
    result = puzzle1(data, folds)
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 1 result is {} and it took {:.3f} ms\n".format(result, time))
    START = perf_counter_ns()
    result = puzzle2(data, folds)
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 2 result is {} and it took {:.3f} ms\n".format(result, time))

readData("test.txt")
readData("input.txt")
