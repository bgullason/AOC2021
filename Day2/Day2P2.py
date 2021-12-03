from csv import reader
import collections

data = []
# open file in read mode
with open('Day2\Input.csv', 'r', encoding='utf-8-sig') as csv_data:
    csv_reader = reader(csv_data)
    for row in csv_reader:
        data.append(row[0])

#      X  Y  aim
pos = [0, 0, 0]

for instruction in data:
    if 'forward' in instruction:
        pos[0] = pos[0] + int(''.join(i for i in instruction if i.isdigit()))
        pos[1] = pos[1] + (pos[2] * int(''.join(i for i in instruction if i.isdigit())))
    elif 'down' in instruction:
        pos[2] = pos[2] + int(''.join(i for i in instruction if i.isdigit()))
    elif 'up' in instruction:
        pos[2] = pos[2] - int(''.join(i for i in instruction if i.isdigit()))

print(f'\nHorizontal Pos: {pos[0]}\nDepth: {pos[1]}\nProduct: {pos[0]*pos[1]}\n')