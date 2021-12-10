#!/usr/bin/python3

from time import perf_counter_ns
import re

def puzzle1(data):
    START = perf_counter_ns()
    result = 0
    for i in data:
        valid, value, line = checkIfLineIsValid(i)
        result += value
    STOP = perf_counter_ns()
    return (STOP-START)/1000000.0, result

def puzzle2(data):
    START = perf_counter_ns()
    validLines = []
    for i in data:
        valid, value, line = checkIfLineIsValid(i)
        if valid:
            validLines.append(line.replace('_', '')[::-1].replace('(', '1').replace('[', '2').replace('{', '3',).replace('<', '4',))
    totalResult = []
    for i in validLines:
        result = 0
        for j in i:
            result *= 5
            result += int(j)
        totalResult.append(result)
    STOP = perf_counter_ns()
    totalResult.sort()
    return (STOP-START)/1000000.0, totalResult[int(len(totalResult)/2)]

def checkIfLineIsValid(line):
    score = {
        ')':3,
        ']':57,
        '}':1197,
        '>':25137
    }
    while re.findall("\(_*\)|\{_*\}|\[_*\]|\<_*\>", line):
        for i in re.findall("\(_*\)|\{_*\}|\[_*\]|\<_*\>", line):
            line = line.replace(i, '_'*len(i))
    for i in line:
        if i  in score.keys():
            return False, score[i], line
    return True, 0, line

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    data = []
    for i in inputData:
        data.append(i.strip())
    time, result = puzzle1(data.copy())
    print("Puzzle 1 result is " + str(result) + " and it took " + str(time) + " ms")
    time, result = puzzle2(data.copy())
    print("Puzzle 2 result is " + str(result) + " and it took " + str(time) + " ms\n")

readData("test.txt")
readData("input.txt")
