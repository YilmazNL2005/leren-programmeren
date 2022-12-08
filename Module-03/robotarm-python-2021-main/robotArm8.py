from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
#max 11 regels inclusief: Import, robotArm.wait(), het laden van de robotArm = 8 regels max nu!!!
robotArm.moveRight()
for i in range(7):
        robotArm.grab()        
        for i in range(8):
             robotArm.moveRight()
        robotArm.drop()
        for i in range(8):    
            robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()