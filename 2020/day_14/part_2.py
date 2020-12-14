filename = 'part_2.txt'

input = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        input.append(line)

import re
from collections import defaultdict
memory = defaultdict(int)
bit_mask = 2 ** 36 - 1


def process_instruction(instruction):
    result = re.search('mem\[(.*)].=.(.+)', instruction)
    memory_addr = int(result.group(1)) & bit_mask
    value = int(result.group(2)) & bit_mask
    bin_memory_addr = bin(memory_addr)[2:]
    bin_memory_addr = '0' * (36 - len(bin_memory_addr)) + bin_memory_addr
    return bin_memory_addr, value


def cal_value(binary_value, curr, i, result):
    if i == len(binary_value):
        result.append(int(''.join(curr), 2))
        return

    if binary_value[i] != 'X':
        cal_value(binary_value, curr + [binary_value[i]], i + 1, result)
    else:
        cal_value(binary_value, curr + ['0'], i + 1, result)
        cal_value(binary_value, curr + ['1'], i + 1, result)


mask = None
for line in input:
    if line.startswith('mask'):
        mask = line[7:]
        continue

    bin_memory_addr, value = process_instruction(line)
    new_val_list = []
    for i in range(36):
        if mask[i] == 'X':
            new_val_list.append('X')
        else:
            new_val_list.append('1' if mask[i] == '1' else bin_memory_addr[i])
    result = []
    masked_value = ''.join(new_val_list)
    cal_value(masked_value, [], 0, result)
    for memory_addr in result: memory[memory_addr] = value

print(sum(memory.values()))
