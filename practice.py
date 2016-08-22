import os
import time

st = time.time()


for x in range (100000001):
    print(x)
print(time.time() -st) 




if time.time() < (60):
    print("Slow af")
else:
    print ("Good")
