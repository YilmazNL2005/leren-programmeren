vraag = ""
aantal = 0
while vraag != "quit":
    vraag = input("Vul quit in. ")
    aantal += 1
    if vraag == "quit":
        print(aantal)
