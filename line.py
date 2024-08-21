import os;

leftScale = 5
leftWidth = 4
up = 2

bottomScale = 10

screenSize = [os.get_terminal_size().columns - leftWidth, os.get_terminal_size().lines - up]

data = [
    {
        "x": 1,
        "y": 3817
    },
    {
        "x": 2,
        "y": 3815
    },
    {
        "x": 3,
        "y": 3810
    },
    {
        "x": 4,
        "y": 3812
    },
    {
        "x": 5,
        "y": 3808
    },
    {
        "x": 6,
        "y": 3803
    },
    {
        "x": 7,
        "y": 3798
    },
    {
        "x": 8,
        "y": 3797
    },
    {
        "x": 9,
        "y": 3795
    },
    {
        "x": 10,
        "y": 3797
    },
    {
        "x": 11,
        "y": 3802
    },
    {
        "x": 12,
        "y": 3807
    },
    {
        "x": 13,
        "y": 3811
    },
    {
        "x": 14,
        "y": 3816
    },
    {
        "x": 15,
        "y": 3817
    },
]

min = min(data, key=lambda x: x["y"])["y"]
for d in data:
    d["y"] -= min

data.sort(key=lambda x: x["x"])

screen = []
for i in range(0, os.get_terminal_size().lines):
    tmp = []
    for j in range(0, os.get_terminal_size().columns):
        tmp.append(" ")
    screen.append(tmp)

maxes = [max(data, key=lambda x: x["x"])["x"], max(data, key=lambda x: x["y"])["y"]]

size = [(screenSize[0] - 1) / maxes[0], (screenSize[1] - 1) / maxes[1]]

last = []
for d in data:
    y = d["y"] * size[1]
    x = d["x"] * size[0]
    
    if len(last) > 0:
        slope = (y - last[1]) / (x - last[0])
        for i in range(round(last[0]), round(x)):
            what = (slope * (i - last[0])) + last[1]
            newY = (len(screen) - 1) - round(what)
            if (screen[newY - up][i + leftWidth] != "*"):
                screen[newY - up][i + leftWidth] = "/" if slope > 0 else "\\" if slope < -0 else "-"
    
    screen[(len(screen) - 1) - round(y + up)][round(x + leftWidth)] = "*"
    last = [x, y]

height = os.get_terminal_size().lines - up
for i in range(0, leftScale):
    toPrint = str(round((maxes[1]) / leftScale * i) + min)
    toPrint += " " * (leftWidth - len(toPrint))
    for j, s in enumerate(toPrint):
        screen[(height - 1) - round((height / leftScale) * i)][j] = s
for i in range (0, height):
    screen[i][leftWidth] = "|"

width = os.get_terminal_size().columns
for i in range(leftWidth, width):
    screen[os.get_terminal_size().lines - 2][i] = "-"

numSize = width / bottomScale
for i in range(0, bottomScale):
    toPrint = str(round(maxes[0] / bottomScale * i))
    toPrint += " " * (round(len(toPrint) - numSize))
    screen[os.get_terminal_size().lines - 1][round(numSize * i) + 1] = toPrint

for l in screen:
    for c in l:
        print(c, end="")