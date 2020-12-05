def process_seat(line):
    row = int(extract_row(line))
    col = int(extract_col(line))
    return row * 8 + col


def extract_row(line):
    return search(line, 0, 127, 'F', 0)
    # l, h = 0, 127
    # i = 0
    # while l < h:
    #     m = (h + l) // 2
    #     if line[i] == 'B':
    #         h = m
    #     else:
    #         l = m + 1
    # return l


def extract_col(line):
    return search(line, 0, 7, 'L', 7)


def search(line, l, h, left, start):
    i = start
    while l < h:
        m = (h + l) // 2
        if line[i] == left:
            h = m
        else:
            l = m + 1
        i += 1
    return l


filename = 'part_1_input'

seat_ids = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        seat_ids.append(process_seat(line))

print(f'Highest seat id: {max(seat_ids)}')
