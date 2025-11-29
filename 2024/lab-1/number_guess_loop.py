import random

# Generate a random number between 1 and 20
secret_number = random.randint(0, 10)

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 20.")

guess = -1
while guess != secret_number:
    # Get the player's guess
    guess = input("Enter your guess (1-20): ")
    
    # Convert the guess to an integer
    guess = int(guess)
    
    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
    
    # Check if the guess is too low
    if guess < secret_number:
        print("Too low! Try again.")
    
    # Check if the guess is too high
    if guess > secret_number:
        print("Too high! Try again.")
    
print("Thanks for playing!")