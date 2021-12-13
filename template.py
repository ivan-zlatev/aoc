#!/usr/bin/python3

from time import perf_counter_ns
import copy

def puzzle1(data):
    for i in data:
        print(i)
    return 0

def puzzle2(data):
    return 0


def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    data = []
    #data = [[0 for x in range(len(inputData[0])+1)]]
    for i in inputData.split(','):
        data.append(i)
        #data.append([0] + [int(char) for char in inputData[i].strip()] + [0])
    #data.append([0 for x in range(len(inputData[0])+1)])
    START = perf_counter_ns()
    result = puzzle1(copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 1 result is {} and it took {:.3f} ms\n".format(result, time))
    START = perf_counter_ns()
    result = puzzle2(copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 2 result is {} and it took {:.3f} ms\n".format(result, time))

readData("test.txt")
#readData("input.txt")
