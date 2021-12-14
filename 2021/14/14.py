#!/usr/bin/python3

from time import perf_counter_ns
import copy

def puzzle1(rules, template):
    pairs = { pair: 0 for pair in rules }
    chars = { char: template.count(char) for char in rules.values() }
    for i in range(len(template)-1):
        pairs[template[i:i+2]] += 1
    for i in range(10):
        pairs, chars = step(rules, pairs.copy(), chars.copy())
    return max(chars.values())-min(chars.values())

def puzzle2(rules, template):
    pairs = { pair: 0 for pair in rules } # checking 2 rows down instead of pair: template.count(pair), because of FFF edge case -> count does not count overlapping substrings
    chars = { char: template.count(char) for char in rules.values() }
    for i in range(len(template)-1):
        pairs[template[i:i+2]] += 1
    for i in range(40):
        pairs, chars = step(rules, pairs, chars)
    return max(chars.values())-min(chars.values())

def step(rules, pairs, chars):
    for pair, value in pairs.copy().items():
        pairs[pair] -= value # break existing pairs
        pairs[pair[0] + rules[pair]] += value # create new pair for every [N-1, N] pair, where N is the new char
        pairs[rules[pair] + pair[1]] += value # create new pair for every [N, N+1] pair, where N is the new char
        chars[rules[pair]] += value # track and increment the number of characters
    return pairs, chars

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    rules = {}
    template = inputData[0].strip()
    for i in inputData:
        if '->' in i:
            pair, element = [x for x in i.strip().split(' -> ')]
            rules[pair] = element
    START = perf_counter_ns()
    result = puzzle1(copy.deepcopy(rules), template)
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 1 result is {} and it took {:.3f} ms".format(result, time))
    START = perf_counter_ns()
    result = puzzle2(copy.deepcopy(rules), template)
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 2 result is {} and it took {:.3f} ms\n".format(result, time))

readData("test.txt")
readData("input.txt")
