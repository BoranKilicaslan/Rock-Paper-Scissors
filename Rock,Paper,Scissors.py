import random
rock = '''Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

move = [rock,paper,scissors]

cp = random.randint(0,2)
user_choice = int(input("What do you choose ? Type 0 Rock, 1 for paper or 2 for scissors "))
print(f"Computer choose {move[cp]}")

print(f"User choose {move[user_choice]}")

if cp == 2 and user_choice == 0:
  print("You win!")
elif cp == 0 and user_choice == 2:
  print("You lose")
elif cp > user_choice:
  print("You lose")
elif user_choice > cp:
  print("You win")
elif cp == user_choice:
  print("It is a draw")
elif user_choice >= 3:
  print("You entered invalid number. You lose")
