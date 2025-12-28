import random
play_again = "y"
while play_again.lower() == "y":
    choices = ['rock', 'paper', 'scissors']
    ai_choice = random.choice(choices)

    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        user_choice = input("Invalid choice. Please choose rock, paper, or scissors: \n").lower()

    else:
        print(f"AI chose: {ai_choice}")

        if user_choice == ai_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and ai_choice == 'scissors') or \
            (user_choice == 'paper' and ai_choice == 'rock') or \
            (user_choice == 'scissors' and ai_choice == 'paper'):
            print("You win!")
        else:
            print("AI wins!")
    play_again = input("Do you want to play again? (y/n): ")
print("Thanks for playing!")