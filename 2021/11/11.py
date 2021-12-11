#!/usr/bin/python3

from time import perf_counter_ns
import copy

def puzzle1(data):
    START = perf_counter_ns()
    result = 0
    for i in range(100):
        data, flashes = simulateStep(data)
        result += flashes
    STOP = perf_counter_ns()
    return (STOP-START)/1000000.0, result

def puzzle2(data):
    START = perf_counter_ns()
    for i in range(10000):
        data, flashes = simulateStep(data)
        if flashes == (len(data)-2)*(len(data[0])-2):
            STOP = perf_counter_ns()
            return (STOP-START)/1000000.0, i+1
    STOP = perf_counter_ns()
    return (STOP-START)/1000000.0, 0

def simulateStep(data):
    flashes = 0
    grid = [ [False] * len(data) for _ in range(len(data[0]))]
    # set the grid edges to true
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if x == 0 or x == len(grid[y])-1:
                grid[y][x] = True
            if y == 0 or y == len(grid)-1:
                grid[y][x] = True
    # increment every octopus by 1
    for i in range(1, len(data)-1):
        for j in range(1, len(data[i])-1):
            data[i][j] += 1
    # simulate a flash
    for y in range(1, len(data)-1):
        for x in range(1, len(data[i])-1):
            data, grid = flash(data, grid, x, y)
    # count the flashes
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            if grid[i][j]:
                flashes += 1
    return data, flashes

def flash(data, grid, x, y):
    if not grid[y][x]:
        if data[y][x] > 9:
            grid[y][x] = True
            data[y][x] = 0
            if not grid[y-1][x]: # top
                data[y-1][x] += 1
                data, grid = flash(data, grid, x, y-1)
            if not grid[y+1][x]: # bot
                data[y+1][x] += 1
                data, grid = flash(data, grid, x, y+1)
            if not grid[y][x-1]: # left
                data[y][x-1] += 1
                data, grid = flash(data, grid, x-1, y)
            if not grid[y][x+1]: # right
                data[y][x+1] += 1
                data, grid = flash(data, grid, x+1, y)
            if not grid[y-1][x-1]: # top left
                data[y-1][x-1] += 1
                data, grid = flash(data, grid, x-1, y-1)
            if not grid[y-1][x+1]: # top right
                data[y-1][x+1] += 1
                data, grid = flash(data, grid, x+1, y-1)
            if not grid[y+1][x-1]: # bot left
                data[y+1][x-1] += 1
                data, grid = flash(data, grid, x-1, y+1)
            if not grid[y+1][x+1]: # bot right
                data[y+1][x+1] += 1
                data, grid = flash(data, grid, x+1, y+1)
    return data, grid


def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    data = []
    data = [[0 for x in range(len(inputData[0])+1)]]
    for i in range(len(inputData)):
        data.append([0] + [int(char) for char in inputData[i].strip()] + [0])
    data.append([0 for x in range(len(inputData[0])+1)])
    time, result = puzzle1(copy.deepcopy(data))
    print("Puzzle 1 result is " + str(result) + " and it took " + str(time) + " ms")
    time, result = puzzle2(copy.deepcopy(data))
    print("Puzzle 2 result is " + str(result) + " and it took " + str(time) + " ms\n")

readData("test.txt")
readData("input.txt")
