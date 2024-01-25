# Rock Paper Scissors Project

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

import random
game_images = [rock, paper, scissors]

player_choice = int(input("Choose:\n0 for Rock\n1 for Paper\n2 for Scissors.\nYour choice:  "))

if player_choice >= 3 or player_choice <0:
    print("Invalid number. You lose!")
else:
    print(game_images[player_choice])

    computer_choice = random.randint(0,2)
    print(f'Computer chose {computer_choice}.\n')
    print(game_images[computer_choice])

    if player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif player_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif computer_choice > player_choice:
        print(f'You lose!')
    elif player_choice > computer_choice:
        print("You win!")
    elif computer_choice == player_choice:
        print("It's a draw!")

