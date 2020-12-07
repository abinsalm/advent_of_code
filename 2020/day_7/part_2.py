filename = 'part_2_input'

from collections import defaultdict

number_of_bags = 0
graph = defaultdict(lambda: defaultdict(int))
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        if 'contain no other bags' in line: continue
        bag_name = line[:line.index('bags') - 1]
        other_bags_split = line[line.index('bags') + 13:-1].split(',')
        for bag_line in other_bags_split:
            count, name = bag_line.lstrip().split(' ', 1)
            name = name[:name.index('bag') - 1]
            graph[bag_name][name] = int(count)

seen = set()
def dfs(bag_name):
    required_bags = 1
    for next_bag in graph[bag_name]:
        required_bags += graph[bag_name][next_bag] * dfs(next_bag)
    return required_bags


number_of_bags = dfs('shiny gold') - 1

print(f"Number of bags required: {number_of_bags}")
