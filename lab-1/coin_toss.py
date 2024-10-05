import random

print("Welcome to the Coin Toss Guessing Game!")
print("Try to guess the outcome of three coin tosses.")
print("Enter 'h' for heads or 't' for tails.")

score = 0

for toss in range(1, 4):
    guess = input(f"Toss {toss}: Enter your guess (h/t): ")
    
    # Generate a random coin toss (0 for tails, 1 for heads)
    coin_toss = random.randint(0, 1)
    
    if coin_toss == 0:
        result = "t"
        print("The coin shows tails.")
    else:
        result = "h"
        print("The coin shows heads.")
    
    if guess == result:
        print("Correct guess!")
        score += 1
    else:
        print("Wrong guess.")

print(f"\nGame over! Your final score is: {score} out of 3")