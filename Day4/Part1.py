# Advent Of Code 2021
# Ben Gullason
# https://github.com/bgullason

# --- Day 4: Giant Squid ---

from csv import reader
from Util import Board

# Set these two variables to enable test mode and set the file path
test_mode = True
day_number = 4


data = []
file_name = 'Input'

# Read from the csv file that contains the data to be processed
if test_mode: 
    file_name = 'Test' 
with open(f'Day{day_number}\{file_name}.csv', 'r', encoding='utf-8-sig') as csv_data:
    csv_reader = reader(csv_data)
    for row in csv_reader:
        data.append(row)


game_numbers = data.pop(0)
game_boards = []

data_index = 1
while data_index < len(data):
    board_row = 0
    board_numbers = []
    while board_row < 5:
        board_numbers_row = (data[data_index + board_row])
        
        # create an array of the row and insert it insead of the whole row string
        
        board_numbers.append(board_numbers_row)
        board_row += 1
    game_boards.append(Board(board_numbers))
    data_index += 6

print('yo')