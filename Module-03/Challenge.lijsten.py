
getal2 = 0
getal = int(input("voer een getal in"))
print(f"Tafel van {getal}")
for x in range (1,11):
    print(f'{x} x {getal} = {x * getal}')

thislist = [36, 19, 27, 3, 25]
print(thislist)
print(len(thislist))

for x in thislist:
    getal2 += x
print(getal2)

thislist.clear()
print(thislist)
