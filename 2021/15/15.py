#!/usr/bin/python3

from time import perf_counter_ns
import copy
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

def puzzle1(data):
    grid = Grid(matrix=data)
    start = grid.node(0,0)
    end = grid.node(len(data)-1, len(data[0])-1)
    finder = AStarFinder()
    path, runs = finder.find_path(start, end, grid)
    print('operations:', runs, 'path length:', len(path))
    print(grid.grid_str(path=path, start=start, end=end))
    return getPathCost(data, path[1:])

def puzzle2(data):
    for y in range(len(data)):
        xRow = data[y].copy()
        for yRepeat in range(0, 4):
            for x in xRow:
                data[y].append(((x+yRepeat)%9)+1)
    origData = data.copy()
    for yRep in range(0, 4):
        for y in range(len(origData)):
            data.append([])
            for x in origData[y]:
                data[len(data)-1].append((x+yRep)%9+1)
    grid = Grid(matrix=data)
    start = grid.node(0,0)
    end = grid.node(len(data)-1, len(data[0])-1)
    finder = AStarFinder()
    path, runs = finder.find_path(start, end, grid)
    print('operations:', runs, 'path length:', len(path))
    #print(grid.grid_str(path=path, start=start, end=end))
    return getPathCost(data, path[1:])

def getPathCost(data, points):
    result = 0
    for x, y in points:
        result += data[y][x]
    return result

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    data = []
    for i in range(len(inputData)):
        data.append([int(char) for char in inputData[i].strip()])
    START = perf_counter_ns()
    result = puzzle1(copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 1 result is {} and it took {:.3f} ms".format(result, time))
    START = perf_counter_ns()
    result = puzzle2(copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 2 result is {} and it took {:.3f} ms\n".format(result, time))

readData("test.txt")
readData("input.txt")
