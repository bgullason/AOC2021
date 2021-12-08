# Advent Of Code 2021
# Ben Gullason
# https://github.com/bgullason

# --- Day 5: Hydrothermal Venture ---

from csv import reader
import re


# Set these two variables to enable test mode and set the file path
test_mode = True
day_number = 5


# Read from the csv file that contains the data to be processed
data = []
file_name = 'Input'
if test_mode: 
    file_name = 'Test' 
with open(f'{file_name}.csv', 'r', encoding='utf-8-sig') as csv_data:
    csv_reader = reader(csv_data)
    for row in csv_reader:
        data.append(row)


# get the second number from the string in the format '123 -> 123'
# s = re.findall(r"[0-9]+.*?([0-9]+)", string)[0]

# use regex to match only lines where x1 = x2, or y1 = y2
for line in [x for x in data if (x[0] == re.findall(r"[0-9]+.*?([0-9]+)", x[1])[0]) or (x[2] == re.findall(r"([0-9]+).*?[0-9]+", x[1])[0])]:
    print(f'{line}')

