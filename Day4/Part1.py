# Advent Of Code 2021
# Ben Gullason
# https://github.com/bgullason

# --- Day 4: Giant Squid ---

from csv import reader
from Util import *
import re


# Set these two variables to enable test mode and set the file path
test_mode = False
day_number = 4


# Read from the csv file that contains the data to be processed
data = []
file_name = 'Input'
if test_mode: 
    file_name = 'Test' 
with open(f'Day{day_number}\{file_name}.csv', 'r', encoding='utf-8-sig') as csv_data:
    csv_reader = reader(csv_data)
    for row in csv_reader:
        data.append(row)
# print(f'\nData (list of rows where each row is a string. first row is a list of numbers)\n{data}\n')


# create a bingo game and get the game numbers from the data
bingo = Bingo()
bingo.game_numbers = data.pop(0)


print(f'\nBingo Game Numbers: {bingo.game_numbers}\n')
# print(f'\nData: {data}\n')


# reverse through data and use empty lines as markers for new boards
board_rows = []
data_index = len(data) - 1
while data_index >= 0:
    if len(data[data_index]) != 0:
        # create board rows list
        row = []
        for num in re.findall(r'[0-9]+', data[data_index][0]):
            row.append(Number(int(num)))
        board_rows.insert(0, row)
    else:
        # create columns list from rows list
        board_cols = []
        col_index = 0
        while col_index < len(board_rows[0]):
            col = []
            for row in board_rows.copy():
                col.append(row[col_index])
            board_cols.append(col)
            col_index += 1
        # create new board and add too board list
        bingo.boards.insert(0, Board(board_rows.copy(), board_cols))
        board_rows.clear()
    data_index -= 1


# now we have a list of game numbers to run through, and a list of game boards.
# each game board has a list of rows, and a list of columns.
# 

# game loop

for game_number in bingo.game_numbers:
    if bingo.game_over: break
    # mark matching numbers in boards rows and columns
    for board in bingo.boards:
        for row in board.board_rows:
            for num in row:
                if num.value == int(game_number):
                    num.marked = True
        for col in board.board_columns:
            for num in col:
                if num.value == int(game_number):
                    num.marked = True
        
        
        # for each number in each row, if a number is not marked in a row then mark winning_row as false
        for row in board.board_rows:
            if bingo.game_over: break
            winning_row = True
            for num in row:
                if not num.marked:
                    winning_row = False
                    break
            if winning_row:
                bingo.game_over = True
                board.winning_board = True
                board.winning_number = game_number
        
        # same as above but for columns
        for column in board.board_columns:
            if bingo.game_over: break
            winning_column = True
            for num in column:
                if not num.marked:
                    winning_column = False
                    break
            if winning_column:
                bingo.game_over = True
                board.winning_board = True
                board.winning_number = game_number
        
        
        # save the index of the winning board
        if bingo.game_over:
            bingo.winning_board = bingo.boards.index(board)
            bingo.winning_number = board.winning_number
            print(f'\nBINGO!\nIndex of Winning Board: {bingo.boards.index(board)}\nWinning Number: {board.winning_number}\n')
            break

# graphical representation of bingo boards
for board in bingo.boards:
    for row in board.board_rows:
        for num in row:
            if num.marked:
                print(f'*{num.value} ', end='')
                # print(f'██ ', end='')    
            else:
                print(f' {num.value} ', end='')
        print()
    print()


# now get sum of unmarked numbers on the winning board then mulitply by winning number
sum_unmarked = 0
for row in bingo.boards[bingo.winning_board].board_rows:
    for num in row:
        if not num.marked:
            sum_unmarked += int(num.value)

score = sum_unmarked * int(bingo.winning_number)

print(f'\n\nWinning Board Score: {score}\n\n')