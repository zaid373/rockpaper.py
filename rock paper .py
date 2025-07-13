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




game_image = [rock, paper, scissors]
print("welcome to the rock paper scissors game")
#round = int(input("how many round do you want to play?\n"))
user_choice = int(input("what do you choose? type 0 for rock,1 for paper and 2 for scissors.\n"))

if user_choice >= 3 or user_choice < 0:
      print("you typed an invalid number, you lose!")
else:
      print(game_image[user_choice])

computer_choice = random.randint(0,2)
print("computer chose:")
print(game_image[computer_choice])
#score_tracking = [user_choice, computer_choice]
#if score_tracking == [0,2] or score_tracking == [1,0] or score_tracking == [2,1]:
 #   print("you win!")
#elif score_tracking == [0,0] or score_tracking == [1,1] #or score_tracking == [2,2]:
 #   print("it's a draw")
#else:
   # print("you lose!")



if user_choice == 0 and computer_choice == 2:
      print("you wins!")
elif computer_choice == 0 and user_choice == 2:
      print("you lose!")
elif user_choice > computer_choice:
      print("you wins!")
elif computer_choice > user_choice:
      print("you lose!")
elif computer_choice == user_choice:
      print("it's a draw")