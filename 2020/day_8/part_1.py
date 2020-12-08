filename = 'part_1_input'

number_of_bags = 0
seen = set()
instructions = list()
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        # nop +0
        # acc +1
        # jmp +4
        ins, val = line.split(" ")
        val = int(val)
        instructions.append((ins, val))
acc = 0

i = 0

while i not in seen:
    seen.add(i)
    ins, val = instructions[i]
    if ins == 'nop':
        i += 1
    elif ins == 'acc':
        acc += val
        i +=1
    else:
        i += val

print(f"accs : {acc}")
