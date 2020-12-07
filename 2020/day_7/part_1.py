filename = 'part_1_input'

from collections import defaultdict

number_of_bags = 0
graph = defaultdict(list)
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        if 'contain no other bags' in line: continue
        bag_name = line[:line.index('bags') - 1]
        other_bags_split = line[line.index('bags') + 13:-1].split(',')
        for bag_line in other_bags_split:
            count, name = bag_line.lstrip().split(' ', 1)
            name = name[:name.index('bag') - 1]
            graph[name].append(bag_name)

seen = set()
q = ['shiny gold']
seen.add('shiny gold')
while q:
    bag_name = q.pop()
    for next_bag in graph[bag_name]:
        if next_bag not in seen:
            number_of_bags += 1
            q.append(next_bag)
            seen.add(next_bag)

print(f"Number of bags: {number_of_bags}")
