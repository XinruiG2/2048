
# print board row by row
def display_board(board):
    print("------------------------------")
    for row in board:
        formatted_row = [str(cell).rjust(max(2, 3 - len(str(cell)))) for cell in row]
        print(' '.join(formatted_row))
    # action = input("Please enter an action (l/r/u/d): ").lower()
    # while action != 'l' and action != 'r' and action != 'u' and action != 'd':
    #     action = input("Please enter a valid action (l/r/u/d): ").lower()
    # return action

def print_output(output):
    print(output)

# handles letting the user restart the game
def restart():
    choice = input("Would you like to play again? If so, enter 'yes'. ")
    return choice
