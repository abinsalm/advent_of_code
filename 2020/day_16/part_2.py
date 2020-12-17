from collections import defaultdict, deque
import re
from functools import reduce
from operator import mul

filename = 'part_2.txt'

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

input.popleft();input.popleft()
my_ticket = list(map(int, input.popleft().split(',')))

input.popleft()
input.popleft()
nearby_tickets = []
while input:
    ticket = list(map(int, input.popleft().split(',')))

    value_not_found = False
    for value in ticket:
        found = False
        for field in fields:
            if fields[field][0][0] <= value <= fields[field][0][1] or fields[field][1][0] <= value <= fields[field][1][1]:
                found = True
                break
        if not found:
            value_not_found = True
            break
    if not value_not_found:
        nearby_tickets.append(ticket)

nearby_tickets.extend([my_ticket])

valid_fields = defaultdict(set)
for ticket in nearby_tickets:
    for i, value in enumerate(ticket):
        curr_set = set()
        for field in fields:
            if fields[field][0][0] <= value <= fields[field][0][1] or fields[field][1][0] <= value <= fields[field][1][1]:
                curr_set.add(field)
        if i not in valid_fields:
            valid_fields[i] = curr_set
        else:
            valid_fields[i] &= curr_set
        # print(ticket, value, curr_set, valid_fields)

# print('valid fields: ', valid_fields)
while sum([len(valid_fields[field]) for field in valid_fields]) > len(valid_fields):
    for field in valid_fields:
        if len(valid_fields[field]) == 1:
            for other_field in valid_fields:
                if other_field == field: continue
                valid_fields[other_field] -= valid_fields[field]
# print(sum(invalid_tickets))
print('valid fields: ', valid_fields)
print(reduce(mul, ([my_ticket[x] for x in valid_fields if list(valid_fields[x])[0].startswith('departure')])))