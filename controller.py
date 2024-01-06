import game_board
import display


# start of the game, display rules and initialize board
# def start_game():
#     # print("Welcome to 2048!")
#     # print("------------------------------")
#     # print("Use the following commands to move the tiles:")
#     # print("'U' or 'u' = Move Up")
#     # print("'D' or 'd' = Move Down")
#     # print("'L' or 'l' = Move Left")
#     # print("'R' or 'r' = Move Right")
#     # print("Tiles with the same number merge into one when they touch.")
#     # print("Add them up to reach 2048 to win!")
#
#     game_board.initialize_board()
#     run_game()

# handles running the game each turn
# def run_game():
#     while(True):
#         action = display.display_board(game_board.board)
#         match action.lower():
#             case 'l':
#                 game_board.shift_left()
#             case 'r':
#                 game_board.shift_right()
#             case 'u':
#                 game_board.shift_up()
#             case _:
#                 game_board.shift_down()
#
#         status = game_board.current_game_state()
#         if status == 'lost':
#             display.print_output("Sorry, you lost!")
#             choice = display.restart()
#             if choice.lower() == 'yes' or choice.lower() == 'y':
#                 print()
#                 start_game()
#             break
#
#         elif status == 'won':
#             display.print_output("Congratulations, you won!")
#             choice = display.restart()
#             if choice.lower() == 'yes' or choice.lower() == 'y':
#                 print()
#                 start_game()
#             break
#
#         game_board.add_random_2()


