import random

print('Dobro dosli u pogadjanje brojeva!')
print('Pogodi jedan broj od 1 do 1000.')

zamisljeni_broj = random.randint(1,1000)
korisnik_je_pogodio = False
broj_pokusaja = 1

while not korisnik_je_pogodio:
    print(broj_pokusaja, ". pokusaj")
    pogodjeni_broj = int( input('Unesi broj:') )
    if pogodjeni_broj < 1 or pogodjeni_broj > 1000:
        print("Broj treba biti izmedju 1 i 1000!")
    else: 
        if pogodjeni_broj == zamisljeni_broj:
            print('Bravo, pogodio si!')
            korisnik_je_pogodio = True

        if pogodjeni_broj < zamisljeni_broj:
            print('Nisi pogodio, zamisljeni broj je veci')

        if pogodjeni_broj > zamisljeni_broj:
            print('Nisi pogodio, zamisljeni broj je manji')
        
        broj_pokusaja = broj_pokusaja + 1