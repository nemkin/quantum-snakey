import random
random.seed(42)

n = 10
k = 10

x_coords: dict = dict()

def add(x: int, y: int):
  x_coords[x] = x_coords.get(x, set([]))
  x_coords[x].add(y)

def check(x: int, y: int):
  return x in x_coords.keys() and y in x_coords[x]

def move(x, y, letters):
  left = not check(x, y-1)
  right = not check(x, y+1)
  
  if left and right:
    choice = random.choice([True, False])
    left = choice
    right = not choice

  if left:
    add(x, y-1)
    return x, y-1, letters[0]
  if right:
    add(x, y+1)
    return x, y+1, letters[1]

x = 0
y = 0

for i in range(k):
  x, y, c = move(x, y, ["L", "R"])
  print(x,y,c)
  y, x, c = move(y, x, ["U", "D"])
  print(x, y, c)
