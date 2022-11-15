from platform import java_ver


gastheer = input("Naam gastheer?")
#gasten = 0
#drank = True
#chips = True

# 1.    een feest met chips, maar zonder drank niet beginnen.                                               ja?
# 2.    een feest met gasten kan niet beginnen als er geen chips en geen drank is.                          ja
# 3.    een gastheer kan een feest geven zonder chips en gasten, maar niet zonder drank.                    nog niet
# 4.    het feest kan alleen beginnen als de gastheer er is tenzij er gasten, chips en drank.               nog niet
# 5.    een feest moet minimaal gasten of een gastheer hebben                                               nog niet
# 6.    alleen chips is geen feest                                                                          nog niet
# 7.    Als de naam van de gastheer Rudi is, dan is er geen feest.
# 8.    Een feest met gasten kan pas beginnen als er minimaal 5 gasten zijn.
# 9.    Een feest kan niet starten als er meer dan 1 aanwezigen zijn.

#if drank and gastheer != or gasten);

gasten = input("Zijn er gasten aanwezig? ")
drank = input("Is er drank aanwezig? ")
chips = input("Is er chips aanwezig?")


if drank and gastheer != "rudi" and (gastheer or gasten >= 5):
    print("Start de Party!")

elif gasten and chips == "nee" and drank == "ja":
    print("Start de Party!")

elif gasten and chips and chips == "ja":
    print("Start de Party!")

else:
    print("Geen Party")




