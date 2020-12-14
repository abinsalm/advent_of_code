filename = 'part_1.txt'

input = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        input.append(line)

import re
memory = dict()
bit_mask = 2**36-1

def process_instruction(instruction):
    result = re.search('mem\[(.*)].=.(.+)', instruction)
    memory_addr = int(result.group(1))
    value = int(result.group(2))
    value &= bit_mask
    bin_value = bin(value)[2:]
    value_binary = '0' * (36 - len(bin_value)) + bin_value
    return memory_addr, value_binary

mask = None
for line in input:
    if line.startswith('mask'):
        mask = line[7:]
        continue

    memory_addr, value_binary = process_instruction(line)
    new_val = 0
    for i in range(36):
        if mask[i] == 'X':
            new_val = new_val * 2 + (value_binary[i] == '1')
        else:
            new_val = new_val * 2 + (mask[i] == '1')
    print(memory_addr, value_binary, new_val)
    memory[memory_addr] = new_val

print(sum(memory.values()))