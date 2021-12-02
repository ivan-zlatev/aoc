#!/usr/bin/python3

def puzzle1(inputData):
    position = 0
    depth = 0
    for i in range(len(inputData)):
        if inputData[i].split(' ')[0] == "forward":
            position += int(inputData[i].split(' ')[1])
        elif inputData[i].split(' ')[0] == "down":
            depth += int(inputData[i].split(' ')[1])
        elif inputData[i].split(' ')[0] == "up":
            depth -= int(inputData[i].split(' ')[1])
        else:
            print("Error, unrecognized input: " + inputData[i])
    return position*depth

def puzzle2(inputData):
    position = 0
    depth = 0
    aim = 0
    for i in range(len(inputData)):
        if inputData[i].split(' ')[0] == "forward":
            position += int(inputData[i].split(' ')[1])
            depth += aim*int(inputData[i].split(' ')[1])
        elif inputData[i].split(' ')[0] == "down":
            aim += int(inputData[i].split(' ')[1])
        elif inputData[i].split(' ')[0] == "up":
            aim -= int(inputData[i].split(' ')[1])
        else:
            print("Error, unrecognized input: " + inputData[i])
    return position*depth


def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    for i in range(len(inputData)):
        inputData[i] = inputData[i].strip()
    print("\nPuzzle 1: " + str(puzzle1(inputData)))
    print("Puzzle 2: " + str(puzzle2(inputData)) + "\n")

readData("test.txt")
readData("input.txt")
