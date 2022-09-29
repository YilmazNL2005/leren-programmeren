#Maak een programma dat 2 gehele getallen opvraagt aan de gebruiker. Stel die getallen zijn toegekend aan de variabelen a en b
#Bepaal (met een if-statement) of a groter is dan b
#Zo ja:
#Ken de waarde van a toe aan een variabele Max
#Laat het programma printen: ‘a is het grootste getal: ’ gevolgd door de waarde van max

#Bepaal (met een elif-statement) of a kleiner is dan b
#Zo ja:
#Ken de waarde van a toe aan een variabele Min
#Laat het programma printen: ‘a is het kleinste getal: ’ gevolgd door de waarde van min
#Doe een commit met de titel “elif-statement”

#Bepaal (met een else-statement) of a gelijk is aan b
#Zo ja:
#Laat het programma printen: ‘a en b zijn even groot’
#Doe een commit met de titel “else-statement”

#Zorg dat in alle gevallen de variabelen Min en Max de juiste waarde krijgen
#Laat het programma daarna printen:
#‘Het minimum is: ’ gevolgd door de waarde van Min
#Het maximum is: ’ gevolgd door de waarde van Max
#Doe een commit met de titel “Min en Max”

a = int(input("Voer een getal in."))
b = int(input("Voer een getal in."))


if a > b:
    print("a is het grootste getal")
    print("b is het kleinste getal")
    max = a
    min = b

elif a < b:
    print("b is het grootste getal. ")
    print("a is het kleinste getal. ")
    max = b
    min = a

else:
    print("a en b zijn even groot.")
    max = a and b
    min = a and b
print(f"Het maximale is {max}")
print(f"Het minimale is {min}")

