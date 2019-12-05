#!/usr/bin/python

import itertools

def main(strings):
   space = 100
   ingredients = {}
   for string in strings:
      string = string.split(': ')
      name = string[0]
      string = string[1].split(', ')
      tmp = {}
      for prop in string:
         tmp[prop.split(' ')[0]] = int(prop.split(' ')[1])
      ingredients[name] = tmp
   k = 0
   ingrList = []
   keys = ingredients.keys()
   for a in range(1, 101):
      for b in range(1, 101):
         for c in range(1, 101):
            for d in range(1, 101):
               if a + b + c + d == 100:
                  ingrList.append([
                     '_'.join([keys[0], str(a)]),
                     '_'.join([keys[1], str(b)]),
                     '_'.join([keys[2], str(c)]),
                     '_'.join([keys[3], str(d)])
                  ])
   best = 0
   bestCalorie = 0
   for r in ingrList:
      capacity = 0
      durability = 0
      flavor = 0
      texture = 0
      calories = 0
      for i in r:
         s = i.split('_')
         capacity += int(s[1])*ingredients[s[0]]['capacity']
         durability += int(s[1])*ingredients[s[0]]['durability']
         flavor += int(s[1])*ingredients[s[0]]['flavor']
         texture += int(s[1])*ingredients[s[0]]['texture']
         calories += int(s[1])*ingredients[s[0]]['calories']
      res = max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)
      if res > best:
         best = res
      if calories == 500:
         if res > bestCalorie:
            bestCalorie = res
   print 'New best found[{}]'.format(best)
   print 'New best(with 500 cal) found[{}]'.format(bestCalorie)


inputData = [
   "Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5",
   "PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1",
   "Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6",
   "Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8",
]

#inputData = [
#   'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
#   'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3',
#]

main(inputData)
