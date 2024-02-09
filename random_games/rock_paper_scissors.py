import random

# Create a list of choices for the computer
choices = ['rock', 'paper', 'scissors']

# Function to get the user's choice
def get_user_choice():
    user_choice = input('Rock, Paper, or Scissors? ').lower()
    while user_choice not in choices:
        print('Invalid choice. Please choose Rock, Paper, or Scissors.')
        user_choice = input('Rock, Paper, or Scissors? ').lower()
    return user_choice

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    if (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        return 'You win!'
    else:
        return 'Computer wins!'

# Main game loop
while True:
    user_choice = get_user_choice()
    computer_choice = random.choice(choices)

    print(f'You chose {user_choice}.')
    print(f'Computer chose {computer_choice}.')

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input('Play again? (yes/no) ').lower()
    if play_again != 'yes':
        break

print('Thanks for playing!')
