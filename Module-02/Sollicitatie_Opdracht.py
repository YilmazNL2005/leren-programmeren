#De kandidaat moet wel voldoen aan de volgende criteria:

#In bezit van een Diploma MBO-4 ondernemen          ja
#In bezit van een geldig Vrachtwagen rijbewijs      ja
#In bezit van een hoge hoed                         ja
#Is man EN heeft Snor breder dan 10 cm OF is vrouw EN draagt rood krulhaar langer dan 20 cm.                                                    ja
#Let op: Je hoeft alleen een man naar zijn snor en snorlengte te vragen en alleen een vrouw naar haar kleur haar en daarna de haarlengte.       ja
#Is langer dan 150 cm en korter dan 220 cm          ja
#Is zwaarder dan 90 kg en lichter dan 120 kg        ja
#Heeft Certificaat “Overleven met gevaarlijk personeel”         ja
#Meer dan 4 jaar praktijkervaring met dieren-dressuur OF meer dan 5 jaar ervaring met jongleren OF meer dan 3 jaar praktijkervaring met acrobatiek.     ja 
#Let op: Vraag de jaren ervaring afzonderlijk voor alle kunsten: dieren-dressuur, jongleren én acrobatiek. Dus 3 vragen!                                ja

#De vragen met getallen mogen de kritieke grens (zoals 4 jaar, of 150 cm) van een criterium niet verklappen.  
# Dus je vraagt bijvoorbeeld:
#'Wat is uw lichaamsgewicht?’ in plaats van 'Weegt  u zwaarder dan 90kg? J/N’

#‘Hoeveel jaar praktijkervaring heeft u met dit-of-dat ?’ 
# in plaats van 'Heeft u meer dan 4 jaar praktijkervaring met dit-of-dat? J/N’

#Let op: eerst alle vragen stellen, daarna pas de geschiktheid berekenen op basis van de gegeven antwoorden! 
#Pas na het berekenen van de geschiktheid geeft u de uitslag van de sollicitatie aan de invuller.


vraag_geslacht = input("Bent u een man of vrouw? ")
if vraag_geslacht == "man":
    vraag_snor = input("Heeft u een snor? ")
    if vraag_snor == "ja":
        vraag_breedte_snor = int(input("Hoe breed is uw snor in cm? "))

elif vraag_geslacht == "vrouw":
    vraag_haarkleur = input("Wat voor haarkleur heeft u? ")
    vraag_lengte_haar = int(input("Hoelang is uw haar in cm? "))


vraag_diploma = input("Bent u in het bezit van een Diploma MBO-4 ondernemen? ")
vraag_rijbewijs = input("Heeft u een vrachtwagen rijbewijs? ")
vraag_hoed = input("Heeft u een hoge hoed? ")
vraag_certificaat = input("Heeft u de certificaat 'Overleven met gevaarlijk personeel? ")
vraag_dieren_dressuur = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
vraag_jongleren = int(input("Hoeveel jaar praktijkervaring heeft u met jongleren? "))
vraag_acrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? "))
vraag_lichaamsgewicht = int(input("Wat is uw lichaamsgewicht in kg? "))
vraag_lengte = int(input("Hoelang bent u in cm? "))

if (vraag_geslacht == "man" and vraag_snor == "ja" and vraag_breedte_snor >= 10 or vraag_geslacht == "vrouw" and vraag_haarkleur == "rood krulhaar" and vraag_lengte_haar >= 20) and vraag_diploma == "ja" and vraag_rijbewijs == "ja" and vraag_hoed == "ja" and vraag_certificaat == "ja" and (vraag_dieren_dressuur >= 4 or vraag_jongleren >= 5 or vraag_acrobatiek >= 3) and 120 >= vraag_lichaamsgewicht >= 90 and 220 >= vraag_lengte >= 150:
    print("Gefeliciteerd, u voldoet aan alle eisen en bent bij deze aangenomen. ")

else:
    print("Helaas u voldoet niet aan alle eisen dus we nemen u niet aan. ")