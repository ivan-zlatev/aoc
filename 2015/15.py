#!/usr/bin/python

def main(strings):
   ingredients = {}
   for string in strings:
      string = string.split(': ')
      name = string[0]
      string = string[1].split(', ')
      tmp = {}
      for prop in string:
         tmp[prop.split(' ')[0]] = prop.split(' ')[1]
      ingredients[name] = tmp
   for i in ingredients.keys():
      print 'Key: {}\tValues: {}'.format(i,ingredients[i])
   for a in ingredients.keys():
      for b in ingredients.keys():
         if b not in [a]:
            for c in ingredients.keys():
               if b not in [a,b]:
                  for d in ingredients.keys():
                     if b not in [a,b,c]:
                        True



inputString = [
"Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5",
"PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1",
"Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6",
"Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8",
]

main(inputString)
