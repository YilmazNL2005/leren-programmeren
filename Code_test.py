import random
CurrentLVL = 0
while CurrentLVL <= 20:
    RandomNumber = random.randint(0,3)
    print("Nummer =", RandomNumber)
    KiesEenDeur = int(input("welke deur bij nummer"))
    if RandomNumber == KiesEenDeur:
        print("Je hebt de goede deur gekozen")
        CurrentLVL += 1
        print("You are im lvl:", CurrentLVL)
    else:
        print("Je hebt de verkeerde deur gekozen!!!")
        print("Game Over!!!")
        break





    #######################################################################################################################################

#while eerste_level != "a" or eerste_level != "b" or eerste_level != "c":
#    eerste_level = input("Level 1, er zijn 3 deuren. Er is maar een goede deur, kies uit: deur A, B of C? ")
#    if eerste_level == "a":
#        print("Je loopt in de val en je krijgt lava over je gegooid!")
#        print("Game Over")
##        break 
#    elif eerste_level == "b":
#        print("Oei, verkeerde deur. Nu val je de leegte in!")
#        print("Game Over")
#        break
#    elif eerste_level == "c":
#        print("Goed gedaan, je hebt de goede deur gekozen.")
#        print("Level 1 voltooid!!!")
#        break
#    else:
#        print("Try again")

#RandomNumber = 


