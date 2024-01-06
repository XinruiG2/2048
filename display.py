
# print board row by row
def display_board(board):
    print("------------------------------")
    for row in board:
        print('  '.join(map(str, row)))
    action = input("Please enter an action (l/r/u/d): ").lower()
    while action != 'l' and action != 'r' and action != 'u' and action != 'd':
        action = input("Please enter a valid action (l/r/u/d): ").lower()
    return action

def print_output(output):
    print(output)

def restart():
    choice = input("Would you like to play again? If so, enter 'yes'")
    return choice
