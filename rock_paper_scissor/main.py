import random
# We are going to create a rock paper scissor game 

print("Do you want a rock, paper, scissor game?")
# create a variable call user_input and port the user a Yes a No
user_input = input("Yes or No? ")
# if the user select no print out "It is sorry to see you don't want to play"

if user_input == "no":
    print("It is sorry to see you don't want to play")

# if the user select yes prompt the user for a input of rock paper sicssor 
elif user_input == "yes":
    """
    Store the user input from this elif statment into a variable, set the variable name to user_choice 
    using python create a words variable called "choice_list" that have three string ["rock", "paper", "sicssor"]
    import random
    using python random get a random choice from the list and store it in a varibles call random_choice

    compare the user choice and the random choice if the user choice match the random choice print aye you guess right 
    else say guess again

    """
    user_choice = input("select rock, paper, sicssor? ")
    choice_list = ["rock", "paper", "scissor"]
    random_choice = random.choice(choice_list)
    if user_choice == random_choice:
        print("aye you guess right")
    else:
        print("guess again")
# else the user don't choice yes or no print out wrong input    
else:
    print("wrong input")
   


