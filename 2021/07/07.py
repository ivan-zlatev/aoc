#!/usr/bin/python3
import statistics
import math

def puzzle1(data):
    med = int(statistics.median(data))
    fuel = 0
    for sub in data:
        fuel += abs(sub - med)
    return fuel

def puzzle2(data):
    mid = math.ceil(statistics.mean(data))
    print(mid)
    fuel = 0
    for sub in data:
        fuel += int((abs(sub - mid)**2 + abs(sub - mid))/2.0)
    return fuel


def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    inputData = inputData[0].strip()
    data = []
    for i in inputData.split(','):
        data.append(int(i))
    print("\nPuzzle 1: " + str(puzzle1(data.copy())))
    print("Puzzle 2: " + str(puzzle2(data.copy())) + "\n")

readData("test.txt")
readData("input.txt")
