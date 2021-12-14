#!/usr/bin/python3

from time import perf_counter_ns
import copy

def puzzle1(data, template):
    counts = {}
    for i in range(10):
        template = insertPolyPairs(data, template)
    for i in template:
        if i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1
    return max(counts.values())-min(counts.values())

def puzzle2(data, template):
    counts = {}
    for i in range(40):
        #print(template)
        template = insertPolyPairs(data, template)
    for i in template:
        if i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1
    return max(counts.values())-min(counts.values())

def insertPolyPairs(data, template):
    result = template[0]
    for i in range(0, len(template)-1):
        key = template[i:i+2]
        if key in data.keys():
            result += data[key]
        result += template[i+1]
    return result

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    data = {}
    template = inputData[0].strip()
    for i in inputData:
        if '->' in i:
            pair, element = [x for x in i.strip().split(' -> ')]
            data[pair] = element
    START = perf_counter_ns()
    result = puzzle1(copy.deepcopy(data), template)
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 1 result is {} and it took {:.3f} ms".format(result, time))
    START = perf_counter_ns()
    result = puzzle2(copy.deepcopy(data), template)
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 2 result is {} and it took {:.3f} ms\n".format(result, time))

#readData("test.txt")
readData("input.txt")
