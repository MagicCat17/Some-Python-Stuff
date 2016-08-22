import os
print ("Welcome to Zork!")
print ("You wake up in a cave, you find yourself alone. You see a backpack full of things, what do you do?")
answer=input("Enter an answer:")

if answer == ('die'):
    print ("Coward!")
if answer == ('look around'):
    print ('You look around and see nothing!')
if answer == ('exit'):
    os._exit(0)

else:
        print (' More Coming Soon!')

