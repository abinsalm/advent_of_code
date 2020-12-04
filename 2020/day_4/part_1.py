filename = 'part_1_input'

passport_data = dict()
all_passports = []
valid_passports = 0
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        if not line:
            all_passports.append(passport_data)
            passport_data = dict()
            continue

        for data in line.split(" "):
            key, val = data.split(":")
            passport_data[key] = val

# add last passport to passport data
all_passports.append(passport_data)


def is_valid_passport(passport_data):
    return 'byr' in passport_data and 'iyr' in passport_data and 'eyr' in passport_data and 'hgt' in passport_data and 'hcl' in passport_data and 'ecl' in passport_data and 'pid' in passport_data


print(f"Number of valid passports: {sum(map(is_valid_passport, all_passports))}")
