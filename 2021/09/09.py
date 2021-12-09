#!/usr/bin/python3

from time import perf_counter_ns

def puzzle1(data):
    START = perf_counter_ns()
    lowPoints, basinSize = getLowPoints(data, False)
    STOP = perf_counter_ns()
    return (STOP-START)/1000000.0, sum(lowPoints) + len(lowPoints)

def puzzle2(data):
    START = perf_counter_ns()
    lowPoints, basinSize = getLowPoints(data, True)
    result = 1
    for x in basinSize:
        result *= x
    STOP = perf_counter_ns()
    return (STOP-START)/1000000.0, result

def getLowPoints(data, basinSizes):
    basinSize = []
    result = []
    for y in range(1, len(data)-1):
        for x in range(1, len(data[y])-1):
            if  data[y][x] < data[y-1][x] and data[y][x] < data[y+1][x] and data[y][x] < data[y][x-1] and data[y][x] < data[y][x+1]:
                result.append(data[y][x])
                if basinSizes:
                    basinSize.append(len(getBasinSize(data, x, y, [])))
    return result, sorted(basinSize)[-3:]

def getBasinSize(data, x, y, result):
    result.append([x, y])
    if data[y][x-1] < 9 and [x-1, y] not in result:
        getBasinSize(data, x-1, y, result)
    if data[y][x+1] < 9 and [x+1, y] not in result:
        getBasinSize(data, x+1, y, result)
    if data[y-1][x] < 9 and [x, y-1] not in result:
        getBasinSize(data, x, y-1, result)
    if data[y+1][x] < 9 and [x, y+1] not in result:
        getBasinSize(data, x, y+1, result)
    return result

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    data = []
    data = [[9 for x in range(len(inputData[0])+1)]]
    for i in range(len(inputData)):
        data.append([9] + [int(char) for char in inputData[i].strip()] + [9])
    data.append([9 for x in range(len(inputData[0])+1)])
    time, result = puzzle1(data.copy())
    print("Puzzle 1 result is " + str(result) + " and it took " + str(time) + " ms")
    time, result = puzzle2(data.copy())
    print("Puzzle 2 result is " + str(result) + " and it took " + str(time) + " ms\n")

readData("test.txt")
readData("input.txt")
