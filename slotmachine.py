"""Simulate all the functionalities of the slot machine"""

import random

ROWS = 3
COLUMNS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}


def spin_slot_machine(rows: int, cols: int, symbols: dict) -> list:
    """Simulate the spin of the slot machine reels"""
    all_symbols: list = []
    for sym, quantity in symbol_count.items():
        all_symbols.extend([sym]*quantity)  # put all symbols available in on list
    columns: list = []  # each of the nested list is a COLUMN
    for col in range(cols):
        new_col = []  # initiate a reel
        all_symbols_copy = all_symbols.copy()  # create new copy for each column
        for row in range(rows):
            temp_symbol = random.choice(all_symbols_copy)  # get the symbol randomly
            all_symbols_copy.remove(temp_symbol)  # remove it from the all_symbols to avoid
            new_col.append(temp_symbol)
        columns.append(new_col)
    return columns


def print_slots(cols: list) -> list:
    """Pretty print the columns into more human format and return columns transposed"""
    cols_transposed = []  # transpose from rows to columns
    for row in range(len(cols[0])):  # iterate over columns for as many iterations as there are rows
        temp_row = []
        for col in cols:
            temp_row.append(col[row])
        cols_transposed.append(temp_row)
    # Pretty print the slot machine reels
    for row in cols_transposed:
        print(f'|{"|".join(row)}|')
    return cols_transposed


def validate_win(reels: list, lines_bet: int) -> bool:
    """Check if there are any homogenous rows"""
    if lines_bet == 0:
        print('You can\'t bet on 0 lines!')
        return False
    hits_counter = 0
    for row in reels:
        if len(set(row)) == 1:
            hits_counter += 1
    if hits_counter == lines_bet:
        print('You\'ve won! Congratulations!')
        return True
    return False


if __name__ == '__main__':
    result = False
    while not result:
        columns = spin_slot_machine(ROWS, COLUMNS, symbol_count)
        transposed_columns = print_slots(columns)
        result = validate_win(transposed_columns, 2)
        print(columns, transposed_columns, result)

