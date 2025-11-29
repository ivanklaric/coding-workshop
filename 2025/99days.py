import random

print('Dobro dosli u 99 dana u sumi!')
print('Cilj igre je prezivjeti cim vise dana u sumi')

energija = 100
vatra = 100
dani = 1

while energija > 0 and vatra > 0:
    print('Danas je ', dani, 'dan')
    print('Trenutno imas ', energija, ' energije, a snaga vatre je ', vatra)
    
    print('Sto zelis napraviti?')
    print(' Unesi 1 ako zelis ici traziti hranu')
    print(' Unesi 2 ako zelis ici traziti drva za vatru')
    odabir = int(input())
    if odabir == 1:
        dodatak_energije = random.randint(-30,90)
        if dodatak_energije == 0:
            print('Bio si u sumi i nista nisi nasao za jest')
        if dodatak_energije < 0:
            print('Napala te zivotinja dok si trazio hranu i izgubio si ', dodatak_energije, ' energije')
        if dodatak_energije > 0:
            print('Nasao si hranu u sumi i pojeo ', dodatak_energije, ' energije')
        energija = energija + dodatak_energije
    if odabir == 2:
        dodatak_vatre = random.randint(-10,80)
        if dodatak_vatre == 0:
            print('Bio si u sumi i nisi nasao drva!')
        if dodatak_vatre < 0:
            print('Bio si u sumi, padala je kisa i smanjila ti je vatru za ', dodatak_vatre)
        if dodatak_vatre > 0:
            print('Bio si u sumi i nasao drva za pojacati vatru ', dodatak_vatre)
        vatra = vatra + dodatak_vatre
        vjerojatnost_napada = random.randint(1,5)
        if vjerojatnost_napada == 2:
            snaga_napada = random.randint(1,10)
            print('Napala te zivotinja dok si trazio drva i uzela ti je ', snaga_napada, ' energije')
            energija = energija - snaga_napada


    dani = dani + 1
    energija = energija - 20
    vatra = vatra - 15

print('Umro si i izdrzao si ', dani, ' dana.')
if energija <= 0:
    print('Umro si od gladi')
if vatra <= 0:
    print('Umro si od hladnoce')
if dani >= 99:
    print('Pobjedio si!!')
else:
    print('Nisi uspio, falilo ti je jos ', 99-dani, ' dana')