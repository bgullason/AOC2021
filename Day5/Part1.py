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
with open(f'Day{day_number}\{file_name}.csv', 'r', encoding='utf-8-sig') as csv_data:
    csv_reader = reader(csv_data)
    for row in csv_reader:
        data.append(row)


# get the second number from the string in the format '123 -> 123'
# s = re.findall(r"[0-9]+.*?([0-9]+)", string)[0]

# use regex to match only lines where x1 = x2, or y1 = y2
# for line in [x for x in data if (x[0] == re.findall(r"[0-9]+.*?([0-9]+)", x[1])[0]) or (x[2] == re.findall(r"([0-9]+).*?[0-9]+", x[1])[0])]:
#     print(f'{line}')



# create and return a list of coordinates from a start and end coordinate
def create_line_list(start, end):
    coordinates = []
    if start.x == end.x:        # if x values are the same then this is a vertical line
        new_x = start.x
        if start.y < end.y:     # if start y is less than end y, start loop from start y
            i = start.y
            while i <= end.y:
                coordinates.append(Coordinate(new_x, i, 1))
                i += 1
        else:                   # else start loop from end y
            i = end.y
            while i <= start.y:
                coordinates.append(Coordinate(new_x, i, 1))
                i += 1
    else:                       # else this is a horizontal line
        new_y = start.y
        if start.x < end.x:     # if start x is less than end x, start loop from start x
            i = start.x
            while i <= end.x:
                coordinates.append(Coordinate(i, new_y, 1))
                i += 1
        else:                   # else start loop from end x
            i = end.x
            while i <= start.x:
                coordinates.append(Coordinate(i, new_y, 1))
                i += 1
    return coordinates


# check if a list contains the c1 coordinate already
def list_contains_coordinate(c1, grid_coordinates):
    for c2 in grid_coordinates:
        if (c1.x == c2.x and c1.y == c2.y):
            return True
    return False


class Coordinate:
    def __init__(self, x = 0, y = 0, value = 0):
        self.x = int(x)
        self.y = int(y)
        self.value = int(value)

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.coordinates = create_line_list(start, end)

# create list of lines
lines_list = []
for row  in data:
    start = Coordinate(row[0], re.findall(r"([0-9]+).*?[0-9]+", row[1])[0], 1)
    end = Coordinate(re.findall(r"[0-9]+.*?([0-9]+)", row[1])[0], row[2], 1)
    lines_list.append(Line(start, end))

# use regex to match only lines where x1 != x2, and y1 != y2
for line in [x for x in lines_list if (x.start.x != x.end.x) and (x.start.y != x.end.y)]:
    # print(f'Removing {line.start.x}, {line.start.y} -> {line.end.x}, {line.end.y}')
    lines_list.remove(line)

# show data
# print('Reduced and sorted List')
# for line in lines_list:
#     print(f'{line.start.x}, {line.start.y} -> {line.end.x}, {line.end.y}')

# for each line in lines_list, figure out which ones are overlapping
# create new list of coordinates to compare lines in
grid_coordinates_list = []
overlap_count = 0
for line in lines_list:
    for coordinate in line.coordinates:
        if list_contains_coordinate(coordinate, grid_coordinates_list):
            print(f'Overlap: {coordinate.x}, {coordinate.y}')
            overlap_count += 1
        else:
            grid_coordinates_list.append(coordinate)


print(f'\nOverlap Count: {overlap_count}\n')