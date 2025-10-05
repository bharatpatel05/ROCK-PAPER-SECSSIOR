import random
# Score tracking
user_score = 0
computer_score = 0

# Choices
choices = ['rock', 'paper', 'scissors']

def get_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

# Game loop
while True:
    print("\n--- Rock, Paper, Scissors Game ---")
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = get_winner(user_choice, computer_choice)

    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Score => You: {user_score} | Computer: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
