filename = 'part_2.txt'

input = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        input.append(line)

busses = [(int(x), i) for i, x in enumerate(input[1].split(',')) if x != 'x']

from functools import reduce
from operator import mul

m = 0
while True:
    if all([(m + i) % x == 0 for x, i in busses]): break
    print([x for x, i in busses if (m+i) % x == 0])
    m += reduce(mul, [x for x, i in busses if (m+i) % x == 0])

print(m)
