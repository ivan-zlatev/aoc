#!/usr/bin/python3

from time import perf_counter_ns
import statistics

def puzzle1(data):
    START = perf_counter_ns()
    med = int(statistics.median(data))
    fuel = 0
    for sub in data:
        fuel += abs(sub - med)
    STOP = perf_counter_ns()
    return (STOP-START)/1000000.0, fuel

def puzzle2(data):
    START = perf_counter_ns()
    mid = round(statistics.mean(data))
    fuel = 0
    for sub in data:
        fuel += int((abs(sub - mid)**2 + abs(sub - mid))/2.0)
    STOP = perf_counter_ns()
    return (STOP-START)/1000000.0, fuel


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
readData("input.txt")
