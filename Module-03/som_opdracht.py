# name of student: Yilmaz
# number of student: ...
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #Hoeveel er betaalt moet worden. (Wordt door gebruiker ingevuld)
paid = int(float(input('Paid amount: ')) * 100) #Met hoeveel er betaald is. (Wordt door gebruiker ingevuld)
change = paid - toPay #De code berekend hoeveel wisselgeld de klant terugkrijgt
amountReturned = ""
if change > 0: #Als er wisselgeld gegeven m 
  coinValue = 50 #
  
  while change > 0 and coinValue > 0: #Als change groter is dan 0 en de coinwaarde is ook groter dan 0
    aantalMunten = change // coinValue #---
    if aantalMunten > 0: #Als aantalMunten groter is dan 0
      print('Maximale wisselgeld ', aantalMunten, " munten van ", coinValue, " cent!" ) #Het print een string
      nrCoinsReturned = int(input("Hoeveel munten van " + str(coinValue) +  " heb je teruggekregen? ")) #---
      change -= nrCoinsReturned * coinValue #---
      amountReturned += str(coinValue) + " x" + str(nrCoinsReturned) + "\n"


# comment on code below: 
#De code laat de coinwaarde zakken totdat het 0 is. 
    if coinValue == 500:
        coinValue = 300
    elif coinValue == 300:
        coinValue = 200
    elif coinValue == 200:
        coinValue = 50
    elif coinValue == 50:
        coinValue = 20
    elif coinValue == 20:
        coinValue = 10
    elif coinValue == 10:
        coinValue = 5
    elif coinValue == 5:
        coinValue = 2
    elif coinValue == 2:
        coinValue = 1
    else:
        coinValue = 0

if change > 0: #Het controleert of al het wisselgeld is teruggegeven
  print('Oh, je hebt niet al het wisselgeld teruggekregen: ', str(change) + ' cents')
else:
  print("Je krijgt geen wisselgeld")