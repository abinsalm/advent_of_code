filename = 'part_2_input'

numbers = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        numbers.append(int(line))


def two_sum(l, h, target):
    seen = set()
    for i in range(l, h + 1):
        num = numbers[i]
        if target - num in seen: return True
        seen.add(num)
    return False


def find_illegal_number(limit):
    for i in range(limit, len(numbers)):
        if not two_sum(i - limit, i, numbers[i]):
            print(f'number is {numbers[i]}')
            return numbers[i]


number = find_illegal_number(25)
prefix_sum = {0: -1}
curr_sum = 0

for i in range(len(numbers)):
    curr_sum += numbers[i]
    if curr_sum - number in prefix_sum:
        sub_array = numbers[prefix_sum[curr_sum - number] + 1: i + 1]
        print(min(sub_array) + max(sub_array))
        break
    prefix_sum[curr_sum] = i
