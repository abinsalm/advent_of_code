from day_5.part_1 import process_seat

filename = 'part_2_input'

seat_ids = []
with open(filename, encoding="utf-8") as f:
    for line in f:
        line = line.strip('\n')
        seat_ids.append(process_seat(line))

seat_ids.sort()
for i in range(1, len(seat_ids)):
    if seat_ids[i-1] == seat_ids[i] - 2:
        print(f'Seat id: {seat_ids[i] - 1}, prev seat {seat_ids[i-1]}, next seat {seat_ids[i+1]}')
