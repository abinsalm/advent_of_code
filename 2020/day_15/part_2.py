from collections import defaultdict, deque

filename = 'part_1.txt'

input = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        input = line.strip('\n').split(',')

seen = defaultdict(lambda: deque(maxlen=2))

for i, num in enumerate(input):
    seen[int(num)].append(i)

last_seen = int(input[-1])
for i in range(len(input), 30000000):
    if last_seen in seen and len(seen[last_seen]) == 1:
        last_seen = 0
        seen[last_seen].append(i)
    else:
        last_seen = seen[last_seen][-1] - seen[last_seen][-2]
        seen[last_seen].append(i)
print(last_seen)
