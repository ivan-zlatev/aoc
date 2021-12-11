#!/usr/bin/python3

from time import perf_counter_ns
import copy

def puzzle1(data):
    START = perf_counter_ns()
    for i in data:
        print(i)
    STOP = perf_counter_ns()
    return (STOP-START)/1000000.0, 0

def puzzle2(data):
    START = perf_counter_ns()
    STOP = perf_counter_ns()
    return (STOP-START)/1000000.0, 0


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
    time, result = puzzle1(copy.deepcopy(data))
    print("Puzzle 1 result is " + str(result) + " and it took " + str(time) + " ms")
    time, result = puzzle2(copy.deepcopy(data))
    print("Puzzle 2 result is " + str(result) + " and it took " + str(time) + " ms\n")

readData("test.txt")
#readData("input.txt")
