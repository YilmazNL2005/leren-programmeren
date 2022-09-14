import math

#pannenkoeken recept

aantal_pannenkoeken = int(input("aantal_pannenkoeken"))
aantal = aantal_pannenkoeken
#print(type(aantal))

naam = "bloem" 

hoeveelheid = 300 / 20

soort = "gram" 


naam_twee = "melk"

hoeveelheid_twee = 800 / 20 

soort_twee = "ml"


naam_drie = "eieren"

hoeveelheid_drie = 3 / 20

soort_drie = "stuks"


naam_vier = "boter" 

hoeveelheid_vier = 30 / 20

soort_vier = "g"


naam_vijf = "zout" 

hoeveelheid_vijf = 3 / 20

soort_vijf = "theelepels"



print(aantal, "2Pannenkoeken")

print(naam, hoeveelheid * math.ceil(aantal), soort)

print(naam_twee, hoeveelheid_twee * math.ceil(aantal), soort_twee)

print(naam_drie, hoeveelheid_drie * math.ceil(aantal), soort_drie)

print(naam_vier, hoeveelheid_vier * math.ceil(aantal), soort_vier)

print(naam_vijf, hoeveelheid_vijf * math.ceil(aantal), soort_vijf)

