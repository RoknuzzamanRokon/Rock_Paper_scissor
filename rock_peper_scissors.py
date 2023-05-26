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


x = 0
y = 0

while True:
    
    
    
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    print("\n")
    computer_choice = random.randint(0,2)



    if user_input == 0 and computer_choice == 0:
        print(f'Your choice rock{rock}\n Computer choice rock{rock}\n')
        print('tai')
        
    elif user_input == 0 and computer_choice == 1:
        print(f'Your choice rock{rock}\n Computer choice paper{paper}\n')
        print("Computer win")
        y = y + 1
        
    elif user_input == 0 and computer_choice == 2:
        print(f'Your choice rock{rock}\n Computer choice scissors{scissors}\n')
        print("You win")
        x = x + 1
        
    elif user_input == 1 and computer_choice == 0:
        print(f'Your choice paper{paper}\n Computer choice rock{rock}\n')
        print('You win')
        x = x + 1
        
    elif user_input == 1 and computer_choice == 1:
        print(f'Your choice paper{paper}\n Computer choice paper{paper}\n')
        print('tai')
        
    elif user_input == 1 and computer_choice == 2:
        print(f'Your choice paper{paper}\n Computer choice scissors{scissors}\n')
        print('Computer win')
        y = y + 1
        
    elif user_input == 2 and computer_choice == 0:
        print(f'Your choice scissors{scissors}\n Computer choice rock{rock}\n')   
        print('Computer win')
        y = y + 1
        
    elif user_input == 2 and computer_choice == 1:
        print(f'Your choice scissors{scissors}\n Computer choice paper{paper}\n')
        print('You win')
        x = x + 1
        
    elif user_input == 2 and computer_choice == 2:
        print(f'Your choice scissors{scissors}\n Computer choice scissors{scissors}\n')
        print('tai')
        
    else:
        print("Unknown keyword")

    print(f"\n\n*************** Your score: {x}\n*************** Computer score: {y}\n")
