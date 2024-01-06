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

        # Pack the frames into the window using grid
        self.game_frame.grid(row=0, column=0, padx=(25, 35), pady=12)
        self.rules_frame.grid(row=0, column=1, padx=25, pady=12)

        self.create_game_frame()
        self.create_rules_frame()

    def create_game_frame(self):
        game_board.initialize_board()

        # Game frame elements (welcome message, restart button, and board)
        self.label = tk.Label(self.game_frame, text="Welcome to 2048!", anchor='w', justify="left", height=2, width=20)
        self.label.pack(anchor='w')

        self.canvas = tk.Canvas(self.game_frame, width=300, height=352)
        self.canvas.pack()

        left_button = tk.Button(self.game_frame, text="Left", command=game_board.shift_left())
        right_button = tk.Button(self.game_frame, text="Right", command=game_board.shift_right())
        up_button = tk.Button(self.game_frame, text="Up", command=game_board.shift_up())
        down_button = tk.Button(self.game_frame, text="Down", command=game_board.shift_down())

        left_button.pack(side="left", padx=3)
        right_button.pack(side="left", padx=3)
        up_button.pack(side="left", padx=3)
        down_button.pack(side="left", padx=3)

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

        self.canvas = tk.Canvas(self.rules_frame, width=200, height=248)
        self.canvas.pack()

    def start_game(self):
        self.run_game()

        self.master.after(100, self.update_board)

    def run_game(self):
        while (True):
            self.master.after(100, self.update_board)
            match action.lower():
                case 'l':
                    game_board.shift_left()
                case 'r':
                    game_board.shift_right()
                case 'u':
                    game_board.shift_up()
                case _:
                    game_board.shift_down()

            status = game_board.current_game_state()
            if status == 'lost':
                display.print_output("Sorry, you lost!")
                choice = display.restart()
                if choice.lower() == 'yes' or choice.lower() == 'y':
                    print()
                    start_game()
                break

            elif status == 'won':
                display.print_output("Congratulations, you won!")
                choice = display.restart()
                if choice.lower() == 'yes' or choice.lower() == 'y':
                    print()
                    start_game()
                break

            game_board.add_random_2()

    def restart_game(self):
        choice = messagebox.askyesno("Restart", "Would you like to play again?")
        if choice:
            game_board.initialize_board()
            self.update_board()

    def update_board(self):
        self.canvas.delete("all")

        for row_idx, row in enumerate(game_board.board):
            for col_idx, cell in enumerate(row):
                x1, y1 = col_idx * 75, row_idx * 75
                x2, y2 = x1 + 75, y1 + 75
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray")
                self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(cell), font=("Helvetica", 16))

        status = game_board.current_game_state()
        if status == 'lost':
            messagebox.showinfo("Game Over", "Sorry, you lost!")
            self.restart_game()
        elif status == 'won':
            messagebox.showinfo("Congratulations", "Congratulations, you won!")
            self.restart_game()
        else:
            action = display.display_board(game_board.board)
            self.handle_action(action)

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



