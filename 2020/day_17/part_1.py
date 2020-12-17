from collections import defaultdict, deque
from bisect import bisect_left
import re

filename = 'part_1.txt'
from collections import defaultdict
from itertools import product

input = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        input.append([0 if x == '.' else 1 for x in list(line.strip('\n'))])

# build graph
n, m = len(input), len(input[0])
active_cells = set()
for i in range(n):
    for j in range(m):
        if input[i][j]: active_cells.add((i, j, 0))


def neighbors(i, j, z):
    return [(i+ni, j+nj, z+nz) for (ni, nj, nz) in list(product([-1, 0, 1], repeat=3)) if (i+ni, j+nj, z+nz) != (i, j, z)]


for _ in range(6):
    cells_count = defaultdict(int)
    for (i, j, z) in active_cells:
        for ni, nj, nz in neighbors(i, j, z):
            cells_count[(ni, nj, nz)] += 1
    to_active = set([(ni, nj, nz) for (ni, nj, nz) in cells_count if
                     (ni, nj, nz) not in active_cells and cells_count[(ni, nj, nz)] == 3])

    remain_active = set([(ni, nj, nz) for (ni, nj, nz) in active_cells if
                         (ni, nj, nz) in cells_count and cells_count[(ni, nj, nz)] in [2, 3]])
    active_cells = to_active | remain_active

print(len(active_cells))
