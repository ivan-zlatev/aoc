#!/tool/pandora64/bin/python

import re

def main(string):
   happinessChart = {}
   people = ['Me']
   for line in string:
      line = line.split(' ')
      if line[0] not in people:
         people.append(line[0])
         happinessChart['Me_'+line[0]] = 0
         happinessChart[line[0]+'_Me'] = 0
      if line[2] == 'lose':
         happinessChart[line[0]+'_'+line[10][:-1]] = int('-{}'.format(line[3]))
      else:
         happinessChart[line[0]+'_'+line[10][:-1]] = int('{}'.format(line[3]))
   print happinessChart
   print people
   best = 0
   for person1 in people:
      for person2 in people:
         if person2 not in {person1}:
            for person3 in people:
               if person3 not in {person1,person2}:
                  for person4 in people:
                     if person4 not in {person1,person2,person3}:
                        for person5 in people:
                           if person5 not in {person1,person2,person3,person4}:
                              for person6 in people:
                                 if person6 not in {person1,person2,person3,person4,person5}:
                                    for person7 in people:
                                       if person7 not in {person1,person2,person3,person4,person5,person6}:
                                          for person8 in people:
                                             if person8 not in {person1,person2,person3,person4,person5,person6,person7}:
                                                for person9 in people:
                                                   if person9 not in {person1,person2,person3,person4,person5,person6,person7,person8}:
                                                      happiness1 = happinessChart['{}_{}'.format(person1,person2)] + happinessChart['{}_{}'.format(person2,person1)]
                                                      happiness2 = happinessChart['{}_{}'.format(person2,person3)] + happinessChart['{}_{}'.format(person3,person2)]
                                                      happiness3 = happinessChart['{}_{}'.format(person3,person4)] + happinessChart['{}_{}'.format(person4,person3)]
                                                      happiness4 = happinessChart['{}_{}'.format(person4,person5)] + happinessChart['{}_{}'.format(person5,person4)]
                                                      happiness5 = happinessChart['{}_{}'.format(person5,person6)] + happinessChart['{}_{}'.format(person6,person5)]
                                                      happiness6 = happinessChart['{}_{}'.format(person6,person7)] + happinessChart['{}_{}'.format(person7,person6)]
                                                      happiness7 = happinessChart['{}_{}'.format(person7,person8)] + happinessChart['{}_{}'.format(person8,person7)]
                                                      happiness8 = happinessChart['{}_{}'.format(person8,person9)] + happinessChart['{}_{}'.format(person9,person8)]
                                                      happiness9 = happinessChart['{}_{}'.format(person9,person1)] + happinessChart['{}_{}'.format(person1,person9)]
                                                      totalHappiness = happiness1+happiness2+happiness3+happiness4+happiness5+happiness6+happiness7+happiness8+happiness9
                                                      if best < totalHappiness:
                                                         best = totalHappiness
   print best

inputString = [
"Alice would lose 57 happiness units by sitting next to Bob.",
"Alice would lose 62 happiness units by sitting next to Carol.",
"Alice would lose 75 happiness units by sitting next to David.",
"Alice would gain 71 happiness units by sitting next to Eric.",
"Alice would lose 22 happiness units by sitting next to Frank.",
"Alice would lose 23 happiness units by sitting next to George.",
"Alice would lose 76 happiness units by sitting next to Mallory.",
"Bob would lose 14 happiness units by sitting next to Alice.",
"Bob would gain 48 happiness units by sitting next to Carol.",
"Bob would gain 89 happiness units by sitting next to David.",
"Bob would gain 86 happiness units by sitting next to Eric.",
"Bob would lose 2 happiness units by sitting next to Frank.",
"Bob would gain 27 happiness units by sitting next to George.",
"Bob would gain 19 happiness units by sitting next to Mallory.",
"Carol would gain 37 happiness units by sitting next to Alice.",
"Carol would gain 45 happiness units by sitting next to Bob.",
"Carol would gain 24 happiness units by sitting next to David.",
"Carol would gain 5 happiness units by sitting next to Eric.",
"Carol would lose 68 happiness units by sitting next to Frank.",
"Carol would lose 25 happiness units by sitting next to George.",
"Carol would gain 30 happiness units by sitting next to Mallory.",
"David would lose 51 happiness units by sitting next to Alice.",
"David would gain 34 happiness units by sitting next to Bob.",
"David would gain 99 happiness units by sitting next to Carol.",
"David would gain 91 happiness units by sitting next to Eric.",
"David would lose 38 happiness units by sitting next to Frank.",
"David would gain 60 happiness units by sitting next to George.",
"David would lose 63 happiness units by sitting next to Mallory.",
"Eric would gain 23 happiness units by sitting next to Alice.",
"Eric would lose 69 happiness units by sitting next to Bob.",
"Eric would lose 33 happiness units by sitting next to Carol.",
"Eric would lose 47 happiness units by sitting next to David.",
"Eric would gain 75 happiness units by sitting next to Frank.",
"Eric would gain 82 happiness units by sitting next to George.",
"Eric would gain 13 happiness units by sitting next to Mallory.",
"Frank would gain 77 happiness units by sitting next to Alice.",
"Frank would gain 27 happiness units by sitting next to Bob.",
"Frank would lose 87 happiness units by sitting next to Carol.",
"Frank would gain 74 happiness units by sitting next to David.",
"Frank would lose 41 happiness units by sitting next to Eric.",
"Frank would lose 99 happiness units by sitting next to George.",
"Frank would gain 26 happiness units by sitting next to Mallory.",
"George would lose 63 happiness units by sitting next to Alice.",
"George would lose 51 happiness units by sitting next to Bob.",
"George would lose 60 happiness units by sitting next to Carol.",
"George would gain 30 happiness units by sitting next to David.",
"George would lose 100 happiness units by sitting next to Eric.",
"George would lose 63 happiness units by sitting next to Frank.",
"George would gain 57 happiness units by sitting next to Mallory.",
"Mallory would lose 71 happiness units by sitting next to Alice.",
"Mallory would lose 28 happiness units by sitting next to Bob.",
"Mallory would lose 10 happiness units by sitting next to Carol.",
"Mallory would gain 44 happiness units by sitting next to David.",
"Mallory would gain 22 happiness units by sitting next to Eric.",
"Mallory would gain 79 happiness units by sitting next to Frank.",
"Mallory would lose 16 happiness units by sitting next to George.",
]

main(inputString)
#main2(inputString2)
