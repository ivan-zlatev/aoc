#!/usr/bin/python3

from time import perf_counter_ns
import re

def puzzle1(data):
    START = perf_counter_ns()
    count = 0
    for row in data:
        for digit in row[1].split(' '):
            if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                count +=1
    STOP = perf_counter_ns()
    return (STOP-START)/1000000.0, count

def puzzle2(data):
    START = perf_counter_ns()
    result = 0
    for row in data:
        result += decodeNumber(row[0].split(' '), row[1].split(' '))
    STOP = perf_counter_ns()
    return (STOP-START)/1000000.0, result

def decodeNumber(inputDigits, displayDigits):
    A,B,C,D,E,F,G = determineSegmentWires(inputDigits)
    number = ''
    for digit in displayDigits:
        if len(digit) == 2:
            number += '1'
        elif len(digit) == 3:
            number += '7'
        elif len(digit) == 4:
            number += '4'
        elif len(digit) == 7:
            number += '8'
        elif len(digit) == 6:
            if G not in digit:
                number += '0'
            elif E not in digit:
                number += '9'
            else:
                number += '6'
        else:
            if F in digit:
                number += '5'
            elif E in digit:
                number += '2'
            else:
                number += '3'
    return int(number)

def determineSegmentWires(inputDigits):
    uniqueDigits = {}
    otherDigits = []
    for word in inputDigits:
        if len(word) == 2:
            uniqueDigits[1] = word
        elif len(word) == 3:
            uniqueDigits[7] = word
        elif len(word) == 4:
            uniqueDigits[4] = word
        elif len(word) == 7:
            uniqueDigits[8] = word
        else:
            otherDigits.append(word)
    A = re.sub('[' + uniqueDigits[1] + ']', '', uniqueDigits[7])
    if len([y for y in [x for x in otherDigits if uniqueDigits[1][1] in x] if uniqueDigits[1][0] not in y]) == 1:
        two = [y for y in [x for x in otherDigits if uniqueDigits[1][1] in x] if uniqueDigits[1][0] not in y][0]
        B = uniqueDigits[1][0]
        C = uniqueDigits[1][1]
    else:
        two = [y for y in [x for x in otherDigits if uniqueDigits[1][0] in x] if uniqueDigits[1][1] not in y][0]
        B = uniqueDigits[1][1]
        C = uniqueDigits[1][0]
    G = [x for x in (re.sub('[' + uniqueDigits[1] + ']', '' ,uniqueDigits[4])) if x in two][0]
    F = re.sub(G, '', re.sub('[' + uniqueDigits[1] + ']', '', uniqueDigits[4]))
    three = [x for x in otherDigits if F not in x and x != two][0]
    D = re.sub('[' + A + B + C + G + ']', '', three)
    E = re.sub('[' + A + B + C + D + F + G + ']', '', uniqueDigits[8])
    return [A,B,C,D,E,F,G]

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    data = []
    for i in range(len(inputData)):
        data.append(inputData[i].strip().split(' | '))
    time, result = puzzle1(data.copy())
    print("Puzzle 1 result is " + str(result) + " and it took " + str(time) + " ms")
    time, result = puzzle2(data.copy())
    print("Puzzle 2 result is " + str(result) + " and it took " + str(time) + " ms\n")

readData("test.txt")
readData("input.txt")
