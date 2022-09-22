
#Iphone 13 = 1300 euro
#Samsung S22 = 1250 euro
#
#Hoe duur is de Iphone 13?
#Hoe duur is de Samsung a22
#
#Advies =   De ... is het duurst, de telefoon kost: ... Euro
#           De ... is het goedkoopst, de telefoon kost ... Euro
#Het advies is dus de ... te kopen. Deze is namelijk ... euro goedkoper/duurder

prijs_Apple = int(input("Hoe duur is de Iphone 13? "))
prijs_Samsung = int(input("Hoe duur is de Samsung Galaxy a22? "))
#Als de prijs van samsung groter is dan de apple prijs dan code uitvoeren.
#Of als de prijs van samsung kleiner is dan het verschil tussen de prijs van samsung en apple, maar gelijk of lager is dan 50 dan code uitvoeren.
if  prijs_Samsung > prijs_Apple or prijs_Samsung < prijs_Samsung - prijs_Apple <= 50:
    print(f"De Samsung Galaxy a22 is het duurst, de telefoon kost {prijs_Samsung} euro. ")
    print(f"De Iphone 13 is het goedkoopst, de telefoon kost {prijs_Apple} euro. ")
    print(f"Het advies is dus de Samsung Galaxy a22 te kopen. Deze is namelijk {prijs_Samsung - prijs_Apple} euro duurder/goedkoper. ") 
#Als de prijs van Apple groter is dan de prijs van Samsung EN als het verschil gelijk of kleiner is dan 50
elif prijs_Apple > prijs_Samsung and prijs_Apple - prijs_Samsung <= 50:
    print(f"De Iphone 13 is het duurst, de telefoon kost {prijs_Apple} euro. ")
    print(f"De Samsung Galaxy a22 is het goedkoopst, de telefoon kost {prijs_Samsung} euro. ")
    print(f"Het advies is dus de Iphone 13 te kopen. Deze is namelijk {prijs_Apple - prijs_Samsung} euro duurder. ")
elif prijs_Apple - prijs_Samsung > 50:
    print(f"De Samsung Galaxy a22 is het duurst, de telefoon kost {prijs_Samsung} euro. ")
    print(f"De Iphone 13 is het goedkoopst, de telefoon kost {prijs_Apple} euro. ")
    print(f"Het advies is dus de Samsung Galaxy a22 te kopen. Deze is namelijk {prijs_Apple - prijs_Samsung} euro duurder/goedkoper. ")