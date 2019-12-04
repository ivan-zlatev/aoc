#!/usr/bin/python

def main():
   grid = []
   i = 20151125
   y = 0
   while True:
      y -= 1
      if y == -1:
         grid.append([i])
         y = len(grid)-1
      else:
         grid[y].append(i)
      i = i * 252533
      i = i % 33554393
      if len(grid) > 2947-1:
         if len(grid[2947-1]) > 3029-1:
            print grid[2947-1][3029-1]
            break
#To continue, please consult the code grid in the manual.  Enter the code at row 2947, column 3029.

main()
