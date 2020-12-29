filename = 'part_1.txt'

images = []
with open(filename, encoding="utf-8") as f:
    lines = f.read().split("\n\n")
    for line in lines:
        line = line.split('\n')
        id = line[0].split(' ')[1][:-1]
        data = line[1:]
        borders = data[0], ''.join([data[i][-1] for i in range(10)]), data[-1], ''.join([data[i][0] for i in range(10)])
        # print(id, borders, data)
        images.append((id, borders))
