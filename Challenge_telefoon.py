
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

if prijs_Samsung > prijs_Apple or prijs_Samsung < prijs_Samsung - prijs_Apple <= 50:
    print(f"De Samsung Galaxy a22 is het duurst, de telefoon kost {prijs_Samsung} euro. ")
    print(f"De Iphone 13 is het goedkoopst, de telefoon kost {prijs_Apple} euro. ")
    print(f"Het advies is dus de Samsung Galaxy a22 te kopen. Deze is namelijk {prijs_Samsung - prijs_Apple} euro duurder. ") 

elif prijs_Apple > prijs_Samsung and prijs_Apple - prijs_Samsung <= 50:
    print(f"De Iphone 13 is het duurst, de telefoon kost {prijs_Apple} euro. ")
    print(f"De Samsung Galaxy a22 is het goedkoopst, de telefoon kost {prijs_Samsung} euro. ")
    print(f"Het advies is dus de Iphone 13 te kopen. Deze is namelijk {prijs_Apple - prijs_Samsung} euro duurder. ")
