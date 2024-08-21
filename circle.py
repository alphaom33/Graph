import os
import math

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getMagnitude(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))



screen = [[" " for _ in range(0, os.get_terminal_size().columns)] for _ in range(0, os.get_terminal_size().lines)]

for y in range(0, len(screen)):
    for x in range(0, len(screen[0])):
        vec = Vec(x - (len(screen[0]) / 2), y - (len(screen) / 2))
        if vec.getMagnitude() < 5:
            screen[y][x] = "*"

for l in screen:
    for c in l:
        print(c, end="")