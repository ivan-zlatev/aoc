#!/usr/bin/python3

from time import perf_counter_ns
import copy
import ast
import math
import re
from itertools import permutations

def puzzle1(data):
    finalSum = sumNums(data)
    return calcMagnitude(ast.literal_eval(finalSum))

def puzzle2(data):
    result = 0
    for permutation in list(permutations(data, 2)):
        result = max(result, calcMagnitude(ast.literal_eval(sumNums(permutation))))
    return result

def sumNums(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result = reduceNum('[' + result + ',' + nums[i] + ']', False, False)
    return result

def reduceNum(num, end=False, debug=False):
    notChars = ['[', ']', ',']
    while not end:
        index = 0
        leftNumberIndex = []
        rightNumberIndex = []
        explodeIndex = []
        leftExplodeVal = -1
        rightExplodeVal = -1
        depth = 0
        old = num
        splitIndex = []
        while index < len(num):
            if debug:
                print('NUM:', num, num[index], index)
            if num[index] == ',':
                index += 1
                continue
            elif num[index] == '[':
                depth += 1
                index += 1
                continue
            elif num[index] == ']':
                depth -= 1
                index += 1
                continue
            else: # found int
                char = re.findall('^[0-9]+', num[index:])[0]
                if len(char) > 1 and len(splitIndex) < 1:
                    firstNum = math.floor(int(char)/2.0)
                    secondNum = math.ceil(int(char)/2.0)
                    splitIndex = [index, index+len(char), firstNum, secondNum]
                if depth == 5 and len(explodeIndex) < 1:
                    leftExplodeVal = char
                    explodeLength = len(leftExplodeVal) + 2 # left val and [ and ,
                    rightExplodeVal = re.findall('^[0-9]+', num[index-1+explodeLength:])[0]
                    explodeLength += len(rightExplodeVal)
                    explodeIndex = [index-1, index+explodeLength]
                    if debug:
                        print('EXPLODE:', num[explodeIndex[0]:explodeIndex[1]], 'leftExplodeVal:', leftExplodeVal, 'rightExplodeVal', rightExplodeVal)
                        print('EXPLODE:', num)
                        print('EXPLODE:' + ' '*index + '^' + '-'*(explodeLength-1) + '^')
                    index += explodeLength-1
                    continue
                else:
                    if len(explodeIndex) < 1: # search for the leftNumberIndex
                        leftNumberIndex = [index, index+len(char)]
                        if debug:
                            print('leftNumberIndex:', leftNumberIndex, num[leftNumberIndex[0]:leftNumberIndex[1]])
                    if len(explodeIndex) > 1: # search for the rightNumberIndex
                        rightNumberIndex = [index, index+len(char)]
                        if debug:
                            print('rightNumberIndex:', rightNumberIndex, num[rightNumberIndex[0]:rightNumberIndex[1]])
                        index = len(num)
                        continue
                    index += len(char)
        if len(explodeIndex) > 1:
            if debug:
                print('Exploding:', num[explodeIndex[0]:explodeIndex[1]])
                print('Exploding:', 'leftNumberIndex:', leftNumberIndex, 'rightNumberIndex:', rightNumberIndex, 'explodeIndex:', explodeIndex, 'explodeLength:', explodeLength)
            num = num[:explodeIndex[0]] + '0' + num[explodeIndex[1]:]
            if len(leftNumberIndex) > 1:
                oldLeftNum = int(num[leftNumberIndex[0]:leftNumberIndex[1]])
                newLeftNum = oldLeftNum + int(leftExplodeVal)
                num = '{}{}{}'.format(num[:leftNumberIndex[0]], newLeftNum, num[leftNumberIndex[1]:])
                explodeLength -= len(str(newLeftNum))-len(str(oldLeftNum))
            if len(rightNumberIndex) > 1:
                rightNumberIndex = [x-explodeLength for x in rightNumberIndex]
                newRightNum = int(num[rightNumberIndex[0]:rightNumberIndex[1]]) + int(rightExplodeVal)
                num = '{}{}{}'.format(num[:rightNumberIndex[0]], newRightNum, num[rightNumberIndex[1]:])
        elif len(splitIndex) > 1:
            if debug:
                print('Found a number that needs to be split:', char)
            num = num[:splitIndex[0]] + '[{},{}]'.format(splitIndex[2], splitIndex[3]) + num[splitIndex[1]:]
        if old == num:
            end = True
        else:
            old = num
    return num

def calcMagnitude(num):
    if isinstance(num[0], int) and not isinstance(num[1], int):
        return 3*num[0] + 2*calcMagnitude(copy.deepcopy(num[1]))
    elif not isinstance(num[0], int) and isinstance(num[1], int):
        return 3*calcMagnitude(copy.deepcopy(num[0])) + 2*num[1]
    elif not isinstance(num[0], int) and not isinstance(num[1], int):
        return 3*calcMagnitude(copy.deepcopy(num[0])) + 2*calcMagnitude(copy.deepcopy(num[1]))
    else:
        return 3*num[0] + 2*num[1]

# testing some magnitudes
assert calcMagnitude(ast.literal_eval('[[1,2],[[3,4],5]]')) == 143
assert calcMagnitude(ast.literal_eval('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')) == 1384
assert calcMagnitude(ast.literal_eval('[[[[1,1],[2,2]],[3,3]],[4,4]]')) == 445
assert calcMagnitude(ast.literal_eval('[[[[3,0],[5,3]],[4,4]],[5,5]]')) == 791
assert calcMagnitude(ast.literal_eval('[[[[5,0],[7,4]],[5,5]],[6,6]]')) == 1137
assert calcMagnitude(ast.literal_eval('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')) == 3488

# testing some reductions
assert reduceNum('[[[[[9,8],1],2],3],4]') == '[[[[0,9],2],3],4]' # (the 9 has no regular number to its left, so it is not added to any regular number).
assert reduceNum('[7,[6,[5,[4,[3,2]]]]]') == '[7,[6,[5,[7,0]]]]' # (the 2 has no regular number to its right, and so it is not added to any regular number).
assert reduceNum('[[6,[5,[4,[3,2]]]],1]') == '[[6,[5,[7,0]]],3]'
assert reduceNum('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]') == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]' # (the pair [3,2] is unaffected because the pair [7,3] is further to the left; [3,2] would explode on the next action).
assert reduceNum('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]') == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'

# testing some splits
assert reduceNum('[[11,18]]') == '[[[5,6],[9,9]]]'
assert reduceNum('[[1,18]]') == '[[1,[9,9]]]'

# testing some sums
assert sumNums(['[1,1]', '[2,2]', '[3,3]', '[4,4]']) == '[[[[1,1],[2,2]],[3,3]],[4,4]]'
assert sumNums(['[1,1]', '[2,2]', '[3,3]', '[4,4]', '[5,5]']) == '[[[[3,0],[5,3]],[4,4]],[5,5]]'
assert sumNums(['[1,1]', '[2,2]', '[3,3]', '[4,4]', '[5,5]', '[6,6]']) == '[[[[5,0],[7,4]],[5,5]],[6,6]]'
assert sumNums(['[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]', '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]', '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]', '[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]', '[7,[5,[[3,8],[1,4]]]]', '[[2,[2,2]],[8,[8,1]]]', '[2,9]', '[1,[[[9,3],9],[[9,0],[0,7]]]]', '[[[5,[7,4]],7],1]', '[[[[4,2],2],6],[8,7]]']) == '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    data = [x.strip() for x in inputData]
    START = perf_counter_ns()
    result = puzzle1(copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 1 result is {} and it took {:.3f} ms".format(result, time))
    START = perf_counter_ns()
    result = puzzle2(copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 2 result is {} and it took {:.3f} ms\n".format(result, time))

assert sumNums(['[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]', '[[[5,[2,8]],4],[5,[[9,9],0]]]', '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]', '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]', '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]', '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]', '[[[[5,4],[7,7]],8],[[8,3],8]]', '[[9,3],[[9,9],[6,[4,9]]]]', '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]', '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]']) == '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'
assert puzzle1(['[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]', '[[[5,[2,8]],4],[5,[[9,9],0]]]', '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]', '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]', '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]', '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]', '[[[[5,4],[7,7]],8],[[8,3],8]]', '[[9,3],[[9,9],[6,[4,9]]]]', '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]', '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]']) == 4140

readData("test.txt")
readData("input.txt")
