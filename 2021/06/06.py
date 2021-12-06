#!/usr/bin/python3

def puzzle1(data):
    for i in range(80):
        data = simulateDay(data)
    return len(data)

def puzzle2(data):
    for i in range(256):
        if i > 100:
            print(i)
        data = simulateDay(data)
    return len(data)

def simulateDay(data):
    for i in range(len(data)):
        if data[i] == 0:
            data[i] = 6
            data.append(8)
        else:
            data[i] -= 1
    return data

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
