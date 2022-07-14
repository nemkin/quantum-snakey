import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

#random.seed(42)

n = 10
k = 1000

x_coords: dict = dict()

def add(x: int, y: int):
  x_coords[x] = x_coords.get(x, set([]))
  x_coords[x].add(y)

def check(x: int, y: int):
  if x < -n or n < x:
    return True
  if y < -n or n < y:
    return True
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

  raise Exception

def plot(x, y):
  fig = plt.figure()
  ax = fig.add_subplot(111)
  line = Line2D(x, y)
  ax.add_line(line)

  mins = -n-1 # min(min(x),min(y))-1
  maxs = n+1  # max(max(x),max(y))+1

  ax.set_xlim(mins, maxs)
  ax.set_ylim(mins, maxs)

  #ax.figure(figsize=(maxx-minx+1, maxy-miny+1))
  #sc = plt.scatter(x, y, s=40**2, marker='s', cmap='gist_rainbow')
  #ax.scatter(x, y, s=(maxs-mins+1)**2)
  #ax.axis('equal')

  diff = 0

  major_ticks = np.arange(mins-diff, maxs+diff+1, 5)
  minor_ticks = np.arange(mins-diff, maxs+diff+1, 1)

  ax.set_xticks(major_ticks)
  ax.set_xticks(minor_ticks, minor=True)
  ax.set_yticks(major_ticks)
  ax.set_yticks(minor_ticks, minor=True)

  ax.grid(which='both')

  plt.show()

x = 0
y = 0

all_x = [x]
all_y = [y]
all_c = []

for i in range(k):
  try:
    x, y, c = move(x, y, ["L", "R"])
    all_x.append(x)
    all_y.append(y)
    all_c.append(c)
    y, x, c = move(y, x, ["U", "D"])
    all_x.append(x)
    all_y.append(y)
    all_c.append(c)
  except:
    break

print(all_x)
print(all_y)
print(all_c)

plot(all_x, all_y)
