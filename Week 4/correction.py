# Assignment on Set:

student_in_A = set(input().split())
student_in_B = set(input().split())

list_of_intersected_students = student_in_A.intersection(student_in_B)
print(list_of_intersected_students)
print(len(list_of_intersected_students))

# ClassWork on "Rock Paper Scissors Game"

import random
print("Welcome to the game")
print("Rock Paper Scissors")

help = '''
This is a simple game that follows the rule below:
Rock wins Scissors
Paper wins Rock
Scissors wins Paper

Choices are R for Rock, P for Paper and S for Scissors

You have only one chance. can you beat me?
'''

print(help)

player_choice = input("what do you choose?\n>").lower()
choices = ['r', 'p', 's']
random.shuffle(choices)
com_choice = random.choice(choices)

if player_choice in choices:
    if (player_choice == 'r' and com_choice == 's') or (player_choice == 'p' and com_choice == 'r') or (player_choice == 's' and com_choice == 'p'):
        print('You Win')

    elif (com_choice == 'r' and player_choice == 's') or (com_choice == 'p' and player_choice == 'r') or (com_choice == 's' and player_choice == 'p'):
        print('Com Win')
    else: 
        print("it's a tie")
else:
    print("Invalid input. You lose!")


# Question 2:
length1 = input("Enter the first size\n>>")
length2 = input("Enter the second size\n>>")
length3 = input("Enter the third size\n>>")

if length1 ==length2==length3:
    print("Equilateral")
elif (length1 == length2) or (length1 == length3) or (length2 == length3):
    print("Isoseles")
else:
    print("scalene")


# Question 3:

data = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

sorted_list = sorted(data, key = lambda k : k['color'])
print(sorted_list)