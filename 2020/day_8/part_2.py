filename = 'part_2_input'

number_of_bags = 0
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

i = 0

seen = set()

def bt(i, acc, changed=0):
    if i >= len(instructions):
        return acc
    elif changed > 1:
        return -1
    elif i in seen: return -1
    else:
        ins, val = instructions[i]
        seen.add(i)
        if ins == 'nop':
            with_actual = bt(i + 1, acc, changed)
            with_skip = bt(i + val, acc, changed+1) if changed == 0 else -1
            return max(with_actual, with_skip)
        elif ins == 'acc':
            return bt(i + 1, acc + val, changed)
        else:
            with_actual = bt(i + val, acc, changed)
            with_skip = bt(i + 1, acc, changed + 1) if changed == 0 else -1
            return max(with_actual, with_skip)


print(f"accs : {bt(0, 0, changed=0)}")
