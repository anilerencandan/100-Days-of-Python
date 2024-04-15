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

game_images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(game_images[choice])

ai_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[ai_choice])

if choice >= 3 or choice < 0: 
  print("You typed an invalid number, you lose!") 
elif choice == 0 and ai_choice == 2:
  print("You win!")
elif ai_choice == 0 and choice == 2:
  print("You lose")
elif ai_choice > choice:
  print("You lose")
elif choice > ai_choice:
  print("You win!")
elif ai_choice == choice:
  print("It's a draw")
