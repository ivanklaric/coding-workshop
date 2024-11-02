import random

def odredi_pobjednika(odabir_prvog, odabir_drugog):
    if odabir_drugog == odabir_prvog:
        return 0
    if (odabir_prvog == 0 and odabir_drugog == 2 or 
        odabir_prvog == 1 and odabir_drugog == 0 or
        odabir_prvog == 2 and odabir_drugog == 1):
        return 2
    else:
        return 1

opcije_odabira = ["kamen", "skare", "papir"]

pobjednik = 0
while pobjednik != 2:
    kompjuterov_odabir = random.randint(0, 2)
    print("Odaberi 0 za kamen, 1 za skare, ili 2 za papir:")
    igracev_odabir = int(input())

    print("Igracev odabir:", opcije_odabira[igracev_odabir])
    print("Kompjuterov odabir:", opcije_odabira[kompjuterov_odabir])
    pobjednik = odredi_pobjednika(kompjuterov_odabir, igracev_odabir)
    if pobjednik == 0:
        print("Nerijeseno!")
    else:
        if pobjednik == 1:
            print("Kompjuter pobjedjuje")
        else:
            print("Igrac pobjedjuje")


