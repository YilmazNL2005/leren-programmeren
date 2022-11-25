import time
def printDelay(t: str, d=1):
    time.sleep(d)
    print(t)
    
for x in range(30,-1,-1):
    printDelay(x)

print("Raketlancering is gereed!!!")