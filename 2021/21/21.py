#!/usr/bin/python3

from time import perf_counter_ns
import copy

def puzzle1(data):
    diceRoll = 0
    roll = 0
    while max([x[1] for x in data.values()]) < 1000:
        for i in range(1, 3):
            diceRoll, roll = rollDice(diceRoll)
            #print(f'Player {i}\'s turn: Position: {data[i][0]}; Score: {data[i][1]}; Dice Roll:{roll};')
            score = (data[i][0] + roll)%10
            if score == 0:
                score = 10
            data[i][0] = score
            data[i][1] += score
            if data[i][1] >= 1000:
                break
    print(data, diceRoll)
    return min([x[1] for x in data.values()])*diceRoll

def puzzle2(data):
    return 0

def rollDice(diceRoll):
    result = 0
    for _ in range(3):
        tmp = (diceRoll%100) + 1
        result += tmp
        diceRoll += 1
    return diceRoll, result

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    data = {}
    for i in inputData:
        tmp = i.strip()
        tmp = tmp.split(' ')
        data[int(tmp[1])] = [int(tmp[4]), 0] # data[player] = [position, score]
    START = perf_counter_ns()
    result = puzzle1(copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 1 result is {} and it took {:.3f} ms".format(result, time))
    START = perf_counter_ns()
    result = puzzle2(copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 2 result is {} and it took {:.3f} ms\n".format(result, time))

readData("test.txt")
readData("input.txt")
