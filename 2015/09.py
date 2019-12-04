#!/tool/pandora64/bin/python

import re

def main(strings):
   routes = {}
   fullRoutes = {}
   locations = []
   for string in strings:
      FROM = string.split(' ')[0]
      TO = string.split(' ')[2]
      distance = int(string.split(' = ')[1])
      routes['{}_{}'.format(FROM, TO)] = distance
      routes['{}_{}'.format(TO, FROM)] = distance
      if FROM not in locations:
         locations.append(FROM)
      if TO not in locations:
         locations.append(TO)
   for stopOne in locations:
      for stopTwo in locations:
         if stopTwo not in {stopOne}:
            stopTwoDist = routes['{}_{}'.format(stopOne,stopTwo)]
            for stopThree in locations:
               if stopThree not in {stopOne,stopTwo}:
                  stopThreeDist = routes['{}_{}'.format(stopTwo,stopThree)]
                  for stopFour in locations:
                     if stopFour not in {stopOne,stopTwo,stopThree}:
                        stopFourDist = routes['{}_{}'.format(stopThree,stopFour)]
                        for stopFive in locations:
                           if stopFive not in {stopOne,stopTwo,stopThree,stopFour}:
                              stopFiveDist = routes['{}_{}'.format(stopFour,stopFive)]
                              for stopSix in locations:
                                 if stopSix not in {stopOne,stopTwo,stopThree,stopFour,stopFive}:
                                    stopSixDist = routes['{}_{}'.format(stopFive,stopSix)]
                                    for stopSeven in locations:
                                       if stopSeven not in {stopOne,stopTwo,stopThree,stopFour,stopFive,stopSix}:
                                          stopSevenDist = routes['{}_{}'.format(stopSix,stopSeven)]
                                          for stopEight in locations:
                                             if stopEight not in {stopOne,stopTwo,stopThree,stopFour,stopFive,stopSix,stopSeven}:
                                                stopEightDist = routes['{}_{}'.format(stopSeven,stopEight)]
                                                dist = stopTwoDist + stopThreeDist + stopFourDist + stopFiveDist + stopSixDist + stopSevenDist + stopEightDist
                                                fullRoutes['{}->{}->{}->{}->{}->{}->{}->{}'.format(stopOne,stopTwo,stopThree,stopFour,stopFive,stopSix,stopSeven,stopEight)] = dist
   distMax = 0
   distMin = 100000
   for route in fullRoutes.keys():
      if fullRoutes[route] < distMin:
         distMin = fullRoutes[route]
      if fullRoutes[route] > distMax:
         distMax = fullRoutes[route]
      #print "{}\t{}".format(route,fullRoutes[route])
   print "Results: {} {}".format(distMin, distMax)

inputString = [
"Tristram to AlphaCentauri = 34",
"Tristram to Snowdin = 100",
"Tristram to Tambi = 63",
"Tristram to Faerun = 108",
"Tristram to Norrath = 111",
"Tristram to Straylight = 89",
"Tristram to Arbre = 132",
"AlphaCentauri to Snowdin = 4",
"AlphaCentauri to Tambi = 79",
"AlphaCentauri to Faerun = 44",
"AlphaCentauri to Norrath = 147",
"AlphaCentauri to Straylight = 133",
"AlphaCentauri to Arbre = 74",
"Snowdin to Tambi = 105",
"Snowdin to Faerun = 95",
"Snowdin to Norrath = 48",
"Snowdin to Straylight = 88",
"Snowdin to Arbre = 7",
"Tambi to Faerun = 68",
"Tambi to Norrath = 134",
"Tambi to Straylight = 107",
"Tambi to Arbre = 40",
"Faerun to Norrath = 11",
"Faerun to Straylight = 66",
"Faerun to Arbre = 144",
"Norrath to Straylight = 115",
"Norrath to Arbre = 135",
"Straylight to Arbre = 127",
]

main(inputString)
#main2(inputString2)
