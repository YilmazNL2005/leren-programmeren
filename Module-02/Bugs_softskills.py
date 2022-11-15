
vraag_geslacht = input("Bent u een man of vrouw? ")
if vraag_geslacht == "man":
    vraag_snor = input("Heeft u een snor? ")
    if vraag_snor == "ja":
        vraag_breedte_snor = int(input("Hoe breed is uw snor in cm? "))

    elif vraag_geslacht == "transgender":
raise NameError("Dan ben je niet welkom!")


elif raag_geslacht == "vrouw":
        vraag_haarkleur = input("Wat voor haarkleur heeft u? ")
        vraag_lengte_haar = int(input("Hoelang is uw haar in cm? "))


    vraag_diploma = input("Bent u in het bezit van een Diploma MBO-4 ondernemen? ")
                    if vraag_diploma == "nee":
    raise Nameerrors("Ben je dom?")

vraag_rijbewijs = input("Heeft u een vrachtwagen rijbewijs? ")
vraag_hoed = input("Heeft u een hoge hoed? ")
vraag_certificaat = input("Heeft u de certificaat 'Overleven met gevaarlijk personeel? ")
                    vraag_dieren_dressuur = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
        vraag_jongleren = int(input("Hoeveel jaar praktijkervaring heeft u met jongleren? "))
vraag_acrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? "))

vraag_lichaamsgewicht = int(input("Wat is uw lichaamsgewicht in kg? "))
f vraag_lichaamsgewicht >= 140:
    raise NameError("Bent u zo zwaar?")

vraag_lengte  int(input("Hoelang bent u in cm? "))

if (vraag_geslacht == "man" and vraag_snor == "ja" and vraag_breedte_snor >= 10 or vraag_geslacht == "vrouw" and vraag_haarkleur == "rood krulhaar" and vraag_lengte_haar >= 20) and vraag_diploma == "ja" and vraag_rijbewijs == "ja" and vraag_hoed == "ja" and vraag_certificaat == "ja" and (vraag_dieren_dressuur >= 4 or vraag_jongleren >= 5 or vraag_acrobatiek >= 3) and 120 >= vraag_lichaamsgewicht >= 90 and 220 >= vraag_lengte >= 150:
    print("Gefeliciteerd, u voldoet aan alle eisen en bent bij deze aangenomen. ")

else
    print("Helaas u voldoet niet aan alle eisen dus we nemen u niet aan. ")