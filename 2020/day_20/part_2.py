import re

filename = 'part_2.txt'

roles = {}
process_roles = True
possible_solutions = set()


def validate_rec(roles, index, word):
    if type(roles[index]) == str:
        if word and word[0] == roles[index]:
            return [word[1:]]
        else:
            return []
    else:
        result = []
        for role_part in roles[index]:
            q = [word]
            for part_index in role_part:
                for _ in range(len(q)):
                    temp_words = validate_rec(roles, int(part_index), q.pop(0))
                    q.extend(temp_words)
            result.extend(q)
    return result


valid_counter = 0
with open(filename, encoding="utf-8") as f:
    for line in f:
        role = line.strip('\n')
        if role and process_roles:
            match = re.match('(\d+): (.*)', role)
            rule_id = int(match.group(1))
            rule_parts = match.group(2)
            if '"' not in rule_parts and '|' not in rule_parts:
                roles[rule_id] = [rule_parts.split(' ')]
            elif '|' in rule_parts:
                rule_parts = rule_parts.split(' ')
                m = len(rule_parts) // 2
                roles[rule_id] = [rule_parts[:m]]
                roles[rule_id].append(rule_parts[m + 1:])
            else:
                roles[rule_id] = rule_parts[1:-1]
        elif not role:
            process_roles = False
            roles[8] = [['42'], ['42', '8']]
            roles[11] = [['42', '31'], ['42', '11', '31']]
        else:
            match_ = [match == '' for match in validate_rec(roles, 0, role)]
            if any(match_): valid_counter += 1

print(valid_counter)
