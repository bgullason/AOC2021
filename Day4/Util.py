# Utilty class for Day4 Part1

class Bingo:
    game_over = False
    winning_board = 0
    winning_number = 0
    boards = []
    game_numbers = []

class Board:
    winning_board = False
    winning_number = 0
    def __init__(self, board_rows = [], board_columns = []):
        self. board_rows = board_rows
        self. board_columns = board_columns

class Number:
    marked = False
    is_winning_number = False
    def __init__(self, value):
        self.value = value

