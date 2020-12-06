filename = 'part_2_input'

total_answers = 0
answers = set()
group_counter = 0
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        if not line:
            total_answers += len(answers)
            answers = set()
            group_counter = 0
            continue

        temp_asnwers = set()
        for c in list(line): temp_asnwers.add(c)

        if group_counter == 0:
            answers |= temp_asnwers
        else:
            answers &= temp_asnwers
        group_counter += 1

# add last passport to passport data
total_answers += len(answers)

print(f"Sum of total answers: {total_answers}")
