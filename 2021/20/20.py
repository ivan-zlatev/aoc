#!/usr/bin/python3

from time import perf_counter_ns
import copy
import numpy as np

def puzzle1(algo, data):
    data = np.array(data)
    frame = 0
    for i in range(2):
        data = enhance(data, algo, frame)
        if frame == 0:
            frame = algo[0]
        else:
            frame = algo[-1]
    return np.sum(data)

def puzzle2(algo, data):
    data = np.array(data)
    frame = 0
    for i in range(50):
        data = enhance(data, algo, frame)
        if frame == 0:
            frame = algo[0]
        else:
            frame = algo[-1]
    return np.sum(data)

def enhance(data,algo,frame):
    result = np.zeros_like(data)
    data = np.pad(data,(2,2),constant_values=frame)
    if frame == 0:
        frame = algo[0]
    else:
        frame = algo[-1]
    result = np.pad(result,(2,2),constant_values=frame)
    for x in range(1, len(data[0])-1):
        for y in range(1, len(data)-1):
            index = int(''.join([str(x) for x in list(data[x-1:x+2,y-1:y+2].reshape(-1))]), 2)
            result[x,y] = algo[index]
    return result

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    keys = {'.':0, '#':1}
    algo = [keys[x] for x in inputData[0].strip()]
    data = []
    for row in inputData[2:]:
        data.append([keys[x] for x in row.strip()])
    START = perf_counter_ns()
    result = puzzle1(algo, copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 1 result is {} and it took {:.3f} ms".format(result, time))
    START = perf_counter_ns()
    result = puzzle2(algo, copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 2 result is {} and it took {:.3f} ms\n".format(result, time))

readData("test.txt")
readData("input.txt")
