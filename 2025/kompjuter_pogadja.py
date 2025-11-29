print('Zamisli neki broj od 1 do 1000!')

niza_granica = 1
visa_granica = 1000

pokusaj = int((niza_granica + visa_granica) / 2)
print('Je li tvoj broj', pokusaj, '?')
print('Unesi 1 ako je, 2 ako je tvoj broj veci, 3 ako je tvoj broj manji')
odgovor = int(input())

while odgovor != 1:
    if odgovor == 2: 
        niza_granica = pokusaj
    if odgovor == 3:
        visa_granica = pokusaj
    pokusaj = int((niza_granica + visa_granica) / 2)
    print('Je li tvoj broj', pokusaj, '?')
    print('Unesi 1 ako je, 2 ako je tvoj broj veci, 3 ako je tvoj broj manji')
    odgovor = int(input())


print('Pogodio sam!')
