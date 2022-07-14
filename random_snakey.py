import random
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def add(x: int, y: int, x_coords: dict):
  x_coords[x] = x_coords.get(x, set([]))
  x_coords[x].add(y)

def check(x: int, y: int, x_coords: dict, n: int):
  if x < -n or n < x:
    return True
  if y < -n or n < y:
    return True
  return x in x_coords.keys() and y in x_coords[x]


def move(x: int, y: int, letters: list, x_coords: dict, n: int):
  left = not check(x, y-1, x_coords, n)
  right = not check(x, y+1, x_coords, n)
  
  if left and right:
    choice = random.choice([True, False])
    left = choice
    right = not choice

  if left:
    add(x, y-1, x_coords)
    return x, y-1, letters[0]
  if right:
    add(x, y+1, x_coords)
    return x, y+1, letters[1]

  raise Exception

def plot(x: list, y: list, n: int, name: str):
  fig = plt.figure()
  ax = fig.add_subplot(111)
  line = Line2D(x, y)
  ax.add_line(line)

  mins = -n-1
  maxs = n+1

  ax.set_xlim(mins, maxs)
  ax.set_ylim(mins, maxs)

  diff = 0

  major_ticks = np.arange(mins-diff, maxs+diff+1, 5)
  minor_ticks = np.arange(mins-diff, maxs+diff+1, 1)

  ax.set_xticks(major_ticks)
  ax.set_xticks(minor_ticks, minor=True)
  ax.set_yticks(major_ticks)
  ax.set_yticks(minor_ticks, minor=True)

  ax.grid(which='both')

  plt.savefig(f'{name}.png')
  plt.close()


def add_counter(orig_path):
    c = 1
    path = f'{orig_path}_{c:04d}'
    while os.path.exists(path + '.txt'):
        c += 1
        path = f'{orig_path}_{c:04d}'

    return path

def run(dir: str, name: str):

  n = 10
  k = 1000

  x_coords: dict = dict()
  
  x = 0
  y = 0
  add(x, y, x_coords)

  all_x: list = [x]
  all_y: list = [y]
  all_c: list = []

  for i in range(k):
    try:
      x, y, c = move(x, y, ["L", "R"], x_coords, n)
      all_x.append(x)
      all_y.append(y)
      all_c.append(c)
      y, x, c = move(y, x, ["U", "D"], x_coords, n)
      all_x.append(x)
      all_y.append(y)
      all_c.append(c)
    except:
      break

  path = add_counter(f'{dir}/{i:03d}_{name}')
  print(path)

  with open(f'{path}.txt', 'w') as f:
    f.write(', '.join(map(str, all_x)) + "\n")
    f.write(', '.join(map(str, all_y)) + "\n")
    f.write(', '.join(map(str, all_c)) + "\n")

  plot(all_x, all_y, n, path)

N: int = 100

for x in range(N):
  run('results', 'res')
