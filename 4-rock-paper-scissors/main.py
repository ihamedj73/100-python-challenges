import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [paper, scissors, rock]


while True:
    player_choice_index = int(
        input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    if player_choice_index > 2 or player_choice_index < 0:
        print("Please select correct choice")
    else:
        break


player_choice = choices[player_choice_index]

computer_choice = random.choice(choices)


game_status = ""

if player_choice == computer_choice:
    game_status = "Its draw"

elif player_choice == paper:
    if computer_choice == rock:
        game_status = "You win!"
    elif computer_choice == scissors:
        game_status = "You lost"
elif player_choice == rock:
    if computer_choice == scissors:
        game_status = "You win"
    elif computer_choice == paper:
        game_status = "You lost"
elif player_choice == scissors:
    if computer_choice == rock:
        game_status = "You lost"
    elif computer_choice == paper:
        game_status = "You win"


print("YOU:")
print(player_choice)
print("Computer")
print(computer_choice)
print(game_status)
