import random
user_choice = int(input("Enter your Preffered choice : Type 0 for Rock,Type 1 for Paper,Type 2 for scissor "))
if user_choice >= 3 or user_choice < 0:
    print("you entered an invalid number,you lose.")
else:
    comp_Choice = random.randint(0,2)
    print("Computer chose: ")
    print(comp_Choice)
    if comp_Choice == user_choice:    
        print("It's a draw.")
    elif comp_Choice == 0 and user_choice == 2:    
        print("Computer Won")
    elif user_choice == 0 and comp_Choice == 2:    
        print("You win")
    elif comp_Choice > user_choice:
        print("Computer won")
    elif user_choice > comp_Choice:
        print("You win.")
