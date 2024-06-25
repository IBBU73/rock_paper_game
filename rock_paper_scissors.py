import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0

        # Game Instructions
        self.instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
        self.instructions_label.pack()

        # User Choice Buttons
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.user_choice = tk.StringVar()
        for choice in self.choices:
            tk.Radiobutton(self.buttons_frame, text=choice, variable=self.user_choice, value=choice).pack(side=tk.LEFT)

        # Play Button
        self.play_button = tk.Button(root, text="Play", command=self.play_game)
        self.play_button.pack()

        # Result Label
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        # Score Label
        self.score_label = tk.Label(root, text="Score: User - 0, Computer - 0")
        self.score_label.pack()

    def play_game(self):
        user_choice = self.user_choice.get()
        computer_choice = random.choice(self.choices)

        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = f"You win! {user_choice} beats {computer_choice}."
            self.user_score += 1
        else:
            result = f"You lose! {computer_choice} beats {user_choice}."
            self.computer_score += 1

        # Update result label and score
        self.result_label.config(text=result)
        self.score_label.config(text=f"Score: User - {self.user_score}, Computer - {self.computer_score}")

        # Ask to play again
        self.ask_play_again()

    def ask_play_again(self):
        answer = messagebox.askyesno("Play Again", "Do you want to play again?")
        if answer:
            # Reset user's choice
            self.user_choice.set("")
            self.result_label.config(text="")
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
