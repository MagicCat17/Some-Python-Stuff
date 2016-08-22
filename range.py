import os
import time

st = time.time()

for x in range (10000001):
    print(x)
print(time.time() -st) 

    
if time.time() < (600):
    print("Slow af")
else:
    print ("Good")
