from tkinter import*
import random
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "ROCK" and computer_choice == "SCISSORS")
        or (player_choice == "PAPER" and computer_choice == "ROCK")
        or (player_choice == "SCISSORS" and computer_choice == "PAPER")
    ):
        return "You win!"
    else:
        return "Computer wins!"
def player_choice(choice):
    computer_choices = ["ROCK", "PAPER", "SCISSORS"]
    computer_choice = random.choice(computer_choices)
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose {computer_choice}\n{result}")
gui = Tk()
gui.title("ROCK, PAPER, SCISSORS Game")
gui.configure(bg="black")
Font="Ariel",20,"bold"
rock_button = Button(gui, text="ROCK", command=lambda: player_choice("ROCK"),font=Font,bg="red")
rock_button.grid(padx=10, pady=5)
paper_button = Button(gui, text="PAPER", command=lambda: player_choice("PAPER"),font=Font,bg="green")
paper_button.grid(padx=10, pady=5)
scissors_button = Button(gui, text="SCISSORS", command=lambda: player_choice("SCISSORS"),font=Font,bg="blue")
scissors_button.grid(padx=10, pady=5)
result_label = Label(gui, text="", padx=20, pady=10,font=Font,bg="orange")
result_label.grid(padx=10,pady=5)
gui.mainloop()