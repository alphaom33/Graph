import os
import math

fills = ["*", ":", "-", "|", ",", "/", "\\", "["]

def is_between(test, low, high):
    return test > low and test <= high

def checkness(test):
    for i in range(0, len(ranges) - 1):
        if is_between(test, ranges[i], ranges[i + 1]):
            return fills[i]
    return str(test)

class Vec:
    def __init__(self, x, y):
        self.x = x / 2
        self.y = y
    def get_magnitude(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
    def get_angle(self):
        return math.atan2(self.y, self.x)
    def __str__(self):
        return str(self.x) + ", " + str(self.y)
    def __mul__(self, other):
        self.x = self.x * other
        self.y = self.y * other
        return self

data = [
    {
        "name": "usdf",
        "num": 1,
    },
    {
        "name": "csdf",
        "num": 9,
    },
    {
        "name": "osdf",
        "num": 10,
    },
    {
        "name": "asdf",
        "num": 10,
    },
    {
        "name": "bsdf",
        "num": 45,
    },
    {
        "name": "ysdf",
        "num": 3,
    },
    {
        "name": "vsdf",
        "num": 22,
    },
    ]

ranges = [0.0 for _ in range(0, len(data) + 1)]
for i, d in enumerate(data):
    ranges[i + 1] = ranges[i] + d["num"] / 100 * math.tau
    ranges[i] -= math.pi
ranges[len(ranges) - 1] -= math.pi

screen = [[" " for _ in range(0, os.get_terminal_size().columns)] for _ in range(0, os.get_terminal_size().lines)]
radius = min((os.get_terminal_size().columns - 2) / 2, os.get_terminal_size().lines - 2) / 2

for y in range(0, len(screen)):
    for x in range(0, len(screen[0])):
        vec = Vec(x - (len(screen[0]) / 2), y - (len(screen) / 2))
        if vec.get_magnitude() < radius:
            screen[y][x] = checkness(vec.get_angle())

def calcVec(angle, dst):
    return [(math.sin(angle) * dst) + (len(screen) / 2),
           (math.cos(angle) * (dst * 2)) + (len(screen[0]) / 2)]

def drawLine(angle, name):
    sign = int(math.copysign(1, math.cos(angle)))
    vec = calcVec(angle, radius)
    if screen[int(vec[0])][int(vec[1])] != " ":
        vec = calcVec(angle, radius + 1)
        
    screen[int(vec[0])][int(vec[1])] = "|" if abs(math.sin(angle)) > 0.5 else "-"
    for i in range(sign * 1, sign * 3, sign):
        screen[int(vec[0])][int(vec[1]) + i] = "-"
    if sign < 0:
        name = name[::-1]
    for i, c in enumerate(name):
        screen[int(vec[0])][int(vec[1]) + (sign * (3 + i))] = c
    
def checkAround(center, thingLen, i):
    tmp1 = screen[round(center[0])][round(center[1] - (thingLen / 2 + 1))] 
    tmp2 = screen[round(center[0])][round(center[1] + (thingLen / 2))] 
    if (tmp1 == " " or tmp2 == " "):
        return None
    return tmp1 == fills[i] and tmp2 == fills[i]
    
for i in range(0, len(ranges) - 1):
    angle = (ranges[i] + ranges[i + 1]) / 2
    dst = radius / 2
    vec = calcVec(angle, dst)
    name = data[i]["name"]
    thingLen = len(name)
    while True:
        match checkAround(vec, thingLen, i):
            case False:
                dst += radius / 10
                vec = calcVec(angle, dst)
            case True:
                for i, c in enumerate(name):
                    screen[round(vec[0])][round(vec[1] - (thingLen / 2)) + i] = c
                break
            case None:
                drawLine(angle, name)
                break

for li in screen:
    for c in li:
        print(c, end="")