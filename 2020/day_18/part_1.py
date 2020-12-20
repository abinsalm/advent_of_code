from collections import defaultdict, deque
from bisect import bisect_left
import re

filename = 'part_1.txt'

input = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        input.append([c for c in list(line.strip('\n')) if c != ' '])


def evaluate(line, start):
    value = 0
    prev_op = '+'

    while start < len(line):
        c = line[start]
        if c.isdigit():
            if prev_op == '+': value += int(c)
            else: value *= int(c)
        elif c in ['+', '*']: prev_op = c
        elif c == '(':
            next_val, start = evaluate(line, start + 1)
            if prev_op == '+': value += next_val
            else: value *= next_val
        else:
            return value, start

        start += 1

    return value, start


print(sum([evaluate(line, 0)[0] for line in input]))