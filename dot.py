import os
import scale

numTicks = 5

data = [1, 1.5, 2, 1, 4, 5]
screen = [[" " for j in range(0, os.get_terminal_size().columns)] for i in range(0, os.get_terminal_size().lines)]

drawn_scale = scale.draw_scale(screen, data, numTicks)
# tickDst = len(screen[0]) / numTicks
tickSize = (max(data) - (min(data))) / (numTicks - 1)
# for i in range(0, numTicks):
#   pos = int(i * tickDst + (tickDst / 2))
#   num = round(tickSize * i + min(data), 1)
#   poses.append([pos, num, 0])
#   for j, c in enumerate(str(num)):
#     screen[len(screen) - 1][pos + j - round(len(str(num)) / 2)] = c

# for i in range(0, len(screen[0])):
#   screen[len(screen) - 2][i] = "-"

for d in data:
  for i, p in enumerate(drawn_scale[2]):
    if p[1] - (tickSize / 2) < d and d <= p[1] + (drawn_scale[1] / 2):
      drawn_scale[2][i][2] += 1
print(drawn_scale)

for p, _, v in drawn_scale[2]:
  for i in range(0, v):
    screen[len(screen) - 3 - i][p - 1] = "*"

for li in screen:
  for c in li:
    print(c, end="")