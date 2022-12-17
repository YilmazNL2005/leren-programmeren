punten_lan1 = 0
punten_lan2 = 0
punten_lan3 = 0

land1 = input("Welk land speelt in groep A? ")
land2 = input("Welk land speelt in groep A? ")
land3 = input("Welk land speelt in groep A? ")

punten_lan1_wed1 = int(input(f"Hoeveel punten heeft {land1} van wedstrijd 1? "))
punten_lan3_wed1 = int(input(f"Hoeveel punten heeft {land3} van wedstrijd 1? "))

punten_lan2_wed2 = int(input(f"Hoeveel punten heeft {land2} van wedstrijd 2? "))
punten_lan1_wed2 = int(input(f"Hoeveel punten heeft {land1} van wedstrijd 2? "))

punten_lan3_wed3 = int(input(f"Hoeveel punten heeft {land3} van wedstrijd 3? "))
punten_lan2_wed3 = int(input(f"Hoeveel punten heeft {land2} van wedstrijd 3? "))


winnaar_wed1 = land1
winnaar_wed2 = land2
winnaar_wed3 = land3


if punten_lan1_wed1 > punten_lan3_wed1:
    punten_lan1 += 3
    winnaar_wed1 = land1
else:
    punten_lan3 += 3
    winnaar_wed1 = land3

if punten_lan2_wed2 > punten_lan1_wed2:
    punten_lan2 += 3
    winnaar_wed2 = land2
else:
    punten_lan1 += 3
    winnaar_wed2 = land1

if punten_lan3_wed3 > punten_lan2_wed3:
    punten_lan3 += 3
    winnaar_wed3 = land3
else:
    punten_lan2 += 3
    winnaar_wed3 = land2
#winnaar_wed1 = abs()
#doelsaldo_wed1 = abs(land1 - land3)


print("Wedstrijd  #   thuis  -  uit  #   Doelpunten land 1  #  Doelpunten land 2   #   Winnaar  ")
print(f"    1           {land1}   -   {land3}               {punten_lan1_wed1}          -          {punten_lan3_wed1}           {winnaar_wed1}                            ")
print(f"    2           {land2}   -   {land1}               {punten_lan2_wed2}          -          {punten_lan1_wed2}           {winnaar_wed2}                            ")
print(f"    3           {land3}   -   {land2}               {punten_lan2_wed2}          -          {punten_lan1_wed2}           {winnaar_wed3}                           ")
print("\n")
print("    Land           Doelsaldo (gemaakt - tegen)           Puntentotaal ")
print(f"    {land1} :          Doelsaldo    {punten_lan1_wed1 - punten_lan3_wed1}           Puntentotaal ")
print(f"    {land2} :          Doelsaldo              N.V.T = 0                          Puntentotaal ")
print(f"    {land3} :          Doelsaldo    {punten_lan3_wed1 - punten_lan1_wed1}           Puntentotaal ")