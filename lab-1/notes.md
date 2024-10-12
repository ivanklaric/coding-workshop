Upute za instalaciju Pythona, Visual Studio Codea, i Python extenzije: https://code.visualstudio.com/docs/python/python-tutorial

Hello world program: hello.py
```python
print("hello, world!")
```

Hello {tvoje_ime} program: hello_2.py
```python
ime = input()
print("Boook, " + ime + "!")
```

Pogadjanje brojeva: number_guess.py
```python
import random

zamisljeni_broj = random.randint(0, 10)

print("Pogodi koji sam broj zamislio (od 0 do 10): ")
pogodjeni_broj = int(input())

print("Ja sam zamislio", zamisljeni_broj)
print("Ti si pogodio", pogodjeni_broj)

if zamisljeni_broj == pogodjeni_broj:
    print("Pogodio si!")
else:
    print("Nisi pogodio!")
```

Zadaca:
 1. Promijenite program da u slucaju netocnog pogotka ispise je li pogodjeni broj veci ili manji od zamisljenog broja 
 2. Napravite varijantu programa s bacanjem novcica: 
      Racunalo simulira bacanje novcica odabirom slucajnog broja od 0 do 1
      Ako je racunalo odabralo 0, reci cemo da je to pismo. Ako je odabralo 1, reci cemo da je to glava.
      Igrac mora pogoditi je li novcic pao na pismo ili na glavu, igra ce mu ispisati je li pogodio
 3. Za nestrpljive, iduci put cemo raditi while petlje: https://www.w3schools.com/python/python_while_loops.asp
      Mozete prouciti primjere na linku i onda pomocu tog znanja pokusati sloziti varijantu programa iz zadatka #1
      koja korisniku daje da pogadja brojeve dok ne uspije pogoditi.


      