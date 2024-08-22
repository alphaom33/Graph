import functools

data = [11, 12, 13, 21, 24]
data.sort()
data = list(map(str, data))

stems = list(set(map(lambda x: x[:len(x) - 1], data)))
stems.sort()

for s in stems:
    toPrint = list(map(lambda x: x[len(x) - 1:], filter(lambda x: x[:len(x) - 1] == s, data)))
    toPrint.sort()
    print(s + "|" + str(functools.reduce(lambda a, b: a + " " + b, toPrint)))