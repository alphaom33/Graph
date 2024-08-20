import os;

leftScale = 5
leftWidth = 3
up = 2

bottomScale = 10

screenSize = [os.get_terminal_size().columns - leftWidth, os.get_terminal_size().lines - up]

data = [
    {
        "x": 0,
        "y": 4
    },
    {
        "x": 5,
        "y": 0
    },
    {
        "x": 10,
        "y": 10
    }
]

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
                screen[newY - up][i + leftWidth] = "/" if slope > 0 else "\\" if slope < 0 else "-"
    
    screen[(len(screen) - 1) - round(y + up)][round(x + leftWidth)] = "*"
    last = [x, y]

height = os.get_terminal_size().lines - up
for i in range(0, leftScale):
    toPrint = str(round(maxes[1] / leftScale * i))
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