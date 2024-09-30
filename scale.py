def calc_dsts(width, data, start, numTicks):
  return [(width - start) / numTicks,
          (max(data) - min(data)) / (numTicks - 1)]

def draw_scale(screen, data, numTicks, start = 0, draw_line = True, invert=False):
  out = []
  numSpot = 0 if invert else len(screen) - 1
  barSpot = 1 if invert else len(screen) - 2
  
  [tickDst, tickSize] = calc_dsts(len(screen[0]), data, start, numTicks)
  for i in range(0, numTicks):
    pos = int(i * tickDst + (tickDst / 2)) + start
    num = round(tickSize * i + min(data), 1)
    out.append([pos, num, 0])
    for j, c in enumerate(str(num)):
      screen[numSpot][pos + j - round(len(str(num)) / 2)] = c

  if (draw_line):
    for i in range(start, len(screen[0])):
      screen[barSpot][i] = "-"

  return [tickDst, tickSize, out]