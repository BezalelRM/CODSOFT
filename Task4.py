import random

def get_user():
    print("\nChoose one: rock, paper, or scissors")
    user = input("Your choice: ").lower()
    while user not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user = input("Your choice: ").lower()
    return user

def get_comp():
    return random.choice(['rock', 'paper', 'scissors'])

def winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "user"
    else:
        return "computer"

def play():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors Game! ")

    while True:
        user = get_user()
        computer = get_comp()

        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}")

        winnervar = winner(user, computer)

        if winnervar == "tie":
            print("It's a tie!")
        elif winnervar == "user":
            print("You win this round! ")
            user_score += 1
        else:
            print("Computer wins this round! ")
            computer_score += 1

        print(f"Score => You: {user_score} | Computer: {computer_score}")

        again = input("\nDo you want to play another round? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print(" You are the overall winner!")
            elif user_score < computer_score:
                print("Computer is the overall winner!")
            else:
                print(" It's a final tie!")
            break

play()
