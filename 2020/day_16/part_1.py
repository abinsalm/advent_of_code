from collections import defaultdict, deque
from bisect import bisect_left
import re

filename = 'part_1.txt'

input = deque()
with open(filename, encoding="utf-8") as f:
    for line in f:
        input.append(line.strip('\n'))

fields = defaultdict(list)
# process fields
while input:
    if not len(input[0]): break
    match = re.match("(.+): (\d+)-(\d+) or (\d+)-(\d+)", input.popleft())
    field = match.group(1)
    first_range = [int(match.group(2)), int(match.group(3))]
    second_range = [int(match.group(4)), int(match.group(5))]
    fields[field].append(first_range)
    fields[field].append(second_range)
    print(field, first_range, second_range)

input.popleft();input.popleft()
my_ticket = list(map(int, input.popleft().split(',')))
print(my_ticket)

input.popleft()
input.popleft()
nearby_tickets = []
while input: nearby_tickets.append(list(map(int, input.popleft().split(','))))

invalid_tickets = []
for ticket in nearby_tickets:
    for value in ticket:
        found = False
        for field in fields:
            if fields[field][0][0] <= value <= fields[field][0][1] or fields[field][1][0] <= value <= fields[field][1][1]:
                found = True
                break
        if not found: invalid_tickets.append(value)

print(sum(invalid_tickets))