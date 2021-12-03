#!/usr/bin/python3

def puzzle1(inputData):
    gammaRate = ''
    epsilonRate = ''
    for i in range(len(inputData[0])):
        tmp = [x[i] for x in inputData]
        if tmp.count('0') >= tmp.count('1'):
            gammaRate = gammaRate + '0'
            epsilonRate = epsilonRate + '1'
        else:
            gammaRate = gammaRate + '1'
            epsilonRate = epsilonRate + '0'
    return int(gammaRate, 2)*int(epsilonRate, 2)

def puzzle2(inputData):
    oxyList = inputData.copy()
    co2List = inputData.copy()
    c = 0
    while len(oxyList) > 1:
        for i in range(len(oxyList)):
            tmp = [x[c] for x in oxyList]
            if tmp.count('0') > tmp.count('1'):
                bit = '0'
            else:
                bit = '1'
        for val in oxyList.copy():
            if not val[c] == bit:
                oxyList.remove(val)
        c += 1
    c = 0
    while len(co2List) > 1:
        for i in range(len(co2List)):
            tmp = [x[c] for x in co2List]
            if tmp.count('0') > tmp.count('1'):
                bit = '1'
            else:
                bit = '0'
        for val in co2List.copy():
            if not val[c] == bit:
                co2List.remove(val)
        c += 1
    return int(oxyList[0], 2) * int(co2List[0], 2)


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
