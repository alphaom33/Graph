import os
import statistics
import math

data = [1, 3, 4, 5, 9]

numTicks = 5

screen = [[" " for i in range(0, os.get_terminal_size().columns)] for j in range(0, os.get_terminal_size().lines)]

tickDst = len(screen[0]) / numTicks
tickSize = (max(data) - min(data)) / (numTicks - 1)
for i in range(0, numTicks):
  pos = int(i * tickDst + (tickDst / 2))
  num = round(tickSize * i + min(data), 1)
  for j, c in enumerate(str(num)):
    screen[len(screen) - 1][pos + j - round(len(str(num)) / 2)] = c

for i in range(0, len(screen[0])):
  screen[len(screen) - 2][i] = "-"

min = min(data)
med = statistics.median(data)
q1 = statistics.median(data[:int(len(data) / 2)])
q3 = statistics.median(data[math.ceil(len(data) / 2):])
max = max(data)

def draw_bar(pos):
  height = (len(screen) - 2) / 4
  half = (len(screen) - 2) / 2
  for y in range(int(half - height), int(half + height)):
    screen[y][int(pos / max * len(screen[0])) - 2] = "|"

def draw_line(pos1, pos2, height):
  for x in range(math.ceil(pos1 / max * len(screen[0])) - 2, int(pos2 / max * len(screen[0])) - 2):
    screen[int(height)][x] = "-"
    
def draw_between(pos1, pos2):
  draw_line(pos1, pos2, (len(screen) - 2) / 2 - 1)
  
def draw_around(pos1, pos2):
  height = (len(screen) - 2) / 4
  half = (len(screen) - 2) / 2
  draw_line(pos1, pos2, half - height)
  draw_line(pos1, pos2, half + height - 1)

draw_bar(min)
draw_between(min, q1)
draw_bar(q1)
draw_around(q1, med)
draw_bar(med)
draw_around(med, q3)
draw_bar(q3)
draw_between(q3, max)
draw_bar(max)

for li in screen:
  for c in li:
    print(c, end="")