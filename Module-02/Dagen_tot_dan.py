#for dag_van_week in (1, 2, 3, 4, 5, 6, 7):
#    dag_van_week = input("Tot welke dag moet ik printen? ")
#    if dag_van_week == "maandag":
#        print("maandag")
#    if dag_van_week == "dinsdag":
#           print("maandag")
#           print("dinsdag")
#    if dag_van_week == "woensdag":
#                print("maandag")
#                print("dinsdag")
#                print("woensdag")
#    if dag_van_week == "donderdag":
#                    print("maandag")
#                    print("dinsdag")
#                    print("woensdag")
#                    print("donderdag")
#    if dag_van_week == "vrijdag":
#                        print("maandag")
#                        print("dinsdag")
#                        print("woensdag")
#                        print("donderdag")
#                        print("vrijdag")
#    if dag_van_week == "zaterdag":
#                            print("maandag")
#                            print("dinsdag")
#                            print("woensdag")
#                            print("donderdag")
#                            print("vrijdag")
#                            print("zaterdag")
#    if dag_van_week == "zondag":
#                                    print("maandag")
#                                    print("dinsdag")
#                                    print("woensdag")
#                                    print("donderdag")
#                                    print("vrijdag")
#                                    print("zaterdag")
#                                    print("zondag")



#dag_van_week = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag") #dit is een tuple
dag_stoppen = input("Voer de dag in waarop je wilt stoppen? ")

for dag_van_week in ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"):
    print(dag_van_week)
    if dag_van_week == dag_stoppen:
        break



#Tuple
