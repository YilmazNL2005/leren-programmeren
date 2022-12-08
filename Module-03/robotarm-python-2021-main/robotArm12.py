from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 4
# Jouw python instructies zet je vanaf hier:
Rows = 9
while Rows != 0:
    robotArm.grab()
    scan = robotArm.scan()
    if scan != "red":
        robotArm.drop()
        robotArm.moveRight()
        Rows -= 1
    else:
        for y in range(Rows):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(Rows - 1):
            robotArm.moveLeft()
        Rows -= 1


# verkeerde_blok = 1
# verplaatsingen = 1
# while verplaatsingen <= 10:
#     robotArm.grab()
#     robotArm.scan()
#     if robotArm.scan() == "red":
#         for x in range(0,1):
#             robotArm.moveRight()
#             robotArm.drop()
#     elif robotArm.scan() != "red" or verkeerde_blok == 9:
#         robotArm.drop()
#         robotArm.moveRight()
#         verkeerde_blok += 1
#         if verkeerde_blok == 10:
#             verplaatsingen = 11
#     verplaatsingen += 1
#     if verplaatsingen == 10:
#         verplaatsingen -= 9
#         verkeerde_blok = 1
#         for z in range(9):
#             robotArm.moveLeft()
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()