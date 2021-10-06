# condition - Rules that guides an operation. 

# Example:
import random
print("Welcome to this game")
list_of_numbers = [96, 60, 55, 67, 65, 57, 82, 52, 16, 91, 60, 46, 70, 1, 6]
chioce = int(input(f"Guess a number from:\n{list_of_numbers}\n"))
random.shuffle(list_of_numbers)
comp_chioce = random.choice(list_of_numbers)
if chioce == comp_chioce:
    print("You win!")
else:
    print("Oopa! You lost to the computer.")



# Exercise:
import random, time
print("Welcome To Rock Paper Scissor Game\n>>")
time.sleep(2)
word_list = ["Rock", "Paper", "Scissors"]
user = input(f"Enter a Word from:\n{word_list}\n").title()
print("Waiting for the computer to make a choice...")
time.sleep(2)
computer = random.choice(word_list)

if (computer == "Paper" and user == "Rock" or 
    computer == "Scissors" and user == "Paper" or 
    computer == "Rock" and  user == "Scissors"):
    print("Computer Wins!")
elif (user == "Paper" and computer == "Rock" or 
    user == "Scissors" and computer == "Paper" or 
    user == "Rock" and  computer == "Scissors"):
    print("You Win!")
elif computer == user:
    print("There's a Tie, Play Again!")
elif user != word_list:
    print("Word out of the list.")
else:
    print("You Lost the Game!")


