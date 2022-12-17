# from RobotArm import RobotArm

# robotArm = RobotArm('exercise 9')

# # Jouw python instructies zet je vanaf hier:
# #max 12 regels inclusief: Import, robotArm.wait(), het laden van de robotArm = 9 regels max nu!!!
# # for x in range(7):
# #     robotArm.moveRight()
# #     robotArm.grab()f
# for i in range(4): 
#     for a in range(i):
#         robotArm.grab()
#         for b in range(5):
#             robotArm.moveRight()
#         robotArm.drop()    
#         for c in range(5): 
#             robotArm.moveLeft()
#     robotArm.moveRight()


# # Na jouw code wachten tot het sluiten van de window:
# robotArm.wait()

from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
#max 11 regels inclusief: Import, robotArm.wait(), het laden van de robotArm = 8 regels max nu!!!
# for x in range(7):
#     robotArm.moveRight()
#     robotArm.grab()f
for i in range(1,5): 
    for a in range(i):
        robotArm.grab()
        for b in range(5):
            robotArm.moveRight()
        robotArm.drop()    
        for c in range(5): 
            robotArm.moveLeft()
    robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()