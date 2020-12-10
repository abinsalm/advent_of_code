filename = 'part_2_input'

numbers = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        numbers.append(int(line))
print(numbers)

numbers.sort()
last_number = max(numbers) + 3
numbers = [0] + numbers + [last_number]

comb = set()

# TOP DOWN
from functools import lru_cache


@lru_cache(None)
def backtrack(curr, index):
    if index == len(numbers):
        return 1
    comb = 0
    while index < len(numbers) and numbers[index] - curr <= 3:
        comb += backtrack(numbers[index], index + 1)
        index += 1

    return comb


print('comb: ', backtrack(0, 1))

# BOTTOM UP
# dp = [0] * len(numbers)
# dp[0] = 1
# for i in range(1, len(numbers)):
#     for j in range(i-1, -1, -1):
#         curr_num = numbers[i]
#         prev = numbers[j]
#         if curr_num - prev > 3: break
#         dp[i] += dp[j]
# print(dp[-1])
