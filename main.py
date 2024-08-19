import os

spacing = 1
labelNum = 10

data = [
    {
        "name": "ninth",
        "num": 24.3
    },
    {
        "name": "graduate",
        "num": 41.4
    },
    {
        "name": "wowthatsgreat",
        "num": 102
    }
]

biggest = len(max(data, key=lambda x: len(x["name"]))["name"]) + spacing

maximum = max(data, key=lambda x: x["num"])["num"]
size = (os.get_terminal_size().columns - biggest) / maximum

dst = (os.get_terminal_size().columns - biggest) / labelNum
print((" " * biggest) + "0" + (" " * (round(dst) - 1)), end="")
for i in range(1, labelNum):
    toPrint = str(round(maximum / (labelNum - i), 2))
    print(toPrint + (" " * (round(dst) - len(toPrint))), end="")
print("")

for d in data:
    ms = d["num"]
    ms_bar = round(ms * size)
    print(d["name"] + " " * (biggest - len(d["name"])) + "*" * ms_bar)