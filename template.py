#!/usr/bin/python3

def puzzle1(data):
    return 0

def puzzle2(data):
    return 0


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
#readData("input.txt")
