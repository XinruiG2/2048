import random

board = []  # a 4x4 game board

# create a 4x4 with all empty values except for one 2
def initialize_board():
    for i in range(4):
        board.append([' '] * 4)

    # add a 2 to a random spot to start the game
    add_random_2()

# add a 2 at a random empty cell on the board
def add_random_2():
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    # continue finding a new position if cell is not empty
    while (board[r][c] != ' '):
        r = random.randint(0, 3)
        c = random.randint(0, 3)

    board[r][c] = 2

# determine current state of the game
def current_game_state():
    # check if any cell contains 2048
    for row in range(4):
        for col in range(4):
            if board[row][col] == 2048:
                return "won"

    # continue if empty cells left
    for row in range(4):
        for col in range(4):
            if board[row][col] == ' ':
                return "continue"

    # continue if board is full but two cells can be merged
    for row in range(3):
        for col in range(3):
            if (board[row][col] == board[row][col + 1]) or (board[row][col] == board[row + 1][col]):
                return "continue"

    # continue if last row is full but two cells can be merged
    for col in range(3):
        if board[3][col] == board[3][col + 1]:
            return "continue"

    # continue if last column is full but two cells can be merged
    for row in range(3):
        if board[row][3] == board[row + 1][3]:
            return "continue"

    # game over if none of the above are true
    return "lost"

