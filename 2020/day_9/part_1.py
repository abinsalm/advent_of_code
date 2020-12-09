filename = 'part_1_input'

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

for i in range(25, len(numbers)):
    if not two_sum(i-25, i, numbers[i]):
        print(f'number is {numbers[i]}')
        break