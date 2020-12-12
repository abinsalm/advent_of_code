filename = 'part_1.txt'

grid = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        grid.append(list(line))

n, m = len(grid), len(grid[0])

matrix = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'L': matrix[i][j] = 0


def get_next_moves(i, j):
    return [(ni, nj) for (ni, nj) in
            [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i - 1, j - 1), (i + 1, j + 1), (i - 1, j + 1),
             (i + 1, j - 1)] if 0 <= ni < n and 0 <= nj < m]


while True:
    changed = False
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1: continue

            nexts = get_next_moves(i, j)

            sum_seats = sum([1 for (ni, nj) in nexts if matrix[ni][nj] != -1 and matrix[ni][nj] & 1])
            if matrix[i][j] == 0 and sum_seats == 0:
                matrix[i][j] = 2
                changed = True
            elif matrix[i][j] == 1 and sum_seats >= 4:
                matrix[i][j] = 1
                changed = True
            elif matrix[i][j] == 1:
                matrix[i][j] = 3
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != -1: matrix[i][j] >>= 1
    if not changed: break

occupied = sum([matrix[i][j] for i in range(n) for j in range(m) if matrix[i][j] == 1])
print(occupied)
