import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

def get_player_choice():
    while True:
        player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if player_choice in choices:
            return player_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    # Generate a random number (0, 1, or 2) and use it to index the choices list
    random_index = random.randint(0, 2)
    return choices[random_index]

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    
    if player_choice == "rock" and computer_choice == "scissors":
        return "You win!"
    if player_choice == "paper" and computer_choice == "rock":
        return "You win!"
    if player_choice == "scissors" and computer_choice == "paper":
        return "You win!"
    
    return "Computer wins!"

def play_game():
    print("Welcome to Rock Paper Scissors!")
    
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Start the game
play_game()