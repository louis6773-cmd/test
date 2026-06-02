# *ENHANCED* using Gemini as ordered on Tuesday

import random
import tkinter as tk


class DiceRollGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roll")
        self.root.geometry("350x150")

        # Save the original default background color of the window
        self.default_bg = self.root.cget("bg")

        # Track state using an instance variable
        self.roll_count = 0

        # Create the UI components
        self.create_widgets()

    def create_widgets(self):
        # Buttons
        self.btn_quit = tk.Button(
            self.root, text="Quit", width=12, command=self.root.destroy
        )
        self.btn_quit.grid(row=0, column=0, padx=10, pady=10)

        self.btn_random = tk.Button(
            self.root, text="Random", width=12, command=self.roll_dice
        )
        self.btn_random.grid(row=0, column=1, padx=10, pady=10)

        # The Red Dice Boxes
        self.lbl_die1 = tk.Label(
            self.root,
            text="",
            bg="red",
            width=12,
            height=2,
            fg="white",
            font=("Arial", 12, "bold"),
        )
        self.lbl_die1.grid(row=1, column=0, padx=10, pady=5)

        self.lbl_die2 = tk.Label(
            self.root,
            text="",
            bg="red",
            width=12,
            height=2,
            fg="white",
            font=("Arial", 12, "bold"),
        )
        self.lbl_die2.grid(row=1, column=1, padx=10, pady=5)

        # Roll Count Tracker
        self.lbl_count_text = tk.Label(self.root, text="roll count =")
        self.lbl_count_text.grid(row=2, column=0, sticky="e")

        self.lbl_count_num = tk.Label(self.root, text="0")
        self.lbl_count_num.grid(row=2, column=1, sticky="w")

    def roll_dice(self):
        # Generate random numbers
        die1 = random.randint(1, 1000)
        die2 = random.randint(1, 1000)

        # Update the text inside the red boxes
        self.lbl_die1.config(text=str(die1))
        self.lbl_die2.config(text=str(die2))
        
        # Increment and update the roll count
        self.roll_count += 1
        self.lbl_count_num.config(text=str(self.roll_count))

        # Check for double sixes and adjust UI colors
        if die1 == 6 and die2 == 6:
            self.root.config(bg="green")
            self.lbl_count_text.config(bg="green", fg="white")
            self.lbl_count_num.config(bg="green", fg="white")
        else:
            # 2. Revert back to the explicitly saved default colors
            self.root.config(bg=self.default_bg)
            self.lbl_count_text.config(bg=self.default_bg, fg="black")
            self.lbl_count_num.config(bg=self.default_bg, fg="black")


# Application entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollGame(root)
    root.mainloop()