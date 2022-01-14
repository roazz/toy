
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
cissors = '''
    _______
---'   ____)____    
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game_image = [rock,paper,cissors]

print("what do you chose? type 0 for Rock, 1 for Paper, 2 for scissors")
user_choice = int(input("My choice? "))

print(game_image[user_choice])

'''
if user_choice == 0:  다른 경우
  print(rock)
elif user_choice == 1:
  print(paper)
else :
  print(cissors)
'''

computer_choice = random.randint(0,2)

print("Computer choice :")
print(game_image[computer_choice])

'''
if computer_choice == 0:  다른 경우
  print(rock)
elif computer_choice == 1:
  print(paper)
else :
  print(cissors)
'''

if user_choice == 0 and computer_choice==2:
  print("you win!")
elif user_choice == 2 and computer_choice == 0:
  print("you lose!")
elif user_choice > computer_choice :
  print("you win!")
elif user_choice == computer_choice :
  print("draw!")
elif user_choice >=3 or user_choice <0 :
  print("you typed an invalid number, you lose! ")
else :
  print("you lose!")