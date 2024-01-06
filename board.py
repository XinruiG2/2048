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

# compress the board to use before and after merges, left shift functionality
# only performing left shift functionality because it can be reused to perform
# other right/up/down shifts
def board_shift():
    global board
    temp_board = []

    for i in range(4):
        temp_board.append([' '] * 4)

    for r in range(4):
        curr_col = 0

        for c in range(4):
            if board[r][c] != ' ':
                temp_board[r][curr_col] = board[r][c]
                curr_col += 1

    board = temp_board

# merge any adjacent cells that have the same value, left shift functionality
def merge_cells():
    for r in range(4):
        for c in range(3):
            if board[r][c] == board[r][c + 1] and board[r][c] != ' ':
                board[r][c] *= 2
                board[r][c + 1] = ' '

# reverse row values on the board
def reverse_board():
    temp_board = []
    for r in range(4):
        temp_board.append([])
        for c in range(4):
            temp_board[r].append(board[r][3 - c])

    return temp_board

# find the transpose of the board
# first row of transpose is first col of original matrix
def transpose():
    temp_board = []
    for r in range(4):
        temp_board.append([])
        for c in range(4):
            temp_board[r].append(board[c][r])

    return temp_board

# handle left key press
def shift_left():
    # compress board to left, merge, and then compress again
    board_shift()
    merge_cells()
    board_shift()

# handle right key press
def shift_right():
    # use reverse function and left shift to imitate right shift
    board = reverse_board()
    shift_left()
    board = reverse_board()

# handle up key press
def up_shift():
    # use transpose function and left shift to imitate up shift
    board = transpose()
    shift_left()
    board = transpose()

# handle down key press
def down_shift():
    # use transpose function and right shift to imitate up shift
    board = transpose()
    shift_right()
    board = transpose()


