#!/usr/bin/python3

from time import perf_counter_ns
import copy

def puzzle1(data):
    grid = {}
    grid['0'] = [tuple(data['0']), [0, 0, 0]]
    del data['0']
    for key, val in data.items():
        data[key] = getListRotations(copy.deepcopy(data[key]))
    while len(data.keys()) > 0:
        toAdd = []
        for key in data.keys():
            if len(toAdd) == 0:
                for gridKey in grid.keys():
                    if len(toAdd) == 0:
                        match, x, y, z = getOffsets(grid[gridKey][0], data[key])
                        if len(match) > 0 and key not in [x[0] for x in toAdd]:
                            toAdd.append([key, [copy.deepcopy(match), [grid[gridKey][1][0]+x, grid[gridKey][1][1]+y, grid[gridKey][1][2]+z]]])
        for add in toAdd:
            grid[add[0]] = copy.deepcopy(add[1])
            del data[add[0]]
        print(data.keys(), grid.keys())
    #for key, val in grid.items():
    #    print(key)
    #    for i in val:
    #        print('    ', i)
    return getUniquePoints(grid)

def puzzle2(data):
    return 0

def getUniquePoints(grid):
    result = []
    for val in grid.values():
        for point in val[0]:
            tmp = [x + y for x, y in zip(point, val[1])]
            if tmp not in result:
                result.append(tmp)
    return len(result)

def getOffsets(groundData, rotationsData, debug=False):
    searchRange = range(-2000, 2000)
    resultX = []
    resultY = []
    resultZ = []
    groundXCoords = tuple([x[0] for x in groundData])
    groundYCoords = tuple([y[1] for y in groundData])
    groundZCoords = tuple([z[2] for z in groundData])
    for rot in rotationsData: # find all X+offsetY matches between groundData and any rotationsData
        testXCoords = [x[0] for x in rot]
        for offsetX in searchRange:
            offsetXCoords = [x+offsetX for x in groundXCoords]
            intersections = list(set(offsetXCoords).intersection(testXCoords))
            if len(intersections) > 11:
                if [rot, offsetX] not in resultX:
                    resultX.append([tuple(rot), -offsetX])
    if debug:
        print('Found the following intersecting rots by X:')
        for i in resultX:
            print(i)
    for rot, offsetX in resultX: # find all Y+offsetY matches between groundData and any rotationsData that matches X+offsetX
        testYCoords = [y[1] for y in rot]
        for offsetY in searchRange:
            offsetYCoords = [y+offsetY for y in groundYCoords]
            interactions = list(set(offsetYCoords).intersection(testYCoords))
            if len(interactions) > 11:
                resultY.append([tuple(rot), offsetX, -offsetY])
    if debug:
        print('Found the following intersecting rots by Y:')
        for i in resultY:
            print(i)
    for rot, offsetX, offsetY in resultY: # find all Z+offsetZ matches between groundData and any rotationsData that matches X+offsetX and Y+offsetY. There should be 0 or 1 resultsZ after this.
        testZCoords = [z[2] for z in rot]
        for offsetZ in searchRange:
            offsetZCoords = [z+offsetZ for z in groundZCoords]
            interactions = list(set(offsetZCoords).intersection(testZCoords))
            if len(interactions) > 11:
                #print(interactions)
                resultZ.append([rot, offsetX, offsetY, -offsetZ])
    if debug:
        print('Found the following intersecting rots by Z:')
        for i in resultZ:
            print(i)
    if len(resultZ) > 0:
        return resultZ[0]
    else:
        return [], 0, 0, 0

def rotateArrayX(data, rotations=1): # [X,y,z] -> [X,-z,y]
    for rot in range(rotations):
        for i in range(len(data)):
            data[i] = tuple([data[i][0], -data[i][2], data[i][1]])
    return data

def rotateArrayY(data, rotations=1): # [x,Y,z] -> [z,Y,-x]
    for rot in range(rotations):
        for i in range(len(data)):
            data[i] = tuple([data[i][2], data[i][1], -data[i][0]])
    return data

def rotateArrayZ(data, rotations=1): # [x,y,Z] -> [y,-x,Z]
    for rot in range(rotations):
        for i in range(len(data)):
            data[i] = tuple([data[i][1], -data[i][0], data[i][2]])
    return data

def getListRotations(data):
    result = []
    for j in range(4): # get the 4 possible positions rotated around the X axis
        newList = rotateArrayX(copy.deepcopy(data), j)
        if newList not in result:
            result.append(copy.deepcopy(newList))
    for i in range(4): # for every rotation around the X axis
        for j in range(4): # get every rotation around the Y axis
            newList = rotateArrayY(copy.deepcopy(result[i]), j)
            if newList not in result: # and append if it does not exist
                result.append(copy.deepcopy(newList))
    for i in range(16): # for every rotation around the X and Y axis
        for j in range(4): # get every rotation around the Z axis
            newList = rotateArrayZ(copy.deepcopy(result[i]), j)
            if newList not in result: # and append if it does not exist
                result.append(copy.deepcopy(newList))
    return result

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    inputData = [x.strip() for x in inputData if len(x) > 3]
    data = {}
    key = ''
    for i in inputData:
        if 'scanner' in i:
            key = i.split(' ')[2]
            data[key] = []
        else:
            data[key].append(tuple([int(x) for x in i.split(',')]))
    START = perf_counter_ns()
    result = puzzle1(copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 1 result is {} and it took {:.3f} ms".format(result, time))
    START = perf_counter_ns()
    result = puzzle2(copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 2 result is {} and it took {:.3f} ms\n".format(result, time))

readData("test.txt")
#readData("input.txt")
