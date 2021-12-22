#!/usr/bin/python3

from time import perf_counter_ns
import copy

def puzzle1(data):
    result = {}
    for i in data:
        for x in range(max(i[1][0], -50), min(i[1][1]+1, 51)):
            for y in range(max(i[2][0], -50), min(i[2][1]+1, 51)):
                for z in range(max(i[3][0], -50), min(i[3][1]+1, 51)):
                    result[(x, y, z)] = i[0]
    return len([x for x in result.values() if x == 1])

def puzzle2(data):
    result = {}
    for i in data:
        print(i)
        for x in range(max(i[1][0], -50), min(i[1][1]+1, 51)):
            for y in range(max(i[2][0], -50), min(i[2][1]+1, 51)):
                for z in range(max(i[3][0], -50), min(i[3][1]+1, 51)):
                    result[(x, y, z)] = i[0]
    return len([x for x in result.values() if x == 1])


def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    data = []
    values = {'on': 1, 'off':0}
    for i in inputData:
        proc = i.strip().split(' ')[0]
        tmp = i.strip().split(' ')[1].split(',')
        data.append([values[proc], [int(x) for x in tmp[0].split('=')[1].split('..')], [int(y) for y in tmp[1].split('=')[1].split('..')], [int(z) for z in tmp[2].split('=')[1].split('..')]])
    START = perf_counter_ns()
    result = puzzle1(copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 1 result is {} and it took {:.3f} ms".format(result, time))
    START = perf_counter_ns()
    result2 = puzzle2(copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 2 result is {} and it took {:.3f} ms\n".format(result2, time))
    return result, result2

assert readData("test.txt") == (39, 39)
assert readData("test2.txt") == (590784, 474140)
#assert readData("test3.txt") == (474140, 2758514936282235)
#readData("input.txt")
