#!/usr/bin/python3
from statistics import median

def puzzle1(data):
    med = int(median(data))
    fuel = 0
    for sub in data:
        fuel += abs(sub - med)
    return fuel

def puzzle2(data):
    fuels = []
    for i in range(min(data), max(data)):
        subsFuel = 0
        for sub in data:
            fuel = 0
            for f in range(abs(sub - i)+1):
                fuel += f
            subsFuel += fuel
        fuels.append(subsFuel)
        #print(fuels)
    return min(fuels)


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
