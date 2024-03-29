#!/usr/bin/python3

from time import perf_counter_ns
import copy
import math

count = 0
def puzzle1(data):
    global count
    count = 0
    raw = ''.join([hexToBin(x) for x in data])
    packet = readPacket(raw)[0]
    #print('Extracted packets at top lvl: ', packet)
    return count

def puzzle2(data):
    raw = ''.join([hexToBin(x) for x in data])
    packet = readPacket(raw)[0]
    #print('Extracted packets at top lvl: ', packet)
    return calculateValues(packet)

def calculateValues(packet):
    pID = packet[1]
    if pID == 4:
        return packet[2]
    elif pID == 0:
        return sum([calculateValues(x) for x in packet[2]])
    elif pID == 1:
        return math.prod([calculateValues(x) for x in packet[2]])
    elif pID == 2:
        return min([calculateValues(x) for x in packet[2]])
    elif pID == 3:
        return max([calculateValues(x) for x in packet[2]])
    elif pID == 5:
        res = [calculateValues(x) for x in packet[2]]
        return res[0] > res[1]
    elif pID == 6:
        res = [calculateValues(x) for x in packet[2]]
        return res[0] < res[1]
    elif pID == 7:
        res = [calculateValues(x) for x in packet[2]]
        return res[0] == res[1]
    return packet

def readPacket(raw):
    global count
    packet = []
    # HEADER
    pVer    = int(raw[0:3], 2)
    count  += pVer
    pID     = int(raw[3:6], 2)
    raw     = raw[6:]
    if pID == 4:
        data, dataLength = readLiteral(raw)
        packet = [pVer, pID, data]
        return packet, 6+dataLength
    else:
        lengthTypeId = int(raw[0])
        raw = raw[1:]
        if lengthTypeId == 0: # 15 bits define what/how many packets are in this one
            bits = int(raw[:15], 2)
            innerRaw = raw[15:15+bits]
            innerPackets = []
            while len(innerRaw) > 0 and '1' in innerRaw:
                innerPacket, innerPacketLength = readPacket(innerRaw)
                innerRaw = innerRaw[innerPacketLength:]
                innerPackets.append(innerPacket)
            packet = [pVer, pID, copy.deepcopy(innerPackets)]
            return packet, 7+15+bits
        else: # 11 bits define the number of packets in this one
            packetNum = int(raw[:11], 2)
            innerRaw = raw[11:]
            innerPackets = []
            totalInnerPacketLength = 0
            while len(innerPackets) < packetNum and '1' in innerRaw:
                innerPacket, innerPacketLength = readPacket(innerRaw)
                innerRaw = innerRaw[innerPacketLength:]
                innerPackets.append(innerPacket)
                totalInnerPacketLength += innerPacketLength
            packet = [pVer, pID, copy.deepcopy(innerPackets)]
            return packet, 7+11+totalInnerPacketLength

def readLiteral(raw): # read a single literal packet and return its int decimal value
    readPacket = True
    packet = []
    while readPacket:
        packet.append(raw[1:5]) # append current packet to packet
        if raw[0] == '0': # check if this is the last packet to be read
            readPacket = False
        raw = raw[5:]
    return int(''.join(packet), 2), 1+len(' '.join(packet))

def readData(inputFile):
    file1 = open(inputFile, 'r')
    inputData = file1.readlines()
    file1.close()
    data = []
    for i in inputData[0].strip():
        data.append(i)
    START = perf_counter_ns()
    result = puzzle1(copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 1 result is {} and it took {:.3f} ms".format(result, time))
    START = perf_counter_ns()
    result = puzzle2(copy.deepcopy(data))
    time = (perf_counter_ns()-START)/1000000.0
    print("Puzzle 2 result is {} and it took {:.3f} ms\n".format(result, time))

def hexToBin(char):
    mapping = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    return mapping[char]

assert puzzle2('C200B40A82') == 3 # sum 1 + 2
assert puzzle2('04005AC33890') == 54 # product 6 * 9
assert puzzle2('880086C3E88112') == 7 # min(7, 8, 9)
assert puzzle2('CE00C43D881120') == 9 # max(7, 8, 9)
assert puzzle2('D8005AC2A8F0') == 1 # 5 < 15
assert puzzle2('F600BC2D8F') == 0 # 5 > 15
assert puzzle2('9C005AC2F8F0') == 0 # 5 == 15
assert puzzle2('9C0141080250320F1802104A08') == 1 # 1 + 3 == 2 * 2

readData("test.txt")
readData("test2.txt")
readData("test3.txt")
readData("test4.txt")
readData("test5.txt")
readData("test6.txt")
readData("test7.txt")
readData("input.txt")

