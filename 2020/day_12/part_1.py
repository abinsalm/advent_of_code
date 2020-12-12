filename = 'part_1.txt'

input = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        input.append(line)

x, y = 0, 0
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
MOVES = {'N': NORTH, 'S': SOUTH, 'E': EAST, 'W': WEST}
MOVE = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = EAST
TURNS = {
    NORTH: {90: EAST, 180: SOUTH, 270: WEST},
    EAST: {90: SOUTH, 180: WEST, 270: NORTH},
    SOUTH: {90: WEST, 180: NORTH, 270: EAST},
    WEST: {90: NORTH, 180: EAST, 270: SOUTH},
}

for line in input:
    d, w = line[0], int(line[1:])
    if d in ['R', 'L']:
        if d == 'L': w = 360 - w
        direction = TURNS[direction][w]
        continue

    temp_direction = direction
    if d != 'F':
        temp_direction = MOVES[d]
    shift = MOVE[temp_direction]
    x += shift[0] * w
    y += shift[1] * w

print(x, y, abs(x) + abs(y))
