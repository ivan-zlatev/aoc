#!/usr/bin/python3

def puzzle1(inputData):
    c = 0
    for i in range(len(inputData)-1):
        if inputData[i] < inputData[i+1]:
            c += 1
    return c

def puzzle2(inputData):
    c = 0
    for i in range(len(inputData)-3):
        if inputData[i]+inputData[i+1]+inputData[i+2] < inputData[i+1]+inputData[i+2]+inputData[i+3]:
            c += 1
    return c


def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    for i in range(len(inputData)):
        inputData[i] = int(inputData[i].strip())
    print("\nPuzzle 1: " + str(puzzle1(inputData)))
    print("Puzzle 2: " + str(puzzle2(inputData)) + "\n")

readData("test.txt")
readData("input.txt")
