#Kosten voor een zwembad:
#
#Voorrijkosten (afhankelijk van de afstand en grootte van het zwembad)
#Kosten voor het uitgraven (gerekend in m3 (kubieke meters))
#Kosten voor het afvoeren van de grond (gerekend per m3)
#Kosten voor het aanbrengen van de wand en vloer (gerekend per m2 (vierkante meter) afhankelijk van de grootte van het bad.)
#
#

print("36", "\n")

#8 bij 3 bij 1,5 meter.
#60 km van Joris z'n bedrijf.


#float
lengte_zwembad = int(input("Hoe lang is het zwembad in meters? "))
breedte_zwembad = int(input("Hoe breed is het zwembad in meters? "))
diepte_zwembad = float(input("Hoe diep is het zwembad in meters? "))
antwoord_uitgraven = int(input("Hoeveel m3 grond moet er uitgegraven worden? "))
antwoord_afvoeren_grond = int(input("Hoeveel m3 grond moet er afgevoerd worden? "))
#antwoord_afstand = int(input("Hoeveel km is van het bedrijf vandaan? "))


prijs_uitgraven_per_m3 = 25
prijs_afvoeren_per_m3 = 32.50
#prijs_voorrijkosten_a = 100 + 1.25 * antwoord_afstand
#prijs_voorrijkosten_b = 100 + 1.15 * antwoord_afstand
#prijs_voorrijkosten_c =
#prijs_voorrijkosten_d =



berekening_uitgraven = prijs_uitgraven_per_m3 * antwoord_uitgraven
berekening_afvoeren_grond = prijs_afvoeren_per_m3 * antwoord_afvoeren_grond
berekening_totaalprijs = berekening_uitgraven + berekening_afvoeren_grond
#berekening_voorrijkosten = 

#8 keer 3 keer 1,5 meter
print(f"Offerte voor een zwembad van {lengte_zwembad} bij {breedte_zwembad} bij {diepte_zwembad} meter (inhoud: 36 m3)")
print(f"Uitgraven:           € {berekening_uitgraven} ")
print(f"Afvoeren grond:      € {berekening_afvoeren_grond} ")
print(f"Totaal:              € {berekening_totaalprijs} ")



#berekening_totaal =




# totaalprijs_



