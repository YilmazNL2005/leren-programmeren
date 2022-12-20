import random
# 1. Maak 1 Tuple waar de volgende kleuren in zitten:
#    oranje - blauw - groen - bruin
# 2. Het programma vraagt met 1 input hoeveel M&M's er aan de zak
#    toegevoegd moeten worden.
# 3. Maak een functionaliteit die 1 lege List datatype (zak met M&M's)
#    vult aan de hand van het gekozen aantal.
#    De kleuren moeten gekozen worden uit de beschikbare kleuren in de Tuple, aangemaakt in punt 1.
# 4. Het programma print als laatste de inhoud van de zak met M&M's.

KLEUREN = ("oranje", "blauw", "groen", "bruin")
aantal = int(input("Hoeveel M&M's moeten er in de zak toegevoegd worden? "))
for x in range(0, aantal):
    y = random.randint(0,3)
    print(KLEUREN[y])


