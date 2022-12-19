import random

# klein = "groter"
# groot = "kleiner"
# ergindebuurt = "Je bent erg warm."
# indebuurt = "Je bent warm."
score = 0
ronde = 1
kansen = 10
MAXRONDES = 20
num1 = random.randint(1, 1000)
raad = 0

while ronde != MAXRONDES and kansen > 0:
    volgende = input("Wil je een getal raden? ja/nee. ")
    if volgende == "nee":
        break
    if volgende == "ja":
        while ronde <= MAXRONDES and kansen > 0:
                print("ronde", ronde)
                print("Aantal punten", score)
                print("Aantal kansen", kansen)
                #print(num1)
                raad = int(input("Noem een getal tussen de 1 en 1000. "))
                #print(num1)
                if raad != num1:
                    kansen-= 1
                    verschil = abs(raad - num1)
                    #print(verschil)
                    if raad < num1:
                        print("Het is hoger.")
                    if raad > num1:
                        print("Het is lager.")
                    if verschil <= 50 and verschil > 20:
                        print("Je bent warm.")
                    if verschil <= 20 and verschil > 0:
                        print("Je bent erg warm.")
                    if verschil > 200:
                        print("Je bent koud.")
                    if kansen == 0:
                        print("Helaas, je hebt niet gewonnen")
                        print(f"Je hebt {score} punten en je kwam niet verder dan ronde {ronde}.")
                if raad == num1:
                    print("Goed gedaan, je hebt het getal geraden.")
                    num1 = random.randint(1, 1000)
                    ronde += 1
                    score += 1
                    vraag = input("wil je doorgaan of stoppen? doorgaan/stoppen?")
                    if vraag == "stoppen":
                        break
                    if vraag == "doorgaan":
                        continue