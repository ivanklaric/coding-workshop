import random

print('Pogadjanje brojeva do 1000')
zamisljeni_broj = random.randint(1, 1000)

broj_pokusaja = 1
pogodjeni_broj = int(input('Pokusaj pogoditi broj:'))
while pogodjeni_broj != zamisljeni_broj:
    print('Pokusaj broj ', broj_pokusaja)
    if pogodjeni_broj < zamisljeni_broj:
        print('Broj je veci')
    if pogodjeni_broj > zamisljeni_broj:
        print('Broj je manji')
    pogodjeni_broj = int(input('Pokusaj pogoditi broj:'))
    broj_pokusaja = broj_pokusaja + 1
print('Pokusaj broj ', broj_pokusaja)
print('Pogodio si!')
