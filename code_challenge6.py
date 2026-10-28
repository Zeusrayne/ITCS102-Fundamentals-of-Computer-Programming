#code challenge 6

rows = int(input("Put how many rows you want to put --->"))

for x in range(0, rows):
  for y in range(0, rows):
    if x+y == rows-1 or x == y:
      print("*", end = " ")
    else:
      print(" ", end = " ")
  print()