from operator import mul

filename = 'part_1_input'

numbers = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        numbers.append(int(line))
numbers.sort()
last_number = max(numbers) + 3
numbers = [0] + numbers + [last_number]

count_1 = 0
count_3 = 0
for n1, n2 in zip(numbers, numbers[1:]):
    diff = n2 - n1
    if diff == 1:
        count_1 += 1
    elif diff == 3:
        count_3 += 1

diff = [b - a for (a, b) in zip(numbers, numbers[1:])]
from collections import Counter
from functools import reduce

counter = Counter(diff)
print(reduce(mul, counter.values()))
