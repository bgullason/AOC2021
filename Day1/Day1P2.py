from csv import reader
import collections

data = []
# open file in read mode
with open('Day1_Input.csv', 'r', encoding='utf-8-sig') as read_Day1_Input:
    csvreader = reader(read_Day1_Input)
    for row in csvreader:
        data.append(row[0])


line_count = len(data)
previous_sum = 0
current_sum = 0
first = True
count = 0
output = ''

while line_count >= 3:
    block = [int(data.pop(0)), int(data[0]), int(data[1])]
    line_count = len(data)

    current_sum = sum(block)

    if first:
        output = f'{current_sum} - No previous Data'
        first = False
    else:
        if current_sum > previous_sum:
            output = f'{current_sum} - Increased'
            count = count + 1
        else:
            output = f'{current_sum} - Decreased'

    print(output)
    previous_sum = current_sum


print(f'Total Increases: {count}')


