from operator import mul

filename = 'part_2.txt'

grid = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        grid.append(list(line))

n, m = len(grid), len(grid[0])

from copy import deepcopy

directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]


def find(i, j, direction, matrix):
    ni, nj = i + direction[0], j + direction[1]
    while 0 <= ni < n and 0 <= nj < m:
        if matrix[ni][nj] == '#': return 1
        if matrix[ni][nj] == 'L': return 0
        ni += direction[0]
        nj += direction[1]
    return 0


while True:
    changed = False
    replica = deepcopy(grid)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.': continue

            occupied_sum = sum([find(i, j, direction, grid) for direction in directions])
            if grid[i][j] == 'L' and occupied_sum == 0:
                replica[i][j] = '#'
                changed = True
            elif grid[i][j] == '#' and occupied_sum >= 5:
                replica[i][j] = 'L'
                changed = True
    grid = replica
    if not changed: break

occupied = 0
for i in range(n):
    for j in range(m):
        occupied += grid[i][j] == '#'
print(occupied)
