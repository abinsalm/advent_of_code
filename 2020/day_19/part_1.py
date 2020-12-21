from collections import defaultdict
import re

filename = 'part_1.txt'

roles = {}
process_roles = True
possible_solutions = set()


# def validate(word, role, start):
#     q = [(role, start)]
#     while q:
#         role, start = q.pop()
#         if type(role) == str:
#             if word[start] == role:
#                 q.append((role, start + 1))
#         elif type(role[0]) == str:
#             for role_part in role:
#                 q.append((roles[int(role_part)], start))
#                 start += 1
#             q.append((role, start))
#         else:
#             for role_part in role:
#                 q.append((role_part, start))
#     return start

# from functools import lru_cache
def validate_rec(word, role, start):
    if start == len(word):
        return start
    if type(role) == str:
        if word[start] == role: return start + 1
        return -1
    if type(role[0]) == str:
        for role_part in role:
            start = validate_rec(word, roles[int(role_part)], start)
            if start == -1: return -1
        return start
    else:
        for role_part in role:
            temp_start = validate_rec(word, role_part, start)
            if temp_start != -1: return temp_start
        return -1

# def build(role_pos, cache={}):
#     if role_pos not in cache:
#         role = roles[role_pos]
#         if type(role) == str:
#             cache[role_pos] = [role]
#         elif type(role[0]) == str:
#             temp_res = []
#             for role_part in role:
#                 curr_res = build(int(role_part), cache)
#                 if not curr_res: temp_res.append(curr_res)
#                 else:
#                     for i in range(temp_res):
#                         for temp_role in curr_res:
#                             temp_res[i] += temp_role
#
#             cache[role_pos] = temp_res
#         else:
#             for role_part in role:
#                 temp_start = validate_rec(word, role_part, start)
#                 if temp_start != -1: return temp_start
#             return -1
#     return cache[role_pos]

valid_counter = 0
with open(filename, encoding="utf-8") as f:
    for line in f:
        role = line.strip('\n')
        if role and process_roles:
            match = re.match('(\d+): (.*)', role)
            rule_id = int(match.group(1))
            rule_parts = match.group(2)
            if '"' not in rule_parts and '|' not in rule_parts:
                roles[rule_id] = rule_parts.split(' ')
            elif '|' in rule_parts:
                rule_parts = rule_parts.split(' ')
                m = len(rule_parts) // 2
                roles[rule_id] = [rule_parts[:m]]
                roles[rule_id].append(rule_parts[m+1:])
            else:
                roles[rule_id] = rule_parts[1:-1]
        elif not role:
            process_roles = False
        else:
            print(role)
            valid_counter += (validate_rec(role, roles[0], 0) == len(role))

print(valid_counter)
