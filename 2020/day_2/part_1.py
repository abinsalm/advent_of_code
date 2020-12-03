from collections import Counter

filename = 'input_part_1'

records = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        requirement, letter, password = line.split(' ')
        requirement = requirement.split('-')
        min_length, max_length = int(requirement[0]), int(requirement[1])
        letter = letter[0]

        records.append((min_length, max_length, letter, password))


def is_valid_password(min_length, max_length, letter, password):
    counter = Counter(password)
    return min_length <= counter[letter] <= max_length


print('Number of valid passwords: ', len([1 for record in records if is_valid_password(*record)]))
