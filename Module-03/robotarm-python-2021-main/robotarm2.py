from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:

for x in range(3):
    if x == 0:
        robotArm.grab()
        for amount in range(9):
            robotArm.moveRight()
        robotArm.drop()
    if x == 1:
        for z in range(5):
            robotArm.moveLeft()
        robotArm.grab()
        for a in range(5):
            robotArm.moveRight()
        robotArm.drop()
    if x == 2:
        robotArm.moveLeft()
        robotArm.moveLeft()
        robotArm.grab()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()