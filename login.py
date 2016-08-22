#!/usr/bin/env python
import time
import sys
#get the username from a prompt
username = input("Login: >> ")

#list of allowed users
user1 = ("Blake")
user2 = ("Trevor")
user3 = ("Jake")
user4 = ("Jared")
user5 = ("Asshat_Hacker_101")



#control that the user belongs to the list of allowed users
if username == user1:
    print ("Access granted")
elif username == user2:
    print ("Welcome to the system")
    time.sleep(5.5)

elif username == user3:
    print ("Access Granted")

elif username == user4:
    print ("Fuck you!")

elif username == user5:
    print ("You have been banned from the server")
else:
    print ("Access Denied!")
