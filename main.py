import tkinter as tk
from tkinter import messagebox
import game_board
import display

class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("2048")
        self.master.geometry("352x550")

        self.game_frame = tk.Frame(self.master)

        self.label = tk.Label(self.game_frame, text="Welcome to 2048!", height=2, width=20)
        self.label.pack()
        self.canvas = tk.Frame(self.game_frame, width=450, height=352, pady=15)
        self.canvas.pack()

        # Pack the frames into the window using grid
        self.game_frame.grid(row=0, column=0, padx=35, pady=18)

        self.create_game_frame()

        # self.start_game()

    def create_game_frame(self):
        game_board.initialize_board()

        self.update_board()

        self.action_frame = tk.Frame(self.game_frame)
        self.action_frame.pack()

        left_button = tk.Button(self.action_frame, text="Left", command=self.left_click)
        right_button = tk.Button(self.action_frame, text="Right", command=self.right_click)
        up_button = tk.Button(self.action_frame, text="Up", command=self.up_click)
        down_button = tk.Button(self.action_frame, text="Down", command=self.down_click)

        left_button.pack(side="left", padx=3, pady=(10, 0))
        right_button.pack(side="left", padx=3, pady=(10, 0))
        up_button.pack(side="left", padx=3, pady=(10, 0))
        down_button.pack(side="left", padx=3, pady=(10, 0))

        self.frame2 = tk.Frame(self.game_frame, width=300, height=352, pady=25)
        self.frame2.pack()

        rules_text = (
            "1. Use the buttons to move the tiles.\n"
            "2. Tiles with the same number merge\ninto one when they touch.\n"
            "3. Add them up to reach 2048\nto win the game!"
        )
        self.title = tk.Label(self.frame2, text="Rules:")
        self.title.pack()
        # Game frame elements (welcome message, restart button, and board)
        self.label = tk.Label(self.frame2, text=rules_text)
        self.label.pack()

        # self.restart_button = tk.Button(self.game_frame, text="Restart", command=self.restart_game, anchor="w", justify="left")
        # self.restart_button.pack(fill='x')

    def left_click(self):
        game_board.shift_left()
        game_board.add_random_2()
        self.update_board()

    def right_click(self):
        game_board.shift_right()
        game_board.add_random_2()
        self.update_board()

    def up_click(self):
        game_board.shift_up()
        game_board.add_random_2()
        self.update_board()

    def down_click(self):
        game_board.shift_down()
        game_board.add_random_2()
        self.update_board()

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
        for widget in self.canvas.winfo_children():
            widget.destroy()

        corresponding_colors = {0: ["#faf8ef", "#766e65"], 2: ["#faf8ef", "#766e65"], 4: ["#eee0c9", "#766e65"],
                                8: ["#f3b279", "#f8f6f1"], 16: ["#f69563", "#f8f6f1"], 32: ["#f77c5f", "#f8f6f1"],
                                64: ["#f75f3b", "#f8f6f1"], 128: ["#edd073", "#f8f6f1"], 256: ["#edcc61", "#f8f6f1"],
                                512: ["#edc750", "#f8f6f1"], 1024: ["#edc43f", "#f8f6f1"], 2048: ["#edc22d", "#f8f6f1"]}

        for i in range(4):
            for j in range(4):
                frame = tk.Frame(
                    master=self.canvas,
                    relief=tk.SUNKEN,
                    borderwidth=2,
                    bg="#bbac9f"
                )
                label_font = ("Helvetica", 16, "bold")
                frame.grid(row=i, column=j, padx=8, pady=8)
                value = game_board.board[i][j]
                label = tk.Label(master=frame,
                                 text=value,
                                 width=4,
                                 height=2,
                                 bg=corresponding_colors[value][0],
                                 fg=corresponding_colors[value][1],
                                 font=label_font)
                label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    game_gui = GameGUI(root)
    root.mainloop()



