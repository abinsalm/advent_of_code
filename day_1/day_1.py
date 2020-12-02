filename = 'input'

seen = set()
with open(filename, encoding="utf-8") as f:
    for line in f:
        entry = int(line)
        comp = 2020 - entry
        if comp in seen:
            print('Found: ', comp * entry)
            break
        else:
            seen.add(entry)
