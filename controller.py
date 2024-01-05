import board
import display


# start of the game, display rules and initialize board
def start_game():
    print("Welcome to 2048!")
    print("------------------------------")
    print("Use the following commands to move the tiles:")
    print("'U' or 'u' = Move Up")
    print("'D' or 'd' = Move Down")
    print("'L' or 'l' = Move Left")
    print("'R' or 'r' = Move Right")
    print("Tiles with the same number merge into one when they touch.")
    print("Add them up to reach 2048 to win!")

    board.initialize_board()
