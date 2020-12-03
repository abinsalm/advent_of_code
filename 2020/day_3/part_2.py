from operator import mul
from functools import reduce

from day_3 import part_1

filename = 'input_part_2'

lines = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        lines.append(line)

line_len = len(lines[0])
lines_count = len(lines)

tree_counts = [part_1.count_trees(slope, lines, lines_count, line_len) for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
print(
    f'Number of trees encountered: {reduce(mul, tree_counts)}')
