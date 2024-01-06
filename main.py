import tkinter as tk
from tkinter import messagebox
import game_board
import display

class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("2048")
        self.master.geometry("712x650")

        self.game_frame = tk.Frame(self.master)
        self.rules_frame = tk.Frame(self.master, height=380)

        # Game frame elements (welcome message, restart button, and board)
        self.label = tk.Label(self.game_frame, text="Welcome to 2048!", height=2, width=20)
        self.label.pack()
        self.canvas = tk.Frame(self.game_frame, width=300, height=352)
        self.canvas.pack()

        # Pack the frames into the window using grid
        self.game_frame.grid(row=0, column=0, padx=(25, 35), pady=12)
        self.rules_frame.grid(row=0, column=1, padx=25, pady=12)

        self.create_game_frame()
        self.create_rules_frame()

        # self.start_game()

    def create_game_frame(self):
        game_board.initialize_board()

        self.update_board()

        left_button = tk.Button(self.game_frame, text="Left", command=game_board.shift_left())
        right_button = tk.Button(self.game_frame, text="Right", command=game_board.shift_right())
        up_button = tk.Button(self.game_frame, text="Up", command=game_board.shift_up())
        down_button = tk.Button(self.game_frame, text="Down", command=game_board.shift_down())

        left_button.pack(side="left", padx=3, pady=(10, 0))
        right_button.pack(side="left", padx=3, pady=(10, 0))
        up_button.pack(side="left", padx=3, pady=(10, 0))
        down_button.pack(side="left", padx=3, pady=(10, 0))

        # self.restart_button = tk.Button(self.game_frame, text="Restart", command=self.restart_game, anchor="w", justify="left")
        # self.restart_button.pack(fill='x')

    def create_rules_frame(self):
        rules_text = (
            "Use the following commands to move the tiles:\n"
            "'U' or 'u' = Move Up\n"
            "'D' or 'd' = Move Down\n"
            "'L' or 'l' = Move Left\n"
            "'R' or 'r' = Move Right\n\n"
            "Tiles with the same number merge into one\nwhen they touch."
            " Add them up to reach 2048\nto win the game!"
        )
        # Game frame elements (welcome message, restart button, and board)
        self.label = tk.Label(self.rules_frame, text=rules_text, anchor='n', justify="left")
        self.label.pack()

        self.canv = tk.Frame(self.rules_frame, width=200, height=248)
        self.canv.pack()

    def start_game(self):
        self.run_game()

    def run_game(self):
        # while (True):
            self.master.after(50, self.update_board)

            status = game_board.current_game_state()
            if status == 'lost':
                display.print_output("Sorry, you lost!")
                choice = display.restart()
                if choice.lower() == 'yes' or choice.lower() == 'y':
                    print()
                    self.start_game()
                # break

            elif status == 'won':
                display.print_output("Congratulations, you won!")
                choice = display.restart()
                if choice.lower() == 'yes' or choice.lower() == 'y':
                    print()
                    self.start_game()
                # break

            game_board.add_random_2()

    def restart_game(self):
        choice = messagebox.askyesno("Restart", "Would you like to play again?")
        if choice:
            game_board.initialize_board()
            self.update_board()
            self.start_game()

    def update_board(self):
        for i in range(4):
            for j in range(4):
                frame = tk.Frame(
                    master=self.canvas,
                    relief=tk.SUNKEN,
                    borderwidth=2
                )
                frame.grid(row=i, column=j, padx=8, pady=8)
                label = tk.Label(master=frame, text=game_board.board[i][j], width=4, height=2)
                label.pack()

    def create_board_row(self, cell_values):
        row_frame = tk.Frame(self.canvas)
        row_frame.pack()

        for value in cell_values:
            button = tk.Button(row_frame, text=value)
            button.pack(side="left", padx=2, pady = 2)

    def handle_action(self, action):
        if action.lower() == 'l':
            game_board.shift_left()
        elif action.lower() == 'r':
            game_board.shift_right()
        elif action.lower() == 'u':
            game_board.shift_up()
        else:
            game_board.shift_down()

        self.master.after(100, self.update_board)

if __name__ == "__main__":
    root = tk.Tk()
    game_gui = GameGUI(root)
    root.mainloop()



