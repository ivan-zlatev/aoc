#!/usr/bin/python3

from time import perf_counter_ns
import copy

def puzzle1(data):
    highest = []
    for x in range(1000):
        for y in range(-1000, 1000):
            result, maxY = simulateLaunch(data, x, y)
            if result:
                highest.append(maxY)
    return max(highest)

def puzzle2(data):
    valid = 0
    for x in range(1000):
        for y in range(-1000, 1000):
            if simulateLaunch(data, x, y)[0]:
                valid += 1
    return valid

def simulateLaunch(data, xVel, yVel, x=0, y=0, maxY=0):
    while True:
        maxY = max(maxY, y) # save current step to the list for logging
        x += xVel # increment the x by one velocity
        y += yVel # increment the x by one velocity
        if xVel > 0: # due to drag, xVel -> 0
            xVel -= 1
        elif xVel < 0:
            xVel += 1
        yVel -= 1 # due to gravitiy yVel -= 1
        if x >= min(data['x']) and x <= max(data['x']) and y >= min(data['y']) and y <= max(data['y']): # if current step is in the area -> return True and the steps log
            return True, maxY
        else:
            if xVel == 0 and (x < min(data['x']) or x > max(data['x'])): # x out of bounds with xVel == 0
                return False, maxY
            elif x > max(data['x']): # overshot x
                return False, maxY
            elif y < min(data['y']): # y out of bounds, below the target area
                return False, maxY

def checkIfProbeInArea(x, y, xRange, yRange):
    xInRange = x >= min(xRange) and x <= max(xRange)
    yInRange = y >= min(yRange) and y <= max(yRange)
    return xInRange and yInRange

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    data = {}
    inputData = inputData[0].strip().split(': ')[1]
    for i in inputData.split(', '):
        tmp = i.split('=')
        data[tmp[0]] = [int(x) for x in tmp[1].split('..')]
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
