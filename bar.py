import os
from enum import Enum

spacing = 1
labelNum = 10

class Type(Enum):
    NOTHING = 0
    PARETO = 1
    HISTOGRAM = 2

type = Type.HISTOGRAM

data = [
    {
        "name": "murder",
        "num": 2.6
    },
    {
        "name": "rape",
        "num": 33.4
    },
    {
        "name": "robbery",
        "num": 93.3
    },
    {
        "name": "house burglary",
        "num": 911.7
    },
    {
        "name": "motor vehicle theft",
        "num": 550.7
    },
    {
        "name": "assault",
        "num": 125.3
    }
]

if (type == Type.HISTOGRAM):
    startData = [31,39,53,47,40,49,53,47,45,26,39,79,45,50,36,49,45,49,43,48,54,50,43,42,42,35,49,45,42,58,42,55,45,71,50,57,49,50,45,46,53,48,53,37,56,63,41,41,51,48]
    startData.sort()

    classWidth = round((max(startData) - min(startData)) / 5)
    data = []
    for i in range(min(startData), max(startData), classWidth):
        data.append({
            "name": (str(i) + " - " + str(i + (classWidth - 1))),
            "num": len(list(filter(lambda x: x >= i and x < i + classWidth, startData)))

        })

if (type == Type.PARETO):
    data.sort(key=lambda x: x["num"], reverse=True)

biggest = len(max(data, key=lambda x: len(x["name"]))["name"]) + spacing

maximum = max(data, key=lambda x: x["num"])["num"]
size = (os.get_terminal_size().columns - biggest) / maximum

dst = (os.get_terminal_size().columns - biggest) / labelNum
print((" " * biggest) + "0" + (" " * (round(dst) - 1)), end="")
for i in range(1, labelNum):
    toPrint = str(round(maximum / labelNum * i, 2))
    print(toPrint + (" " * (round(dst) - len(toPrint))), end="")
print("")

for d in data:
    ms = d["num"]
    ms_bar = round(ms * size)
    print(d["name"] + " " * (biggest - len(d["name"])) + "*" * ms_bar)