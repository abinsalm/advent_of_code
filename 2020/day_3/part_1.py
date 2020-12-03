def count_trees(slope, lines, lines_count, line_len):
    tree_counts = 0
    i, j = 0, 0
    while i + slope[1] < lines_count:
        j = (j + slope[0]) % line_len
        i += slope[1]
        tree_counts += int(lines[i][j] == '#')
    return tree_counts


if __name__ == '__main__':
    filename = 'input_part_1'

    lines = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip('\n')
            lines.append(line)

    line_len = len(lines[0])
    lines_count = len(lines)
    print(f'Number of trees encountered: {count_trees([3, 1], lines, lines_count, line_len)}')
