filename = 'input_part_2'

records = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        requirement, letter, password = line.split(' ')
        requirement = requirement.split('-')
        first_valid_index, second_valid_index = int(requirement[0]) - 1, int(requirement[1]) - 1
        letter = letter[0]

        records.append((first_valid_index, second_valid_index, letter, password))


def is_valid_password(first_valid_index, second_valid_index, letter, password):
    return password[first_valid_index] != password[second_valid_index] and (
                letter in [password[first_valid_index], password[second_valid_index]])


print('Number of valid passwords: ', len([1 for record in records if is_valid_password(*record)]))
