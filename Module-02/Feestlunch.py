#17 croissantjes. 39 cent per stuk
#2 stokbroden. 2,78 euro per stuk
#3 kortingsbonnen = 50 cent per stuk





prijs_per_stuk_croissantjes = 0.39
prijs_per_stuk_stokbroden = 2.78
kortingsbon = 0.50

aantal_a = int(input("hoeveel croissantjes?"))
aantal_b = int(input("hoeveel stokbroden?"))
aantal_c = int(input("hoeveel kortingsbonnen?"))

berekening_a = prijs_per_stuk_croissantjes * aantal_a
berekening_b = prijs_per_stuk_stokbroden * aantal_b
berekening_c = kortingsbon * aantal_c

totale_prijs = berekening_a + berekening_b - berekening_c
totale_prijs = round(totale_prijs, 2);
print("De feestlunch kost je bij de bakker", totale_prijs, "euro voor de", aantal_a, "croissantjes en de",  aantal_b, "stokbroden als de ",aantal_c," kortingsbonnen nog geldig zijn!")





















