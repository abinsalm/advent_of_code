filename = 'part_2.txt'

input = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        input.append(line)

wx, wy = 10, 1
x, y = 0, 0
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
MOVES = {'N': NORTH, 'S': SOUTH, 'E': EAST, 'W': WEST}
MOVE = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def rotate_right(degree, wx, wy):
    if degree == 90:
        return wy, -wx
    if degree == 180:
        return -wx, -wy
    if degree == 270:
        return -wy, wx


for line in input:
    d, w = line[0], int(line[1:])
    if d in ['R', 'L']:
        if d == 'L': w = 360 - w
        wx, wy = rotate_right(w, wx, wy)
        continue

    if d in MOVES:
        wx, wy = wx + MOVE[MOVES[d]][0] * w, wy + MOVE[MOVES[d]][1] * w
        continue

    x += (wx) * w
    y += (wy) * w

print(x, y, abs(x) + abs(y))
