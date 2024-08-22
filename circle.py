import os
import math

fills = ["*", ":", "-", "|", ",", "/", "\\", "["]

def is_between(test, low, high):
    return test > low and test <= high

def checkness(test):
    for i in range(0, len(ranges) - 1):
        if is_between(test, ranges[i], ranges[i + 1]):
            return fills[i]
    return print(test)

class Vec:
    def __init__(self, x, y):
        self.x = x / 2
        self.y = y
    def get_magnitude(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
    def get_angle(self):
        return math.atan2(self.y, self.x)

data = [
    {
        "name": "asdf",
        "num": 30,
    },
    {
        "name": "bsdf",
        "num": 50,
    },
    {
        "name": "vsdf",
        "num": 20,
    },
    ]
labels = ["a", "b", "c", "d"]
ranges = [0 for _ in range(0, len(data) + 1)]
for i, d in enumerate(data):
    ranges[i + 1] = ranges[i] + ((d["num"] / 100) * math.tau)
    ranges[i] -= math.pi
ranges[len(ranges) - 1] -= math.pi

screen = [[" " for _ in range(0, os.get_terminal_size().columns)] for _ in range(0, os.get_terminal_size().lines)]
radius = min(os.get_terminal_size().columns / 2, os.get_terminal_size().lines) / 2

for y in range(0, len(screen)):
    for x in range(0, len(screen[0])):
        vec = Vec(x - (len(screen[0]) / 2), y - (len(screen) / 2))
        if vec.get_magnitude() < radius:
            screen[y][x] = checkness(vec.get_angle())

for i in range(0, len(ranges) - 1):
    biggest = (0, 0)
    for j, l in enumerate(screen):
        count = 0
        for c in l:
            if c == fills[i]:
                count += 1
        biggest = max(biggest, (count, j), key=lambda x: x[0])
    start = screen[biggest[1]].index(fills[i])
    for j, c in enumerate(data[i]["name"]):
        screen[biggest[1]][start + j + round((biggest[1] / 2))] = c



for l in screen:
    for c in l:
        print(c, end="")