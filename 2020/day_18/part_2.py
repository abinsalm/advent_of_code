from collections import defaultdict, deque
from bisect import bisect_left
import re

filename = 'part_2.txt'

input = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        input.append([c for c in list(line.strip('\n')) if c != ' '])

from operator import mul
from functools import reduce
def evaluate(line, start):
    stack = []
    prev_op = '*'

    while start < len(line):
        c = line[start]
        if c.isdigit():
            if prev_op == '+': stack[-1] += int(c)
            else: stack.append(int(c))
        elif c in ['+', '*']:
            prev_op, prev_prev_op = c, prev_op
        elif c == '(':
            next_val, start = evaluate(line, start + 1)
            if prev_op == '+': stack[-1] += next_val
            else: stack.append(next_val)
        else:
            return reduce(mul, stack), start

        start += 1

    return reduce(mul, stack), start


for line in input:
    print(evaluate(line, 0))
print(sum([evaluate(line, 0)[0] for line in input]))