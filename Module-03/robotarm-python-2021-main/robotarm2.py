from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:

for x in range(3):
    if x == 0:
        robotArm.grab()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.drop()
    if x == 1:
        robotArm.moveLeft()
        robotArm.moveLeft()
        robotArm.moveLeft()
        robotArm.moveLeft()
        robotArm.moveLeft()
        robotArm.grab()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.moveRight()
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