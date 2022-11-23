from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:

for x in range(7):
     robotArm.moveRight()

#één blokje verplaatsen    
for z in range(8):
    print(z)
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()    
    if z < 7:
        robotArm.moveLeft() # extra left

# #één blokje verplaatsen    
# robotArm.grab()
# robotArm.moveRight()
# robotArm.drop()
# robotArm.moveLeft()
# robotArm.moveLeft()

# #één blokje verplaatsen    
# robotArm.grab()
# robotArm.moveRight()
# robotArm.drop()
# robotArm.moveLeft()
# robotArm.moveLeft()


#     for x in range(8, 1, -1):
#         robotArm.grab()
#         for x in range (8, 1, -1): 
#             robotArm.moveLeft()

        


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()