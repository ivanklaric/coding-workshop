import random

# Generate a random number between 1 and 20
zamisljeni_broj = random.randint(0, 10)

print("Pogodi koji sam broj zamislio (od 0 do 10): ")
pogodjeni_broj = int(input())

print("Ja sam zamislio", zamisljeni_broj)
print("Ti si pogodio", pogodjeni_broj)

if zamisljeni_broj == pogodjeni_broj:
    print("Pogodio si!")
else:
    print("Nisi pogodio!")