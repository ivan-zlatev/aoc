#!/usr/bin/python3

def puzzle1(data):
    fishes = {
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0
    }
    for i in data:
        fishes[i] += 1
    for day in range(80):
        fishes = simulateDay(fishes)
    return sum(fishes.values())

def puzzle2(data):
    fishes = {
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0
    }
    for i in data:
        fishes[i] += 1
    for day in range(256):
        fishes = simulateDay(fishes)
    return sum(fishes.values())

def simulateDay(fishes):
    fishesUpdated = {
        0:fishes[1],
        1:fishes[2],
        2:fishes[3],
        3:fishes[4],
        4:fishes[5],
        5:fishes[6],
        6:fishes[0]+fishes[7],
        7:fishes[8],
        8:fishes[0]
    }
    return fishesUpdated

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
