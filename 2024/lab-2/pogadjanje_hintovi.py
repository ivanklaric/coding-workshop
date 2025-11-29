import random

# Generate a random number between 1 and 20
tajni_broj = random.randint(0, 10)

print("Pogodi broj izmedju 0 i 10!")

pokusaj = -1
while pokusaj != tajni_broj:
    # Get the player's guess
    pokusaj = int(input("Odaberi broj: "))
    
    # Check if the guess is correct
    if pokusaj == tajni_broj:
        print("Pogodak!")
        break
    
    # Check if the guess is too low
    if pokusaj < tajni_broj:
        print("Broj je veci!")
    
    # Check if the guess is too high
    if pokusaj > tajni_broj:
        print("Broj je manji!")
    