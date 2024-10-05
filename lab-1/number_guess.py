import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 20.")

# Set the maximum number of guesses
max_guesses = 10

for turn in range(1, max_guesses + 1):
    # Get the player's guess
    guess = input(f"Guess {turn}: Enter your guess (1-20): ")
    
    # Convert the guess to an integer
    guess = int(guess)
    
    # Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {turn} tries!")
        break
    
    # Check if the guess is too low
    if guess < secret_number:
        print("Too low! Try again.")
    
    # Check if the guess is too high
    if guess > secret_number:
        print("Too high! Try again.")
    
    # Check if the player has used all their guesses
    if turn == max_guesses:
        print(f"Sorry, you've used all {max_guesses} guesses. The number was {secret_number}.")

print("Thanks for playing!")