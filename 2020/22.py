#!/usr/bin/python

import copy
import re
import math
import sys

sys.setrecursionlimit(9999)

def main(data):
   p1Deck = numerize(data[0][1:])
   p2Deck = numerize(data[1][1:])
   while len(p1Deck) > 0 and len(p2Deck) > 0:
      p1Deck, p2Deck = playRound(p1Deck, p2Deck)
   if len(p1Deck) > 0:
      print "Q1: Player 1 wins with a score of {}".format(calculateScore(p1Deck))
   else:
      print "Q1: Player 2 wins with a score of {}".format(calculateScore(p2Deck))
   p1Deck = numerize(data[0][1:])
   p2Deck = numerize(data[1][1:])
   decks = []
   i = 0
   while len(p1Deck) > 0 and len(p2Deck) > 0:
      i += 1
      p1Deck, p2Deck, decks, inSubgame = playRoundRecursive(p1Deck, p2Deck, decks)
      #print i, p1Deck, p2Deck
   if len(p1Deck) > 0:
      print "Q1: Player 1 wins with a score of {}".format(calculateScore(p1Deck))
   else:
      print "Q1: Player 2 wins with a score of {}".format(calculateScore(p2Deck))

def calculateScore(data):
   weight = len(data)
   result = 0
   while len(data) > 0:
      result += data[0]*weight
      data = data[1:]
      weight -= 1
   return result

def numerize(data):
   for i in range(len(data)):
      data[i] = int(data[i])
   return data

def playRoundRecursive(p1Deck, p2Deck, decks, inSubgame = False):
   #if inSubgame:
   #   print '\t',
   #print p1Deck, p2Deck
   if [p1Deck, p2Deck] in decks:
      #print 'recursion!, player1 wins'
      return True
   decks.append([p1Deck, p2Deck])
   card1 = p1Deck[0]
   p1Deck = p1Deck[1:]
   card2 = p2Deck[0]
   p2Deck = p2Deck[1:]
   if len(p1Deck) >= card1 and len(p2Deck) >= card2:
      #print "NEW GAME BEGINS"
      if playRoundRecursive(p1Deck[:card1], p2Deck[:card2], [], True):
         #print "player1 wins the subgame"
         p1Deck.append(card1)
         p1Deck.append(card2)
      else:
         #print "player2 wins the subgame"
         p2Deck.append(card2)
         p2Deck.append(card1)
   else:
      if card1 > card2:
         p1Deck.append(card1)
         p1Deck.append(card2)
      else:
         p2Deck.append(card2)
         p2Deck.append(card1)
   if inSubgame:
      if len(p1Deck) == 0:
         return False
      elif len(p2Deck) == 0:
         return True
      else:
         return playRoundRecursive(p1Deck, p2Deck, decks, inSubgame)
   else:
      return p1Deck, p2Deck, decks, inSubgame

def playRound(p1Deck, p2Deck):
   card1 = p1Deck[0]
   p1Deck = p1Deck[1:]
   card2 = p2Deck[0]
   p2Deck = p2Deck[1:]
   if card1 > card2:
      p1Deck.append(card1)
      p1Deck.append(card2)
   else:
      p2Deck.append(card2)
      p2Deck.append(card1)
   return p1Deck, p2Deck

inputData = [
   [
   'Player 1:',
   '9',
   '2',
   '6',
   '3',
   '1',
   ],[
   'Player 2:',
   '5',
   '8',
   '4',
   '7',
   '10',
   ]
]
main(inputData)

inputData = [
   [
   'Player 1:',
   '43',
   '19',
   ],[
   'Player 2:',
   '2',
   '29',
   '14',
   ]
]
#main(inputData)

inputData = [
   [
   'Player 1:',
   '30',
   '42',
   '25',
   '7',
   '29',
   '1',
   '16',
   '50',
   '11',
   '40',
   '4',
   '41',
   '3',
   '12',
   '8',
   '20',
   '32',
   '38',
   '31',
   '2',
   '44',
   '28',
   '33',
   '18',
   '10',
   ],[
   'Player 2:',
   '36',
   '13',
   '46',
   '15',
   '27',
   '45',
   '5',
   '19',
   '39',
   '24',
   '14',
   '9',
   '17',
   '22',
   '37',
   '47',
   '43',
   '21',
   '6',
   '35',
   '23',
   '48',
   '34',
   '26',
   '49',
   ]
]
main(inputData)

