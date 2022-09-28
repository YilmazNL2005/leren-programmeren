#Maak een programma dat 2 gehele getallen opvraagt aan de gebruiker. Stel die getallen zijn toegekend aan de variabelen a en b
#Bepaal (met een if-statement) of a groter is dan b
#Zo ja:
#Ken de waarde van a toe aan een variabele Max
#Laat het programma printen: ‘a is het grootste getal: ’ gevolgd door de waarde van max

a = int(input("Voer een getal in."))
b = int(input("Voer een lager getal in."))


if a > b:
    print("a is het grootste getal")
    max = a

elif a < b:
    print("a is het kleinste getal")
    min = a



