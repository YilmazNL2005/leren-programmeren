from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
# Scan______ Geeft de kleur van het blok dat de robotarm op dat moment vast heeft. 
# Indien de robotarm geen blok vast heeft geeft hij als kleur de waarde '', dus een lege string.

verplaatsingen = 1
while verplaatsingen < 8:
    robotArm.grab()
    robotArm.scan()
    print(robotArm.scan())
    if robotArm.scan() == "white":
        for x in range(1):
            robotArm.moveRight()
        robotArm.drop()
    else:
        robotArm.drop()
        verplaatsingen = verplaatsingen + 1
    robotArm.moveRight()
        
        

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()