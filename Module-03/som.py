getal = 50
som = 50
beginGetal = "50"

while som < 1000:
    getal += 1
    som += getal
    beginGetal += f" + {getal} "
    print(f"{beginGetal} = {som}")