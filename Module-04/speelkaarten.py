import random
# Maak een programmaatje die een standaard deck met kaarten genereert (54 kaarten), 
# deze schudt en de bovenste 7 er afhaalt op het scherm toont en daarna de overige kaarten in het deck.

# De volgende regels gelden voor dit programma:

# Het deck bestaat uit 4 “kleuren” (harten, klaveren, schoppen & ruiten)
# Iedere kleur heeft 13 kaarten (2 t/m 10, een boer, een vrouw, een heer en een aas)
# Er zitten ook 2 jokers in het deck
# 
# Je code:
# 
# 1.    Mag geen uitgeschreven deck bevatten (moet gegenereerd worden).
# 2.    Bestaat uit minder dan 20 regels (exclusief lege regels).


#handStapel = ("kaart", 1, 2, 3, 4, 5, 6 ,7)
#print(soorten_kaarten * 5)     Deze print toont 5 keer de lijst soorten_kaarten in de terminal
#    soorten_kaarten.append(random.choice(soorten_kaarten),getalWaarde)

nummer = [2, 3, 4, 5, 6, 7, 8, 9, 10, "heer", "vrouw", "boer"]
soorten_kaarten = ["harten", "schoppen", "ruiten", "klaver"]

for x in range(1,8):
    getalWaarde = random.randint(2,10)
    print(f"kaart {x} : ", random.choice(soorten_kaarten), getalWaarde)

print("\n" "Deck van 47 kaarten:" "\n")

for z in range(47):
    a = random.choice(soorten_kaarten)
    b = random.choice(nummer)
    print(a, b)


#    onderste twee code horen bij de for loop z

#    getalWaarde = random.randint(2,10)
#    print(random.choice(soorten_kaarten), getalWaarde)