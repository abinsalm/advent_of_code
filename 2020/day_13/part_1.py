filename = 'part_1.txt'

input = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        input.append(line)

print(input)
start = int(input[0])
busses = [int(x) for x in input[1].split(',') if x != 'x']

bus_stop = None
min_time = float('inf')
for stop in busses:
    if stop % start == 0:
        print(stop)
        break

    next_stop = int(start//stop) * stop + stop
    if next_stop < min_time:
        min_time = next_stop
        bus_stop = stop

print(bus_stop, bus_stop * (min_time - start))

