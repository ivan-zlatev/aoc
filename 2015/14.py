#!/tool/pandora64/bin/python

import re

def main(string):
   chart = {}
   for tmp in string:
      tmp = tmp.split(' ')
      # i            = Name
      # chart[i][0]  = speed
      # chart[i][1]  = can fly for
      # chart[i][2]  = should rest for
      # chart[i][3]  = flying time
      # chart[i][4]  = resting time
      # chart[i][5]  = distance traveled
      # chart[i][6]  = Last state
      # chart[i][7]  = Points
      chart[tmp[0]] = [int(tmp[3]), int(tmp[6]), int(tmp[13]), 0, 0, 0, True, 0]
   chart = race(chart, 2503)
   distance = 0
   points = 0
   for racer in chart.keys():
      if distance < chart[racer][5]:
         distance = chart[racer][5]
         winner = racer
      if points < chart[racer][7]:
         points = chart[racer][7]
         winner2 = racer
      print '{}\t{}'.format(racer,chart[racer][5])
   print "Winner (based on distance) is '{}' with total distance traveled: {}".format(winner,distance)
   print "Winner (based on points) is '{}' with total points accumulated: {}".format(winner2,points)

def race(chart, seconds):
   for i in range(1,seconds+1):
      distance = 0
      for racer in chart.keys(): # calculate distance
         if chart[racer][6]: # flying
            if chart[racer][3] < chart[racer][1]: # increase flying time
               chart[racer][3] += 1
               chart[racer][5] += chart[racer][0] # increase distance traveled by speed
            if chart[racer][3] == chart[racer][1]: # if max flying time reached
               chart[racer][3] = 0 # reset flying time
               chart[racer][6] = False # set flag for resting
         else: # resting
            if chart[racer][4] < chart[racer][2]: # increase resting time
               chart[racer][4] += 1
            if chart[racer][4] == chart[racer][2]: # if max resting time reached
               chart[racer][4] = 0 # reset resting time
               chart[racer][6] = True # set flag for flying
         if distance < chart[racer][5]:
            distance = chart[racer][5]
      for racer in chart.keys(): # calculate points
         if chart[racer][5] == distance:
            chart[racer][7] += 1
   return chart


inputString = [
"Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.",
"Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.",
"Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.",
"Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.",
"Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.",
"Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.",
"Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.",
"Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.",
"Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds.",
]

main(inputString)
