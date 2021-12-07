#!/usr/bin/python3

from time import perf_counter_ns

def puzzle1(data):
    print(data)
    START = perf_counter_ns()
    STOP = perf_counter_ns()
    return (STOP-START)/1000.0, 0

def puzzle2(data):
    START = perf_counter_ns()
    STOP = perf_counter_ns()
    return (STOP-START)/1000.0, 0


def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    inputData = inputData[0].strip()
    data = []
    for i in inputData.split(','):
        data.append(int(i))
    time, result = puzzle1(data.copy())
    print("Puzzle 1 result is " + str(result) + " and it took " + str(time) + " ms")
    time, result = puzzle2(data.copy())
    print("Puzzle 2 result is " + str(result) + " and it took " + str(time) + " ms\n")

readData("test.txt")
#readData("input.txt")
