ticket_p_p = 7.45 

aantal_personen = int(input("met hoeveel mensen ben je?"))

vip_vr_prijs_per_minuut = 0.074

aantal_minuten_vr = int(input("hoeveel minuten wil je gebruik maken van de vip vr gameset?"))

totaal_a = ticket_p_p * aantal_personen
totaal_b = vip_vr_prijs_per_minuut * aantal_minuten_vr * aantal_personen
totale_prijs = totaal_a + totaal_b

totaal_a = round (totaal_a, 2);
totaal_b = round (totaal_b, 2);
print(f"de totale prijs voor de tickets is {ticket_p_p * aantal_personen} euro en voor de vip vr gameset is het {totaal_b} euro")



totale_prijs = round (totale_prijs, 2);
print("Dit geweldige dagje-uit met", aantal_personen, "mensen in de Speelhal met", aantal_minuten_vr, "minuten VR kost je maar", totale_prijs , "euro.")


#Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar 44.44 euro

#vip_vr_prijs_per_minuut * aantal_minuten_vr * aantal_personen
#totaal_a + totaal_b











