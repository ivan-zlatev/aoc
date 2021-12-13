#!/usr/bin/python3

from time import perf_counter_ns
import copy

results = []
result = []

def puzzle1(data):
    START = perf_counter_ns()
    global results, result
    results = []
    result = []
    recFunc(data)
    STOP = perf_counter_ns()
    return (STOP-START)/1000000.0, len(set(results))

def puzzle2(data):
    START = perf_counter_ns()
    global results, result
    results = []
    result = []
    for i in data.keys():
        if i.islower() and not (i in ['start', 'end']):
            recFunc(data, i)
    STOP = perf_counter_ns()
    return (STOP-START)/1000000.0, len(set(results))

def recFunc(data, smallCave='', thisNode='start'):
    global results, result
    if thisNode == "end":
        tup = tuple(result + [thisNode])
        results.append(tup)
    else:
        for val in data[thisNode]:
            if (val == smallCave and len([x for x in result if x == smallCave]) < 2) or not ((val.islower() and val in result)):
                result.append(thisNode)
                recFunc(data, smallCave, val)
                result = result[:-1]

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    data = {}
    inputDataList = []
    for i in inputData:
        inputDataList.append(i.strip().split('-'))
        inputDataList.append(i.strip().split('-')[::-1])
    for i in inputDataList:
        if i[0] in data.keys():
            if i[1] not in data[i[0]]:
                data[i[0]].append(i[1])
        else:
            data[i[0]] = [i[1]]
    time, result = puzzle1(copy.deepcopy(data))
    print("Puzzle 1 result is " + str(result) + " and it took " + str(time) + " ms")
    time, result = puzzle2(copy.deepcopy(data))
    print("Puzzle 2 result is " + str(result) + " and it took " + str(time) + " ms\n")

readData("test.txt")
readData("test2.txt")
readData("test3.txt")
readData("input.txt")
