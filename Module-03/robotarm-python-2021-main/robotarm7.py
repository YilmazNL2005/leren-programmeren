from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
#max 11 regels inclusief: Import, robotArm.wait(), het laden van de robotArm = 8 regels max nu!!!

for i in range(5):
    for i in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    robotArm.moveRight()
    robotArm.moveRight()

# for x in range(3):
#     if x == 0:
#         robotArm.moveRight()
#         robotArm.moveRight()
#         robotArm.moveRight()
#         if x > 0:
#             robotArm.moveRight()
#     robotArm.grab()
#     robotArm.moveLeft()
#     robotArm.drop()
#if x == 3:
#for z in range:



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()