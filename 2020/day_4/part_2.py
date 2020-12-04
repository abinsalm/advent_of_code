filename = 'part_2_input'

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
    return all([has_valid_byr(passport_data), has_valid_iyr(passport_data), has_valid_eyr(passport_data),
                has_valid_hgt(passport_data), has_valid_hcl(passport_data), has_valid_ecl(passport_data),
                has_valid_pid(passport_data)])


def has_valid_byr(passport_data):
    return 'byr' in passport_data and len(passport_data['byr']) == 4 and '1920' <= passport_data['byr'] <= '2002'


def has_valid_iyr(passport_data):
    return 'iyr' in passport_data and len(passport_data['iyr']) == 4 and '2010' <= passport_data['iyr'] <= '2020'


def has_valid_eyr(passport_data):
    return 'eyr' in passport_data and len(passport_data['eyr']) == 4 and '2020' <= passport_data['eyr'] <= '2030'


def has_valid_hgt(passport_data):
    if 'hgt' not in passport_data: return False
    height = passport_data['hgt']
    if height.endswith('cm'): return '150' <= height[:-2] <= '193'
    if height.endswith('in'): return '59' <= height[:-2] <= '76'


def has_valid_hcl(passport_data):
    if 'hcl' not in passport_data: return False
    hcl_ = passport_data['hcl']
    return hcl_.startswith('#') and all('a' <= c <= 'f' or c.isdigit() for c in hcl_[1:])


def has_valid_ecl(passport_data):
    if 'ecl' not in passport_data: return False
    ecl_ = passport_data['ecl']
    return ecl_ in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def has_valid_pid(passport_data):
    if 'pid' not in passport_data: return False
    pid_ = passport_data['pid']
    return len(pid_) == 9 and all(c.isdigit() for c in pid_)


print(f"Number of valid passports: {sum(map(is_valid_passport, all_passports))}")
