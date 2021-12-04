#!/usr/bin/python3

import copy

def puzzle1(numbers, boards):
    for number in numbers:
        for i in range(len(boards)):
            boards[i] = markNumberIfFound(boards[i], number)
        for board in boards:
            if checkIfWinningBoard(board):
                return calculateResult(board, number)
    return 0

def puzzle2(numbers, boards):
    lastBoardNumber = -1
    for number in numbers:
        for i in range(len(boards)):
            boards[i] = markNumberIfFound(boards[i], number)
        doneBoards = []
        counter = 0
        for i in range(len(boards)):
            doneBoards.append(checkIfWinningBoard(boards[i]))
            if not doneBoards[-1]:
                counter = i
        if doneBoards.count(False) == 1:
            lastBoardNumber = counter
        if doneBoards.count(False) == 0:
            return calculateResult(boards[lastBoardNumber], number)
    return 0

def checkIfWinningBoard(board):
    # check if winning row
    for row in board:
        winning = True
        for col in row:
            if not col[1]:
                winning = False
        if winning:
            return winning
    # check if winning col
    for i in range(len(board[0])):
        winning = True
        for row in board:
            if not row[i][1]:
                winning = False
        if winning:
            return winning
    return winning

def markNumberIfFound(board, number):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if number == board[row][col][0]:
                board[row][col][1] = True
    return board

def calculateResult(board, number):
    sum = 0
    for row in board:
        for col in row:
            if not col[1]:
                sum += col[0]
    return sum*number

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    for i in range(len(inputData)):
        inputData[i] = inputData[i].strip()
    numbers = inputData[0].split(',')
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    boards = []
    inputData.remove(inputData[0])
    for i in range(int(len(inputData)/6)):
        tmp = []
        for j in inputData[i*6+1:i*6+6]:
            row = []
            for k in j.split():
                row.append([int(k), False])
            tmp.append(row)
        boards.append(tmp)
    print("\nPuzzle 1: " + str(puzzle1(numbers, copy.deepcopy(boards))))
    print("Puzzle 2: " + str(puzzle2(numbers, copy.deepcopy(boards))) + "\n")

readData("test.txt")
readData("input.txt")
