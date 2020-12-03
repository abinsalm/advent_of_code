filename = 'input_part_2'

with open(filename, encoding="utf-8") as f:
    lines = [int(num.rstrip('\n')) for num in f.readlines()]
    lines.sort()
    for i, number in enumerate(lines):
        left, right = i + 1, len(lines) - 1
        comp = 2020 - number
        while left < right:
            current_sum = lines[left] + lines[right]
            if comp == current_sum:
                print('Found: ', number * lines[left] * lines[right])
                exit(0)
            if current_sum < comp:
                left += 1
            else:
                right -=1