filename = 'part_1_input'

total_answers = 0
answers = set()
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        if not line:
            total_answers += len(answers)
            answers = set()
            continue

        for c in list(line): answers.add(c)

# add last passport to passport data
total_answers += len(answers)


print(f"Sum of total answers: {total_answers}")
