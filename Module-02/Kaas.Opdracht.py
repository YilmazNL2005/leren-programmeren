# Zoals de meeste van jullie het spel “wie is het” wel kennen, 
# ga jij een soortgelijk spel programmeren. 
# Het is de bedoeling dat jouw programma door vragen te stellen aan de gebruiker erachter komt welke kaas de gebruiker in gedachte heeft. 
# In de bijgevoegde PDF zie je een boomstructuur van de mogelijke vragen. 
# Deze boomstructuur dien jij in een python script te programmeren door gebruik te maken van “if-else statements”. 
# Daarbij gebruik je de comparison operators om de gegeven antwoorden te checken.



antwoord_geel = input("Is de kaas geel? ") 

if antwoord_geel == "ja":
    antwoord_gaten = input("Zitten er gaten in? ")
    if antwoord_gaten == "ja":
        antwoord_duur = input("Is de kaas belachelijk duur? ")
        if antwoord_duur == "ja":
            print("Emmenthaler")
        elif antwoord_duur == "nee":
            print("Leerdammer")
    
    elif antwoord_gaten == "nee":
        antwoord_steen = input("Is de kaas hard als steen? ")
        if antwoord_steen == "ja":
            print("Parmigiano Reggiano")
        elif antwoord_gaten == "nee":
            print("Goudse kaas")


if antwoord_geel == "nee":
    antwoord_schimmel = input("heeft de kaas een blauwe schimmel? ")
    if antwoord_schimmel == "ja":
        antwoord_korst = input("Heeft de kaas een korst? ")
        if antwoord_korst == "ja":
            print("Blue de Rochbaron")
        elif antwoord_korst == "nee":
            print("Foume d'Ambert")
    
    elif antwoord_schimmel == "nee":
        antwoord_korst = input("Heeft de kaas een korst? ")
        if antwoord_korst == "ja":
            print("Camembert ")
        elif antwoord_schimmel == "nee":
            print("Mozzarella ")






