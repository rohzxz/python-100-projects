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


#Write your code below this line 👇


list_image = [rock,paper,scissors]
you_choose = int(input("What do you choose type 0 for rock, 1 for Paper or 2 for Scissors. \n "))
# if you_choose == 0:
#     print(rock)
# elif you_choose == 1:
#     print(paper)
# elif you_choose == 2:
#     print(scissors)
# else:
#     print("GAME OVER")
# if list_image == len(list_image):
# print(list_image[you_choose]) 
# computer_choose =(random.choice(list_game))
if you_choose >= 3 or you_choose <= 0:
    print("Invalid choice. Please choose 0 for rock, 1 for paper, or 2 for scissors.") 
else:
    print(list_image[you_choose])
    computer_choose = random.randint(0,2)
    print("computer_choose :")
    print(list_image[computer_choose])
    if you_choose == 0 and computer_choose == 2:
     print("you win")
    elif you_choose == 2 and computer_choose == 0:
     print("you lose")
    elif computer_choose > you_choose:
     print("you lose")
    elif you_choose > computer_choose:
     print("you win")
    elif you_choose == computer_choose:
     print("it,s a draw")




