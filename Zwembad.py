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
antwoord_afstand = int(input("Hoeveel km is van het bedrijf vandaan? "))
opp_zwembad = lengte_zwembad * breedte_zwembad * diepte_zwembad

prijs_uitgraven_per_m3 = 25
prijs_afvoeren_per_m3 = 32.50
voorrijkosten = 0
voorrijkosten_vasteprijs_ab = 100
voorrijkosten_vasteprijs_cd = 250
voorrijkosten_extra_a = 1.25
voorrijkosten_extra_b = 1.15
voorrijkosten_extra_c = 2.15
voorrijkosten_extra_d = 2.05



#prijzen veranderen in variabelen
if antwoord_afstand < 50 and opp_zwembad < 20:
    prijs_voorrijkosten_a = voorrijkosten_vasteprijs_ab + voorrijkosten_extra_a * antwoord_afstand

elif antwoord_afstand >= 50 and opp_zwembad < 20:
    prijs_voorrijkosten_b = voorrijkosten_vasteprijs_ab + voorrijkosten_extra_b * antwoord_afstand

elif antwoord_afstand < 50 and opp_zwembad >= 20:
    prijs_voorrijkosten_c = voorrijkosten_vasteprijs_cd + voorrijkosten_extra_c * antwoord_afstand

elif antwoord_afstand >= 50 and opp_zwembad >= 20:
    prijs_voorrijkosten_d = voorrijkosten_vasteprijs_cd + voorrijkosten_extra_d * antwoord_afstand
else:
    print("Foutje!!!")

berekening_uitgraven = prijs_uitgraven_per_m3 * antwoord_uitgraven
berekening_afvoeren_grond = prijs_afvoeren_per_m3 * antwoord_afvoeren_grond
berekening_totaalprijs = berekening_uitgraven + berekening_afvoeren_grond

berekening_voorrijkosten = prijs_voorrijkosten_a or prijs_voorrijkosten_b or prijs_voorrijkosten_c or prijs_voorrijkosten_d 
#berekening_voorrijkosten = voorrijkosten_vaste_prijs + extra_km * antwoord_afstand



#8 keer 3 keer 1,5 meter
print(f"Offerte voor een zwembad van {lengte_zwembad} bij {breedte_zwembad} bij {diepte_zwembad} meter (inhoud: {opp_zwembad} m3)")
print(f"Uitgraven:           € {berekening_uitgraven:.2f}      ")
print(f"Afvoeren grond:      € {berekening_afvoeren_grond:.2f} ")
print(f"Voorrijkosten:       € {berekening_voorrijkosten:.2f}  ")
print(f"Totaal:              € {berekening_totaalprijs:.2f}    ")



#berekening_totaal =




# totaalprijs_



