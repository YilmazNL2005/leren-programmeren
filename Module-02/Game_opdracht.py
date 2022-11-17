import random
Gouden_sleutel = "ja of nee"
begin = "a"
volgende = "b"
eerste_level = "z"
volgende = "g"

while begin != "start":
    begin = input("Type start in om te beginnen ")
    if begin == "start":
        naam = input("Hallo, wat is je naam? \n ")

print(f"Welkom {naam} bij The mystery doors.\n")
print("Even in het kort hoe het spel werkt.")
print("Je krijgt bij ieder level, 4 deuren. Bij de 4 deuren is er maar 1 deur goed.")
print("Wanneer je de goede deur hebt gekozen, heb je het level voltooid en mag je naar het volgende level.")
print("Wanneer je de instant-win deur hebt gekozen, dan heb je het gehele spel gewonnen, maar le Je moet dan wel een sleutel hebben gevonden anders kan je er niet langs en verlies je. \n")
print("Je wordt wakker in een kamer met 3 deuren. Hoe je in de kamer bent gekomen weet je niet, maar je wilt wel weg. Als je opstaat en de 3 deuren ziet, zie je dat er een briefje bij hangt met daarop:\n")
print("Kies verstandig met welke deur je neemt. 1 deur is de goede, maar de andere 2 hebben vreselijke gevolgen voor je. Veel geluk.")


while True:
    volgende = input("Type verder in om verder te gaan. \n ")
    if volgende == "verder":
        print("Laden....")
        break

CurrentLVL = 1
while CurrentLVL < 21:
    RandomNumber = random.randint(1,4)
    print("Nummer =", RandomNumber)
    KiesEenDeur = int(input("Je ziet nu 4 deuren voor je. Welke deur ga je kiezen? Kies uit de deuren: 1, 2, 3 of 4? "))
    if RandomNumber == KiesEenDeur:
        print("Je hebt de goede deur gekozen")
        CurrentLVL += 1
        if CurrentLVL <= 20:
            print("Goed gedaan, Level:", CurrentLVL)
            if CurrentLVL == 10:
                Gouden_sleutel = input("Je hebt een gouden sleutel gevonden. Wil je deze sleutel meenemen? Ja of nee? ")
                
    else:
        mylist = ["Je valt nu in een kuil met lava.", "Oei, er wordt nu lava over je heen gegooid.", "Au, je loopt een martelkamer in en je gewordt nu gemarteld.", "Helaas, je valt nu de oneindige diepte in.", "Je trapt in de val en nu schieten er van verschillende kanten pijlen op je af."]
        print(random.choice(mylist))
        print("Game Over!!!")
        break
    if CurrentLVL == 21 and RandomNumber == KiesEenDeur and Gouden_sleutel == "ja":
        print("Slim, je hebt de gouden sleutel meegenomen en daarmee de laatste deur geopend.")
        print(f"Gefeliciteerd {naam}, je hebt de game voltooid!!!")
    elif CurrentLVL == 21 and RandomNumber == KiesEenDeur and Gouden_sleutel == "nee":
        print("Super, maar doordat je de gouden sleutel niet hebt meegenomen kan je deze deur niet openen.")
        print("Game Over!!!")
        #if CurrentLVL == 21:
        #print(f"Gefeliciteerd {naam}, je hebt de game voltooid!!!")




