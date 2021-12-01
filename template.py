#!/usr/bin/python3

def puzzle1(inputData):
    return 0

def puzzle2(inputData):
    return 0


def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    for i in range(len(inputData)):
        inputData[i] = int(inputData[i].strip())
    print("\nPuzzle 1: " + str(puzzle1(inputData)))
    print("Puzzle 2: " + str(puzzle2(inputData)) + "\n")

readData("test.txt")
#readData("input.txt")
