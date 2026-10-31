import random

print('Dobro dosli u pogadjanje brojeva!')
print('Pogodi jedan broj od 1 do 1000.')

zamisljeni_broj = random.randint(1,1000)
korisnik_je_pogodio = False

while not korisnik_je_pogodio:
    pogodjeni_broj = int( input('Unesi broj:') )
    if pogodjeni_broj == zamisljeni_broj:
        print('Bravo, pogodio si!')
        korisnik_je_pogodio = True

    if pogodjeni_broj < zamisljeni_broj:
        print('Nisi pogodio, zamisljeni broj je veci')

    if pogodjeni_broj > zamisljeni_broj:
        print('Nisi pogodio, zamisljeni broj je manji')